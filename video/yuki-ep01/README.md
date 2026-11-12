# Yuki's Cozy Kitchen Diaries — Episode 01 (HyperFrames)

A 60-second, 9:16 (1080×1920, 24 fps) motion-design cooking short made with
[HyperFrames](https://hyperframes.heygen.com): HTML + GSAP rendered to MP4 on this machine.
No AI video generation, no credits.

It follows the 20-shot script in `../../storyboards/yuki-chicken-teriyaki/` (3 s per shot) and
uses the three reference images:
- **The rainy window and the dog** come from the kitchen image. A script repaints the sunny sky as a grey, misty rainy afternoon.
- **Yuki** comes from her portrait.
- **The cooking steps** come from the recipe card's step photos, kitchen-tools panel and ingredient lists. They are shown as "diary photo" cards.
- **The steamer and the rice-bowl plating** (shots 15–19) are animated SVG illustrations, so the food is added in the right order: rice → chicken → vegetables → garnish.

The ASMR track is generated with code from noise and tones: rain, droplets, knife, seasoning, whisk, ignition, sizzle, bubbles, rice, chopsticks and sesame. It has no music and no voice.

## Rebuild

```bash
python3 tools/build_images.py   # needs Pillow + numpy; writes assets/img/*
python3 tools/build_audio.py    # needs numpy; writes assets/audio/asmr.wav
ffmpeg -y -i assets/audio/asmr.wav -c:a aac -b:a 192k assets/audio/asmr.m4a && rm assets/audio/asmr.wav
```

## Preview, check, render

```bash
npx hyperframes@0.9.38 preview          # live Studio in the browser
npx hyperframes@0.9.38 check            # lint, layout, motion and contrast checks
npx hyperframes@0.9.38 render -f 24 -o renders/yuki-ep01.mp4
```

Requirements: Node.js 22+, FFmpeg and Chrome/Chromium.
