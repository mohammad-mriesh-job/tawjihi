# How the ministry writes semester-2 mathematics items — analysis

Purpose: the semester-2 mock papers must feel like the *next* ministry paper. This document records what the official
papers in this folder show about the ministry's semester-2 items (integration, vectors, statistics), so new items follow
the same method and together cover every idea the ministry has asked. It is the semester-2 companion of
`semester-1/previous-ministry/ANALYSIS.md`; every rule cites items from the papers listed in `README.md`.

Papers read item by item (all multiple-choice items, plus a one-line summary of every essay part):

| paper | items | units 5 · 6 · 7 | curriculum |
|---|---|---|---|
| 2026 summer, 2008 generation (`2026-summer-items-26-50.pdf`) | 26–50 | 12 · 8 · 5 | current (2008) |
| 2026 summer repeaters paper 2 (`2026-summer-paper2-repeaters.pdf`) | 1–25 | 12 · 8 · 5 | 2023–2025 books |
| 2025 summer · 2025 supplementary paper 2 | 1–25 · 1–25 | 12 · 8 · 5 each | 2023–2025 books |
| 2024 summer · 2024 supplementary paper 2 | 1–25 · 1–25 | 13 · 7 · 5 / 12 · 8 · 5 | 2023–2025 books |
| 2023 summer · 2023 supplementary paper 2 | 1–25 · 1–25 | 13 · 7 · 5 each | 2023–2025 books |

200 multiple-choice items in all. Every one of them, and every essay part, fits the lesson lists of the 2008 units 5–7
(`u5.py`, `u6.py`, `u7.py`): unlike semester 1, nothing in the 2023–2025 semester-2 papers is outside the curriculum.

## 1. Paper format

- 2026 (the format the next exam follows): one paper of 50 items for both semesters; semester 2 = items 26–50:
  unit 5 items 26–37, unit 6 items 38–45, unit 7 items 46–50. 2023–2025: a 25-item multiple-choice part per paper in the
  same unit order (12–13 · 7–8 · 5), followed by essay questions.
- Our semester-2 mocks follow the official half-year trial (30 items / 90 minutes): unit 5 items 1–16, unit 6 items
  17–25, unit 7 items 26–30, in lesson order inside each unit.
- Devices: one shared ❖ stem for two items (2026 #39–40: points A, B, C(α, 3, −4) with AB = BD); one ❖ normal table for
  the last three items (2026 #48–50); `ملحوظة: يمكنك الاستفادة من القاعدة التجريبية …` with the empirical-rule curve;
  a table inside a single item (2023 #25, 2024s #25, 2025 #25).
- Answer keys are not balanced (2026 items 26–50: a 5 · b 7 · c 6 · d 7). Our mocks keep 8·8·7·7.

## 2. The distractor rule

The 2×2 grid of two independent mistakes dominates and is growing: 2026 — 15 of 25 items (plus #31, two pairs);
2025 — 13; 2024s, 2025s, 2026r — 11; 2023 — 10; 2023s, 2024 — 9. The rest are lists of same-kind values (±k pairs,
consecutive integers, powers of e, special angles, table values) or vectors whose components differ only in sign.

| item | the two switches |
|---|---|
| 2026 #26 ∫cot(x/2) | ln\|sin\| vs −ln\|cos\| (∫tan) × coefficient 2 vs ½ |
| 2026 #27 ∫2^{2x+2}/ln 2 | exponent 2x+2 vs 2x+1 (chain factor absorbed) × ln 2 vs (ln 2)² |
| 2026 #29 curve from dy/dx | sign of the e^{−x} term × sign of the constant |
| 2026 #32 ∫sin²3x/cos⁴3x | coefficient 1/9 vs 3 × tan vs sec |
| 2026 #33 (x²+3)/(x³+x) | sign × the two coefficients swapped |
| 2026 #34 ∫sec²√x | sign of each of the two terms |
| 2026 #37 separable DE | ½ vs ¼ sin 2y × sign of cot x |
| 2026 #38 line equation | point and direction swapped × the missing component misplaced |
| 2026 #46 geometric ratio → E | p vs 1 − p × reciprocal |
| 2025 #14 unit vector | normalised or not × GH vs HG |
| 2025s #19 parallelogram ratio | sign (RN vs NR) × reciprocal |
| 2024 #8 ∫₀¹ 20x(1−x)³ | sign (limits after dx = −du) × x = 1−u vs 1+u |
| 2024s #1 ∫(½)^{2x−4} | sign of ln ½ × both limits vs one |
| 2023s #25 N(μ, μ²/4) | z = 2 vs 0.5 (σ factor inverted) × complement |

Typical switches in semester 2: chain factor divided vs multiplied, ln a in the denominator or not, sign of an
antiderivative (∫csc² = −cot, ∫e^{−x} = −e^{−x}, ∫tan = −ln|cos|), the constant from e⁰ = 1 or ln 1 = 0, the lower limit
forgotten, distance vs displacement, start position added or not, AB vs BA, ratio vs its reciprocal, unit vector vs
scaled, σ vs σ², complement or not, p vs 1 − p.

## 3. Item templates (phrasing)

- `ناتج: ∫ … dx هو:` (indefinite) · `قيمة: ∫ₐᵇ … dx هي:` (definite) · `إذا كان: ∫ … = …، فإنّ قيمة الثابت a هي:`
- `يُمثّل الاقتران: dy/dx = … ميل المماس لمنحنى الاقتران y. إذا كان مُنحنى y يمرّ بالنقطة (0, 2)، فإنّ قاعدة الاقتران y هي:`
- `إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: v(t) = …، حيث v سرعته بالمتر لكلّ ثانية، و t الزمن بالثواني، فإنّ المسافة الكلّية … في الفترة … هي:`
- `يُبيّن الشكل الآتي منحنى السرعة – الزمن لجسم يتحرّك على المحور x في الفترة [0, 8]. إذا بدأ الجسم الحركة من x = 2 …، فإنّ الموقع النهائي للجسم هو:`
- `اعتمادًا على التمثيل البياني الآتي … فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور x … هو:`
- `حلّ المعادلة التفاضلية: … (الذي تُحقّقه النقطة …) هو:`
- `إذا كان المستقيم l يوازي المتّجه: …، ويمرّ بالنقطة A التي متّجه موقعها: …، فإنّ للمستقيم l معادلة متّجهة هي:` (each option names a different line: r, m, n, p)
- `في الشكل الآتي UXWV متوازي أضلاع. إذا كان: …، فإنّ قيمة الثابت k هي:`
- `إذا كان: X ∼ Geo(p)، وكان: P(X = 2)/P(X = 5) = 125/8، فإنّ التوقّع للمتغيّر العشوائي X هو:`
- `يختار قسم ضبط الجودة … عيّنة … وتُرفَض الشحنة إذا وُجدت في العيّنة رقاقتان مَعيبتان فأكثر … فإنّ احتمال رفض … هو تقريبًا:`
- `يدلّ المتغيّر العشوائي الطبيعي: X ∼ N(3.2, σ²) على كُتل … إذا كانت كُتل 2% منهم تزيد على 4 kg، فإنّ قيمة الانحراف المعياري … (مُقرَّبًا إلى أقرب منزلتين عشريتين) هي:`

## 4. Content per 2026 item (semester 2) — the blueprint

| # | lesson | what is asked | answer form |
|---|---|---|---|
| 26 | special integrals | ∫cot(x/2) | 2 ln\|sin(x/2)\| + C |
| 27 | special integrals | ∫2^{2x+2}/ln 2 | 2^{2x+1}/(ln 2)² + C |
| 28 | special integrals | ∫₀^π sin²x = aπ (power reduction) | a = ½ |
| 29 | special integrals | curve from dy/dx = e^{3x} − e^{−x} through (0, 2) | y = ⅓e^{3x} + e^{−x} + ⅔ |
| 30 | special integrals | total distance, v = 4 sin t on [0, 2π] | 16 |
| 31 | substitution | ∫x⁵(1 + 1/x)⁵ = ∫(x + 1)⁵ | ⅙(x + 1)⁶ + C |
| 32 | substitution | ∫sin²3x/cos⁴3x = ∫tan²3x sec²3x | (1/9) tan³3x + C |
| 33 | partial fractions | (x² + 3)/(x³ + x) | 3 ln\|x\| − ln(x² + 1) + C |
| 34 | by parts | ∫sec²√x (u = √x, then parts) | 2√x tan√x + 2 ln\|cos√x\| + C |
| 35 | areas | area under 4/x from 1 to a = 12 | a = e³ |
| 36 | volumes (figure) | f(x) = √(ln x) to x = e² about the x-axis | π(e² + 1) |
| 37 | differential equations | dy/dx = 1/(sin²x cos²y) | ½y + ¼ sin 2y = −cot x + C |
| 38 | lines | line through 2î − k̂ parallel to 3î − 5ĵ + 2k̂ | r = ⟨2, 0, −1⟩ + t⟨3, −5, 2⟩ |
| 39–40 | vectors (shared stem) | D from AB = BD; α < 0 from \|AC\| = √21 | ⟨11, −14, 8⟩ ; −1 |
| 41 | vectors (figure) | midpoint of AF in a box with B(3, 5, 6) | (3, 5/2, 3) |
| 42 | vectors | collinear: AB = ⟨3, a+1, 3⟩, AC = ⟨4, 12, 4⟩ | a = 8 |
| 43 | dot product | MN·MP from MN and PN | −8 |
| 44 | vectors (figure) | parallelogram UXWV, Y midpoint of UW, XW : WZ = k : 1 | k = 3/2 |
| 45 | dot product | area of ABC from BA, BC (right angle not stated) | 45 |
| 46 | geometric | P(X = 2)/P(X = 5) = 125/8 → E(X) | 5/3 |
| 47 | binomial | 7 chips, 10 % defective, reject if 2 or more | 0.1497 |
| 48 | normal (table) | N(105, 225), P(X < 96) | 0.2743 |
| 49 | normal (table) | P(−k/16 < Z < k/16) = 0.516 | k = 11.2 |
| 50 | normal (table) | σ from 2 % above 4 kg, closest entry | 0.39 kg |

2026 is short and direct: most items take one or two steps with one trap, and the difficulty comes from options that
differ by exactly that trap. Three figures only (#36, #41, #44).

## 5. Every pattern the ministry has asked (2023–2026), by lesson

The list mock papers must cover. Items marked † were asked in two or more papers.

**Unit 5 — integration**
- Special integrals: trig of a linear inner (2026 #26, 2023 #2, 2023 #3, 2023s #2, 2024 #1)†; exponentials a^{kx}, also
  definite and with a base < 1 or e/2 (2026 #27, 2026r #1, 2025s #1, 2023 #1, 2023s #1, 2024s #1, 2025 #5)†; an identity
  first — power reduction (2026 #28), Pythagorean (2023s #3, 2024 #2, 2026r #2)†, double angle (2024s #2), sum-to-product
  (2025 #1); definite integrals of |linear| or a piecewise function (2023 #4, 2024 #4, 2024s #5, 2025s #2, 2023s #4)†;
  definite integrals giving a logarithm or a constant (2026r #4, 2024 #3, 2025 #4, 2025s #4)†.
- Function from its derivative and a point (2026 #29, 2023 #5, 2023s #5, 2024 #5)†, also in context: population, price,
  drug concentration (2024s #6, 2025 #8, 2025s #9)†.
- Motion: total distance (2026 #30, 2026r #5)†, displacement (2024 #6, 2023 #6, 2023s #6)†, position from a start
  (2024s #7, 2025s #7)†, and from a v–t graph: final position, distance or displacement (2023 #12, 2023s #12, 2024 #12,
  2024s #12, 2025 #11, 2025s #11, 2026r #11)† — the most frequent figure in the semester-2 papers.
- Substitution: simplify first (2026 #31, 2025 #7, 2025s #8, 2024s #4)†; powers of trig functions (2026 #32, 2023 #8,
  2023s #8, 2024 #7, 2026r #10, 2025 #9)†; f′·fⁿ and ln forms (2023 #7, 2023s #7, 2024s #3, 2024s #9)†; definite
  substitutions (2026r #9, 2024s #10, 2024 #8, 2025 #6, 2025s #6)†.
- Partial fractions: an irreducible quadratic factor (2026 #33); two linear factors (2026r #7, 2024 #9, 2024s #11,
  2025s #10)†; a repeated factor (2025 #10); an improper fraction (2026r #3, 2025 #2, 2025s #5)†.
- By parts: substitution then parts (2026 #34; essays 2026r, 2025); x^n ln x and ln of a power (2023 #9, 2024 #10,
  2023s #9)†; x·trig (2023 #10, 2023s #10)†; definite x·a^x (2023 #11); ∫x f′(x) from given values (2023s #11).
- Areas and volumes: area under k/x or k/(x + c) → a constant (2026 #35, 2026r #6, 2024s #8)†; area from a figure
  (2025 #3, 2025s #3, 2026r #8)†; volume of revolution from a figure (2026 #36). Area between two curves and washers
  appear only in essays (2023–2025, 2026r) — candidates for the next multiple-choice paper.
- Differential equations: separable general solution (2026 #37, 2024 #11)†; particular solution by direct integration
  (2023 #13, 2023s #13)†; separable particular solution (2026r #12, 2024 #13, 2025 #12, 2025s #12)†.

**Unit 6 — vectors**
- Midpoint: position vector, endpoint from the midpoint, unknowns, the magnitude |ON| (2023 #15, 2024 #17, 2024s #14,
  2025s #13, 2026r #13)† — the most frequent vectors idea.
- Parallel or collinear with unknowns (2026 #42, 2024 #20, 2025 #18, 2025s #18)†; ratio problems in a figure —
  parallelogram or triangle (2026 #44, 2026r #18, 2024s #16, 2025s #19, 2024 #14)†.
- Linear combinations (2023 #16, 2024 #16, 2024s #17, 2025s #14, 2026r #15)†; displacement vectors (2023s #17, 2024s #13,
  2025s #15, 2026r #17)†; magnitude with an unknown (2026 #40, 2023s #15, 2024 #15, 2024s #15, 2025 #13)†; a fourth point
  from equal vectors (2026 #39, 2026r #16, 2025 #17, 2025s #16)†; a point dividing a segment (2023 #17, 2025 #15)†;
  a vector of a given magnitude along v (2024 #18, 2026r #14)†; unit vector (2025 #14); p a − q b (2025 #16); a point in a
  coordinate plane (2023s #14); geometric addition in a closed triangle (2023s #16); a box or cube read from a figure
  (2026 #41, 2023 #14)†.
- Lines: equation through a point parallel to a vector (2026 #38, 2024s #18)†; a point on a line → a constant (2023 #18,
  2024s #19)†; where a line meets a coordinate plane (2024 #19, 2025s #17)†; the line through a cube vertex and its
  centre (2025 #19); the vector PF to the foot in general form (2023s #18); the distance with the foot given (2026r #20,
  2025s #20)†.
- Dot product: perpendicular vectors → a constant (2023 #19, 2026r #19)†; the sign of u·v from a figure (2023 #20,
  2023s #20)†; u·c with u = AB (2023s #19); a dot product from two side vectors (2026 #43); triangle area (2026 #45);
  |b| from the angle (2024s #20); the angle from magnitudes (2025 #20).

**Unit 7 — statistics**
- Geometric: P(X = k) in context, until the first success — a die, chips, a spinner (2023s #21, 2024s #21, 2026r #21,
  2025s #21)†; P(X > k) and E(X) from it (2023 #21, 2025 #22)†; E(X) (2023s #23); a ratio of two probabilities (2026 #46);
  which experiment is geometric (2025 #21).
- Binomial: quality control and P(X = k) in context (2026 #47, 2023s #22, 2024 #21)†; at least n − 1 successes with
  expression options (2023 #22); variance and mean — Var of a given B, n from E and Var, Var from E and p, p from Var,
  P(X = 1) = P(X = 2) (2024s #22, 2026r #22, 2025s #22, 2023 #23, 2024 #22)†.
- Normal: probabilities with a short table (2026 #48, 2025s #23, 2024 #25)†; the empirical rule — three bands, a
  percentage in words, σ from 95 % or from 2.5 % tails (2023 #24, 2023s #24, 2024 #23, 2024s #23, 2025 #23, 2025s #25)†
  (6 of 8 papers); symmetry without a table (2025 #24, 2025s #24, 2026r #24)†; a shaded area in a figure (2024s #24,
  2026r #23)†; a value x from a probability (2023 #25, 2024s #25, 2025 #25, 2026r #25)†; a symmetric interval → k
  (2026 #49); σ or μ from a percentage (2026 #50; essays every year)†; σ given in terms of μ (2023s #25, 2024 #24)†.

## 6. Contexts, figures and numbers

- Contexts are short: endangered animals, the price of a product (x in hundreds), drug concentration in mg/cm³, chips,
  refrigerators, a dart player, rainfall in mm, bolts, newborns' masses, women's ages, chickens' masses in kg.
- Figures: the v–t graph (7 of 8 papers), the empirical-rule curve (6 of 8), a shaded normal area, the area under a curve
  with no numbers on the axes (the limits come from the formula), a box or cube on an isometric grid, a parallelogram or
  triangle with labelled side vectors, a spinner of congruent sectors, a square.
- Numbers are exact and small; decimals appear in statistics (4 decimals from the table) and in context derivatives.

## 7. Trend 2023 → 2026

More grids (9–10 per paper in 2023–2024, 15 in 2026), shorter items, fewer figures in 2026, one item per lesson pattern,
and the essay skills of 2023–2025 (area between curves, washers, collinearity proofs, two lines, μ and σ from two tails)
moved out of the 2026 paper: they are the most likely new multiple-choice items.

## 8. Checklist for a new semester-2 mock item

1. Name the official item it is modelled on (sections 4–5) in a comment above the `Q(...)`; keep its stem, kind of
   function, numbers and steps; change only the function, numbers or context. Never harder than the model.
2. Build the options from the model's grid (section 2); explain each wrong option by its switch.
3. Add the figure the model has (section 6), drawn like the ministry's.
4. Verify with `qb.py`; check the new formula and context against the unit banks and the other mocks.

## 9. How mock papers 6–10 were written (item-by-item modelling)

1. **Catalogue every official semester-2 item** (sections 1–5): the 200 multiple-choice items of the eight papers were
   transcribed (stem, options, how each option was built, the number of steps) and grouped into the patterns of section 5.
2. **Assign one official item to every slot** of the 16 · 9 · 5 layout, lesson by lesson:
   - every 2026 item is modelled: 15 of them in two papers, and nine more come back in a second paper as the same
     pattern from another year (2026r #5 for #30, 2024s #8 for #35, 2024s #18 for #38, 2025 #17 for #39, …);
     the other patterns of section 5 are spread over the five papers;
   - patterns the ministry asked in several papers (the v–t graph, midpoints, parallel vectors, the empirical rule) appear
     in three papers;
   - no two items of one pattern in a paper, and two papers share at most two patterns of one lesson;
   - ideas missing from papers 1–5 come first: the empirical rule (asked in 6 of 8 papers, in none of papers 1–5), a
     spinner, n from E and Var, the 2026 #38 and #44 figures, a cube read from a figure, |linear| and piecewise
     definite integrals, a function from its rate in context.
3. **Write a sibling, never harder**: the model's stem, kind of function, numbers and option grid, with a new function,
   numbers or context; the same steps and the same trap (four slots were changed for this: a chain factor the model lacks
   (2026 #37), a numerator that removed the partial fractions (2026 #33), a lower limit giving ln 1 = 0 (2026r #4), and a
   second-derivative version of 2023s #11, now in the model's own form). Contexts are new to the site (eggs, melons, cables, phone calls, a customer-service line, newborns,
   flights, app subscribers, a town's population).
4. **Check against the earlier mocks, the unit banks and each other**: no repeated formula, option set or context; about
   twenty slots got new numbers or a new context because a check found a repeat.
5. **Record the model** in a comment above each `Q(...)` in `mock-exams/s2_papers_6_10.py`; the table below is generated
   from those comments.

Papers 6–10 model 137 different official items, including all 25 semester-2 items of 2026. Models used: 2026 — 40 items,
2026r — 21, 2023 — 18, 2023s — 16, 2025 — 16, 2025s — 16, 2024s — 14, 2024 — 12 (some items name two models). The few
patterns they do not repeat are in the unit exams (which experiment is geometric, E(X) of a given geometric variable,
p from the variance, x from P(μ < X < x)).

| item | modelled on (official item) · option grid |
|---|---|
| n6q1 | 2026 #26: integral of a trig quotient of x/n; options = -ln\|cos\| (tan) vs ln\|sin\| (cot) x coefficient 3 (divided by the inner 1/3) vs 1/3 (multiplied) |
| n6q2 | 2023s #1: definite integral of a^x on [-1, 1]; options = divided by ln a or not x numerator a - 1/a (both limits) vs 1 - 1/a (a^0 used for a^1) |
| n6q3 | 2026 #28: a squared trig function over an interval = a pi (power reduction); options = +-1/4, +-1/2 (the 1/2 of the identity dropped; sign) |
| n6q4 | 2023 #5: f' = (cubic + constant)/x split term by term, and f(1) -> f; options = the x^2 term left un-integrated, sign of the constant, sign of the ln term |
| n6q5 | 2026 #30: total distance for v = k trig(t) over two equal arches (one interior zero, no chain factor, as in the model); options = a list from nameable slips: the distance, the displacement 0, one arch only (also the amplitude), doubled |
| n6q6 | 2026 #31: x^n (1 + c/x)^n = (x + c)^n, then the power rule; options = (x+c)^(n+1)/(n+1), (x+c)^n/n (power not raised), the bracket's power ignored (x^n + c x^(n-1) integrated) with either sign |
| n6q7 | 2026r #10: an odd power of cos times an even power of sin (u = sin x); options = coefficients matched to the powers or swapped x sign of the second term |
| n6q8 | 2023 #7: (ln x)^n / x by u = ln x; options = new power n + 1 vs n + 2 x (ln x)^k vs ln x^k |
| n6q9 | 2026r #9: definite integral of x times a cube root of (x + c)^2 by u = x + c; options = sign x x = u - c (a difference) vs u + c (a sum) |
| n6q10 | 2026 #33: (x^2 + a)/(x^3 + bx) = A/x + Bx/(x^2 + b), Bx a multiple of the derivative 2x as in the model (so no 1/2 appears); options = which ln carries which coefficient x sign of the second term |
| n6q11 | 2026r #3: improper fraction, a cubic without an x^2 term over a linear factor, quotient x^2 - cx and remainder 1 (as in the model); options = power rule divided or not x sign of the quotient's second term |
| n6q12 | 2026 #34: a trig function of sqrt(x): u = sqrt(x), then by parts; options = signs of the two terms |
| n6q13 | 2023s #11: integral of x f'(x) on [0, 1] from given values, by parts; options = the right value, the boundary term only, f(1) - f(0) (taken as the integral of f'), f(1) - f(0) - the given integral |
| n6q14 | 2026 #35 / 2026r #6: shaded area under k/x from x = 1 to x = a equals a value -> a = e^n (figure as 2026r #6); options = powers of e: the right one, k not divided (e^12), the coefficient taken as the exponent (e^3), ln 1 taken as 1 (e^5) |
| n6q15 | 2023 #12: velocity-time graph (a new shape: a dip below the axis, then a constant stretch), start x0 given -> final position; options = displacement or distance x start added or not |
| n6q16 | 2026 #37: dy/dx = 1/(trig^2 x . trig^2 y), separable, both sides direct as in the model (sin^2 y by power reduction, csc^2 x -> -cot x); options = 1/4 vs 1/2 sin 2y x sign of cot x |
| n6q17 | 2023 #15: midpoint with two unknowns, a from one coordinate first, then b; options = +-k list (a itself, a + b, sign slip) |
| n6q18 | 2026 #39 (shared stem with 2026 #40): AB = BD -> position vector of D; options = 2B - A, A (the equation read as AB = DB), -A, -(2B - A) |
| n6q19 | 2026 #40: \|AC\| = sqrt(n) with alpha < 0; options = negative values: the right root, the (alpha + x_A) sign slip, the root before adding x_A, no square root taken and the sign slip |
| n6q20 | 2026 #41: cuboid in the ministry's drawing, vertex B given, midpoint of a face diagonal (CF, on the face y = 4, not AF/GA); options = one vertex misread each time (C read as G, F read as G, C read as D) |
| n6q21 | 2023s #16: three arrows head to tail around a triangle (a closed loop, the other orientation) -> the right geometric sum; options = the zero-sum relation and three relations with a sign flipped (values: lhs - rhs from the drawing's coordinates) |
| n6q22 | 2026 #38: line parallel to v through a position vector with a missing component (j), options as in the model with the four line names r, m, n, p: point and direction swapped x the missing component put in the wrong slot |
| n6q23 | 2026r #20: distance from a point to a line, the foot F given; options = \|PF\| or \|PF\|^2 x sign slip with the negative coordinate (1 - (-3) taken as 1 - 3) |
| n6q24 | 2026r #19: perpendicular vectors with the parameter in three components -> a quadratic; options = the right factor pair of 24 or the other pair (4, 6) x which root is negative |
| n6q25 | 2023s #19: u . c with u = AB; options = AB or BA (overall sign) x a sign slip in one product ((-3)(-4) taken as -12) |
| n6q26 | 2026 #46: ratio of two geometric probabilities -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) (p vs 1 - p x value vs reciprocal) |
| n6q27 | 2025s #22: E(X) and p of a binomial -> n -> Var(X); options = npq, E used as n (E.p.q), q, twice the variance |
| n6q28 | 2026 #48: P(X < a) below the mean for N(mu, sigma^2), with the table shared by items 28-29; options = complement or not x z right (-0.75) or the variance used in z (9/144 ~ 0.06, a z not in the table, as in the model) |
| n6q29 | 2026 #49: P(-k/c < Z < k/c) given -> k; options = the right table entry times c, the neighbouring entry times c, the probability looked up directly (closest entry 0.7734 -> 0.75) times c, c/z (the equation inverted) |
| n6q30 | 2024s #23 / 2023 #24: probability between mu - sigma and mu + 2 sigma by the empirical rule (figure), sigma from a decimal variance as in 2023 #24; options = the right three-band sum, mu +- 2 sigma, mu +- sigma, one side only (mu to mu + 2 sigma) |
| n7q1 | 2023 #2: 1/sin^2(kx) plus the constant pi; options = cot vs tan x {minus sign and pi x} vs {plus sign and pi} |
| n7q2 | 2026 #27: a^(mx+n) divided by ln a; options = exponent (chain factor 4 = 2^2 absorbed or not) x ln 2 vs (ln 2)^2 |
| n7q3 | 2023s #3: cot^2(kx) - csc^2(kx) = -1; options = -x, x (identity sign), and the two term slips of the model: cot^2 = 1 - csc^2 (wrong identity) and the second term added instead of subtracted |
| n7q4 | 2026 #29: dy/dx = e^(2x) - e^(-x), curve through (0, 1); options = antiderivative (sign of the e^(-x) term) x sign of the constant |
| n7q5 | 2025s #7: v = c - (2t - 6)^2 and the initial position -> position at t = 3; options = sign of the constant, constant taken as the initial position (the 36 at t = 0 forgotten), the initial position not added |
| n7q6 | 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2 with k = 1/2; options = coefficient (divided vs multiplied by the chain factor) x tan vs sec |
| n7q7 | 2023s #7: (linear) times the cube root of a quadratic whose derivative is minus the linear factor; options = sign x cube root of u^4 vs fourth root of u^3 (truth with the real cube root, as in school) |
| n7q8 | 2024 #8: definite integral of k x (1 - x)^3 by u = 1 - x; options = sign (limits) x (x = 1 - u vs 1 + u) |
| n7q9 | 2025 #8: rate k x / sqrt(c + x^2) in context, one value given in units that must be converted (pieces -> thousands); options = coefficient (x2 vs x1/2 when integrating u^(-1/2)) x sign of the constant (each constant fits its coefficient) |
| n7q10 | 2026r #7: (px + q)/(x^2 + cx) with two linear factors; options = constants swapped x sign of the second |
| n7q11 | 2025 #10: 1/(x^2 (x + c)) with a repeated factor; options = which log carries the minus x sign of the 1/x term |
| n7q12 | 2023 #9: k x^n ln x by parts; options = power of x in the first term x sign of the second |
| n7q13 | 2023s #10: x csc^2(kx) by parts; options = sign of v = -cot/k (both terms flip) x ln\|sin\| vs ln\|cos\| |
| n7q14 | 2026 #36: volume about the x-axis of the region under sqrt(x ln x) from its x-intercept (x = 1, not printed) to the line x = e (figure like the model); one round of parts; options = sign of the lower-limit term x v = x^2/2 vs x^2 |
| n7q15 | 2025s #3: area under a cubic with a double zero between its zeros (figure, no numbers); x^2(4 - x) on [0, 4] (the blueprint's x^2(3 - x) is the mirror image of u5e7q10's region, same area 27/4); options = reciprocal pair and the two terms of the antiderivative taken alone |
| n7q16 | 2026r #12: dy/dx = y times a linear polynomial through (1, 1), answer in ln\|y\| form; options = sign of x^2 x sign of the constant |
| n7q17 | 2026 #42: collinear points, AB (with the unknown) and AC given; options = right value, the constant moved with the wrong sign (the model's 10), the middle component matched with AC's first (the model's 3), the ratio forgotten (AB = AC) |
| n7q18 | 2026 #44: parallelogram, Y the midpoint of the diagonal RT, Z on ST produced, YZ given -> k in ST:TZ = k:1 (figure); options = k, the coefficient of TZ (stopped early), the coefficient of ST, the ratio read the other way |
| n7q19 | 2023 #17: position vector of F with PF = (3/4) PQ; options as the model: F, PQ itself, PF (P not added), P plus PF with a sign slip in two components |
| n7q20 | 2026r #15: linear combination of two vectors (2u - 3v here); options = component sign variants (as the model: all signs reversed = 3v - 2u, the third or the first component reversed) |
| n7q21 | 2025 #14: unit vector in the direction of GH from two points (\|GH\| = 9); options = normalised or not x GH vs HG |
| n7q22 | 2023 #18: a point with one unknown coordinate (3a) lies on a line; options = a vs the coordinate 3a x sign |
| n7q23 | 2024 #19: point where a line meets a coordinate plane (XY here); options = right point, the sign of t slipped, the points on the wrong planes (XZ, YZ) |
| n7q24 | 2026 #43: three points, DE and FE given -> DE . DF; options = +-(right value) (DF vs FD), +-(DE . FE used directly) |
| n7q25 | 2023s #20: which figure shows u . v = 0 (non-zero vectors); options = the four panels (acute, straight, obtuse, right) |
| n7q26 | 2026 #47: binomial quality control, the tray is rejected if 2 or more of 5 eggs are cracked; options = cut-off (at least 1 vs at least 2) x event vs complement: P(X >= 2), P(X = 0), P(X <= 1), P(X >= 1) |
| n7q27 | 2025 #22: P(X > 3) = q^3 gives q, then E(X) = 1/p; options = 1/p, 1/q (p and q swapped), q/p, p itself |
| n7q28 | 2026 #50: sigma from the percentage above a value, closest table entry, rounded to two decimals; options = sigma, the z-value itself, d.z, z/d |
| n7q29 | 2026r #23: shaded area between a negative and a positive z, the two P(Z < z) values given (figure); options = right, the negative bound taken as positive, 0.5 plus a tail (each tail) |
| n7q30 | 2025s #24: symmetry, P(X > mu + c) given in context -> P(X < mu - c); options = a, 1 - a, 1 - 2a, 2a |
| n8q1 | 2023s #2: sin of (c - kx); options = right, sign lost when dividing by -k, chain factor dropped, inner function integrated |
| n8q2 | 2026r #1: k e^(mx) + a^(mx); options = coefficient of e^(mx) (k/m or the k dropped) x chain factor m under a^(mx) (kept or lost) |
| n8q3 | 2023 #4: \|linear\| on an interval where it keeps one sign (no splitting); options = +-4, +-2 (the model's list) |
| n8q4 | 2024s #6: a count changing at k e^(rt), the initial count -> N(t); options = decimal slip in k/r (9 or 0.9) x constant adjusted with e^0 = 1 or not (as in the model: 0.9 with the constant of 9, 0.9 with its own constant, C = N(0)) |
| n8q5 | 2026r #5: total distance for v = k cos t on [0, 3pi/2]; options = right, \|displacement\|, the second part only, half (the model's list) |
| n8q6 | 2026 #31: x^n (1 - 1/x)^n = (x - 1)^n, then the power rule; options = right, power kept (n), the bracket's power ignored (x^n - x^(n-1)) and its sign switch |
| n8q7 | 2023s #8: a power of a trig function times sin 2x; options = right, sign, the other function (sin for cos), sin 2x treated as sin x |
| n8q8 | 2024s #9: e^x over a power of (c + e^x); options = sign x divided or multiplied by the new power 3 |
| n8q9 | 2025 #6: root(a^2 x^2 - x^4) on a negative interval (\|x\| = -x), then substitution; options = sign (\|x\| taken as x) x the 1/2 from du = -2x dx (kept or lost) |
| n8q10 | 2026 #33: a linear and an irreducible quadratic factor (x^3 + cx), A = 4 and B = -2 (3 and -2 in the model); options = which log carries the coefficient x sign of the second log |
| n8q11 | 2024s #11: (px + q)/(x - x^2); options = partial fractions or the fake ln of the denominator, x sign of the second log (the inner -1 of 1 - x) |
| n8q12 | 2026 #34: substitution u = root x, then by parts (cos of 2 root x here); options = sign of each of the two terms |
| n8q13 | 2023 #11: definite integral of x a^x by parts; options = sign of the second term x the lower-limit term a^0 = 1 kept or forgotten |
| n8q14 | 2024s #12: distance from a velocity-time graph (a part below the axis), the start given as a distractor; options = distance, displacement, final position, the area above the axis only |
| n8q15 | 2026 #36: volume about the x-axis of the region under root(f) (figure); the limits are the curve's x-intercepts, not printed (0 and pi here; the lower limit 1 in the model), then by parts; options = right, the product integrated factor by factor, the pi of the formula forgotten, both slips |
| n8q16 | 2023 #13: dy = (derivative of a trig function) dx through a point; options = antiderivative (-csc x or csc x, each with the constant that fits the point) x sign of the constant |
| n8q17 | 2024s #14: magnitude of the position vector of a midpoint; options = k root m, \|OP + OQ\| (not halved), and the coefficient and the radicand swapped in both (as in the model: 3 root 2, 2 root 3, 2 root 6, 6 root 2) |
| n8q18 | 2026r #17: displacement vector from A to B; options = sign variants of the components (the subtraction order mixed between components; A - B itself is not offered, as in the model) |
| n8q19 | 2025 #17: square ABCD from three vertices (figure, no coordinates) -> D = A + C - B; options = 2A - B, A + B - C, the vertex B |
| n8q20 | 2025 #15: PK = 1/3 KQ -> K; options = ratio 1/4 (right) or 1/3 (PK = 1/3 PQ), x K measured from P (right) or from Q; P and Q are placed so that the from-Q slip flips the signs of two components, the model's grid, and every distractor is the real result of its slip |
| n8q21 | 2023s #14: a point with one zero coordinate lies in a coordinate plane; options = two planes x two axes (the axis of the zero coordinate is the trap) |
| n8q22 | 2025s #19: parallelogram (a and b on the sides from the bottom-left vertex), M on a diagonal in a given ratio (1:3 here, 3:2 there), CM = k(3a + b); options = k, -k, 1/k, -1/k |
| n8q23 | 2023s #18: F the foot of the perpendicular from P -> PF in terms of t (the general point of the line minus P); options = F - P, F + P, the constant part reversed (P - r0 + t d), P + t d |
| n8q24 | 2026 #45: triangle from BA and BC with a zero dot product (the right angle is not stated); options = 1/2 \|BA\|\|BC\|, without the 1/2, and two same-kind decoys (as in the model) |
| n8q25 | 2025 #20: angle from the magnitudes and the dot product; options = special angles in degrees (the minus sign dropped, root 2 taken as 2, divided by one magnitude only) |
| n8q26 | 2026r #21: repeated trials until the first success (a context), P(X = 3); options = q^2 p, q p (X = 2), q^3 p (X = 4, rounded as the model prints 0.073), q |
| n8q27 | 2026r #22: n from E(X) and Var(X); options = E/p, E/q (p and q swapped), E/(pq), and a value checked by substitution |
| n8q28 | 2025s #25: sigma from the interval holding 95% (empirical rule, figure); options = sigma, sigma^2, 2 sigma (95% read as mu +- sigma), the width of the interval |
| n8q29 | 2026 #48: P(X > a) with a below the mean (shared table); options = P(Z < z) or its complement, x z right or with the decimal slip z = -0.09 (also what dividing by the variance 100 gives; Phi(0.09) is not in the table, as Phi(0.06) in the model) |
| n8q30 | 2026r #25 / 2023 #25: x from an upper-tail probability (shared table); options = mu + z sigma, the z itself, z sigma (mu forgotten), mu + z sigma^2 (the variance used) |
| n9q1 | 2026 #26: integral of cot(kx); options = ln\|sin\| vs -ln\|cos\| (the antiderivative of tan) x coefficient 1/3 (divided by the chain factor) vs 3 (multiplied) |
| n9q2 | 2026 #27: a^(mx+n) divided by ln a; options = exponent 3x+1 (chain factor 3 absorbed) vs 3x+2 (forgotten) x (ln 3)^2 vs ln 3 |
| n9q3 | 2025 #1: sum-to-product turns the integrand into a constant (here the sum is on top, so the constant is 2); options = sign x 2 vs 1 (the factor 2 of the identity forgotten) |
| n9q4 | 2024 #5: f from f' = (a e^x + b)^2 and f(0); all four options pass f(0) = 13/2 and differ in the expansion or the integration (1/2 of e^(2x) forgotten, the 2ab term halved, the 2ab term dropped) |
| n9q5 | 2023s #4: definite integral of a piecewise function split at x = 1; options = first piece only, second piece only, the first piece with its sign slipped (chain factor -2) |
| n9q6 | 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2, u = tan kx; options = coefficient 1/12 (divided by the chain factor 4 and the power 3) vs 4/3 (multiplied by the chain factor) x tan vs sec |
| n9q7 | 2025 #7: e^(kx)(1 - 1/e^x)^n = e^x (e^x - 1)^n, u = e^x - 1, definite (only the lower limit contributes); options = sign x power 4 vs 3 (power not raised; that slip gives the base 1 - 1/e) |
| n9q8 | 2024s #3: kx/(1 - cx^2), u = 1 - cx^2; options = sign (du = -8x dx) x 1/4 vs 1/2 (derivative of 4x^2 taken as 4x) |
| n9q9 | 2023 #6: displacement from v = kt/(t^2 + c) (ln form); options = sign (limits subtracted the wrong way) x ln 4 vs ln 9 (ln 12 - ln 3 taken as ln(12 - 3)) |
| n9q10 | 2024 #9: k/((x - a)(x + a)) by partial fractions; options = the sign of B lost, "ln of the denominator" shortcuts x6 and x3 |
| n9q11 | 2025s #5: improper fraction, one-step division, match the coefficient a of ax^2; options = reciprocal pairs (2, 1/2), (4, 1/4) |
| n9q12 | 2023 #10: by parts, kx cos(kx); options = x sin vs x cos (v not integrated) x sign of the 1/4 term |
| n9q13 | 2023s #9: definite integral of ln x^n by parts; options = the lower-limit value ignored, its sign slipped, the factor 3 of ln x^3 = 3 ln x forgotten |
| n9q14 | 2025 #3: area in the first quadrant under c - a^x (figure without numbers; the limits 0 and 2 come from the formula); options = divided vs multiplied by ln 3 x the lower-limit value 3^0 = 1 kept or forgotten |
| n9q15 | 2024s #8: k from the shaded area under k/(x + c) (figure with the ticks 0 and 6 only); options = k, the ratio of logs inverted, the lower-limit term ln 2 forgotten (k ln 8 = ln 64), both |
| n9q16 | 2024 #11: general solution of dy/dx = 1/(x y^n); options = variables in place vs swapped x the factor y^2 integrated vs ignored |
| n9q17 | 2024 #20: parallel vectors with an unknown in each -> a + b; options = a + b, the sign of k slipped, a - b, one unknown (b) only |
| n9q18 | 2026r #18: parallelogram, Y on a side with EY = 4YF, Z on a produced side, k from the given YZ; options = consecutive integers |
| n9q19 | 2024s #15: PQ = QR with an unknown coordinate -> two values; options = mirrored pairs: right, the k - (-1) sign slip, the x and y parts of QR forgotten, both |
| n9q20 | 2025s #15: displacement vector from C to A (A - C) with a double negative in one component; options = sign of the x component x the y component right or slipped (10 + (-5)) |
| n9q21 | 2026r #14: vector of a given magnitude in the direction of v; options = scaled vs unit vector (stopped early) x same vs opposite direction (all four exact) |
| n9q22 | 2024s #18: line through a position vector with a missing i component, parallel to a vector; options = point and direction swapped x the missing component put in the wrong slot (the lines are named r, m, n, q as in the model) |
| n9q23 | 2025 #19: line through a cube vertex read from the figure and the cube's centre; options = the vertex misread (x and y swapped) with the right direction, lines through M along the other space diagonals (names r, m, n, p as in the model) |
| n9q24 | 2026 #43: PR built from PQ and RQ, then PQ . PR; options = sign (RP used) x RQ used directly (+-PQ . RQ) |
| n9q25 | 2024s #20: \|b\| from the angle, the dot product and \|a\|; options = cos ignored, multiplied by cos instead of dividing, \|a\| ignored |
| n9q26 | 2023 #22: at least n - 1 successes of n, options as expressions (n(1 - p) = 1 makes the coefficient vanish); options = X = n only, one ordering of the n - 1 successes, the second term written with (1 - p)^n |
| n9q27 | 2024s #21: a die with more faces thrown until an event; options = (1-p)^2 p, (1-p)^2 (the final success dropped), (1-p) p^2 (exponents swapped), (1-p)^3 (the third throw counted as a failure). p = 1/5 (p = 1/4 would repeat the option values of n4q26) |
| n9q28 | 2026 #49: symmetric interval P(-k/c < Z < k/c) -> k (the one table for items 28-30, like 2026 #48-50); options = c z, c times a neighbouring table entry (0.84 and 0.67), c / z (the equation inverted) |
| n9q29 | 2026 #50 asked for the mean: the percentage above a value -> mu; options = mu, the sign slipped (x + z sigma), z not multiplied by sigma, the variance used as sigma |
| n9q30 | 2023s #25: sigma given in terms of mu, P(X > 2mu) from the table; options = z = 1.5 vs 0.67 (the factor of sigma inverted) x complement or the table value |
| n10q1 | 2024s #2: 1/(sin^2 x cos^2 x) = 4 csc^2 2x -> -2 cot 2x (here 3x inside: 4 csc^2 6x); options = tan vs cot x sign |
| n10q2 | 2026r #4: definite integral of k/(ax + b) giving k ln m, the lower limit not giving ln 1 = 0; options = k ln m values: lower limit dropped (= chain factor forgotten, as in the model), ln 9 - ln 3 taken as ln 6, chain factor multiplied |
| n10q3 | 2026 #28: definite integral of sin^2 (power reduction) = a pi; options = +-1/6, +-1/3 (the 1/2 of the identity dropped) |
| n10q4 | 2026 #29: dy/dx = e^(kx) - e^(-x) through (0, 2); options = the right antiderivative (1/4 e^(4x) + e^(-x)) or the model's wrong one (3/4 e^(4x) - e^(-x), coefficient and constant swapped, sign of e^(-x) slipped) x sign of the constant |
| n10q5 | 2024 #6: displacement for v = A cos(t/k) on an interval ending at t/k = 2pi/3; options = sign x sqrt3 or not (antiderivative sign slip, cosine kept instead of integrated, sin(2pi/3) taken as 1/2) |
| n10q6 | 2025s #8: (x^2 - 2x + 1)^3 / x^8 = (1 - 1/x)^6 / x^2, u = 1 - 1/x (here (x + 1)^4 / x^6, u = 1 + 1/x); options = power 5 vs 4 (power not raised) x sign |
| n10q7 | 2025 #9: tan x sec^3 x = sec^2 x (sec x tan x), u = sec x, definite; options = the cube computed (8 vs 2) x sign of the lower-limit term |
| n10q8 | 2025s #6: substitution whose du is the whole numerator (sin 2x = derivative of 4 + sin^2 x), definite; options = logs of simple numbers (lower-limit value ln 4 dropped, limits reversed, ln 5 - ln 4 taken as ln(5 - 4) = 0) |
| n10q9 | 2025s #9: a quantity from its rate -k e^(-kt)/(1 + e^(-kt))^2 and its starting value (drug concentration in the model; newspaper subscribers here), u = 1 + e^(-kt); options = sign of the fraction x the constant (right constant for the wrong sign, or the constant's sign flipped) |
| n10q10 | 2025s #10: partial fractions with two distinct linear factors; options = B from a sign slip (6 + 3 -> 6 - 3) x sign of A |
| n10q11 | 2025 #2: improper rational function, one-step division x + c/(x - a); options = x^2/2 vs x^2 x sign of the ln term |
| n10q12 | 2024 #10: ln of a root -> k ln x, then the integral of ln x by parts; options = sign of the x term x the factor 3/2 on both terms or only on x ln x |
| n10q13 | 2023s #11: integral of x f'(x) on [0, 1] by parts from given values (the model's own form: the integral of f is handed over); options = right, the boundary term only, f(1) - f(0) taken as the answer, f(1) - f(0) - the given integral |
| n10q14 | 2025 #11: displacement from a piecewise-linear v-t graph, answered with its direction; the start x0 is not needed; options = displacement 4 vs distance 16 x right/left |
| n10q15 | 2026r #8: area under x e^(c x^2) from 0 (substitution); options = factor 1/4 kept vs dropped x -+1 (e^0 = 1) |
| n10q16 | 2024 #13: dy/dx = e^(ax + by) through (0, 0), separated; options = chain factor divided vs multiplied x sign of the constant; one of them passes through (0, 0) but fails the equation (the model's trap) |
| n10q17 | 2026r #13: endpoint B from A and the midpoint N; options = 2N - A, A - 2N, and A - 2N in one component |
| n10q18 | 2025s #18: parallel vectors, unknown component; options = sign x multiplied vs divided by the factor 2 |
| n10q19 | 2023 #14: coordinates of one labelled vertex of a cube read from the ministry's drawing (the vertex above the y-axis end here, above the x-axis end in the model); options = other vertices of the cube (x/y swapped, the one below it, the front one) |
| n10q20 | 2025s #14: 2f - g in i, j, k with a vanishing component (3f - g and the j component here, since u6e5q1 asks 2f - g); options = the vanishing component kept (0) vs slipped (3(3) + 9 = 18) x sign of the rest (g - 3f) |
| n10q21 | 2024 #18: vector of a given magnitude along v (\|v\| an integer), each option named with its own letter; options = 3v (right), the unit vector, v/\|v\|^2 times the magnitude (root forgotten), v divided by the magnitude |
| n10q22 | 2025 #16: p a - q b = given vector, a has a zero component that hands over q at once -> p + q; options = sum vs difference x sign |
| n10q23 | 2024s #19: a point whose coordinates all contain a lies on a line -> a; options = +-1, +-2 |
| n10q24 | 2026 #45: triangle area from two side vectors, the right angle not stated (at A here, at B in the model); options = (1/2)\|AB\|\|AC\|, without 1/2, the two lengths added, \|AB\| taken as the sum of its components (the model's list) |
| n10q25 | 2023 #19: perpendicular vectors, linear in c; options = right, sign slip, first components equated, a sign slip in one product |
| n10q26 | 2026 #47: quality control, a box rejected when the sample has defective items (one or more here, two or more in the model); options = P(X >= 1), P(X = 0), P(X = 1), P(X >= 2) |
| n10q27 | 2025s #21: spinner of congruent sectors (figure), X = spins until the pointer first stops on a given kind of sector -> E(X); options = 1/p, p, q/p, 1/q |
| n10q28 | 2024 #23: empirical rule in words, one side of the mean (figure); "less than the mean by more than one sigma" = below mu - sigma here; options = 16 %, 34 % (mu - sigma .. mu), 84 % (the complement), 13.5 % (one band only) |
| n10q29 | 2025s #23: probability below a value under the mean in context, mean and SD in words, with the table; options = right, the table value, the table value - 0.5, 0.5 + the tail |
| n10q30 | 2024 #25: P(-a < Z < b) from the table; options = right, -a treated as +a, from 0, the neighbouring column with the sign ignored |
