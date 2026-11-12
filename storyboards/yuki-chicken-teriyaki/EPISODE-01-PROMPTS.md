# Yuki's Cozy Kitchen Diaries: Episode 01 · Scene-by-scene generation prompts

These prompts follow the 20-shot script exactly: 20 shots × 3 s = 60 s, 9:16, 1080 × 1920, 24 fps.

Every prompt below is **self-contained**. Video generators don't remember earlier clips, so each prompt repeats the character, kitchen, light and style descriptions word for word. This is what keeps the 20 clips looking like one film.

## How to use

1. **Make the start frame first** for each shot using the **Start frame** prompt in an image model. Attach the references:
   - `refs/01-character-yuki.jpg` for any shot where Yuki or her hands appear
   - `refs/02-kitchen.jpg` for every shot
2. **Animate that frame** with the **Motion** prompt in an image-to-video model, set to 3 s, 9:16 and 24 fps.
3. **Sound:** if the model generates audio, add the **ASMR** line to the prompt. Otherwise, generate it separately as a 3 s sound effect.
4. Add the **Negative prompt** to every generation.
5. **Continuity trick:** for shots that follow straight on from the previous one (marked 🔗), use the **last frame of the previous clip** as an extra reference image.

## Negative prompt (use on every shot)

```
different face, different hairstyle, short hair, bun, ponytail, braid, blonde hair, black hair, red hair, missing ribbon, different earrings, blue eyes, green eyes, different clothes, different apron color, extra fingers, missing fingers, fused fingers, deformed hands, extra limbs, distorted face, text, watermark, logo, subtitles, sunny weather, clear sky, harsh shadows, 3D render, photorealistic, CGI, dog on counter, dog eating food, burnt food, raw-looking cooked chicken, cooked food before cooking, messy kitchen, different kitchen, location change, music, dialogue, voice, whoosh, sudden sound
```

---

## ACT 1 — A PEACEFUL RAINY AFTERNOON

### SHOT 01 · 00:00–00:03 · Establishing the kitchen

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. Wide shot of a cozy Japanese countryside kitchen on a rainy afternoon: rustic warm wooden countertops, deep sage-green shaker cabinets with brass handles, a large wooden-framed window, climbing ivy and small white flowers around the window, potted herbs, open wooden shelves with glass jars and ceramic cups, hanging wooden utensils, a black enamel pendant lamp glowing warm golden above the counter, a small kettle on the stove with a faint wisp of steam. Through the window: gentle rain, raindrops on the glass, green meadows, trees and misty blue mountains under a soft grey cloudy sky. Warm golden interior light contrasted with cool blue-grey rainy daylight from the window. No people. Peaceful, nostalgic, intimate.
```

**Motion (3 s):**
```
Slow cinematic push-in toward the rainy window. Raindrops slide down the glass, white flowers and ivy leaves sway gently in the breeze, a thin curl of steam rises from the kettle, and the pendant lamp glows steadily. Smooth, calm, no cuts.
```

**ASMR:** `Continuous gentle rainfall on window glass and roof, faint distant birds, soft breeze, a quiet kettle simmer. No music, no voice.`

---

### SHOT 02 · 00:03–00:06 · Introducing Yuki

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. Medium side shot of Yuki, a beautiful young adult anime woman with very long, thick, flowing dark chocolate-brown wavy hair falling over her shoulders and down her back, a large ivory-white ribbon tied at the back of her hair, small pearl flower earrings, large expressive dark brown eyes, soft rosy cheeks, delicate features and a gentle smile. She wears a cream-white puff-sleeve blouse and a sage-green floral apron. She stands beside a rustic wooden kitchen counter with deep sage-green cabinets, a warm golden pendant lamp above her and a large wooden-framed window beside her showing gentle rain, raindrops on the glass and misty green mountains. Warm golden light on her face, cool blue-grey rim light from the window.
```

**Motion (3 s):**
```
Yuki slowly turns her head toward the rainy window, blinks naturally and smiles softly. A few strands of her long wavy hair move gently, and the ivory ribbon stays visible. Rain trickles down the window behind her. The camera is almost still with a very subtle drift. Her face stays identical to the reference throughout.
```

**ASMR:** `Gentle rainfall, two soft footsteps on a wooden floor, a soft cotton apron rustle. No music, no voice.`

---

### SHOT 03 · 00:06–00:09 · Her little companion

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. Intimate close-up of a fluffy golden retriever resting on a woven mat beside a large wooden-framed kitchen window, looking peacefully out at the gentle rain, with raindrops on the glass and misty green mountains outside. A woman's slender hand with a cream-white puff sleeve gently strokes the dog's golden head. A sage-green floral apron and long dark chocolate-brown wavy hair are visible at the edge of the frame. Warm golden interior light on the dog's fur, cool blue-grey window light.
```

**Motion (3 s):**
```
The golden retriever blinks slowly, twitches its ears and gently wags its tail. The hand strokes its head once, softly and naturally. Raindrops slide down the window. Slow, peaceful, intimate.
```

**ASMR:** `Soft fur brushing under the hand, a light paw shift on the woven mat, a slow tail swish, rain pattering on the window glass close by. No music, no voice.`

---

### SHOT 04 · 00:09–00:12 · Preparing to cook

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. Medium shot of Yuki at the rustic wooden kitchen counter: a beautiful young adult anime woman with very long, thick, flowing dark chocolate-brown wavy hair, a large ivory-white ribbon at the back of her hair, small pearl flower earrings, large dark brown eyes, soft rosy cheeks and a gentle smile, wearing a cream-white puff-sleeve blouse and a sage-green floral apron. On the counter: a cream ceramic mixing bowl, a light-oak wooden cutting board, a chef's knife with a dark wood handle, small ceramic sauce bowls and wooden spoons and spatula. Deep sage-green cabinets, a warm golden pendant lamp and a rainy window with misty mountains behind her.
```

**Motion (3 s):**
```
Yuki gently places the wooden cutting board and ceramic bowls on the counter, then straightens the front of her apron with both hands. The camera eases from a medium shot into a countertop close-up of the neatly arranged utensils. Graceful, slow movements with natural hands. Rain continues outside.
```

**ASMR:** `Soft ceramic bowl taps on wood, wooden utensils set down on the counter, gentle fabric rustle, rain in the background. No music, no voice.`

---

## ACT 2 — FRESH INGREDIENT PREPARATION

### SHOT 05 · 00:12–00:15 · Cutting the chicken 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration, soft cinematic lighting. Vertical 9:16. Extreme close-up of fresh raw boneless chicken thigh on a light-oak wooden cutting board on a rustic wooden counter. A woman's slender hands with natural nails and cream-white puff sleeves pushed up, a sage-green floral apron just visible, hold a chef's knife with a dark wood handle mid-cut, using a careful claw grip. A few even, bite-sized raw pink chicken pieces are already separated. Warm golden pendant light glints on the steel blade, with a soft blue-grey rainy window glow in the blurred background.
```

**Motion (3 s):**
```
The knife slices through the chicken in smooth, rhythmic strokes, and even bite-sized pieces separate neatly and gather to one side. Natural hand anatomy and a realistic knife technique. The camera holds steady with shallow depth of field.
```

**ASMR:** `Crisp, soft knife slices through meat onto a wooden board, gentle cutting-board taps, a light blade scrape. Rain faint in the background. No music, no voice.`

---

### SHOT 06 · 00:15–00:18 · Seasoning the chicken 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Top-down close-up of raw bite-sized pink chicken pieces in a cream ceramic mixing bowl on a rustic wooden counter. A slender hand with a cream-white puff sleeve sprinkles salt from her fingertips, with a wooden pepper mill and a small ceramic dish of white cornstarch beside the bowl. Warm golden pendant light, soft cool rainy window light on one side.
```

**Motion (3 s):**
```
Salt crystals and freshly ground black pepper fall naturally onto the chicken, then a spoonful of cornstarch dusts down like soft snow. Her fingers gently toss and mix the chicken until every piece is evenly coated. The chicken stays raw. Smooth and graceful.
```

**ASMR:** `Fine salt sprinkling, a pepper mill grinding, a soft powdery cornstarch fall, gentle mixing in a ceramic bowl. Rain in the background. No music, no voice.`

---

### SHOT 07 · 00:18–00:21 · Chopping garlic and ginger

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Macro close-up of fresh peeled garlic cloves and a knob of fresh ginger on a light-oak wooden cutting board. A chef's knife with a dark wood handle is held by a slender hand with a cream-white puff sleeve, the sage-green floral apron softly blurred. Finely chopped garlic and ginger are beginning to gather. Warm golden light, shallow depth of field.
```

**Motion (3 s):**
```
The knife moves in small, precise, rapid chopping motions, and the finely chopped garlic and ginger gather into two neat little piles. The flat of the blade scrapes them together at the end. Macro detail with natural hand movement.
```

**ASMR:** `Crisp, rapid tiny knife taps on wood, fine chopping, a soft blade scrape across the board. Rain in the background. No music, no voice.`

---

### SHOT 08 · 00:21–00:24 · Preparing vegetables

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Colorful fresh raw vegetables on a light-oak wooden cutting board and rustic wooden counter: bright orange carrots being cut into thin julienne strips, fresh green broccoli florets separated into small pieces, and spring onions sliced into delicate green rings. A slender hand with a cream-white puff sleeve holds the chef's knife. Warm golden pendant light, cool rainy window glow, shallow depth of field.
```

**Motion (3 s):**
```
A slow cinematic pan across the colorful ingredients. Thin carrot strips fall onto the board, broccoli florets are separated carefully by hand, and spring onion rings scatter naturally under the knife. Gentle, smooth camera movement.
```

**ASMR:** `Crisp carrot slicing, the soft snap of broccoli florets, light spring onion chopping, gentle knife taps. Rain in the background. No music, no voice.`

---

### SHOT 09 · 00:24–00:27 · Making homemade teriyaki sauce

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Top-down view of a small cream ceramic bowl on a rustic wooden counter, surrounded by a bottle of dark soy sauce, a bottle of golden mirin, a small cup of sake, a dish of brown sugar, minced garlic and grated ginger. A slender hand with a cream-white puff sleeve is pouring dark soy sauce into the bowl. Warm golden pendant light.
```

**Motion (3 s):**
```
Soy sauce, mirin and a little sake pour naturally into the bowl one after another, then brown sugar, garlic and ginger are added. A small whisk swirls everything into a smooth, glossy, dark amber sauce. The camera moves from top-down into an extreme close-up of the glossy sauce surface.
```

**ASMR:** `Liquid pouring from bottles, a soft sugar spill, gentle whisking in ceramic, a light spoon tap against the bowl rim. Rain in the background. No music, no voice.`

---

## ACT 3 — COOKING THE TERIYAKI CHICKEN

### SHOT 10 · 00:27–00:30 · Heating the skillet

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. Extreme close-up at pan level of an empty black cast-iron skillet on a gas stove with a soft blue flame beneath it. A slender hand with a cream-white puff sleeve tilts a small glass bottle of golden cooking oil over the pan. The warm golden kitchen and a sage-green cabinet are softly blurred behind, with a cool rainy window glow in the distance.
```

**Motion (3 s):**
```
The stove flame flickers to life, then a thin golden stream of oil flows into the skillet, spreads naturally across the hot surface and shimmers gently, with faint heat haze rising. Steady camera.
```

**ASMR:** `Gas stove ignition click and soft whoomp, a low flame hiss, gentle oil pouring, a faint rising crackle. Rain in the background. No music, no voice.`

---

### SHOT 11 · 00:30–00:33 · Frying the chicken 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Close-up of a black cast-iron skillet with shimmering hot oil on a gas stove. A slender hand with a cream-white puff sleeve uses silver tongs to place raw cornstarch-coated chicken pieces into the pan. Several pieces are already in the oil with small bubbles forming around their edges. Warm golden pendant light, light steam.
```

**Motion (3 s):**
```
Coated chicken pieces are placed one by one and settle into the hot oil, sizzling immediately, with small bubbles forming around every edge and delicate steam rising into the warm light. The chicken is still pale on top. Steady close-up.
```

**ASMR:** `Crisp sizzling as each piece hits the oil, gentle oil crackling, a light tong click. Rain faint in the background. No music, no voice.`

---

### SHOT 12 · 00:33–00:36 · Turning the chicken 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Low-angle macro shot at the rim of a black cast-iron skillet full of sizzling chicken pieces. Silver tongs held by a slender hand with a cream-white puff sleeve are turning a piece to reveal a beautiful crispy golden-brown crust. Steam rises, and warm golden pendant light glints on the oil.
```

**Motion (3 s):**
```
The tongs turn the chicken pieces one after another. Each piece rotates naturally, revealing its golden-brown crust, and oil bubbles and steam rise. Low-angle macro, steady and smooth.
```

**ASMR:** `Tongs clicking, a renewed sizzle with each turn, occasional soft contact of tongs on cast iron. Rain faint in the background. No music, no voice.`

---

### SHOT 13 · 00:36–00:39 · Adding teriyaki sauce 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Extreme close-up of golden-brown cooked chicken pieces in a black cast-iron skillet. A slender hand with a cream-white puff sleeve tilts a small cream ceramic bowl, pouring a smooth stream of dark amber homemade teriyaki sauce over the chicken. Steam rises, with warm golden pendant light.
```

**Motion (3 s):**
```
A smooth stream of dark amber teriyaki sauce flows into the hot pan and spreads around the golden chicken, and small bubbles immediately begin forming at the edges. Steam billows softly into the warm light.
```

**ASMR:** `Sauce pouring, an instant hiss as it hits the hot pan, bubbling liquid and soft sizzling. Rain faint in the background. No music, no voice.`

---

### SHOT 14 · 00:39–00:42 · The glossy teriyaki glaze 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Slow macro shot of bite-sized chicken pieces coated in a thick, glossy, mahogany teriyaki glaze in a black cast-iron skillet. A wooden spatula held by a slender hand with a cream-white puff sleeve gently stirs them. Slow sauce bubbles and delicate steam rise into warm golden pendant light. The glaze glistens.
```

**Motion (3 s):**
```
The wooden spatula stirs gently, the chicken pieces turn naturally, and the sauce thickens and coats every piece in a sticky, glossy glaze. Slow bubbles pop softly and delicate steam rises. Slow macro push-in.
```

**ASMR:** `Sticky sauce bubbling, a wooden spatula stirring against cast iron, gentle frying. Rain faint in the background. No music, no voice.`

---

### SHOT 15 · 00:42–00:45 · Steaming the vegetables

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Close-up of a small bamboo steamer on a pot of simmering water on the stove. A slender hand with a cream-white puff sleeve lifts the lid, and a cloud of steam reveals bright green broccoli florets and tender orange carrot strips inside. A small cream ceramic dish waits beside it on the rustic wooden counter. Warm golden pendant light.
```

**Motion (3 s):**
```
The steamer lid lifts and soft steam billows up and drifts. Wooden chopsticks gently transfer the bright green broccoli and orange carrots into the ceramic dish. Close-up with a gentle drift.
```

**ASMR:** `Water bubbling softly, the steamer lid lifting with a puff of steam, vegetables gently touching ceramic, light chopstick taps. Rain in the background. No music, no voice.`

---

## ACT 4 — PLATING AND THE FINAL MOMENT

### SHOT 16 · 00:45–00:48 · Fluffy white rice

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Top-down close-up of a beautiful handmade cream ceramic donburi bowl with a thin sage-green rim on a rustic wooden counter. A wooden rice paddle held by a slender hand with a cream-white puff sleeve scoops freshly steamed fluffy white rice into the bowl. Individual glistening grains, gentle steam, warm golden pendant light.
```

**Motion (3 s):**
```
Fluffy rice falls naturally from the wooden paddle into the bowl, and she gently smooths the surface into a soft mound. Gentle steam rises. Top-down, steady.
```

**ASMR:** `Soft rice landing, a wooden paddle gently touching ceramic, a quiet smoothing scrape. Rain in the background. No music, no voice.`

---

### SHOT 17 · 00:48–00:51 · Adding the teriyaki chicken 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Close-up food plating shot of a cream ceramic donburi bowl with a sage-green rim, filled with fluffy white rice. Wooden chopsticks held by a slender hand with a cream-white puff sleeve place glossy golden-brown teriyaki chicken pieces on top. The thick glaze glistens under warm golden pendant light, with gentle steam.
```

**Motion (3 s):**
```
She places the glossy teriyaki chicken pieces one by one onto the rice and arranges them beautifully. The sticky glaze catches the warm light and steam rises softly. Slow, careful, graceful.
```

**ASMR:** `Gentle chopstick contact, soft sticky sauce sounds as each piece settles, a faint ceramic touch. Rain in the background. No music, no voice.`

---

### SHOT 18 · 00:51–00:54 · Adding colorful vegetables 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Top-down view of a cream ceramic donburi bowl with a sage-green rim: fluffy white rice topped with glossy teriyaki chicken. Wooden chopsticks held by a slender hand with a cream-white puff sleeve place bright green steamed broccoli florets beside the chicken, with orange carrot strips waiting in a small ceramic dish. Warm golden pendant light, gentle steam.
```

**Motion (3 s):**
```
Slow top-down camera movement. Bright green broccoli and orange carrot strips are placed gently beside the chicken one by one, and the bowl becomes colorful and beautifully balanced. Soft steam rises.
```

**ASMR:** `Gentle vegetable placement, tiny chopstick taps on the ceramic dish and bowl rim. Rain in the background. No music, no voice.`

---

### SHOT 19 · 00:54–00:57 · The final garnish 🔗

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, detailed food illustration. Vertical 9:16. Extreme macro food shot with a beautiful shallow depth of field: a completed chicken teriyaki rice bowl with glossy mahogany chicken, bright green broccoli and orange carrot strips on fluffy white rice in a cream ceramic bowl. Fingertips sprinkle white sesame seeds and delicate green spring onion rings from above. The extra teriyaki glaze catches the warm golden light, and steam rises.
```

**Motion (3 s):**
```
White sesame seeds and green onion rings fall slowly in gentle slow motion onto the glossy chicken, bouncing softly. Steam rises naturally from the finished bowl. Extreme macro with a very subtle push-in.
```

**ASMR:** `Delicate sesame seeds sprinkling like tiny rain, soft garnish landing, gentle ambient rainfall. No music, no voice.`

---

### SHOT 20 · 00:57–01:00 · The perfect rainy-day meal

**Start frame:**
```
Hand-painted 2D Japanese anime film still, delicate watercolor textures, soft cinematic lighting. Vertical 9:16. A finished, steaming chicken teriyaki rice bowl (glossy chicken, broccoli, carrots, sesame, green onion) in a cream ceramic bowl on a small wooden table beside the large wooden-framed rainy window, with raindrops on the glass and misty green mountains outside. Yuki sits next to it smiling peacefully: a beautiful young adult anime woman with very long, thick, flowing dark chocolate-brown wavy hair, a large ivory-white ribbon at the back of her hair, small pearl flower earrings, large dark brown eyes, soft rosy cheeks, a cream-white puff-sleeve blouse and a sage-green floral apron. A golden retriever rests on a woven mat nearby. A warm golden pendant lamp lights the meal, contrasting with cool blue-grey rainy light.
```

**Motion (3 s):**
```
The camera slowly moves toward the steaming rice bowl, then gently tilts up to reveal Yuki, who picks up her wooden chopsticks and smiles peacefully. The golden retriever's tail wags slowly. Rain keeps falling outside. End by holding on the beautiful steaming bowl.
```

**ASMR:** `Gentle rainfall, wooden chopsticks lightly touching ceramic, a soft tail swish on the mat, peaceful kitchen ambience fading softly at the end. No music, no voice.`

---

## Edits I made to keep the script consistent

- **Shot 18 vs 19:** your script adds spring onions in both shots. I kept shot 18 to broccoli and carrots, and put all the spring onions in shot 19 with the sesame, so the garnish happens once.
- **Shot 20:** to stay in the same kitchen (continuity rule 4), the "dining table" is a small wooden table beside the same rainy window.
- **Shot 15:** the vegetables are steamed in a bamboo steamer that only appears in this shot. Keep it identical if you regenerate the shot.
- **Rule 8** (no cooked food before it's cooked): the chicken is described as raw in shots 05–06, pale on top in shot 11, golden in shot 12, and glazed from shot 14 onwards.
