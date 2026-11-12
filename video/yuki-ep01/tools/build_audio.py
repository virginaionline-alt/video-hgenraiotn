"""Synthesise the ASMR soundtrack for Yuki Ep.01 (60 s, 48 kHz stereo). Deterministic (fixed seed).

No music, no voice: rain bed plus cooking Foley placed on the 20-shot / 3-second grid.
"""
import wave
from pathlib import Path
import numpy as np

SR = 48000
DUR = 60.0
N = int(SR * DUR)
rng = np.random.default_rng(20261112)
OUT = Path(__file__).resolve().parents[1] / "assets" / "audio" / "asmr.wav"
OUT.parent.mkdir(parents=True, exist_ok=True)
mix = np.zeros((N, 2), dtype=np.float64)

def shot(i):  # start time of shot i (1-based)
    return 3.0 * (i - 1)

def bandpass(x, lo, hi):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = ((f >= lo) & (f <= hi)).astype(float)
    # soft edges
    m = np.convolve(m, np.hanning(9) / np.hanning(9).sum(), mode="same")
    return np.fft.irfft(X * m, n=len(x))

def norm(x):
    p = np.max(np.abs(x)) or 1.0
    return x / p

def place(sig, t, gain=1.0, pan=0.0):
    """Add a mono signal at time t (s) with constant-power pan (-1..1)."""
    s = int(t * SR)
    if s >= N:
        return
    sig = sig[: N - s]
    l = np.cos((pan + 1) * np.pi / 4)
    r = np.sin((pan + 1) * np.pi / 4)
    mix[s : s + len(sig), 0] += sig * gain * l
    mix[s : s + len(sig), 1] += sig * gain * r

def env(n, attack, decay_tau):
    t = np.arange(n) / SR
    a = np.clip(t / max(attack, 1e-4), 0, 1)
    return a * np.exp(-t / decay_tau)

def burst(dur, lo, hi, attack=0.002, tau=0.02):
    n = int(dur * SR)
    return norm(bandpass(rng.standard_normal(n), lo, hi)) * env(n, attack, tau)

def tone(freqs, dur, tau, amps=None):
    n = int(dur * SR)
    t = np.arange(n) / SR
    amps = amps or [1.0] * len(freqs)
    s = sum(a * np.sin(2 * np.pi * f * t) for f, a in zip(freqs, amps))
    return norm(s) * env(n, 0.001, tau)

# ---------------------------------------------------------------- rain bed (0-60 s)
seg = rng.standard_normal(N)
rain_l = norm(bandpass(seg, 250, 7000))
rain_r = norm(bandpass(np.roll(seg, 9173) * 0.7 + rng.standard_normal(N) * 0.3, 250, 7000))
low = norm(bandpass(rng.standard_normal(N), 60, 400))
t = np.arange(N) / SR
flutter = 0.85 + 0.15 * np.sin(2 * np.pi * 0.11 * t) * np.sin(2 * np.pi * 0.037 * t + 1.3)
# louder at the window (shots 1-3 and 19-20), softer under busy cooking
level = np.interp(t, [0, 0.8, 9, 11, 27, 30, 45, 54, 57, 60], [0, 0.16, 0.16, 0.10, 0.10, 0.07, 0.08, 0.10, 0.15, 0.15])
fade_out = np.clip((60.0 - t) / 1.6, 0, 1)
level = level * fade_out
mix[:, 0] += rain_l * level * flutter + low * level * 0.35
mix[:, 1] += rain_r * level * flutter + low * level * 0.35
# droplets on the glass
for _ in range(int(DUR * 14)):
    tt = rng.uniform(0, 59.5)
    g = np.interp(tt, [0, 9, 12, 54, 57, 60], [0.10, 0.10, 0.05, 0.05, 0.10, 0.0])
    place(burst(0.03, 2500, 9000, tau=rng.uniform(0.003, 0.009)), tt, g * rng.uniform(0.3, 1.0), rng.uniform(-0.9, 0.9))
# gutter drip, slow and irregular
for tt in np.arange(1.3, 59, 2.7) + rng.uniform(-0.4, 0.4, 22):
    place(tone([1450, 2900], 0.12, 0.03, [1, 0.3]), tt, 0.05, 0.6)

# ---------------------------------------------------------------- Act 1
# 01: kettle simmer + faint birds
kettle = norm(bandpass(rng.standard_normal(int(3.2 * SR)), 1800, 5200)) * np.interp(np.arange(int(3.2 * SR)), [0, SR, 2.6 * SR, 3.2 * SR], [0, 1, 1, 0])
place(kettle, shot(1), 0.03, 0.3)
for tt in (0.9, 1.25, 2.1):
    n = int(0.09 * SR); tw = np.arange(n) / SR
    chirp = np.sin(2 * np.pi * (3400 + 2600 * tw / 0.09) * tw) * env(n, 0.005, 0.03)
    place(chirp, shot(1) + tt, 0.018, -0.7)
# 02: two soft footsteps + apron rustle
for tt, p in ((0.25, -0.2), (0.8, 0.1)):
    place(burst(0.18, 60, 500, attack=0.004, tau=0.04), shot(2) + tt, 0.22, p)
    place(burst(0.12, 1500, 6000, tau=0.03), shot(2) + tt + 0.02, 0.03, p)
for tt in (1.2, 1.9):
    place(burst(0.45, 2000, 9000, attack=0.08, tau=0.12), shot(2) + tt, 0.07, 0.0)
# 03: fur brushing + paw shift + tail swish
for k in range(3):
    place(burst(0.7, 1500, 8000, attack=0.15, tau=0.18), shot(3) + 0.3 + k * 0.8, 0.08, -0.2)
place(burst(0.12, 80, 600, tau=0.04), shot(3) + 2.4, 0.12, -0.3)
place(burst(0.35, 500, 3000, attack=0.05, tau=0.08), shot(3) + 1.7, 0.06, -0.4)
# 04: ceramic taps on wood, utensils, fabric
for tt, f, p in ((0.4, 2300, -0.3), (0.9, 1900, 0.2), (1.5, 2600, 0.0)):
    place(tone([f, f * 2.71, f * 5.1], 0.6, 0.09, [1, 0.4, 0.15]), shot(4) + tt, 0.10, p)
    place(burst(0.06, 100, 900, tau=0.015), shot(4) + tt, 0.12, p)
for tt in (1.9, 2.2):
    place(burst(0.08, 300, 2500, tau=0.02), shot(4) + tt, 0.10, 0.3)  # wooden spoon
place(burst(0.5, 2000, 9000, attack=0.1, tau=0.15), shot(4) + 2.4, 0.06, 0.0)

# ---------------------------------------------------------------- Act 2
def chop(t0, gain=0.3, pan=0.0):
    place(burst(0.12, 70, 700, tau=0.025), t0, gain, pan)            # board thock
    place(burst(0.05, 2500, 9000, tau=0.006), t0, gain * 0.25, pan)  # blade edge
# 05: slicing chicken, 8 strokes
for k in range(8):
    chop(shot(5) + 0.25 + k * 0.33, 0.30, 0.05)
place(burst(0.35, 1000, 6000, attack=0.05, tau=0.12), shot(5) + 2.8, 0.05, 0.0)
# 06: salt, pepper mill, cornstarch, mixing
for _ in range(60):
    place(burst(0.01, 4000, 11000, tau=0.002), shot(6) + 0.2 + rng.uniform(0, 0.6), 0.05, rng.uniform(-0.3, 0.3))
for k in range(9):
    place(burst(0.05, 1500, 6000, tau=0.01), shot(6) + 0.9 + k * 0.07, 0.10, 0.2)
place(burst(0.6, 600, 4000, attack=0.1, tau=0.25), shot(6) + 1.5, 0.08, 0.0)
for k in range(4):
    place(burst(0.25, 200, 2500, attack=0.03, tau=0.07), shot(6) + 2.0 + k * 0.22, 0.08, -0.1)
# 07: rapid fine mincing + scrape
for k in range(18):
    chop(shot(7) + 0.2 + k * 0.11, 0.17, -0.05)
place(burst(0.4, 1200, 7000, attack=0.05, tau=0.15), shot(7) + 2.4, 0.07, 0.0)
# 08: vegetables — crisp carrot, broccoli snaps, spring onion
for k in range(6):
    chop(shot(8) + 0.2 + k * 0.2, 0.26, -0.15)
    place(burst(0.04, 3000, 9000, tau=0.004), shot(8) + 0.2 + k * 0.2 + 0.01, 0.08, -0.15)
for tt in (1.5, 1.85):
    place(burst(0.06, 800, 5000, tau=0.01), shot(8) + tt, 0.12, 0.25)
for k in range(5):
    chop(shot(8) + 2.1 + k * 0.15, 0.16, 0.1)
# 09: pouring soy/mirin/sake, sugar, whisking, spoon tap
for k, tt in enumerate((0.1, 0.55, 0.95)):
    n = int(0.4 * SR); tw = np.arange(n) / SR
    glug = norm(bandpass(rng.standard_normal(n), 300, 2500)) * (0.6 + 0.4 * np.sin(2 * np.pi * 14 * tw)) * np.interp(tw, [0, 0.03, 0.33, 0.4], [0, 1, 1, 0])
    place(glug, shot(9) + tt, 0.09, 0.1)
place(burst(0.2, 3000, 9000, attack=0.02, tau=0.06), shot(9) + 1.35, 0.06, 0.1)
for k in range(10):
    place(burst(0.12, 1500, 8000, attack=0.02, tau=0.04), shot(9) + 1.6 + k * 0.12, 0.09, 0.15 * (-1) ** k)
    if k % 3 == 0:
        place(tone([3100, 7400], 0.25, 0.05, [1, 0.3]), shot(9) + 1.6 + k * 0.12, 0.03, 0.0)
place(tone([2600, 6900], 0.5, 0.08, [1, 0.3]), shot(9) + 2.85, 0.08, 0.0)

# ---------------------------------------------------------------- Act 3
# 10: ignition click, whoomp, flame hiss, oil pour
place(burst(0.02, 2000, 10000, tau=0.002), shot(10) + 0.15, 0.25, 0.2)
place(burst(0.02, 2000, 10000, tau=0.002), shot(10) + 0.30, 0.20, 0.2)
place(burst(0.5, 60, 700, attack=0.03, tau=0.15), shot(10) + 0.35, 0.22, 0.2)
n = int(2.7 * SR)
place(norm(bandpass(rng.standard_normal(n), 800, 5000)) * np.interp(np.arange(n), [0, 0.3 * SR, n], [0, 1, 1]), shot(10) + 0.3, 0.025, 0.2)
n = int(0.9 * SR); tw = np.arange(n) / SR
place(norm(bandpass(rng.standard_normal(n), 400, 2200)) * np.interp(tw, [0, 0.1, 0.8, 0.9], [0, 1, 1, 0]), shot(10) + 1.2, 0.05, 0.0)

def sizzle(t0, t1, gain, pops_per_s=25, pan=0.0, swell=None):
    n = int((t1 - t0) * SR)
    tw = np.arange(n) / SR
    base = norm(bandpass(rng.standard_normal(n), 3000, 12000))
    am = 0.75 + 0.25 * np.abs(norm(bandpass(rng.standard_normal(n), 2, 18)))
    shape = np.interp(tw, [0, 0.15, (t1 - t0) - 0.2, t1 - t0], [0, 1, 1, 0])
    if swell is not None:
        shape = shape * swell(tw)
    place(base * am * shape, t0, gain, pan)
    for _ in range(int((t1 - t0) * pops_per_s)):
        place(burst(0.015, 2000, 11000, tau=rng.uniform(0.001, 0.004)), t0 + rng.uniform(0, t1 - t0 - 0.05), gain * rng.uniform(0.6, 1.8), pan + rng.uniform(-0.4, 0.4))

# 11-14: the pan — sizzle swells as each piece goes in, tongs, sauce hiss, sticky bubbling
sizzle(shot(11) + 0.2, shot(15) + 0.4, 0.07, pops_per_s=30, swell=lambda tw: np.clip(0.4 + tw / 2.0, 0, 1))
for k in range(5):
    place(burst(0.35, 2500, 11000, attack=0.005, tau=0.12), shot(11) + 0.25 + k * 0.5, 0.10, 0.1)  # piece hits oil
    place(tone([4200, 9100], 0.12, 0.02, [1, 0.4]), shot(11) + 0.2 + k * 0.5, 0.03, 0.1)        # tong click
for k in range(4):  # turning
    place(tone([3900, 8600], 0.15, 0.02, [1, 0.4]), shot(12) + 0.3 + k * 0.65, 0.05, 0.0)
    place(burst(0.5, 2500, 11000, attack=0.005, tau=0.18), shot(12) + 0.35 + k * 0.65, 0.09, 0.0)
place(burst(1.4, 1500, 11000, attack=0.01, tau=0.5), shot(13) + 0.2, 0.18, 0.0)  # sauce hits pan
def bubbles(t0, t1, rate, gain, fmin=250, fmax=700):
    for _ in range(int((t1 - t0) * rate)):
        n = int(0.06 * SR); tw = np.arange(n) / SR
        f0 = rng.uniform(fmin, fmax)
        b = np.sin(2 * np.pi * (f0 + 900 * tw / 0.06) * tw) * env(n, 0.002, 0.015)
        place(b, rng.uniform(t0, t1 - 0.06), gain * rng.uniform(0.5, 1.0), rng.uniform(-0.3, 0.3))
bubbles(shot(13) + 0.6, shot(15), 9, 0.06)
for k in range(5):  # wooden spatula stirring
    place(burst(0.35, 300, 3000, attack=0.05, tau=0.1), shot(14) + 0.3 + k * 0.5, 0.07, 0.0)
# 15: steamer water, lid lift + steam puff, veg on ceramic
bubbles(shot(15), shot(16) - 0.2, 14, 0.04, 180, 420)
place(tone([1700, 4100], 0.4, 0.06, [1, 0.3]), shot(15) + 0.5, 0.07, -0.2)
n = int(0.9 * SR); tw = np.arange(n) / SR
place(norm(bandpass(rng.standard_normal(n), 400, 6000)) * np.interp(tw, [0, 0.08, 0.9], [0, 1, 0]), shot(15) + 0.55, 0.08, 0.0)
for tt in (1.6, 2.1, 2.6):
    place(tone([2900, 6100], 0.2, 0.03, [1, 0.3]), shot(15) + tt, 0.05, 0.1)

# ---------------------------------------------------------------- Act 4
# 16: rice — paddle scoops, soft pats
for tt in (0.4, 1.2):
    place(burst(0.35, 300, 3500, attack=0.04, tau=0.1), shot(16) + tt, 0.10, 0.0)
    place(burst(0.12, 100, 900, tau=0.03), shot(16) + tt + 0.3, 0.08, 0.0)
for k in range(3):
    place(burst(0.1, 200, 1500, tau=0.03), shot(16) + 2.0 + k * 0.25, 0.06, 0.0)
# 17-18: chopsticks placing chicken and vegetables (sticky sounds)
for k in range(5):
    place(tone([3300, 7700], 0.12, 0.02, [1, 0.35]), shot(17) + 0.3 + k * 0.5, 0.04, 0.1)
    place(burst(0.12, 200, 2000, attack=0.01, tau=0.04), shot(17) + 0.35 + k * 0.5, 0.06, 0.1)
for k in range(5):
    place(tone([3500, 8100], 0.12, 0.02, [1, 0.35]), shot(18) + 0.3 + k * 0.5, 0.04, -0.1)
    place(burst(0.06, 1500, 7000, tau=0.01), shot(18) + 0.35 + k * 0.5, 0.05, -0.1)
# 19: sesame patter like tiny rain
for _ in range(140):
    place(burst(0.008, 3500, 11000, tau=0.0015), shot(19) + 0.3 + rng.beta(2, 2) * 2.2, 0.06, rng.uniform(-0.4, 0.4))
# 20: chopsticks touch ceramic, tail swish, then the rain closes the film
place(tone([3000, 7200], 0.4, 0.06, [1, 0.35]), shot(20) + 1.1, 0.06, 0.0)
place(tone([3200, 7500], 0.4, 0.06, [1, 0.35]), shot(20) + 1.25, 0.04, 0.0)
place(burst(0.4, 500, 3000, attack=0.05, tau=0.1), shot(20) + 1.8, 0.05, -0.5)

# ---------------------------------------------------------------- master
# gentle high-shelf softening so nothing is harsh, then peak-normalise to -3 dBFS
for c in range(2):
    X = np.fft.rfft(mix[:, c])
    f = np.fft.rfftfreq(N, 1 / SR)
    X *= np.where(f > 9000, 0.6, 1.0)
    mix[:, c] = np.fft.irfft(X, n=N)
mix *= np.clip(t / 0.5, 0, 1)[:, None]  # fade in from silence
peak = np.max(np.abs(mix))
mix = mix / peak * 10 ** (-3 / 20)
pcm = (mix * 32767).astype("<i2")
with wave.open(str(OUT), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(OUT, f"{N / SR:.1f}s")
