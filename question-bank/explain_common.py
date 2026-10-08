"""Shared wording for the explanations (explain_*.py). Steps starting with '## ' are stage headings."""
from qb import explanation as E, synth, SYNTH_HOW  # noqa: F401  (re-exported for the explain files)

# ---- unit 1
REM = r"نظرية الباقي: إذا قُسم كثير الحدود $f(x)$ على $(x-a)$ فإن الباقي يساوي $f(a)$ ، أي نعوّض صفر المقسوم عليه في الاقتران."
FAC = r"نظرية العوامل: $(x-a)$ عامل من عوامل $f(x)$ إذا وفقط إذا كان $f(a)=0$ (أي الباقي صفر)."
MULT = r"نضرب طرفي المعادلة في المقام الأصلي، فتختفي الكسور من الطرفين:"
# ---- trigonometry
QUADS = r"حدود الأرباع: الأول بين $0$ و $\frac{\pi}{2}$ ، الثاني بين $\frac{\pi}{2}$ و $\pi$ ، الثالث بين $\pi$ و $\frac{3\pi}{2}$ ، الرابع بين $\frac{3\pi}{2}$ و $2\pi$"
SIGNS = r"قاعدة الإشارات: في الربع الأول كل النسب موجبة، في الثاني $\sin$ فقط موجب، في الثالث $\tan$ فقط موجب، في الرابع $\cos$ فقط موجب (وتأخذ $\csc,\ \sec,\ \cot$ إشارة مقلوباتها)"
