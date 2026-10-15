"""Run question-bank generators after verifying them; each writes its .ts (and fig/*.svg) next to itself.

    python src/global/question-bank/run.py u3              # one unit
    python src/global/question-bank/run.py mock_s1 mock_s2 # mock papers
    python src/global/question-bank/run.py all             # every generator

Generators live in their unit folders (src/semesters/semester-N/unit-M/uM.py, .../mock-exams/mock_sN.py).
All question-bank folders share one import namespace (explain files import each other across units),
so every .py file name under src/ must be unique.
"""
import os, re, runpy, subprocess, sys
from glob import glob

HERE = os.path.dirname(os.path.abspath(__file__))
SEMESTERS = os.path.normpath(os.path.join(HERE, '..', '..', 'semesters'))


def modules():
    """{module name: path} for every .py file in global/question-bank and the semester folders."""
    found = {}
    for path in sorted(glob(os.path.join(HERE, '*.py')) + glob(os.path.join(SEMESTERS, '**', '*.py'), recursive=True)):
        name = os.path.splitext(os.path.basename(path))[0]
        if name in found:
            sys.exit(f'duplicate module name {name!r}: {found[name]} and {path}')
        found[name] = path
    return found


def generators(mods):
    """Semester modules that write a data file (call build/build_mock); the rest (explain_*, helpers,
    paper lists) are imported by them."""
    def builds(path):
        with open(path, encoding='utf-8') as f_:
            return re.search(r'^\s*build(_mock)?\(', f_.read(), re.M) is not None
    return [n for n in mods if os.path.dirname(mods[n]) != HERE and builds(mods[n])]


def run_one(path, mods):
    sys.path[:0] = sorted({os.path.dirname(p) for p in mods.values()})
    sys.argv = [path]
    runpy.run_path(path, run_name='__main__')


def main(args):
    mods = modules()
    gens = generators(mods)
    names = gens if args == ['all'] else args
    if not names:
        sys.exit(__doc__ + '\ngenerators: ' + ' '.join(gens))
    unknown = [n for n in names if n not in gens]
    if unknown:
        sys.exit(f'unknown generator(s) {unknown}; available: {" ".join(gens)}')
    if len(names) == 1:
        run_one(mods[names[0]], mods)
        return
    # one process per generator, so they never share sympy/matplotlib state
    for n in names:
        subprocess.run([sys.executable, __file__, n], check=True)


if __name__ == '__main__':
    main(sys.argv[1:])
