# How the ministry writes semester-1 mathematics items — analysis

Purpose: the mock papers must feel like the *next* ministry paper. This document records what the official papers
in this folder show about the ministry's item writing, so new items follow the same method. It is evidence-based:
every rule below cites items from the papers in this folder (file names in `README.md`).

Papers read item by item (multiple-choice part):

| paper | items read | curriculum |
|---|---|---|
| 2026 summer, 2008 generation (`2026-summer-items-01-25.pdf`) | 1–25 (all semester-1 items) | current (2008) |
| 2025 summer paper 1 | 1–25 | 2023–2025 books |
| 2024 summer paper 1 | 1–25 | 2023–2025 books |
| 2024 supplementary paper 1 | 1–13 | 2023–2025 books |
| 2025 supplementary paper 1 | 4–8, 13–16, 21–25 | 2023–2025 books |
| 2022 summer paper 1, 2021 summer paper 1 (`old-curriculum/`) | 1–11, 11–17 | pre-2023 books |

The rest of the folder (2023, 2026 repeaters, 2020–2022 papers) was scanned page by page for format and figures.

## 1. Paper format (2026, the format the next exam follows)

- One paper for both semesters: **50 multiple-choice items, 3 hours, 12 pages**, model (1).
  Semester 1 = items 1–25: unit 1 items 1–3, unit 2 items 4–8, unit 3 items 9–18, unit 4 items 19–25.
  (Our 30-item / 90-minute semester-1 mocks keep this order, scaled to 4 · 6 · 12 · 8.)
- Options are `a) b) c) d)` on the question paper; the bubble sheet uses أ ب ج د. Options are one per line, short.
- Items follow the lesson order of the book inside each unit; there is **no separation by difficulty** —
  a hard item can sit between two easy ones.
- `❖ ملحوظة: في جميع الفقرات من 19 إلى 25، فإنّ i = √−1 حيثما وردت.` before the complex-numbers block.
- Exactly one shared stem in semester 1: `❖ إذا كان: z = 2 + 3i, w = −2 + 10i ، فاعتمد ذلك للإجابة عن الفقرتين (20) و (21) الآتيتين:`
  (the 2023–2025 papers have the same device, also for complex numbers; older papers used it for graphs).
- The answer key of 2026 is *not* balanced (a 4, b 9, c 7, d 5 over items 1–25). Our mocks keep a balanced key
  (8·8·7·7) — a deliberate difference, because a student should not be able to profit from guessing a letter.

## 2. The distractor rule: a 2×2 grid of two "switches"

The single most consistent feature. The ministry takes the correct answer and flips **two independent features**,
each one a specific mistake; the four combinations are the four options. Options therefore look alike and the
student must get *both* decisions right.

| item | options | the two switches |
|---|---|---|
| 2026 #1 (other two roots) | x = 3, 5 · −3, −5 · −3, 5 · 3, −5 | sign of each root |
| 2026 #3 (remainder, find p) | −12 · −4 · 4 · 12 | sign × magnitude |
| 2026 #4 (tan θ/2) | 1/√5 · −1/√5 · √5 · −√5 | sign (quadrant) × reciprocal |
| 2026 #5 (simplify) | (√3/2) cos x · ½ cos x · (√3/2) sin x · ½ sin x | coefficient × function |
| 2026 #9 (f′·f) | −sin 2x · −cos 2x · cos 2x · sin 2x | sign × sin/cos |
| 2026 #11 (f″ + 2f′) | −8e^{2x} · −8e^{−2x} · 8e^{−2x} · 8e^{2x} | sign × exponent |
| 2026 #12 (rate, °C/h) | ½ · ¼ · −¼ · −½ | sign × magnitude |
| 2026 #13 (log₃ composite) | e/ln 27 · e/ln 9 · 1/(e ln 27) · 1/(e ln 9) | e vs 1/e × ln 27 vs ln 9 |
| 2026 #14 (graph, h′(1)) | 5 · 7 · −5 · −7 | sign × magnitude |
| 2026 #18 (tank, L/min) | 50/π · 20/π · 1/(50π) · 1/(20π) | unit conversion × radius/diameter |
| 2026 #20, #21 (shared stem) | 4+i · 24+5i · 24+i · 4+5i ; 26−14i · −34−14i · −34+14i · 26+14i | real part × imaginary part |
| 2026 #23 (quadratic from root) | x²−2x+5 · x²+2x+5 · x²−5x+2 · x²+5x+2 | sign of the sum × sum/product swapped |
| 2026 #25 (region) | \|z\| ≤ 3 with Arg(z∓1), ≤/< at the lower angle | centre sign × strictness |
| 2025 #5 (normal slope) | ±81/(4 ln 2) · ±1/(324 ln 2) | sign × slope/normal-slope |
| 2025 #12 (camera, rad/h) | ±2.5 · ±2500 | sign × km/m conversion |
| 2025 #23, 2025s #23 (regions) | centre (z+a+bi vs z−a−bi) × which end is strict | centre sign × strictness |
| 2024s #11 (log₄ composite) | 7/ln 4 · 7/(10 ln 4) · 7/10 · 7 ln 4/10 | ln a missing/inverted × chain factor |

Frequency (items read in full): 2026 — 17 of 25 items are grids; 2025 — 16 of 25; 2024 — 11 of 25.
The remaining items use a short list of *plausible values of the same kind*: `±1, ±2, ±3, ±4` for two-valued
constants (2026 #22), unit fractions `1/3, 1/5, 1/4, 1/2` (2026 #16), small integers `15, 10, 6, 3` (2026 #17),
quadrantal angles `3π/2, 0, π/2, π` for a single-solution equation (2026 #7).

Consequences for writing items:
- Choose the two most common mistakes for the skill, make each a switch, and let the grid produce the options.
  Sign, reciprocal, a missing `ln a`, a missing chain factor, radius vs diameter, unit conversion, quadrant,
  the centre of a locus, `<` vs `≤`, sin vs cos, `z` vs `z̄`, sum vs product.
- Never use a distractor that is wrong "in a different way" from the others; all four must look like the same answer.
- Solution sets of trig equations: same numerators with a different denominator, or the same angles shifted out of
  the interval (2026 #8: 5π/8, 7π/8 · 5π/4, 11π/4 · 13π/4, 15π/4 · 13π/8, 15π/8).

## 3. Item templates (phrasing)

- `إذا كان: … ، فإنّ … هو / هي / تساوي:` — the default stem.
- `إذا كان x = −1 حلًّا للمعادلة: …، فإنّ لها حلَّين آخرين هما:` (the equation is *not* set to zero: `x³ + 3x² = 13x + 15`).
- `أيُّ الآتية يُمثِّل تجزئة المقدار النسبي … إلى كسور جزئية؟` · `أيُّ الآتية مكافئ للمقدار: …؟` · `أبسط صورة للمقدار: … هي:`
- `حلّ المعادلة: … في الفترة [0, 2π) هو:` (single solution) · `حلول المعادلة: … في الفترة (π, 2π) هي:`
- `إذا أمكن التعبير عن … بالاقتران: …، حيث t … ، فإنّ معدّل تغيّر … عندما t = 2 هو:` (context items name the units).
- `يُبيّن الشكل الآتي منحنيي الاقترانين f(x) و g(x). إذا كان: h(x) = …، فإنّ h′(1) هي:`
- `إذا مثّل المستقيم l مماسًّا لمنحنى العلاقة: … عند النقطة (4, 9)، فإنّ المقطع y للمستقيم l هو:`
- `يُبيّن الشكل الآتي خزّانًا … مُلئ … بمعدّل 200 L/min ، فإنّ معدّل تغيّر ارتفاع … عند أيّ لحظة هو:`
- `فإنّ القيمتين المُمكنتين للثابت b اللتين تجعلان z عددًا حقيقيًّا هما:` (answer `±3`).
- `نظام المتباينات (بدلالة z) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المظلَّلة في الشكل الآتي هو:`

## 4. Content per 2026 item (semester 1) — the blueprint

| # | lesson | what is asked | answer form |
|---|---|---|---|
| 1 | remainder & factor theorems | other two roots given one root | `x = 3, x = −5` |
| 2 | partial fractions | decomposition with a repeated linear factor | two fractions |
| 3 | remainder theorem | equal remainders → constant | integer |
| 4 | identities 2 | tan(θ/2) from cos θ and quadrant | ±1/√5-type |
| 5 | identities 1 | simplest form with sum/difference | `½ cos x`-type |
| 6 | identities 1 | equivalent expression | `sec x`-type |
| 7 | trig equations | quadratic in cos with a rejected root | single angle |
| 8 | trig equations | reciprocal ratio + double angle in an interval | two angles |
| 9 | special derivatives | product of f and f′ simplifies to a double angle | `−sin 2x` |
| 10 | product rule | constant from f′(−1) | integer |
| 11 | higher derivatives | f″ + 2f′ for a sum of exponentials | `8e^{−2x}`-type |
| 12 | rate of change (context) | temperature after sunset, °C/h | signed fraction + units |
| 13 | chain rule, log base ≠ e | f′(e) for log₃(2 + ln x) | `1/(e ln 27)` |
| 14 | graph | h = f² − g from two piecewise-linear graphs | integer |
| 15 | parametric | dy/dx at t = π/4 (sec/tan) | `1/2`-type |
| 16 | implicit | 4ˣ ln y = x/y − 1 at y = 1 | unit fraction |
| 17 | implicit + tangent | y-intercept of tangent to √x + √y = 5 | integer |
| 18 | related rates (figure) | cylinder, L/min → m/min | `1/(50π) m/min` |
| 19 | trig form | z = 2 + ib, b < 0, \|z\| = 4 | `4(cos(−π/3) + i sin(−π/3))` |
| 20–21 | operations (shared stem) | z + iw + 12 ; zw | `24 + i` ; `−34 − 14i` |
| 22 | real/imaginary condition | two values of b making (b + 9i)/(1 + bi) real | `±3` |
| 23 | complex roots | quadratic with root 1 − 2i | `x² − 2x + 5 = 0` |
| 24 | argument | smaller angle between √3 − i and −3 − 3i | `7π/12` |
| 25 | locus (figure) | disc \|z\| ≤ 3 ∩ wedge from −1 | grid of 4 systems |

## 5. Contexts, figures and numbers

- Contexts are short and concrete, with units in the stem *and* in the options: temperature after sunset (°C/h),
  a fuel tank (m/min), a plant's height (m/month), bacteria (cells/h), a satellite's ground distance, a camera
  following a motorbike (rad/h), a balloon watched from a point (rad/min), a growing cube (cm³/min).
- Figures (2023–2026): two piecewise-linear graphs on a grid (every paper), the graph of f or of f′ for reading
  values, an applied diagram for related rates (cylinder 2026 #18, satellite 2025 #7, camera 2025 #12,
  balloon 2024 #11), a point or polygon in the complex plane (2025 #18, #23), the shaded region (every paper).
- Numbers are clean but not trivial: constants such as `6371 km`, `200e`, `4ˣ`, `log₃(2 + ln x)`, `∛x(x³ + b)`.
  Answers are exact (π, ln, surds); decimals appear only when the context forces them (rad/min, cm).

## 6. What did not carry over to the 2008 curriculum

2023–2025 papers also test limits/continuity (pre-2023 only), extrema, monotonicity, concavity and optimisation
(2025 #13–17, 2024 #13–17, 2024s #13). These lessons are not in the 2008 semester-1 units, so mocks must not use
them. Units 1–2 (polynomials, partial fractions, trig identities and equations) appear only in the 2026 paper —
for those, the 2026 items 1–8 are the only official model.

## 7. Trend 2020 → 2026

- 2020–2022: Arabic notation, options in one row, limits/continuity heavy; already sign/magnitude grids and shared
  stems for graph items.
- 2023–2025: English notation, 25 MCQ + written questions per semester paper; grids in about half the items;
  applied contexts with figures grow every year.
- 2026: all multiple choice, both semesters in one paper; the most systematic grids (17 of 25), short stems,
  each item tests one book lesson, one item per lesson pattern.

## 8. Checklist for a new mock item

1. Map it to a 2008 lesson and to the closest 2026 blueprint row (section 4).
2. Use a section-3 template; keep the stem short; give units in context items.
3. Build the options as a 2×2 grid of the two most likely mistakes (section 2), or a list of same-kind values.
4. Add a figure when the ministry would (graphs, applied related rates, complex plane, regions).
5. Verify with `qb.py` (truth, option text, stem formulas); for regions, encode each option as a predicate.
6. Explain each wrong option by naming its switch(es) — the explanation must match how the option was built.
