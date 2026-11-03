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
- The answer key of 2026 is close to balanced (a 6, b 6, c 6, d 7 over items 1–25). Our mocks keep an exactly balanced
  key (8·8·7·7), so a student cannot profit from guessing a letter.

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
| 2026 #18 (tank, L/min) | 50/π · 20/π · 1/(50π) · 1/(20π) | unit conversion (L → m³) × base area πr² = 4π vs the height 10 used instead |
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
| 5 | identities 1 | simplest form with sum/difference | `(√3/2) cos x` |
| 6 | identities 1 | equivalent expression | `sec x`-type |
| 7 | trig equations | quadratic in cos with a rejected root | single angle |
| 8 | trig equations | reciprocal ratio + double angle in an interval | two angles |
| 9 | special derivatives | product of f and f′ simplifies to a double angle | `cos 2x` |
| 10 | product rule | constant from f′(−1) | integer |
| 11 | higher derivatives | f″ + 2f′ for a sum of exponentials | `8e^{2x}` |
| 12 | rate of change (context) | temperature after sunset, °C/h | signed fraction + units |
| 13 | chain rule, log base ≠ e | f′(e) for log₃(2 + ln x) | `1/(e ln 27)` |
| 14 | graph | h = f² − g from two piecewise-linear graphs | integer |
| 15 | parametric | dy/dx at t = π/4 (sec/tan) | `√2/2` |
| 16 | implicit | 4ˣ ln y = x/y − 1 at y = 1 | unit fraction |
| 17 | implicit + tangent | y-intercept of tangent to √x + √y = 5 | integer |
| 18 | related rates (figure) | cylinder, L/min → m/min | `1/(20π) m/min` |
| 19 | trig form | z = 2 + ib, b < 0, \|z\| = 4 | `4(cos(−π/3) + i sin(−π/3))` |
| 20–21 | operations (shared stem) | z + iw + 12 ; zw | `4 + i` ; `−34 + 14i` |
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

1. Pick the official item it is modelled on (sections 4 and 9; section 10 shows how the mocks use them) and name it in a comment
   above the `Q(...)`. Keep the model's stem structure, kind of function and numbers, skill and difficulty; change
   only the function and the numbers. Check the 2008 lesson it belongs to.
2. Use a section-3 template; keep the stem short; give units in context items.
3. Build the options as a 2×2 grid of the two most likely mistakes (section 2), or a list of same-kind values.
4. Add a figure when the ministry would (graphs, applied related rates, complex plane, regions).
5. Verify with `qb.py` (truth, option text, stem formulas); for regions, encode each option as a predicate.
6. Explain each wrong option by naming its switch(es) — the explanation must match how the option was built.

## 9. Every in-scope pattern of the ministry papers, by lesson

Every multiple-choice item of the seven papers in this folder (2026, 2026r, 2025, 2025s, 2024, 2024s, 2023; 175 items)
was transcribed for the November 2026 revision (stem, options, key, how the options were built) and grouped into
pattern families: same skill and same stem structure. 146 items are in scope for the 2008 units (the rest are limits,
extrema, monotonicity, concavity and optimisation). The family ids (`1a` … `13g`) are used by the mock blueprint.
"E:" marks an *expected* family: a skill of the 2008 book that no ministry paper has asked yet. Units 1–2 appear only in
the 2026 paper, so most of their families are expected; they are written with a ministry template (section 3) and are
never harder than the ministry items of their lesson (≤ 2 computational steps and one trap, no 2×2 system unless one
condition gives one unknown at once, no extraneous roots, at most one synthetic division).

### u1-l1 remainder & factor theorems (only 2026 is official)
- 1a other two roots given one root, equation not set to zero — 2026 #1
- 1b remainder theorem -> constant (equal remainders / relation between remainders) — 2026 #3
- E: 1c factor theorem -> constant (x - a or ax - b is a factor)
- E: 1d factor + remainder -> two constants
- E: 1e remainder on a quadratic divisor from two remainders (r = ax + b)
- E: 1f divisible by a quadratic -> constants
- E: 1g remainder with high powers (f(-1) parity)
- E: 1h synthetic division by (ax - b): quotient and remainder
- E: 1i rational zeros: set of zeros / complete factorisation
- E: 1j rational zeros theorem: which value cannot be a zero
- E: 1k application (volume of a box: other dimensions)
- E: 1l division algorithm f(x) = (x - a)q(x) + r -> value

### u1-l2 partial fractions (only 2026 is official)
- 2a which is the decomposition: repeated linear factor — 2026 #2
- E: 2b which is the decomposition: distinct linear factors
- E: 2c which is the decomposition: irreducible quadratic factor
- E: 2d improper fraction (divide first)
- E: 2e constants of a given decomposition (A + B, ABC, ...)
- E: 2f correct form of the decomposition (unknown constants A, B, C)

### u2-l1 identities 1 (only 2026 is official)
- 3a simplest form with a sum/difference identity — 2026 #5
- 3b equivalent expression (basic / Pythagorean identities) — 2026 #6
- E: 3c exact value by sum/difference (cos 7pi/12, tan 5pi/12)
- E: 3d sin/cos/tan(A +- B) from ratios in given quadrants
- E: 3e cofunction / even-odd: which is not an identity
- E: 3f tan(pi/4 +- x) type simplification

### u2-l2 identities 2 (only 2026 is official)
- 4a half angle from a ratio and a quadrant — 2026 #4
- E: 4b double angle from a ratio and a quadrant
- E: 4c double angle by squaring (sin x - cos x = k)
- E: 4d power reduction / sqrt(2 + 2cos 4x)
- E: 4e product to sum (exact value)
- E: 4f sum to product (exact value / simplest form of a quotient)
- E: 4g double-angle exact value (2 sin 15 cos 15, cos^2 - sin^2)

### u2-l3 trig equations (only 2026 is official)
- 5a quadratic in one ratio, one root rejected, single answer — 2026 #7
- 5b reciprocal ratio + double angle in an interval, options shifted out of it — 2026 #8
- E: 5c equation with a double-angle identity (cos 2x + sin x ...)
- E: 5d Pythagorean substitution -> quadratic
- E: 5e multiple angle in an interval (sin 3x = 1, tan 2x = 1)
- E: 5f number of solutions / sum of solutions in an interval
- E: 5g which value is not a solution (general solution)
- E: 5h half-angle equation in [0, 4pi)
- E: 5i extraneous roots after squaring (sec x + tan x = k)
- E: 5j reciprocal ratio equation 2 sin x = csc x

### u3-l1 special derivatives, tangent/normal, motion
- 6a derivative value of a trig (or trig + exponential) combination at a special angle — 2025 #2, 2025s #2, 2024 #2, 2024s #3, 2024s #6, 2025s #6, 2023 #4, 2026r #1, 2026r #5
- 6o f'(x) f(x) for f = sin x + cos x simplifies to a double angle — 2026 #9
- 6p simplify by an identity, then differentiate ((sin^2 + cos^2)/cos x) — 2026r #10
- 6b ln with log laws first (ln(a x^3), ln(x^n / e)) — 2025 #1, 2025s #1
- 6c exponential quotient that simplifies — 2024s #2
- 6d power rule with a radical — 2024s #9
- 6e b^(kx) with f'(a) given -> a — 2024s #10
- 6f slope of the normal (a^(linear); a ln x + b/x) — 2025 #5, 2025s #5, 2026r #2
- 6g applied figure: h(theta) = r csc(theta) - r, dh/dtheta — 2025 #7
- 6h growth model: rate given -> initial constant N — 2025s #8
- 6i tangent parallel to a given line (e^x - kx) — 2024 #6
- 6j motion: instants of rest — 2023 #3; from an s(t) graph — 2024s #15 (shared graph with #16)
- 6k motion: velocity when the acceleration is zero — 2024s #4; position when the acceleration is zero — 2026r #4
- 6l motion: position when v = 0 (s = A sin kt) — 2025 #4; position at the first instant of rest — 2025s #10
- 6m motion: velocity when the particle returns to its start — 2024 #3
- 6n motion: interval of motion in the negative/positive direction — 2023 #15; from an s(t) graph — 2024s #16

### u3-l2 product/quotient, higher derivatives
- 7a product rule symbolic ((x - a) cos x) — 2023 #2
- 7b higher derivative: f''' from f' (rational) — 2023 #5; f''' of ax - 1/x — 2024s #7; f'' of csc x + e^2 at pi/4 — 2024 #5
- 7h combination of derivatives f'' + k f' of e^(kx) + e^(-kx) (one term cancels) — 2026 #11
- 7g constant from f'(a) for a product with a cube root — 2026 #10
- 7c one/two graphs (product/quotient rule): f g — 2024s #5; f + k/g — 2025 #3; g e^(-x) at a smooth max — 2025s #3; -1/f — 2024 #4; f/(g + c) — 2026r #3
- 7d quotient rule with sin 2x / cos 2x, simplified — 2025 #6
- 7e rate of change of a rational model in context (units in the options) — 2026 #12 (temperature k/(t + c)^2, deg C/h), 2025s #4 (plant height)
- 7f point where f' equals a value, domain picks one root — 2025s #7

### u3-l3 chain rule, parametric
- 8a exponential of a root e^(cbrt x) — 2023 #1
- 8b sqrt(ln x) expressed through f — 2023 #6
- 8c a^(quadratic): horizontal tangent — 2023 #7, 2026r #8; f'(x0) given -> a — 2024 #7
- 8d parametric dy/dx: a sec t, tan t + c at pi/4 — 2026 #15; tan^2 t, sec^2 t (constant slope) — 2023 #8
- 8e ln of a squared trig ratio at a special angle — 2024s #8
- 8f log base a of a composite — 2026 #13 (log3(2 + ln x) at e), 2024s #11 (quadratic at a point), 2025 #11 (log10 of a product), 2025s #11 ((log2(x - 1))^3), 2024 #8 (log10 tan x), 2026r #9 (log10 of a polynomial)
- 8g product of an exponential composite and a root composite at 0 — 2025 #8
- 8h composite of f from values: h = root of (c + k f^m) — 2025 #9; h = (c - k f)^n — 2026r #6
- 8k two graphs, chain rule: h = f^2 - g — 2026 #14
- 8l trig of a power of x: x - k cos((ax)^2) — 2026r #7
- 8m exponential composite in context: bacteria k a^(1/(t + 1)) — 2026r #11
- 8i k^(cot x), f'(a) given as a logarithm -> k — 2025 #10
- 8j (f o g)'(a) from a list of values — 2025s #9

### u3-l4 implicit differentiation
- 9a implicit slope at a point (point found from y = 1; cos with e^(ln x); y^2 = ln(xy)) — 2026 #16, 2023 #9, 2024 #9
- 9c tangent to an implicit curve, intercept (sqrt x + sqrt y = c) — 2026 #17
- 9b logarithmic differentiation (d/dx ln y for x^(x^2); x^(1/x)) — 2023 #10, 2024 #10

### u3-l5 related rates
- 10a two perpendicular roads, fixed station — 2023 #11
- 10b isosceles triangle, angle rate -> area rate — 2023 #12
- 10c ripples: dA/dt -> dC/dt — 2024s #12
- 10d camera above a road, angle rate when right below (figure) — 2025 #12
- 10e particle on a curve: dx/dt -> dy/dt — 2025s #12
- 10f balloon / rising object, angle of elevation (figure) — 2024 #11
- 10g cube side growing at a constant rate, dV/dt after t — 2024 #12
- 10h cylindrical tank filled in L/min, dh/dt in m/min (figure) — 2026 #18
- 10i sphere (balloon): dr/dt -> dV/dt — 2026r #13

### u4-l1 complex numbers
- 11a i^n times the root of a negative number — 2023 #18, 2024 #18, 2024s #18
- 11n trig form of z = a + ib with a sign condition and |z| — 2026 #19; trig form of k i (a + bi) — 2026r #18
- 11o smaller angle between two numbers (difference of arguments) — 2026 #24
- 11b equality of complex numbers -> unknown — 2023 #19, 2024s #20
- 11c modulus fixes a constant — 2023 #20, 2024 #19
- 11d conjugate read from an Argand diagram — 2024s #19
- 11e modulus and an Arg range fix a constant — 2024s #21
- 11f trig form with a quadrantal angle -> standard form — 2024s #22
- 11g Arg of an expression in z -> constant — 2024s #23, 2025 #20, 2026r #20 (Arg(a + i) = pi/6)
- 11h Arg of the number with swapped parts in terms of alpha — 2024 #20
- 11i trig form of a point drawn as a vector — 2025 #18
- 11j shared stem: Arg(z - w) — 2025 #21, 2025s #21
- 11k |z^2| — 2025s #18
- 11l |z| and Arg(conj z) -> standard form — 2025s #20
- 11m |z1 z2| given -> two values of p — 2025s #25

### u4-l2 operations
- 12a (a^2 + b^2)/(a + bi) = p + qi -> ab — 2023 #21; equality with a quotient -> a — 2024 #22
- 12b quotient in trig form — 2023 #22; z^2 in trig form from a "minus" form — 2024 #23
- 12c a square root has a given form -> a — 2023 #23, 2024 #24
- 12d cube of a complex number — 2024s #24
- 12e z -+ k conj(z) = a + bi -> z — 2025 #19, 2026r #19
- 12f shared stem, two operations on z, w — 2026 #20-21 (z + iw + k; zw), 2026r #21-22 (z/w; 2z - 3w), 2025 #22 (1/z + w/|z|^2), 2025s #22 (z + k conj w), 2024 #21 (z^2 - w^2)
- 12g square in the complex plane, two adjacent vertices — 2025 #23
- 12h |z1/z2| = k -> +-p — 2025 #24
- 12i division by a pure imaginary number — 2025s #19
- 12j quadratic with a complex root: which equation — 2026 #23; root given -> b — 2025s #24; -> a + b — 2026r #24
- 12k two values of b making a quotient real (+-k) — 2026 #22
- 12l |z1 z2| for two given numbers (surd) — 2026r #25

### u4-l3 loci
- 13a greatest Arg on a circle — 2023 #24
- 13b perpendicular bisector drawn with its two points -> equation — 2023 #25, 2024 #25 (flawed: line through O)
- 13c closed disc read from the figure (centre coordinates x sign) — 2024s #25
- 13d annulus, inner solid / outer dashed (centre sign x strictness) — 2025 #25
- 13e wedge from a point, one ray dashed (vertex sign x strictness) — 2025s #23
- 13f disc cut by a wedge whose vertex is not the centre, one ray dotted — 2026 #25
- 13g a single ray Arg(z - z0) = theta read from a figure (vertex sign x angle) — 2026r #23

Patterns asked by the ministry in most papers: a derivative value of a trigonometric combination at a special angle
(`6a`, 9 items), a logarithm to base a of a composite (`8f`, 6 of 7 papers), a graph item (`7c`/`8k`, every paper), a
shared stem on two complex numbers (`12f`, every paper since 2025), a shaded region or a line in the complex plane
(`13*`, every paper). The written questions add parametric second derivatives, implicit tangents and a sand cone
(related rates); they are not multiple choice, so the mocks take only their skills.

## 10. How the ten mock papers were written (item-by-item modelling)

**First versions.** Papers 1–5 were written from the textbook in the ministry's style. Papers 6–10 were first written
from the textbook and only restyled (options turned into grids); that is not enough, so on 2026-10-15 they were
rewritten item by item, each as a sibling of a named official item.

**Revision of all ten papers (2026-11-03).** A student found the papers repetitive, and the user asked for papers that
together cover every ministry pattern plus the items one can expect from the ministry's way of writing:

1. **Transcribe and catalogue** every official semester-1 item (section 9).
2. **Map the 300 existing items onto the families.** The 2026 patterns sat in 7–10 papers each (implicit slope at a
   point 9, half angle 8, simplest form with a sum identity 8, other two roots 7, parametric 7), while 18 official
   families were missing (instants of rest, the applied csc figure, a single ray from a figure, the camera above a road,
   a quadrantal trig form, …).
3. **Blueprint, slot by slot** (KEEP / NEW / REWRITE), with the variety rule of CLAUDE.md applied to the mock papers:
   each 2026 item is modelled directly in at most five papers (most in three to five); no two items of one pattern in
   one paper; any two papers share at most half of their patterns per lesson (sub-forms of a family count as different
   patterns, e.g. `log₃(2 + ln x)` at e vs `log₁₀` of a product); every official in-scope family appears at least once,
   except "extraneous roots after squaring", left out as harder than the ministry; a shared stem and a complex-plane
   figure in every paper, as the ministry does, with different operations and regions.
4. **Write and check.** 112 items are new questions: the 76 planned slots, plus kept items made easier because they
   were harder than their model (an extra step, a 2×2 system, a quartic) and items that repeated another paper or a
   unit-bank item; 29 more got a corrected difficulty label. Every
   item names its model in a comment above its `Q(...)`; the five region items of papers 1–5, formerly verified by hand,
   are now computed like the others (options as predicates).

Models used by the ten papers: direct siblings 214 (2026 — 83, 2025s — 23, 2025 — 22, 2026r — 22, 2023 — 22,
2024 — 22, 2024s — 20), expected items 85; 137 distinct official items are cited. The table below is generated from
the comments in `mock-exams/s1_papers_1_5.py` and `s1_papers_6_10.py`.

| item | modelled on (official item) · option grid |
|---|---|
| m1q1 | 2026 #1: one root given, equation not set to zero (x^3 + ax^2 = bx + c), the quotient factors over the integers; options = sign of each of the other two roots |
| m1q2 | E (expected: remainder on a quadratic divisor from two remainders), template 2026 #3: the divisor x gives b at once, then f(2) gives a; options = zero of (x - 2) right or wrong (sign of a) x remainder written ax + b or bx + a |
| m1q3 | 2026 #2: which is the decomposition, repeated linear factor; options = constants swapped, sign of B, the constant term taken as A |
| m1q4 | E (expected: constants of a given decomposition), template 2026 #2 / #10: x = 4 gives a at once, then x = -2 gives A; options = small integers (a alone, A alone, a slip) |
| m1q5 | 2026 #4: sin(theta/2) from cos theta and a quadrant (3rd); options = sign x sin/cos half-angle formula |
| m1q6 | 2026 #5: simplest form with a sum identity, one term cancels; options = coefficient (cos vs sin of pi/3) x surviving function, and the coefficient dropped |
| m1q7 | E (expected: double angle from a ratio and a quadrant), template 2026 #4: cos 2theta from tan theta in the 2nd quadrant; options = sign x cos 2theta / sin 2theta value |
| m1q8 | E (expected: sum to product, exact value), template 2026 #5: cos 75 + cos 15; options = special values (sin 30 used for cos 30, cos 30 alone, 1) |
| m1q9 | 2026 #7: quadratic in sin x, one root rejected (sin x = -3); options = solution pairs (sign of sin x, reference angle, quadrant) |
| m1q10 | E (expected: half-angle equation in an interval), template 2026 #8: tan(x/2) + 1 = 0 in [0, 2pi), so x/2 in [0, pi); options = doubled or not x interval of x/2 halved or not (an extra solution shifted out of the interval) |
| m1q11 | 2026 #9: f'(x) and f(x) combine into one ratio (f = sec x + tan x, f'/f = sec x); options = sec x, tan x, sec x tan x, csc x |
| m1q12 | 2025 #6: dy/dx of (a + sin 2x)/(b + cos 2x), numerator simplified with sin^2 + cos^2, denominator rewritten as (b - 1 + 2cos^2 x)^2; options = numerator constant 2 vs 1 x denominator form (right, wrong identity, not rewritten) |
| m1q13 | 2025s #7: point on y = k/(x + c) with a domain restriction where f'(x) has a given value, the domain rejects one root; options = which root of (x - 1)^2 = 4 x sign of the y-coordinate |
| m1q14 | 2024s #11: log base a of a quadratic at a point; options = ln a missing / inverted, chain factor slip |
| m1q15 | 2026r #5: f'(special angle) of a reciprocal-trig function minus (c + another one): tan x - (2 + csc x) at pi/4 -> sec x - (4 + cot x) at pi/6; options = list of values (the sum, sign slip on the bracket term, each term alone) |
| m1q16 | 2023 #15: interval of motion in the negative direction for a cubic s(t); options = intervals built from the zeros of v |
| m1q17 | 2024s #5: two piecewise-linear graphs, product rule h = f g at a point; options = integers from the readings (sign of g', f(1) alone) |
| m1q18 | 2025s #4 (plant height t^2/(4 + t^2): quotient rule at t = 1, units in the options): drug concentration 20t/(t^2 + 4); options = numerator order (sign), the value C(1), a slip |
| m1q19 | 2026 #15: parametric with csc/cot at a special t; options = reciprocal (dx/dy), sign, sin used for cos |
| m1q20 | 2024 #9: implicit dy/dx of y^2 = ln(xy) at (e, 1) -> y^3 = ln(xy) at (e, 1); options = y'/y kept or dropped in d/dx ln y x sign of that term when it is collected |
| m1q21 | 2026 #17: tangent to an implicit curve at a lattice point, y-intercept; options = sign slip in the line, the slope, sign of the intercept |
| m1q22 | 2026 #18: cylindrical tank (figure: height and base diameter in m) filled in L/min, constant dh/dt in m/min; options = L -> m^3 conversion done or not x base area pi r^2 vs the height used instead of r^2 |
| m1q23 | 2026 #19: z = a + bi with a sign condition and |z| given -> trig form; options = quadrant and reference-angle slips |
| m1q24 | 2026 #20 (z + iw + k) / 2026r #22 (2z - 3w): shared stem, 2z - iw; options = real part x imaginary part slips |
| m1q25 | 2026r #21: second item of the shared stem, the quotient z/w; options = sign of the imaginary part, parts divided separately, i^2 slip |
| m1q26 | 2024 #19: z = c + ai with |z| given -> the positive value of a; options = 2x2 value grid (5 or 3 under the root x root taken or not) |
| m1q27 | 2024s #18: sqrt(-p/q) x k i^n in simplest form (answer real and negative); options = sign x real vs imaginary |
| m1q28 | 2026 #24: smaller angle between two numbers in different quadrants (difference of the arguments below pi); options = the larger angle, Arg z2 taken positive, Arg z1 alone |
| m1q29 | E (expected: Cartesian equation of a locus |z - z1| = |z - z2|), template 2023 #25 (perpendicular bisector): square both moduli and simplify; options = sign slips, the slope of the segment itself |
| m1q30 | 2026 #25: disc (solid) cut by a wedge whose vertex is not the centre, one ray dashed; options = vertex sign x which boundary is strict |
| m2q1 | E (expected: rational zeros, the set of zeros of a cubic), template 2026 #1: one zero, one synthetic division, factor the quotient; options = sets of three zeros (signs) |
| m2q2 | 2026 #3: remainders on division by (x - 3) and (x + 1) related (here one is twice the other) -> the constant k; options = small integers |
| m2q3 | E (expected: partial fractions with an irreducible quadratic factor), template 2026 #2: which is the decomposition; options = sign of A x sign of C |
| m2q4 | E (expected: remainder on division by the quadratic x(x - 1), high power), template 2026 #3: remainder theorem at the zeros 0 and 1 of the divisor; options = ax + b vs its pieces |
| m2q5 | E (expected: exact value by a sum identity), template 2026 #5: cos(pi/3 + pi/4) with exact values; options = sign x sqrt2 - sqrt6 vs sqrt2 + sqrt6 |
| m2q6 | 2026 #6: equivalent expression for tan x + cot x (quotient identities -> common denominator -> Pythagorean -> reciprocal); options = single trig expressions |
| m2q7 | E (expected: sin(A + B) from ratios in given quadrants), template 2026 #4: the missing ratio with its quadrant sign; options = sign x 87 vs 297 (one sign slip) |
| m2q8 | E (expected: double angle by squaring sin x - cos x = k), template 2026 #4: a double-angle value from a given relation; options = 1 - k^2 vs the slips k^2, sign, 1 + k^2 |
| m2q9 | E (expected: general solution -- which value is not a solution), template 2026 #7: one trig equation; options = four angles, three of them from x = 2pi/3 + n pi |
| m2q10 | E (expected: equation with a double-angle identity), template 2026 #7: cos 2x = 1 - 2 sin^2 x gives a factorable quadratic in sin x; options = complete set vs a lost factor x sign |
| m2q11 | E (expected: derivatives of a^x and log_a x), template 2025 #2: value of the derivative of a two-term combination at a point; options = ln 4 below / missing / multiplied x sign |
| m2q12 | 2024s #4 with the roles swapped (v = 0 as in 2025 #4 / 2025s #10): acceleration at the instant of rest; options = values with units (a(0), v(1)) |
| m2q13 | 2024 #6: x-coordinate where the tangent is parallel to a line ax + by + c = 0 (linear minus k ln x here); options = slope -a/b vs +a/b vs the x-coefficient, and the y-coordinate |
| m2q14 | 2024s #7 (higher derivative), exponential as in 2026 #11: f^(5) of e^(-2x); options = sign of (-2)^5 x 32 vs 10 / 16 |
| m2q15 | 2026 #10: constant from a given derivative value (a quotient here instead of the product with a cube root); options = small integers (-4 = numerator order of the quotient rule reversed, 3 = the -1 term lost) |
| m2q16 | 2024 #4: g = -1/f with f(a) and f'(a) read from ONE piecewise-linear graph; options = sign x f(a)^2 vs f(a) |
| m2q17 | 2025 #8: f'(0) of c e^(x^n) sqrt(kx + b), product of two composites with the first term vanishing at 0; options = small values (inner factor 2 lost, 1/2 of the root lost, 0) |
| m2q18 | 2023 #7: x where a^(x^2 + c) has a horizontal tangent; options = small integers 0-3 (2 = the base, 3 = the constant of the exponent) |
| m2q19 | E (expected: second derivative by implicit differentiation), template 2026 #16: implicit derivative at a given point; options = sign x factor slips |
| m2q20 | E (expected: horizontal tangent of an implicit curve), template 2026 #17: tangent to an implicit curve at lattice points; options = numerator vs denominator of dy/dx set to 0 (vertical tangents) x signs of the roots read off the factors |
| m2q21 | 2024 #12: cube whose side grows at a constant rate from a given length; dV/dt after t minutes (update the side first); options = side 12 vs 9 (time added instead of rate x time) x rate factor kept/dropped |
| m2q22 | 2024 #11: angle of elevation of an object rising vertically, watched from a point a fixed distance away (figure); dtheta/dt at a given height; options = decimals with the unit |
| m2q23 | E (expected: negative and large powers of i), template 2023 #18: value of an expression in powers of i; options = sign of the real part x sign of the imaginary part |
| m2q24 | 2025s #21: first item of a shared stem, Arg(z - w) where z - w is purely imaginary; options = sign x pi/2 vs pi/4 (w - z, z + w) |
| m2q25 | 2025s #22: second item of the shared stem, z + 2 conj(w); options = sign of the real part x sign of the imaginary part (6 - 7i = conj(z) + 2w) |
| m2q26 | 2026 #23: quadratic (real coefficients) with the complex root 3 - i; options = sign of the sum / product with i^2 = +1 / sum halved |
| m2q27 | 2023 #22: quotient of two numbers given in trig form (unlike denominators, one negative argument), answer in trig form; options = moduli divided vs subtracted x arguments subtracted vs the sign of -pi/4 lost |
| m2q28 | 2025 #19: z - k conj(z) = a + bi -> z; options = sign of the real part / sign of the imaginary part / the given number misread |
| m2q29 | E (expected: intersection of two loci), template 2023 #25 (perpendicular bisector |z - z1| = |z - z2|) with the circle |z| = r: the points on both; options = line y = -x vs y = x / radius slip / one point lost |
| m2q30 | 2026 #25 (13f): solid disc cut by a dashed perpendicular-bisector half-plane; options = centre sign x which boundary is strict |
| m3q1 | E (expected: synthetic division by (ax - b)), template 2026 #1: divide by the zero 2/3, then the quotient by 3; options = quotient divided by 3 or not x remainder kept or tripled (+ a sign slip) |
| m3q2 | E (expected: factor theorem in an application, box volume), template 2026 #1: divide V(x) by the given height, then factor the quotient; options = signs of the two factors / other factor pairs of 10 |
| m3q3 | E (expected: improper fraction, divide first), template 2026 #2: one division step (quotient x), then two linear factors; options = quotient kept or dropped x sign of the second constant |
| m3q4 | E (expected: constants of a given decomposition), template 2026 #2: three distinct linear factors, one substitution per constant (x = 0, 1, -1); options = small integers |
| m3q5 | E (expected: related angles and even-odd identities, which one is NOT an identity), template 2026 #6 ("أيُّ الآتية"); options = four related-angle statements, tan(pi - x) = tan x is the false one |
| m3q6 | E (expected: tan(pi/4 + x) by the sum identity), template 2026 #5 ("أبسط صورة"): one expression, tan(pi/4) = 1; options = numerator/denominator swapped (difference formula) x sign of the denominator |
| m3q7 | 2026 #4: tan(theta/2) from cos theta and a quadrant; options = sign x reciprocal |
| m3q8 | E (expected: product to sum, exact value), template 2026 #5 (one identity, then exact values): sin 105 cos 15; options = surd forms (difference instead of sum, sin 90 lost) |
| m3q9 | E (expected: number of solutions in a closed interval), template 2026 #7: quadratic in cos x on [0, 2pi], the end 2pi counted; options = small counts |
| m3q10 | E (expected: half-angle equation), template 2026 #8: cos(x/2) = 1/2 on [0, 4pi), the interval halved; options = halved or not x the second solution |
| m3q11 | 2024s #2: y'(1) of an exponential quotient by x that simplifies (here e^3 x^2 - e^(3x)); options = sign (the factors 2 and 3 swapped) x a stray constant 1 (as the model) |
| m3q12 | 2023 #6: f'(x) of the root of a logarithm, written through f(x) (here sqrt(2 ln x)); options = arrangements of x, f(x) and a constant (derivative of the log inverted, derivative of the root inverted, the 1/2 dropped) |
| m3q13 | 2025 #7: applied right-triangle figure, h = r csc(theta) - r (here a boat and a round island, r = 300 m), dh/dtheta at pi/4; options = sign x sqrt2 vs 1/sqrt2 (csc vs sin of pi/4) |
| m3q14 | 2023 #3: instants of rest of a cubic s(t) with a fractional coefficient (v = 0 has integer roots); options = pairs of times (the zero 5/2 of a(t) mixed in, as the model) |
| m3q15 | 2026 #10: constant from a derivative value of a product (product rule, evaluate, solve a linear equation); options = small values |
| m3q16 | 2026 #14 (composite version, as m9q16): two piecewise-linear graphs, p = f(g(x)), p'(5); options = sign, g(5) used for g'(5), one factor only |
| m3q17 | 2024 #8: log base a of a trig function (here log2(cos x)), its value at pi/4; options = sign x ln 2 divided or multiplied (+ tan(pi/4) taken as sqrt2) |
| m3q18 | 2026r #11: exponential model in context, rate of growth at a given time (here the simpler 1000 e^(0.05t)); options = the rate vs the value P(20) x e^(0.05t) kept or dropped |
| m3q19 | E (expected: tangent line to a parametric curve), template 2026 #15: the point and dy/dx at t = 0, then the line; options = intercept slips x slope inverted |
| m3q20 | E (expected: normal to an implicit curve, its y-intercept), template 2026 #17: slope at a lattice point, normal slope -1/m, then x = 0; options = values from the slips (tangent instead of normal, slope not negated, y0 dropped) |
| m3q21 | 2026 #16: implicit slope at a point with a ln y term (here x ln y + y^2 = 4, the point handed over); options = sign x the factor 2y dropped (+ ln 2 taken as 1) |
| m3q22 | 2025 #12: an elevated observer above a straight road (here a hovering helicopter's searchlight, 120 m) tracking a car at 60 km/h, dtheta/dt when the car is right below; options = sign x km/h not converted to m/h. Figure. |
| m3q23 | 2026 #19: z = a + bi with b < 0 and |z| given -> trigonometric form; options = quadrant x reference angle |
| m3q24 | 2026 #22: a constant making a quotient real (one value here, the constant in the numerator only); options = sign x magnitude (3/2 = the pure-imaginary condition) |
| m3q25 | 2023 #21: (a^2 + b^2)/(a + bi) = p + qi -> a x b (the quotient is the conjugate a - bi); options = product vs sum x sign of b (the quotient read as a + bi) |
| m3q26 | 2026 #20-21: first item of a shared stem on z, w (here the modulus |z - w|, a modulus as 2026r #25); options = |z + w|, the sum of the parts, |z| - |w| |
| m3q27 | 2026 #21: second item of the shared stem, a product (here z times conj w); options = i^2 slip, the imaginary part |
| m3q28 | 2026 #24: smaller angle between two numbers in the lower half-plane (4th and 3rd quadrants), difference of the arguments; options = sizes added, |Arg z2| alone, |Arg z1| alone |
| m3q29 | 2026r #23: equation of a single ray Arg(z - z0) = theta read from a figure (open vertex, dashed reference line); options = vertex sign x the angle vs its reference angle |
| m3q30 | 2025 #25: annulus with one dashed circle (here its upper half, cut along a diameter like the 2026 #25 disc and wedge); options = centre sign x which circle is strict |
| m4q1 | 2026 #1: one root given (here the fraction 1/2, equation already set to zero) -> the other two roots; options = sign of each root |
| m4q2 | E (expected: divisible by a quadratic -> one constant; one zero of the divisor gives it at once), template 2026 #3: options = sign x magnitude (14 = the value of 2k, not divided by 2) |
| m4q3 | E (expected: decomposition with distinct linear factors), template 2026 #2: which is the decomposition; options = numerators swapped / sign of one numerator (a list, as the model) |
| m4q4 | E (expected: one constant of a given decomposition), template 2026 #2 (repeated linear factor): C from x = 2; options = the values of C, A, B and the coefficient 3 |
| m4q5 | 2026 #5: simplest form with the sum/difference identities (the sin terms cancel); options = coefficient x cos/sin |
| m4q6 | 2026 #6: equivalent expression (common denominator, Pythagorean identity -> one reciprocal function); options = 2csc vs 2sec, the constant 2, csc without the factor 2 |
| m4q7 | E (expected: double-angle formula used backwards: cos theta from cos 2theta and the quadrant), template 2026 #4; options = cos vs sin of theta, the square root forgotten, a value that fails the check |
| m4q8 | E (expected: power reduction sin^2 u = (1 - cos 2u)/2), template 2026 #5 grid: sin^2x cos^2x = (1 - cos 4x)/8; options = coefficient 1/8 vs 1/4 (the 1/2 squared or not) x 1 - cos 4x vs 1 + cos 4x (sin^2 vs cos^2 formula) |
| m4q9 | E (expected: reciprocal-ratio equation 2 sin x = csc x), template 2026 #8 (solutions in an interval); options = the interval respected or not / a quadrant missed / the square root forgotten |
| m4q10 | E (expected: multiple angle sin 3x = 1 in [0, 2pi)), template 2026 #8 (interval of the multiple angle, then divide); options = one turn only / the values of 3x not divided / a value that is not a solution |
| m4q11 | 2025 #1 / 2025s #1: ln(a x^n) simplified by the log laws (here ln 5x); options = the constant 5 kept x u'/u slips |
| m4q12 | 2024 #5 / 2024s #7: a higher derivative at a point (product rule once, then the power rule); options = small values |
| m4q13 | 2026r #10: an expression that collapses by a Pythagorean identity to one reciprocal function, then f'(x); options = csc vs sec x sign |
| m4q14 | 2026r #4: cubic s(t), position when the acceleration is zero; options = v(2) / s at the instant v = 0 / 0 (in m) |
| m4q15 | E (expected: n-th derivative of sin/cos by the cycle of 4), template 2026 #9 (f = sin x + cos x); options = the four derivatives f''', f', f'', f |
| m4q16 | 2026 #14: two piecewise-linear graphs, h = f^2 - g, h'(1); options = sign of the g' term / g' dropped / sign |
| m4q17 | E (expected: ln of a quotient, split by the log laws first), template 2025s #1 (log laws, then the derivative); options = sign x one term dropped |
| m4q18 | 2026r #11: exponential model in context, rate at a given time, units in the options (bacteria -> a cooling cup of tea); options = sign / the factor 0.5 dropped / e^(-1) read as e |
| m4q19 | 2024 #7: a^(quadratic) whose exponent vanishes at x = 3, f'(3) given -> a (a power of e); options = chain factor kept/dropped x sign of the exponent |
| m4q20 | E (expected: second derivative of a parametric curve), template 2026 #15 (parametric dy/dx); options = the first derivative given instead / slips in the second division |
| m4q21 | 2023 #10: d/dx(ln y) for y = x^(x^3) (variable base and exponent); options = sign x ln x^3 vs (ln x)^3 |
| m4q22 | 2026 #18: cylindrical tank (figure: base diameter) leaking in L/min -> constant rate of the level in cm/min; options = L -> cm^3 conversion done or not x r^2 vs r (one filler, 120/pi) |
| m4q23 | E (expected: principal argument of r(cos + i sin) written with a negative r), template 2024 #23 (a "minus" trig form); options = the printed angle kept / not reduced to (-pi, pi] / wrong quadrant |
| m4q24 | 2026 #20: first item of a shared stem (conj(z) - 2w); options = real part x imaginary part slips |
| m4q25 | 2026 #21: second item of the shared stem (product zw); options = i^2 = +1 / sign of the imaginary part / parts multiplied separately |
| m4q26 | 2024 #24: a - i sqrt2 (a > 0) is a square root of 1 - 2i sqrt6 -> a; options = same-kind surds (sqrt2 dropped from 2a sqrt2 = 2 sqrt6; multiplied instead of divided; a filler, as the model) |
| m4q27 | 2026 #23: quadratic with a given complex root; options = sign of the sum / product slips |
| m4q28 | 2024s #22: r(cos theta + i sin theta) with a quadrantal angle (3pi/2 here) -> standard form; options = imaginary vs real axis x sign |
| m4q29 | 2023 #25: perpendicular bisector drawn on a grid with its two points (the line does not pass through O); options = sign of each point's term |
| m4q30 | 2025 #25: ring between two circles with the same centre, one circle dashed (here the inner one); options = centre sign x which circle is strict |
| m5q1 | E (expected: complete factorisation, one zero found by trial), template 2026 #1: one synthetic division + factor the quadratic quotient; options = signs of the two other factors (2026 #1 grid) |
| m5q2 | E (expected: factor + remainder -> constants; the equal-remainder condition gives b at once), template 2026 #3: equal remainders -> constant; options = sign x 4a not divided by 4 (2026 #3 grid) |
| m5q3 | E (expected: decomposition with an irreducible quadratic factor), template 2026 #2: which is the decomposition; options = numerator sign / A not halved (6) / a constant over the quadratic |
| m5q4 | E (expected: the correct FORM of a decomposition with a repeated linear factor), template 2026 #2: which is the decomposition (repeated linear factor); options = lower power missing / wrong factor repeated / two first-power terms |
| m5q5 | E (expected: cofunction / even-odd identities), template 2026 #6 («أيُّ الآتية …؟»); options = four identities of the same shape, the false one has the sign of a cofunction switched |
| m5q6 | E (expected: tan(A + B) from two ratios in given quadrants), template 2026 #4: a ratio and a quadrant -> exact value; options = sign x tan B with the wrong sign (= tan(A - B)) |
| m5q7 | E (expected: double-angle exact value), template 2026 #5 (one identity, 2x2 grid); options = sin vs cos of 2a x coefficient kept vs doubled |
| m5q8 | E (expected: power reduction under a root), template 2026 #5: simplest form; options = angle 2x vs 4x, coefficient 2 vs sqrt2, cos vs sin |
| m5q9 | E (expected: sum of the solutions in an interval), template 2026 #7: quadratic in sin x on [0, 2pi); options = roots lost by dividing by sin x / only sin x = 0 / 3pi/2 taken for sin x = 1 |
| m5q10 | E (expected: Pythagorean substitution -> quadratic in sin x, one root rejected), template 2026 #7: quadratic in one ratio with a root outside [-1, 1]; options = sign of sin x x reference angle pi/6 vs pi/3 |
| m5q11 | 2024s #9: f'(x) of a root of a power of x, answer as a radical (power rule); options = sign x root in the denominator (exponent -1/4) vs numerator (+1/4) |
| m5q12 | 2023 #2: product rule, symbolic f'(x); options = sign x which function survives (product rule written as a difference) |
| m5q13 | 2025 #4: s(t) = A sin(kt) in cm, position when the velocity is zero; options = +-A, +-k, 0, +-Ak (new context: a fishing float on waves) |
| m5q14 | E (expected: x-intercept of a tangent line), template 2026 #17: tangent at a point -> intercept; options = values from the tangent-line computation (point coordinate, sign slip, 1/2) |
| m5q15 | 2026 #10: cube root times a polynomial with a constant, f'(-1) given -> constant; options = small integers (1/3 dropped, sign of the second term, (-1)^2 taken as -1) |
| m5q16 | 2026r #3: quotient of two piecewise-linear graphs at a point; options = sign x magnitude (numerator order reversed, slope of f read with the wrong sign, + instead of -) |
| m5q17 | 2024s #11: log base a of an algebraic composite at a point; options = ln 3 missing / (sqrt x)' taken as 1/sqrt x / not divided by u(1) = 2 |
| m5q18 | E (expected: context model, the time when the rate of change is zero), template 2026 #12 (rate of a context function, units in the options); options = list of times (0.5 and 10 are constants of the model) |
| m5q19 | E (expected: point of a horizontal tangent of a parametric curve), template 2026 #15; options = sign of y / t = -2 (rejected) / t = 1 (vertical tangent) |
| m5q20 | 2024 #10: dy/dx of a variable base and exponent by logarithmic differentiation, answer in x and y; options = factor y kept/forgotten x (sqrt x)' with/without the 2 |
| m5q21 | 2026 #17: tangent to an implicit curve at a lattice point, y-intercept; options = values from the tangent-line computation (sign slip, the slope, the constant of the relation) |
| m5q22 | 2026r #13: sphere, related rates between V and r (here dV/dt given -> dr/dt); options = reciprocal / r^2 slips |
| m5q23 | 2025s #25: |z1 z2| given -> the two values of p in z1 = a + pi; options = +-k pairs (|z2|, no squaring, |z1|) |
| m5q24 | 2023 #22: quotient of two numbers given in trig form, answer in trig form; options = moduli divided vs subtracted x arguments subtracted vs added |
| m5q25 | 2026r #20: the real a from Arg(a + bi) = special angle; options = list (tan inverted, |z| from sin, its negative) |
| m5q26 | 2026r #22: first item of a shared stem, a linear combination a z + b w; options = overall sign (subtraction reversed) x imaginary part 17 vs 1 (-2(-4i) taken as -8i) |
| m5q27 | 2024 #21 family: second item of the shared stem, w^2 in standard form; options = i^2 = +1 slip x middle term 2ab halved |
| m5q28 | 2023 #24: greatest principal Arg of the points on a circle |z - c| = r with |c| = 2r; options = multiples of pi/6 (Arg of the centre, the half-angle alone, half-angle pi/3 from cos) |
| m5q29 | E (expected: equation of a circle from its centre and a point on it), template 2023 #25 (equation in z of a locus); options = centre sign / radius vs r^2 / conjugate centre |
| m5q30 | 2025s #23: wedge from a point, one ray dashed, open vertex; options = vertex sign x which ray is strict |
| m6q1 | E (expected: factor theorem, (x + 2) is a factor -> the constant), template 2026 #3: options = sign x magnitude (10 = the value of -2k, not divided by -2) |
| m6q2 | 2026 #2: repeated linear factor, "which is the decomposition", options = numerators swapped x sign |
| m6q3 | 2026 #3: equal remainders on two linear divisors -> constant, options = sign x magnitude |
| m6q4 | E (expected: decomposition with distinct linear factors), template 2026 #2: which is the decomposition; options = numerators swapped x signs of the factors |
| m6q5 | 2026 #4: tan(theta/2) from cos theta and a quadrant, options = sign x reciprocal |
| m6q6 | 2026 #5: simplest form with a sum identity (cos(x + pi/3) + k sin x, the sin terms cancel); options = coefficient x cos/sin |
| m6q7 | E (expected: simplest form with related angles pi + x, pi/2 - x and the even function cos), template 2026 #5 grid: options = sign of sin(pi + x) x cofunction cos(pi/2 - x) = sin x right or wrong (cos vs sin survives) |
| m6q8 | E (expected: double-angle exact value from 1 - 2sin^2 a = cos 2a), template 2026 #9 grid (double angle): options = sign (quadrant of 2a) x cos 2a vs sin 2a |
| m6q9 | 2026 #7: quadratic in sin x factoring as (sin x - 2)(sin x + 1), one root rejected, single quadrantal answer; options = the four quadrantal angles (sign slip in the factors / sin-cos confusion) |
| m6q10 | 2026 #8: reciprocal ratio -> double angle, interval (pi, 2pi); options = halved or not x shifted or not |
| m6q11 | 2026 #9: f'(x) x f(x) for a sin/cos sum collapses to a double angle; options = sign x sin/cos |
| m6q12 | 2025s #5 (also 2025 #5): slope of the normal to a^(linear) at a point; options = tangent vs normal slope x sign (2025s #5 grid) |
| m6q13 | 2026 #10: root times polynomial with a constant, f'(a) given -> constant; options = small integers |
| m6q14 | 2026 #11: combination of f'' and f' for a sum of exponentials; options = sign x exponent |
| m6q15 | 2026 #12 (temperature after sunset -> a patient's temperature after a fever reducer): c + k/(t + 1)^2, rate at t = 1, units in stem and options; options = sign x the factor 2 of the power dropped (2026 #12 grid) |
| m6q16 | 2024s #5: h = f g read from two graphs (product rule), graphs and options in the 2026 #14 format (two piecewise-linear graphs on a grid; options = sign x magnitude) |
| m6q17 | 2026 #13: log base a of (c + ln x), f'(e); options = e vs 1/e x ln(a^n) right vs wrong |
| m6q18 | 2025 #9: h = root of (c + f^m) from the values f(a), f'(a); options = sign x missing 1/2 (model: sign x missing inner factor) |
| m6q19 | 2026 #15: parametric with sec/tan at a special t; options = reciprocal x factor 2 |
| m6q20 | 2026 #16: a^x ln y = rational in x, y; point found from y = 1; options = unit fractions |
| m6q21 | 2026 #17: tangent to a root relation at a lattice point, y-intercept; options = integers from typical slips |
| m6q22 | 2024s #12 (ripples -> an oil spill): dA/dt given -> dC/dt at a radius; options = factor 2 x pi slip (3/pi = dr/dt, as the model) |
| m6q23 | 2026 #19: z = a + bi with a sign condition and |z| given -> trigonometric form; options = quadrant x reference angle |
| m6q24 | 2026 #20: first item of a shared stem (z + iw + k -> 2z - iw); options = i^2 = +1 slip x sign slip in the imaginary part |
| m6q25 | 2026 #21: second item of the shared stem (product zw); options = real part x imaginary part slips |
| m6q26 | 2025 #19: z - k conj(z) = a + bi -> z; options = sign of the imaginary part (z vs conj z) x real and imaginary parts swapped |
| m6q27 | 2026 #22: two values of a constant making a quotient real; options = +-k list |
| m6q28 | 2026 #23: quadratic with a given complex root; options = sign of the sum x sum/product swapped |
| m6q29 | 2026 #24: smaller angle between two numbers in the lower half-plane (difference of the arguments < pi); options = the difference / the sizes added / one argument alone / reference angles subtracted |
| m6q30 | 2026 #25: disc (solid) cut by a wedge whose vertex is not the centre, one ray dashed; options = vertex sign x strictness |
| m7q1 | 2026 #1 with a fractional root (zero of 2x - 1), equation not set to zero; options = signs of the other two roots |
| m7q2 | E (expected: decomposition with an irreducible quadratic factor), template 2026 #2: which is the decomposition; options = A halved or not x sign of the linear numerator |
| m7q3 | E (expected: factor theorem then remainder theorem), template 2026 #3: the factor (x - 2) gives a at once, then the remainder on (x + 1) is f(-1); options = sign slip in a x zero of (x + 1) taken as 1 |
| m7q4 | E (expected: remainder theorem with high powers of -1), template 2026 #3: remainder on (x + 1) = f(-1); options = the parity slips |
| m7q5 | E (expected: product to sum, exact value), template 2026 #5 (special values): cos A cos B with A - B = pi/6, A + B = pi/4; options = + vs - between the cosines x factor 1/2 kept/lost |
| m7q6 | 2026 #5 with a difference identity; options = coefficient x sin/cos |
| m7q7 | E (expected: tan(pi/4 + x) = k -> tan x), template 2026 #4 grid: tangent-sum identity, then a linear equation; options = sign of tan x in the identity x numerator/denominator order (reciprocal) |
| m7q8 | E (expected: exact value by a difference identity), template 2026 #5: sin(pi/3 - pi/4) with exact values; options = order of the surds x sum vs difference |
| m7q9 | E (expected: Pythagorean substitution -> quadratic in cos x), template 2026 #7: factorable quadratic in cos x, three solutions; options = include 0 x sign of cos |
| m7q10 | 2026 #8: reciprocal ratio -> sin 2x = -1/2 on the half-period interval (pi, 2pi), doubled for 2x; options = halved or not x interval doubled or not |
| m7q11 | 2025 #2 / 2026r #5: value of the derivative of a trig combination; options = sec^2 vs sec x sign of the cos term |
| m7q12 | 2024 #6: x-coordinate where the tangent is parallel to a given line (exponential minus linear); options = chain factor 2 lost / slope sign / ln 4 not halved |
| m7q13 | 2025s #8: exponential growth model, rate given -> the initial constant N; options = slips with the 0.5 |
| m7q14 | 2024s #7: third derivative of a polynomial plus a reciprocal; options = sign x keeping a constant |
| m7q15 | 2026r #3 (h = f/(g + 1)) / 2024s #5 (both rule terms): two piecewise-linear graphs, h = f/g at a grid point; options = numerator order x slope sign |
| m7q16 | 2025 #8: product of an exponential composite and a root composite at 0; options = chain-factor slips |
| m7q17 | 2026r #9: dy/dx of log (base 10, not written) of a polynomial, domain given; options = ln 10 below / above / missing, or the fraction inverted |
| m7q18 | 2025 #10: k^(trig x), f'(a) given as a logarithm -> k; options = k, its reciprocal, its square, negative |
| m7q19 | 2026 #15 / 2023 #8: parametric (polynomial and log); options = reciprocal x missing chain factor |
| m7q20 | E (expected: normal line to an implicit curve), template 2026 #17: a line at a lattice point of an implicit curve, one intercept asked; options = normal vs tangent x x- vs y-intercept |
| m7q21 | 2024 #10: dy/dx (slope at any point) of x^(ln x) by logarithmic differentiation, answer in x and y; options = factor y kept/forgotten x factor 2 of (ln x)^2 |
| m7q22 | 2024 #11: angle of elevation of an object rising vertically, watched from a point a fixed distance away (figure); dtheta/dt at a given height; options = sign x sec^2 kept/forgotten |
| m7q23 | 2025 #18: trigonometric form of a number shown as a point (here in the third quadrant); options = sign of the argument (quadrant III vs II) x reference angle pi/6 vs pi/3 |
| m7q24 | 2025 #21: first item of a shared stem, Arg(z - w) on a diagonal (reference angle pi/4); options = the four angles with reference pi/4 |
| m7q25 | 2026r #21: the quotient z/w of the shared numbers (there it is the first item of the stem); options = i^2 slip x conjugate slip |
| m7q26 | 2025s #25: |z1 z2| given -> the two values of p in z1 = a + pi (|z2| = 5 from 3 + 4i); options = +-k pairs (+-10 = |z1| itself) |
| m7q27 | 2026r #24 / 2025s #24: complex root with one unknown part of a real quadratic -> a + b; options = sign of b x a vs a^2 |
| m7q28 | 2025 #20 / 2024s #23: Arg of an expression in z given -> constant; options = quadrant x sign of the shift |
| m7q29 | 2023 #24: greatest Arg of the points on a circle |z - c| = r with |c| = 2r; options = multiples of pi/6 (pi/6 = Arg of the centre, 0 = least value) |
| m7q30 | 2025 #25: annulus with one dashed circle; options = centre sign x which circle is strict |
| m8q1 | E (expected: factor theorem in an application), template 2026 #1: volume of a cylindrical can and its height (x + 3) given -> divide, the quotient is r^2 = (x + 2)^2; options = sign x radius vs diameter |
| m8q2 | E (expected: improper fraction, divide first), template 2026 #2: quotient kept or dropped x constants swapped |
| m8q3 | 2026 #3: a relation between two remainders -> constant; options = sign x parity slip |
| m8q4 | E (expected: remainder on a quadratic divisor, the remainder on x gives b at once), template 2026 #3: r(x) = ax + b with f(0) = b, f(-3) = -3a + b; options = sign of a (the zero of x + 3 taken as 3) x remainder written bx + a |
| m8q5 | 2026 #4: sin(theta/2) from sec theta and a quadrant; options = sign x sin/cos half-angle formula |
| m8q6 | E (expected: related angles and the odd identity), template 2026 #5 ("أبسط صورة", two terms combine into one): cos(pi/2 + x) = -sin x, sin(-x) = -sin x; options = sign of the first reduction x sign of the odd identity (k sin x) |
| m8q7 | 2026 #6: equivalent expression (common denominator, Pythagorean and reciprocal identities); options = factor 2 kept or lost x sec vs csc |
| m8q8 | E (expected: double angle by squaring), template 2026 #4 (one given value -> another ratio): sin x - cos x = 2/3; options = sign x 1 -/+ (2/3)^2 |
| m8q9 | 2026 #7: quadratic in cos with one solution rejected (here by the OPEN interval); options = single angles |
| m8q10 | E (expected: equation with a double-angle identity), template 2026 #8 (solutions in an interval): factor, do not divide by cos x; options = cos x = 0 kept or lost x sin/cos angles |
| m8q11 | 2025s #2: sin/cos with a pi coefficient at a quadrantal angle; options = sign x which term survives |
| m8q12 | 2026r #2: slope of the normal for a ln x + b/x; options = sign x slope/normal slope |
| m8q13 | 2024s #4: velocity when the acceleration is zero; options = velocity sign x other quantities |
| m8q14 | 2023 #5: f' given (a rational expression to split first), f''' asked; options = sign x one derivative too many |
| m8q15 | 2025s #4 (plant height): quotient model in context; options = sign x squared denominator |
| m8q16 | 2025s #3: one graph, h = an exponential times f (product rule), h'(1); options = sign x f(1) -/+ f'(1) |
| m8q17 | 2025s #11: power of a logarithm to base a; options = ln a position x chain factor 2 |
| m8q18 | 2025s #9: composite from a list of values (one decoy value); options = sign x g' evaluated at the wrong point |
| m8q19 | 2026r #6: h = (c - k f(x))^n with f(a), f'(a) given (here (5 - 2f)^3 at x = 2); options = the inner factor -2 kept or lost x sign |
| m8q20 | 2023 #9: implicit relation with a trig term (pi coefficient) at a lattice point; options = sign of cos(pi) x a term moved with the wrong sign |
| m8q21 | 2026 #17: tangent to an implicit curve at a lattice point, here its x-intercept; options = slope slips |
| m8q22 | 2026 #18: cylinder with a figure, L/min -> m/min, draining; options = unit conversion x radius/diameter |
| m8q23 | 2026r #18: trigonometric form of k i (a + bi); options = quadrant x reference angle |
| m8q24 | 2025s #22 (and 2026r #22, a linear combination): shared stem, conj(z) + 2w; options = which number is conjugated |
| m8q25 | 2026r #25: |z1 z2| for two given numbers (here the second item of the shared stem); options = moduli added vs multiplied, |z|^2 |
| m8q26 | 2024 #22: equality with a quotient -> the real constant a; options = sign x answering b instead of a |
| m8q27 | 2023 #23: one square root of a complex number has a given form (real part given) -> b; options = sign x b vs b^2 |
| m8q28 | 2024 #20: Arg of a related number in terms of alpha (here -3 + 2i = i(2 + 3i), a rotation by pi/2); options = pi/2 vs pi x order/sign |
| m8q29 | 2023 #25: perpendicular bisector drawn with its two points (the line does not pass through O); options = sign of each point's term |
| m8q30 | 2025s #23: a wedge from a point (open vertex), one ray dashed; options = vertex sign x strictness |
| m9q1 | E (expected: division algorithm f(x) = (x - a)q(x) + r), template 2026 #3: remainder on division by (x - 1) given -> the constant; options = +-2, +-6 (zero sign, term moved, k taken as that remainder) |
| m9q2 | 2026 #2: repeated linear factor, "which is the decomposition"; options as the model = A, B swapped and two wrong forms (linear numerator over the square, + and -) |
| m9q3 | 2026 #3 (remainder theorem -> constant) with one remainder and a divisor (ax + b); options = the right zero -1/2, the zeros +1/2 and -2, a sign slip |
| m9q4 | E (expected: rational zeros theorem, a value that is not a possible zero), template «أيُّ الآتية …؟» (2026 #2, #6); options = fractions p/q, the answer is the swapped fraction 4/3 |
| m9q5 | E (expected: double angle by squaring), template 2026 #4 (a given relation -> a value): sin x + cos x = 1/3 -> sin 2x; options = sign (1 moved the wrong way) x halved (sin x cos x) |
| m9q6 | 2026 #5: simplest form, ONE difference formula sin(x - pi/6) plus k cos x, the cos terms cancel; options = coefficient x sin/cos |
| m9q7 | E (expected: cos(A - B) from one ratio of each angle in given quadrants), template 2026 #4 (ratio + quadrant -> value); options = difference vs sum formula x sign of cos B (+-77/85, +-13/85) |
| m9q8 | E (expected: sum to product, exact value), template 2026 #5: cos A - cos B at multiples of pi/12; options = sign of -2 sin sin x sin(pi/6) vs cos(pi/6) |
| m9q9 | E (expected: equation with a double-angle identity), template 2026 #8 (solutions in an interval): cos 2x = cos x on [0, pi]; options = signs of the factors x the quadrantal root kept or dropped |
| m9q10 | 2026 #8 without the reciprocal ratio: cos 2x = -1/2 on (pi, 2pi), interval doubled for 2x; options = interval doubled or not x halved or not |
| m9q11 | 2025s #1: ln of a power of x over a power of e, log laws first; options = constant kept x chain factor of sqrt x (1/(2x) vs 1/sqrt x) |
| m9q12 | 2025s #6 (cot pi x at 1/4) / 2024s #6: tan of a multiple of x at a point; options = chain factor pi kept or dropped x sec squared or not |
| m9q13 | 2025s #10: s = c - k sin t, position at the first instant of momentary rest (the first zero of v); options = the start s(0), the second rest, the amplitude |
| m9q14 | 2026 #11: f'' + 2f' for sin 2x + cos 2x (2026: e^(2x) + e^(-2x)), one function cancels; options = sign x surviving function |
| m9q15 | 2026r #11: growth model c a^(1/(t+m)) in a new context (fish; base 1/8, exponent 1/(t+2)), rate at t = 1, unit in the stem only; options = sign x missing square (40 vs 120) |
| m9q16 | 2026 #14 with a composite: h = f(g(x)) read from two graphs; options = sign x evaluating f' at x instead of g(x) |
| m9q17 | 2025 #11: log10 of a product (a - x)(a + x) on an interval; options = ln 10 up or down x sign (denominator written x^2 - 4) |
| m9q18 | 2024s #8: ln of a squared trig ratio (csc^2 here, sec^2 in 2024s) at a special angle; options = sign x cot vs tan |
| m9q19 | 2026 #15 (x = a sec t, y = tan t) asked as a function of t, as 2023 #8 asks the derivative itself; options = reciprocal x sign |
| m9q20 | 2026 #16: a^(xy) relation, the point from x = 0 (2026 finds x from y = 1); options = sign of ln 3 x sign of 1 (y' moved across) |
| m9q21 | E (expected: horizontal tangent of an implicit curve), template 2026 #17 (tangent to a relation): x^2 + xy + y^2 = 12 at (a, b), b > 0 -> a; options = numerator vs denominator of dy/dx = 0 (2 vs 4) x the sign of b |
| m9q22 | 2023 #11: two perpendicular roads, fixed station, the car moving away; options = sign x divided by the fixed side 8 instead of the hypotenuse 10 |
| m9q23 | 2024 #23: a power of z given in a "minus" form r cos(theta) - i r sin(theta); options = modulus power (16 vs 8) x sign of the angle |
| m9q24 | 2024 #21: z^2 - w^2 as the FIRST item of a shared stem (the device of 2026 #20-21 / 2025 #21-22); options = i^2 slip x order of subtraction |
| m9q25 | 2025 #22: second item of the shared stem, 1/z + w/|z|^2; options = conjugate forgotten in 1/z x w vs conj(w) |
| m9q26 | 2024s #21: z = a + ik with |z| and an Arg interval -> k; options = sign (quadrant) x magnitude (k vs the modulus 4) |
| m9q27 | 2024s #20: x + y + (x^2 - c)i = a + bi with x > 0 -> y; options = sign slip x the rejected root x = -3 |
| m9q28 | 2023 #18: i^n x sqrt(-k^2) with n = 1 (mod 4) and a perfect square; options = sign (i^2025 = +-i) x real vs imaginary (sqrt(-25) = 5i vs 5) |
| m9q29 | 2025 #23: square in the complex plane from two adjacent vertices (z3 on the real axis), here z4 only; options = rotation direction, the vertex z1, the side vector |
| m9q30 | 2026 #25 family: a dashed disc cut by a solid perpendicular-bisector half-plane (2026: a wedge); options = centre sign x which boundary is strict |
| m10q1 | 2026 #1: the other two roots are fractions/negatives; options = sign of each root |
| m10q2 | 2026 #2: repeated linear factor with a negative second constant; options = sign x constants swapped |
| m10q3 | E (expected: synthetic division by (ax - b): quotient and remainder), template 2026 #1 (synthetic division, "... هما:"): divide by the zero -1/2 of (2x + 1), then halve the quotient; options = quotient halved or not x remainder halved or not |
| m10q4 | E (expected: factor theorem -> constant), template 2026 #3: (2x - 1) is a factor, so f(1/2) = 0; options = the zero used (2 or -1/2 instead of 1/2), a sign slip |
| m10q5 | 2026 #4: cos(theta/2) from cos theta and a quadrant (2nd); options = sign x cos/sin half-angle formula |
| m10q6 | E (expected: compressed difference formula sin A cos B - cos A sin B -> exact value), template 2026 #5 (difference identity with special angles, "... هي:"); options = special values (sum formula used, angles in reverse order, cos for sin) |
| m10q7 | 2026 #6: cos x + sin x tan x = sec x -> sin x + cos x cot x = csc x (quotient identity, common denominator, Pythagorean, reciprocal); options = reciprocal vs double x sin vs cos (2 sin x = cot x taken as sin x / cos x) |
| m10q8 | E (expected: exact value by power reduction), template 2026 #4 (a value from a half-angle identity, "... تساوي:"): cos^2(pi/8) = (1 + cos(pi/4))/2; options = sign (cos^2 vs sin^2 formula) x coefficient 1/2 kept or dropped |
| m10q9 | 2026 #7: quadratic in cos with one root rejected (|cos x| <= 1); options = sign x reference angle |
| m10q10 | E (expected: multiple angle in an interval), template 2026 #8: sin 2x = cos 2x -> tan 2x = 1 in [0, pi), so 2x in [0, 2pi); options = halved or not x second solution kept or lost |
| m10q11 | 2024 #2: f'(pi/2) of a trig function of a shifted angle plus a polynomial over pi (2 sin(x + pi) - x^2/pi -> 3 cos(x - pi) + x^2/(2pi)); options = sign x magnitude |
| m10q12 | 2024s #10: b^(linear) with the value f'(a) given -> the point a (2^(-3x) -> 3^(2x - 1)); options = small integers |
| m10q13 | 2024 #3: velocity when the particle returns to its starting position (solve s(t) = s(0), t > 0); options = v(0), v(2), sign |
| m10q14 | 2024 #5: f'' at a special angle of a reciprocal trig function plus a constant (csc x + e^2 at pi/4 -> sec x - pi^2 at pi/3); options = one product-rule term only (6, 8), the constant differentiated |
| m10q15 | 2025s #12: particle moving on a curve, dx/dt given -> dy/dt; options = sign x missing inner derivative |
| m10q16 | 2025 #3: two graphs, u = f + c/g; options = sign x squared denominator |
| m10q17 | 2023 #1: exponential of a root; options = coefficient 2/3 vs 3/2 x root in the denominator or numerator |
| m10q18 | 2026r #7: trig of a power of x (chain rule); options = inner derivative kept x sign of cos |
| m10q19 | 2026r #8: x of the horizontal tangent of a^(quadratic) (6^(1 - x^2) -> 4^(2x - x^2)); options = list (the zeros 0 and 2 of the exponent, the base 4 = f(1)) |
| m10q20 | 2026 #16: a^x ln y = x/y - 1 at y = 1 -> x e^y + y = 2x - 1 at y = 0 (the point found first); options = unit fractions and slips |
| m10q21 | 2023 #10: d/dx (ln y) for a variable base and exponent; options = cot vs tan x sign |
| m10q22 | 2023 #12: isosceles triangle, angle rate -> area rate (with a figure); options = cos vs sin x factor 1/2 |
| m10q23 | 2025s #20: modulus and Arg of the conjugate -> standard form; options = sign of the imaginary part x cos/sin swapped |
| m10q24 | 2025s #19: division by a pure imaginary number (a single item there), here the first item of a shared stem as in 2026 #20-21; options = sign of the real part x sign of the imaginary part |
| m10q25 | 2025s #18: |z^2| for z = a + bi (a single item there), here the second item of the shared stem; options = |z|, a part of z^2, |z|^4 |
| m10q26 | 2024 #18 / 2023 #18: power of i times a root of a negative number; options = sign x real/imaginary |
| m10q27 | 2024s #24: cube of a complex number; options = i^2 and i^3 slips |
| m10q28 | 2023 #20: modulus fixes a constant inside a fraction; options = small values |
| m10q29 | 2024s #19: conjugate read from a point in the complex plane; options = which signs change |
| m10q30 | 2024s #25: a disc read from the figure; options = centre coordinates swapped x signs |
