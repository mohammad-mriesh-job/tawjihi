# How the ministry writes semester-1 mathematics items — analysis

Purpose: the mock papers must feel like the *next* ministry paper. This document records what the official papers
in this folder show about the ministry's item writing, so new items follow the same method. It is evidence-based:
every rule below cites items from the papers in this folder (file names in `README.md`).

Papers read item by item (multiple-choice part):

| paper | items read | curriculum |
|---|---|---|
| 2026 summer, 2008 generation (`2026-summer-items-01-25.pdf`) | 1–25 (all semester-1 items) | current (2008) |
| 2026 summer repeaters paper 1 (`2026-summer-paper1-repeaters.pdf`) | 1–25 | 2023–2025 books |
| 2025 summer paper 1 · 2025 supplementary paper 1 | 1–25 · 1–25 | 2023–2025 books |
| 2024 summer paper 1 · 2024 supplementary paper 1 | 1–25 · 1–25 | 2023–2025 books |
| 2023 summer paper 1 | 1–25 | 2023–2025 books |
| 2022 summer paper 1, 2021 summer paper 1 (`old-curriculum/`) | 1–11, 11–17 | pre-2023 books |

The rest of the folder (2020–2022 papers) was scanned page by page for format and figures.

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

1. Pick the official item it is modelled on (section 4, or the items listed in section 9) and name it in a comment
   above the `Q(...)`. Keep the model's stem structure, kind of function and numbers, skill and difficulty; change
   only the function and the numbers. Check the 2008 lesson it belongs to.
2. Use a section-3 template; keep the stem short; give units in context items.
3. Build the options as a 2×2 grid of the two most likely mistakes (section 2), or a list of same-kind values.
4. Add a figure when the ministry would (graphs, applied related rates, complex plane, regions).
5. Verify with `qb.py` (truth, option text, stem formulas); for regions, encode each option as a predicate.
6. Explain each wrong option by naming its switch(es) — the explanation must match how the option was built.

## 9. How mock papers 6–10 were written (item-by-item modelling)

The first version of papers 6–10 was written from the textbook and only *restyled* afterwards (options turned into
grids). That is not enough: a mock simulates the ministry only if the **stem, the kind of function and numbers, the
skill and the difficulty** come from real ministry items. Papers 6–10 were therefore rewritten item by item:

1. **Catalogue every official semester-1 item** (sections 1–4 above): stem wording, the function or numbers used,
   the skill, the answer form and how the four options were built.
2. **Assign one official item to every slot** of the 4 · 6 · 12 · 8 layout. The 2026 paper is the blueprint (it is
   the only paper of the 2008 generation): every new paper covers its patterns in the same order. 2023–2025 and the
   2026 repeaters paper add the other in-scope patterns (motion, normal slope of aˣ, kᶿ-type constants, log of a
   product, logarithmic differentiation, h = √(…f…) from values, f∘g from values, a particle on a curve, an
   isosceles-triangle area rate, roads and a fixed station, Argand point → trig form, z – k z̄ equations, a square
   in the plane, Arg of i·z, max Arg on a circle, square roots, the perpendicular bisector from a figure, an
   annulus, a wedge, a single disc). Extrema, concavity and optimisation are skipped (not in the 2008 units).
3. **Write a sibling, not a copy**: keep the model's structure (e.g. 2026 #13 `log₃(2 + ln x)` at `e` →
   `log₂(3 + ln x)` at `e`, answer `1/(e ln 16)`, same e-vs-1/e × ln-power grid; 2026 #16 `4ˣ ln y = x/y − 1` at
   `y = 1` → `5ˣ ln y = x/y − y + 1` at `y = 1`, unit-fraction options), change the function and numbers, keep the
   difficulty (same number of steps, same kind of trap).
4. **Rebuild the options with the model's grid** (section 2) and make every distractor a real, nameable mistake;
   when a ministry list has no mistake behind it (small integers, unit fractions), the explanation checks the value
   by substitution instead of inventing a reason.
5. **Check against the earlier mocks and the unit banks**: no repeated formula and no repeated context with new
   numbers (two items were replaced for that: a repeated drug-concentration context and a repeated denominator).
6. **Record the model** in a comment above each `Q(...)` in `mock-exams/s1_papers_6_10.py`; the table below is
   generated from those comments.

Models used by papers 6–10: 2026 — 77 items, 2025 — 20, 2025s — 18, 2023 — 17, 2024 — 16, 2024s — 14,
2026r — 13 (some items name two models).

| item | modelled on (official item) · option grid |
|---|---|
| m6q1 | 2026 #1: one root given, equation not set to zero, options = signs of the other two roots |
| m6q2 | 2026 #2: repeated linear factor, "which is the decomposition", options = numerators swapped x sign |
| m6q3 | 2026 #3: equal remainders on two linear divisors -> constant, options = sign x magnitude |
| m6q4 | 2026 #2 (distinct linear factors version): which is the decomposition, options = numerators swapped x factor signs |
| m6q5 | 2026 #4: tan(theta/2) from cos theta and a quadrant, options = sign x reciprocal |
| m6q6 | 2026 #5: simplest form with a sum identity, options = coefficient x sin/cos |
| m6q7 | 2026 #6: equivalent expression (one reciprocal ratio), options = csc/sec/2sin/2cos |
| m6q8 | 2026 #4 sibling (double angle from one ratio and a quadrant), options = sign x sin/cos value |
| m6q9 | 2026 #7: quadratic in a trig ratio, one root rejected, single quadrantal answer |
| m6q10 | 2026 #8: reciprocal ratio -> double angle, interval (pi, 2pi); options = halved or not x shifted or not |
| m6q11 | 2026 #9: f'(x) x f(x) for a sin/cos sum collapses to a double angle; options = sign x sin/cos |
| m6q12 | 2025 #5 / 2025s #5: slope of the normal to an exponential a^(linear); options = sign x slope/normal slope |
| m6q13 | 2026 #10: root times polynomial with a constant, f'(a) given -> constant; options = small integers |
| m6q14 | 2026 #11: combination of f'' and f' for a sum of exponentials; options = sign x exponent |
| m6q15 | 2026 #12 (temperature after sunset): a cooling model in context, units in stem and options; sign x power slip |
| m6q16 | 2026 #14 / 2024s #5: two piecewise-linear graphs, h built from f and g; options = sign x magnitude |
| m6q17 | 2026 #13: log base a of (c + ln x), f'(e); options = e vs 1/e x ln(a^n) right vs wrong |
| m6q18 | 2025 #9 / 2026r #6: h = root of an expression in f, values f(a), f'(a) given; options = sign x missing 1/2 |
| m6q19 | 2026 #15: parametric with sec/tan at a special t; options = reciprocal x factor 2 |
| m6q20 | 2026 #16: a^x ln y = rational in x, y; point found from y = 1; options = unit fractions |
| m6q21 | 2026 #17: tangent to a root relation at a lattice point, y-intercept; options = integers from typical slips |
| m6q22 | 2024s #12 (ripples): area rate given, rate of the circumference; options = factor 2 x pi slip |
| m6q23 | 2026 #19: z = a + bi with a sign condition and /z/ given -> trigonometric form; options = quadrant x reference angle |
| m6q24 | 2026 #20-21: one shared stem, two operations; options = real part x imaginary part slips |
| m6q25 | 2026 #21: second item of the shared stem (product zw); options = real part x imaginary part slips |
| m6q26 | 2026r #19 / 2025 #19: equation in z and its conjugate; options = sign of each part |
| m6q27 | 2026 #22: two values of a constant making a quotient real; options = +-k list |
| m6q28 | 2026 #23: quadratic with a given complex root; options = sign of the sum x sum/product swapped |
| m6q29 | 2026 #24: smaller angle between two numbers in different quadrants (difference > pi) |
| m6q30 | 2026 #25: disc (solid) cut by a wedge whose vertex is not the centre, one ray dashed; options = vertex sign x strictness |
| m7q1 | 2026 #1 with a fractional root (zero of 2x - 1), equation not set to zero; options = signs of the other two roots |
| m7q2 | 2026 #2 (irreducible quadratic factor version); options = A halved or not x sign of the linear numerator |
| m7q3 | 2026 #3 extended to two constants (factor + remainder); options = sign of each constant |
| m7q4 | 2026 #3 (remainder theorem) with high powers of a negative number; options = the parity slips |
| m7q5 | 2026 #4 with cos(theta/2) from tan theta; options = sign x sin/cos of the half angle |
| m7q6 | 2026 #5 with a difference identity; options = coefficient x sin/cos |
| m7q7 | 2026 #6 (equivalent expression) |
| m7q8 | 2026 #5 family: exact value from a difference of special angles; options = order of the surds x sign |
| m7q9 | 2026 #7 after a Pythagorean substitution (quadratic in cos x, three solutions); options = include 0 x sign of cos |
| m7q10 | 2026 #8: reciprocal ratio -> sin 2x; options = halved or not x second period or not |
| m7q11 | 2025 #2 / 2026r #5: value of the derivative of a trig combination; options = sec^2 vs sec x sign of the cos term |
| m7q12 | 2024 #6: x-coordinate where the tangent is parallel to a given line (exponential minus linear) |
| m7q13 | 2025s #8: exponential growth model, rate given -> the initial constant N; options = slips with the 0.5 |
| m7q14 | 2024s #7: third derivative of a polynomial plus a reciprocal; options = sign x keeping a constant |
| m7q15 | 2026r #3 / 2025 #3: two graphs, h a quotient of f and g; options = numerator order x slope sign |
| m7q16 | 2025 #8: product of an exponential composite and a root composite at 0; options = chain-factor slips |
| m7q17 | 2024s #11: log base a of a quadratic at a point; options = ln a missing / inverted x divided by u or not |
| m7q18 | 2025 #10: k^(trig x), f'(a) given as a logarithm -> k; options = k, its reciprocal, its square, negative |
| m7q19 | 2026 #15 / 2023 #8: parametric (polynomial and log); options = reciprocal x missing chain factor |
| m7q20 | 2024 #9: y^2 and ln(xy) at a point; options = terms of d/dx ln(xy) dropped |
| m7q21 | 2024 #10 / 2023 #10: variable base and exponent, logarithmic differentiation; options = factor y x factor 2 |
| m7q22 | 2024 #11 / 2025 #12: angle of elevation of a rising object, with a figure; options = sign x missing cos^2 |
| m7q23 | 2025 #18: trigonometric form of a number shown as a point; options = quadrant x reference angle |
| m7q24 | 2025 #21-22 / 2025s #21-22: shared stem, Arg of a difference then a quotient |
| m7q25 | 2026r #21: second item of the shared stem (quotient z/w); options = i^2 slip x conjugate slip |
| m7q26 | 2025 #24 / 2025s #25: modulus of a product given -> two values of a constant |
| m7q27 | 2026r #24 / 2025s #24: a complex root of a quadratic with unknown real coefficients |
| m7q28 | 2025 #20 / 2024s #23: Arg of an expression in z given -> constant; options = quadrant x sign of the shift |
| m7q29 | 2023 #24: greatest Arg of points on a circle |
| m7q30 | 2025 #25: annulus with one dashed circle; options = centre sign x which circle is strict |
| m8q1 | 2026 #1 phrased with a given factor; options = signs of the other two zeros |
| m8q2 | 2026 #2 (improper fraction): quotient kept or dropped x constants swapped |
| m8q3 | 2026 #3: a relation between two remainders -> constant; options = sign x parity slip |
| m8q4 | remainder theorem with a quadratic divisor from two given remainders (2026 #3 extension) |
| m8q5 | 2026 #4 with sec theta given, asking sin(theta/2); options = sign x sin/cos half-angle formula |
| m8q6 | 2026 #5: simplest form (sum of two sines); options = coefficient x sin/cos |
| m8q7 | 2026 #6: equivalent expression (Pythagorean identities in a quotient) |
| m8q8 | double angle from a squared relation (2026 #4 family); options = sign x 1 -/+ (1/2)^2 |
| m8q9 | 2026 #7: quadratic in cos with one solution rejected by an OPEN interval; options = single angles |
| m8q10 | 2026 #8 family: double angle against a single angle, factor (do not divide by cos x) |
| m8q11 | 2025s #2: sin/cos with a pi coefficient at a quadrantal angle; options = sign x which term survives |
| m8q12 | 2026r #2: slope of the normal for ln plus reciprocal; options = sign x slope/normal slope |
| m8q13 | 2024s #4: velocity when the acceleration is zero; options = velocity sign x other quantities |
| m8q14 | 2023 #5: f' given, a higher derivative asked; options = sign x one derivative too many |
| m8q15 | 2025s #4 (plant height): quotient model in context; options = sign x squared denominator |
| m8q16 | 2025s #3 / 2024 #4: one graph, h = exponential times f; options = sign x f -/+ f' |
| m8q17 | 2025s #11: power of a logarithm to base a; options = ln a position x chain factor 2 |
| m8q18 | 2025s #9: composite from tables of values; options = sign x evaluating g' at the wrong point |
| m8q19 | 2026 #15: parametric (cos/sin) at a special angle; options = sign x reciprocal |
| m8q20 | 2023 #9 / 2026 #16: implicit with a trig term at a lattice point; options = sign of cos(pi) x moving a term |
| m8q21 | 2026 #17: tangent to an implicit curve, x-intercept; options = slope slips |
| m8q22 | 2026 #18: cylinder with a figure, L/min -> m/min, draining; options = unit conversion x radius/diameter |
| m8q23 | 2026r #18: trigonometric form of a product written as i-multiple; options = quadrant x reference angle |
| m8q24 | 2026r #21-22: shared stem (conjugate and modulus of a product) |
| m8q25 | 2026r #25: second item of the shared stem (/zw/); options = add vs multiply moduli |
| m8q26 | 2024 #22 / 2023 #21: equality with a quotient -> real constant; options = sign x answering b instead of a |
| m8q27 | 2023 #23 / 2024 #24: one square root of a complex number has a given form |
| m8q28 | 2024 #20: Arg of a related number in terms of alpha (multiplication by i rotates by pi/2) |
| m8q29 | 2024 #25 / 2023 #25: perpendicular bisector shown with its two points; options = sign of A x sign of B |
| m8q30 | 2025s #23 / 2026r #23: a wedge from a point, one ray dashed; options = vertex sign x strictness |
| m9q1 | 2026 #1: one negative root given, equation not set to zero |
| m9q2 | 2026 #2 with a repeated factor and a distinct factor; options = B,C swapped x sign of A |
| m9q3 | 2026 #3 with a divisor (ax + b); options = right zero x sign slips |
| m9q4 | 2026 #1 family: complete factorisation (find a zero by trial, then factor); options = sign patterns |
| m9q5 | 2026 #4 from sin theta in the 4th quadrant; options = sign x reciprocal |
| m9q6 | 2026 #5: simplest form; options = coefficient x sin/cos |
| m9q7 | 2026 #6: equivalent expression (fraction minus a ratio) |
| m9q8 | sum-to-product exact value (2026 #5 family); options = surd slips |
| m9q9 | 2026 #7 family: Pythagorean identity gives a perfect square in tan; options = second quadrant vs third x one solution |
| m9q10 | 2026 #8: double angle in the interval (pi, 2pi); options = shifted or not x halved or not |
| m9q11 | 2025 #1 / 2025s #1: ln of a quotient with a power of e; options = constant kept x 1/(2x) vs 1/sqrt x |
| m9q12 | 2024s #6 / 2025s #6: tan/cot of a multiple of x at a point; options = chain factor pi x squared or not |
| m9q13 | 2025s #10 / 2025 #4: position at the first instant of momentary rest; options = positions at other instants |
| m9q14 | 2026 #11: combination of derivatives of a trig sum; options = sign x sin/cos |
| m9q15 | 2026r #11: bacteria with a fractional exponent base, units in options; options = sign x missing square |
| m9q16 | 2026 #14 with a composite: h = f(g(x)) read from two graphs; options = sign x evaluating f' at x instead of g(x) |
| m9q17 | 2025 #11: log of a product of conjugate factors; options = ln 10 position x sign of the denominator |
| m9q18 | 2024s #8: ln of a squared trig ratio at a special angle; options = sign x cot vs tan |
| m9q19 | 2023 #8: parametric derivative as a function of t; options = reciprocal x sign |
| m9q20 | 2026 #16: a^(xy) relation, point from x = 0; options = sign x ln a dropped |
| m9q21 | 2026 #17: tangent to x y^2 = c at a lattice point, y-intercept; options = slope slips |
| m9q22 | 2023 #11: two perpendicular roads, distance to a fixed station; options = sign x wrong side in the ratio |
| m9q23 | 2024 #23: power of a number given in a "minus" trig form; options = modulus power x sign of the angle |
| m9q24 | 2024 #21 + 2025 #22: shared stem (difference of squares; 1/z + w/5) |
| m9q25 | 2025 #22: second item of the shared stem (1/z + w/5); options = conjugate slips |
| m9q26 | 2024s #21: modulus and an Arg range fix a constant |
| m9q27 | 2024s #20 / 2023 #19: equal complex numbers with a quadratic real part condition |
| m9q28 | 2023 #22: quotient in trigonometric form; options = divide/multiply moduli x subtract/add arguments |
| m9q29 | 2025 #23: a square in the complex plane, rotation by i; options = rotation direction x wrong vertex |
| m9q30 | 2026 #25 family: disc cut by a perpendicular bisector; options = centre sign x which boundary is strict |
| m10q1 | 2026 #1: the other two roots are fractions/negatives; options = sign of each root |
| m10q2 | 2026 #2: repeated linear factor with a negative second constant; options = sign x constants swapped |
| m10q3 | 2026 #3: equal remainders; options = sign x parity slip in f(-1) |
| m10q4 | factor theorem with (2x - 1) -> constant (2026 #3 family); options = the zero used |
| m10q5 | 2026 #4 from tan theta in the 2nd quadrant, asking cos(theta/2); options = sign x sin/cos formula |
| m10q6 | 2026 #5: simplest form (difference of two cosines); options = coefficient x sin/cos |
| m10q7 | 2026 #6: equivalent expression for tan + cot |
| m10q8 | product-to-sum exact value; options = sign x missing factor 2 |
| m10q9 | 2026 #7: quadratic in cos with one root rejected (/cos x/ <= 1); options = sign x reference angle |
| m10q10 | 2026 #8 family: tan 2x = 1 in [0, pi); options = halved or not x second solution |
| m10q11 | 2024 #2: trig with a shifted angle plus a polynomial over pi; options = sign of sin(-pi/2) x sign of the result |
| m10q12 | 2024s #10 / 2024 #7: a^(linear), f'(a) given -> a |
| m10q13 | 2024 #3: velocity when the particle returns to its starting position |
| m10q14 | 2024 #5: second derivative of sec x plus a constant; options = one product-rule term missing x constant differentiated |
| m10q15 | 2025s #12: particle moving on a curve, dx/dt given -> dy/dt; options = sign x missing inner derivative |
| m10q16 | 2025 #3: two graphs, u = f + c/g; options = sign x squared denominator |
| m10q17 | 2023 #1: exponential of a root; options = coefficient 2/3 vs 3/2 x root in the denominator or numerator |
| m10q18 | 2026r #7: trig of a power of x (chain rule); options = inner derivative kept x sign of cos |
| m10q19 | 2026 #15: parametric with exponentials at t = ln 2; options = reciprocal x missing chain factor 2 |
| m10q20 | 2026 #16: x e^y + y = 2x - 1, point from y = 0; options = unit fractions / slips |
| m10q21 | 2023 #10: d/dx (ln y) for a variable base and exponent; options = cot vs tan x sign |
| m10q22 | 2023 #12: isosceles triangle, angle rate -> area rate (with a figure); options = cos vs sin x factor 1/2 |
| m10q23 | 2025s #20: modulus and Arg of the conjugate -> standard form; options = sign of the imaginary part x cos/sin swapped |
| m10q24 | 2025s #18-19: shared stem (quotient by a pure imaginary; modulus of a square) |
| m10q25 | 2025s #18: second item of the shared stem (/z^2/); options = /z/, a part of z^2, /z/^4 |
| m10q26 | 2024 #18 / 2023 #18: power of i times a root of a negative number; options = sign x real/imaginary |
| m10q27 | 2024s #24: cube of a complex number; options = i^2 and i^3 slips |
| m10q28 | 2023 #20: modulus fixes a constant inside a fraction; options = small values |
| m10q29 | 2024s #19: conjugate read from a point in the complex plane; options = which signs change |
| m10q30 | 2024s #25: a disc read from the figure; options = centre coordinates swapped x signs |
