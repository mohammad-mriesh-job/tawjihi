# CLAUDE.md — Tawjihi advanced mathematics practice site (2008 generation)

A static React + Vite site (deployed to GitHub Pages from `main`) where Jordanian Tawjihi students practise the
ministry mathematics exam: per-unit tests, full mock papers that simulate the ministry paper, and a comprehensive
random exam. **The goal of every question is to simulate the next ministry paper.** Students' progress lives in
their browser, so published content must stay stable (see "Invariants").

## Layout

```
src/
  global/                      shared by everything
    main.tsx App.tsx theme.ts components/ pages/ lib/
    data/                      types.ts, index.ts (units from all semesters), mocks.ts (mock sets)
    question-bank/             qb.py (verification framework), explain_common.py, run.py (runs generators)
  semesters/
    index.ts                   list of semesters
    semester-N/
      index.ts                 the semester's units + mock set
      unit-M/                  uM.py (questions) · explain_uM.py (explanations) · uM.ts (GENERATED) · fig/
                               (unit-5: exams 5–10 in u5_exams_5_10.py, helpers in u5_helpers.py, explanations split
                               into explain_u5_e5…e10.py with shared wording in explain_u5_common.py)
      mock-exams/              mock_sN.py (entry) · sN_papers_*.py · sN_helpers.py · explain_sN*.py · sN.ts (GENERATED) · fig/
      previous-ministry/       official past papers (PDF), README.md index, ANALYSIS.md (semester 1)
```

Nothing content-related lives outside `src/` (only `public/favicon.svg`). `previous-ministry/` PDFs are reference
material; the site never imports them.

## Commands

```bash
npm run dev | npm run lint | npm run build          # lint + build must pass (CI runs both)
python3 -m venv .venv && .venv/bin/pip install sympy "antlr4-python3-runtime==4.11" matplotlib numpy
.venv/bin/python src/global/question-bank/run.py u3        # one generator (writes u3.ts + fig/ next to u3.py)
.venv/bin/python src/global/question-bank/run.py mock_s1   # mock papers
.venv/bin/python src/global/question-bank/run.py all
```

Never edit generated `uN.ts` / `sN.ts` by hand. Regenerating rewrites SVGs with new metadata only — if you did not
change a figure, restore it with `git checkout -- <svg>` so diffs stay clean.

## Invariants (do not break students' saved data)

- Question ids, exam ids, paper ids, routes and localStorage keys never change once published.
- Mock answer positions come from a seeded RNG consumed paper by paper (`build_mock`, seed 2026). **New papers are
  appended after existing ones; never insert, reorder or remove a published paper**, and never change a published
  question's options — a saved attempt stores the chosen option index. Before committing, confirm the old papers in
  the generated `sN.ts` are byte-identical to the previous commit.
- If a published paper must be rewritten anyway (done once: semester-1 papers 6–10 on 2026-10-15), add it to
  `REVISION` in `src/global/lib/mockStore.ts` (or bump its number) so saved sessions/results of the old questions are
  not replayed against the new ones.
- Do not modify published papers when asked to improve "new" ones (the user's explicit rule: e.g. restyle semester-1
  papers 6–10 only, never 1–5).
- While a student is solving (unit exams, the comprehensive exam, mock papers) never show the question's lesson or
  difficulty, nor the difficulty mix of an exam; both belong to the review after submission (the user's explicit rule).
- Every `.py` file name under `src/` must be unique (explanation files import each other across units; `run.py`
  puts all question-bank folders on one import path and stops on duplicates).

## How to write questions (process and mentality)

Read `src/semesters/semester-1/previous-ministry/ANALYSIS.md` before writing or editing any item. In short:

1. **Start from a specific ministry item, not from the textbook exercise.** Every new item is a *sibling* of one
   named official item: same skill, same stem structure, same kind of function and numbers, same difficulty and
   option grid — only the function and numbers change. Write the model in a comment above the `Q(...)`
   (e.g. `# 2026 #13: log base a of (c + ln x), f'(e); options = e vs 1/e x ln(a^n)`); ANALYSIS.md section 9
   lists the mapping for papers 6–10. Restyling options alone is NOT modelling (that was tried for papers 6–10
   and rejected). The blueprint is the 2026 paper (items 1–25 = semester 1: unit 1 → 1–3, unit 2 → 4–8, unit 3 →
   9–18, unit 4 → 19–25); our 30-item semester-1 mocks scale this to 4 · 6 · 12 · 8 in the same order, cover
   every 2026 pattern, and take the remaining slots from 2023–2025 and the 2026 repeaters paper.
2. **Stay inside the 2008 curriculum.** Lesson ids are in each `uN.py` `meta`. Extrema, monotonicity, concavity,
   optimisation, limits/continuity appear in 2023–2025 papers but are NOT in the 2008 semester-1 units.
3. **Phrase like the ministry**: `إذا كان: …، فإنّ … هو/هي:` · `أيُّ الآتية …؟` · `حلول المعادلة … في الفترة … هي:`;
   short stems, units in context stems and in options, `❖` notes and one shared stem for two items (complex numbers).
4. **Build options as a 2×2 grid of the two most likely mistakes** (the ministry's signature: 17 of 25 semester-1
   items in 2026). Typical switches: sign, reciprocal, missing `ln a`, missing chain factor, radius vs diameter,
   unit conversion (L→m³, km→m), quadrant / reference angle, `z` vs `z̄`, sum vs product, `<` vs `≤`, centre sign.
   Otherwise use a list of values of the same kind (±k pairs, unit fractions, small integers, quadrantal angles).
   All four options must look like the same answer.
5. **Regions in the complex plane**: options = centre sign × which boundary is strict; give the figure at least one
   dashed boundary so strictness matters. Encode every option as a predicate (`disk`, `outside`, `sector`,
   `nearer`, `closer`, `bisector`, `both` in `s1_papers_6_10.py`); `region_truth` checks the options differ from the shaded
   region inside the plane and on its boundary, and the figure is shaded from the correct predicate.
6. **Figures where the ministry uses them**: two piecewise-linear graphs on a grid, the graph of f or f′, an applied
   diagram for related rates (tank, ladder, kite, camera…), points in the complex plane, the shaded region.
7. **Explain like a teacher** (`explain_*.py`, Arabic, addressing the student in the feminine as the site does):
   `idea`, staged `steps` (`## ` headings), optional `quick` exam shortcut, `wrong` = one reason per wrong option
   that names the switch it was built from, optional `tip`. Formulas must not start with `=`/arrows and must not
   contain Arabic (the build asserts this).
8. **Verify** — every item goes through `qb.verify` (truth computed independently matches only the correct option,
   each option's LaTeX parses to its value, stem formulas parse to the expression the truth came from). Use
   `IndexQ` + a property for interval/region answers; `manual=` only when nothing can be computed (avoid).
   Parser pitfalls: `\log` parses as `ln` (write a base-10 `log` stem as plain text, not through `F`), and
   `2x\ln 10` loses the `x` (write `2x\cdot\ln 10`).
9. **Check before handing over**: generator passes; no repeated formula *or repeated context with new numbers* across
   papers and unit banks; KaTeX renders every formula; look at every new figure (render
   the SVG to PNG and view it); no formula/value duplicates the earlier mocks or the unit banks; answer key of each
   new paper stays balanced (8·8·7·7); old papers byte-identical; `npm run lint && npm run build`; drive a paper in
   a headless browser (start → submit → review) to see figures and explanations.

## Past ministry papers (`previous-ministry/`)

- Source: the ministry's official archive, linked from https://moe.gov.jo/ar/node/50540 → public Drive folder
  `1yUbburoYgd3-ab9LDC21AuL_1UanCasS` ("دورات سابقة كل الفروع", 2018–2026). PDFs are scans that bundle every
  subject of an exam day.
- How they were collected: list the Drive folders (the folder page embeds the file list), download each academic-
  branch PDF, OCR the top of every page with macOS Vision (a small Swift `VNRecognizeTextRequest` tool, Arabic) to
  find `المبحث: الرياضيات` headers and the branch, derive page ranges from the next exam header, check every range by
  eye on contact sheets, then cut the pages with PyMuPDF. Each folder's `README.md` lists file, session, date,
  paper, curriculum and the original file + pages.
- Curricula: 2023–2025 papers + 2026 "المنهاج القديم" (repeaters) use the 2023–2025 books (closest to ours);
  2026 "الثاني عشر الأكاديمي" is the 2008 generation (the blueprint); 2020–2023 `old-curriculum/` uses Arabic
  notation and older content. Not included: 2023 supplementary paper 1 (not in the archive), 2020 supplementary
  (branch unreadable), 2018–2019 (handwritten model answers only).
- When a new session is published: add it with the same pipeline, update the README index, re-read its semester
  items and update `ANALYSIS.md` (blueprint table, grid frequency, new contexts) before writing new mock papers.

## Docs

`README.md` (Arabic, for maintainers), `QUALITY.md` (sources, verification, per-mock-set coverage),
`previous-ministry/ANALYSIS.md` (ministry item-writing analysis). Update them when content changes.
