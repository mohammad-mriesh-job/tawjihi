from qb import *

L1, L2, L3 = 'u6-l1', 'u6-l2', 'u6-l3'
meta = dict(id='u6', number=6, semester=2, title='المتجهات',
    description='النقاط والمتجهات في الفضاء: المقدار ومتجه الوحدة والتوازي ونقطة المنتصف ومسائل النسبة، معادلة المستقيم في الفضاء والعلاقة بين مستقيمين ونقطة التقاطع، والضرب القياسي والزاوية بين متجهين.',
    lessons=[dict(id=L1, title='المتجهات في الفضاء'), dict(id=L2, title='المستقيمات في الفضاء'),
             dict(id=L3, title='الضرب القياسي')])
R = Rational
P = pi
V = lambda *c_: Matrix(c_)
T3 = lambda m_: Tuple(*list(m_))
def vt(*c_):
    return r'\langle ' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + r'\rangle'
def vec_opt(*c_):
    return O(vt(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'vec')
def pt_opt(*c_):
    return O('(' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + ')', Tuple(*[sympify(q_) for q_ in c_]), 'tuple')
def line_opt(p_, d_):
    return O(r'\vec{\mathbf{r}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')
def par(u_, v_): return Matrix(u_).cross(Matrix(v_)) == zeros(3, 1)
def on_line(pt_, ln):
    p0, d0 = Matrix(ln[0]), Matrix(ln[1])
    return par(Matrix(pt_) - p0, d0)
def classify(a1, d1, a2, d2):
    a1, d1, a2, d2 = map(Matrix, (a1, d1, a2, d2))
    if par(d1, d2):
        return 'coincident' if par(a2 - a1, d1) else 'parallel'
    s_, t_ = symbols('s_ t_')
    return 'intersect' if solve(list(a1 + t_*d1 - a2 - s_*d2), [t_, s_], dict=True) else 'skew'
def inter(a1, d1, a2, d2):
    a1, d1, a2, d2 = map(Matrix, (a1, d1, a2, d2))
    s_, t_ = symbols('s_ t_')
    sol = solve(list(a1 + t_*d1 - a2 - s_*d2), [t_, s_], dict=True)[0]
    return T3(a1 + sol[t_]*d1)
REL = [('متوازيان', 'parallel'), ('متقاطعان', 'intersect'), ('متخالفان', 'skew'), ('منطبقان', 'coincident')]
def rel_opts(first):
    order = [r_ for r_ in REL if r_[1] == first] + [r_ for r_ in REL if r_[1] != first]
    return [T(t_, v_) for t_, v_ in order]
def ang(u_, v_):
    u_, v_ = Matrix(u_), Matrix(v_)
    return acos(u_.dot(v_)/(u_.norm()*v_.norm()))
va, vb, vc = symbols('a b c')     # stand-ins for the vectors a, b, c in ratio problems
def vtex(expr):
    """LaTeX for a combination of the vector symbols a, b, c, written like the book: 4/3 a + b"""
    expr = expand(expr)
    out = ''
    for sym_, name in ((va, 'a'), (vb, 'b'), (vc, 'c')):
        cf = expr.coeff(sym_)
        if cf == 0:
            continue
        sign = '-' if cf < 0 else ('+' if out else '')
        mag = abs(cf)
        coef = '' if mag == 1 else latex(mag)
        out += f'{sign}{coef}' + r'\vec{\mathbf{' + name + '}}'
    return out


# ---------- figures
def fig_triangle(fig, ax):
    ax.set_xlim(-0.5, 6.5); ax.set_ylim(-0.6, 4.2); ax.axis('off'); ax.set_aspect('equal')
    O_, A_, B_ = (0, 0), (2, 3.5), (6, 0)
    M_ = (A_[0] + (B_[0] - A_[0])/3, A_[1] + (B_[1] - A_[1])/3)
    for (p1, p2) in [(O_, A_), (O_, B_), (A_, B_)]:
        ax.annotate('', xy=p2, xytext=p1, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6)) if (p1, p2) != (A_, B_) else ax.plot([A_[0], B_[0]], [A_[1], B_[1]], color='#1f5fbf', lw=1.6)
    ax.annotate('', xy=M_, xytext=O_, arrowprops=dict(arrowstyle='-|>', color='#d04a1a', lw=1.6))
    for (p_, s_, dx, dy) in [(O_, 'O', -0.35, -0.3), (A_, 'A', -0.1, 0.2), (B_, 'B', 0.1, -0.3), (M_, 'M', 0.15, 0.1)]:
        ax.text(p_[0] + dx, p_[1] + dy, f'${s_}$', fontsize=13)
    ax.text(0.45, 2.0, r'$2\vec{\mathbf{a}}$', fontsize=12, color='#1f5fbf')
    ax.text(2.8, -0.45, r'$3\vec{\mathbf{b}}$', fontsize=12, color='#1f5fbf')
    ax.plot(*M_, 'o', color='#d04a1a', ms=4)

def fig_box(fig, ax):
    import numpy as np
    ax.axis('off'); ax.set_aspect('equal')
    def proj(x_, y_, z_):  # oblique projection: x toward lower-left
        return (y_ - 0.55*x_, z_ - 0.35*x_)
    vtx = {'O': (0, 0, 0), 'P': (4, 0, 0), 'Q': (4, 6, 0), 'R': (0, 6, 0), 'S': (0, 0, 3), 'T': (4, 0, 3), 'U': (4, 6, 3), 'V': (0, 6, 3)}
    edges = ['OP', 'PQ', 'QR', 'RO', 'SR', 'OS', 'PT', 'QU', 'RV', 'ST', 'TU', 'UV', 'VS']
    for e in ['OP', 'PQ', 'QR', 'RO', 'OS', 'PT', 'QU', 'RV', 'ST', 'TU', 'UV', 'VS']:
        a1, a2 = proj(*vtx[e[0]]), proj(*vtx[e[1]])
        hidden = e in ('OP', 'RO', 'OS')
        ax.plot([a1[0], a2[0]], [a1[1], a2[1]], ls='--' if hidden else '-', color='#555555', lw=1.3)
    for ax_end, lab in [((6.5, 0, 0), 'x'), ((0, 8.2, 0), 'y'), ((0, 0, 4.6), 'z')]:
        a2 = proj(*ax_end)
        ax.annotate('', xy=a2, xytext=proj(0, 0, 0), arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2))
        ax.text(a2[0] + 0.1, a2[1] + 0.1, f'${lab}$', color='#1f5fbf', fontsize=12)
    for k_, p_ in vtx.items():
        q_ = proj(*p_)
        ax.plot(*q_, 'o', color='#222222', ms=3)
        ax.text(q_[0] + 0.12, q_[1] + 0.12, f'${k_}$', fontsize=12)
    ax.set_xlim(-4.2, 8.8); ax.set_ylim(-2.6, 5.2)

def fig_parallelogram(fig, ax):
    ax.axis('off'); ax.set_aspect('equal')
    O_, A_, C_ = (0, 0), (4, 0), (1.5, 3)
    B_ = (A_[0] + C_[0], A_[1] + C_[1])
    Mx = ((B_[0] + C_[0])/2, (B_[1] + C_[1])/2)
    Pp = (2*B_[0]/3, 2*B_[1]/3)
    ax.plot([O_[0], A_[0], B_[0], C_[0], O_[0]], [O_[1], A_[1], B_[1], C_[1], O_[1]], color='#1f5fbf', lw=1.6)
    ax.plot([O_[0], B_[0]], [O_[1], B_[1]], color='#888888', lw=1.2, ls='--')
    ax.annotate('', xy=A_, xytext=O_, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
    ax.annotate('', xy=C_, xytext=O_, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
    ax.annotate('', xy=Mx, xytext=Pp, arrowprops=dict(arrowstyle='-|>', color='#d04a1a', lw=1.6))
    for (p_, s_, dx, dy) in [(O_, 'O', -0.35, -0.3), (A_, 'A', 0.1, -0.35), (B_, 'B', 0.1, 0.1), (C_, 'C', -0.35, 0.1), (Mx, 'M', -0.1, 0.18), (Pp, 'P', 0.15, -0.25)]:
        ax.text(p_[0] + dx, p_[1] + dy, f'${s_}$', fontsize=13)
        ax.plot(*p_, 'o', color='#222222', ms=3)
    ax.text(1.7, -0.5, r'$2\vec{\mathbf{a}}$', fontsize=12, color='#1f5fbf')
    ax.text(0.05, 1.7, r'$3\vec{\mathbf{c}}$', fontsize=12, color='#1f5fbf')
    ax.set_xlim(-0.6, 6.2); ax.set_ylim(-0.8, 3.6)

# ============================================================== Exam 1
A1, B1 = V(1, 2, -3), V(4, -1, 2)
E1 = [
Q('u6e1q1', L1, 'easy',
  r"إذا كانت: $A(3,\,-2,\,2)$ ، $B(-3,\,1,\,4)$ نقطتين في الفضاء، فإنّ مقدار المتجه $\overrightarrow{AB}$ هو:",
  [O('7', 7), O('49', 49), O('5', 5), O(r'\sqrt{13}', sqrt(13))],
  r"$\overrightarrow{AB}=\langle -3-3,\,1+2,\,4-2\rangle=\langle -6,\,3,\,2\rangle$ ، و $|\overrightarrow{AB}|=\sqrt{36+9+4}=\sqrt{49}=7$",
  truth=(V(-3, 1, 4)-V(3, -2, 2)).norm()),
Q('u6e1q2', L1, 'medium',
  r"إذا كانت: $A(1,\,2,\,-3)$ ، $B(4,\,-1,\,2)$ ، وكانت $D$ نقطة في الفضاء بحيث $\overrightarrow{AB}=\overrightarrow{BD}$ ، فإنّ متجه الموقع للنقطة $D$ هو:",
  [vec_opt(7, -4, 7), vec_opt(-7, 4, -7), vec_opt(3, -3, 5), vec_opt(R(5, 2), R(1, 2), R(-1, 2))],
  r"$\overrightarrow{AB}=\overrightarrow{BD} \Rightarrow B-A=D-B \Rightarrow D=2B-A$" "\n"
  r"$D=\langle 8-1,\,-2-2,\,4+3\rangle=\langle 7,\,-4,\,7\rangle$ (أي أن $B$ منتصف $\overline{AD}$)",
  truth=T3(2*B1-A1)),
Q('u6e1q3', L1, 'medium',
  r"إذا كانت: $A(1,\,2,\,-3)$ ، $C(\alpha,\,3,\,2)$ ، وكان: $|\overrightarrow{AC}|=\sqrt{30}$ ، حيث $\alpha>0$ ، فإنّ قيمة الثابت $\alpha$ هي:",
  [O('3', 3), O('-1', -1), O('5', 5), O('1', 1)],
  r"$\overrightarrow{AC}=\langle \alpha-1,\,1,\,5\rangle$ ، و $(\alpha-1)^2+1+25=30 \Rightarrow (\alpha-1)^2=4$" "\n"
  r"$\alpha-1=\pm2 \Rightarrow \alpha=3$ أو $\alpha=-1$ ، وبما أن $\alpha>0$ فإن $\alpha=3$",
  truth=lambda: [r_ for r_ in solve((x-1)**2+1+25-30, x) if r_ > 0][0]),
Q('u6e1q4', L1, 'easy',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 6,\,-2,\,3\rangle$ ، فإنّ متجه الوحدة في اتجاه المتجه $\vec{\mathbf{v}}$ هو:",
  [vec_opt(R(6, 7), R(-2, 7), R(3, 7)), vec_opt(R(6, 49), R(-2, 49), R(3, 49)), vec_opt(R(-6, 7), R(2, 7), R(-3, 7)), vec_opt(R(6, 11), R(-2, 11), R(3, 11))],
  r"$|\vec{\mathbf{v}}|=\sqrt{36+4+9}=7$ ، ومتجه الوحدة $\dfrac{\vec{\mathbf{v}}}{|\vec{\mathbf{v}}|}=\left\langle \frac67,\,-\frac27,\,\frac37\right\rangle$",
  truth=T3(V(6, -2, 3)/7)),
Q('u6e1q5', L1, 'hard',
  r"في الشكل الآتي $OAB$ مثلث فيه: $\overrightarrow{OA}=2\vec{\mathbf{a}}$ ، $\overrightarrow{OB}=3\vec{\mathbf{b}}$ ، والنقطة $M$ تقع على الضلع $\overline{AB}$ بحيث $AM:MB=1:2$. المتجه $\overrightarrow{OM}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [O(vtex(R(4, 3)*va+vb), R(4, 3)*va+vb), O(vtex(R(2, 3)*va+2*vb), R(2, 3)*va+2*vb), O(vtex(2*va+vb), 2*va+vb), O(vtex(va+R(3, 2)*vb), va+R(3, 2)*vb)],
  r"$\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}=3\vec{\mathbf{b}}-2\vec{\mathbf{a}}$ ، و $\overrightarrow{AM}=\frac13\overrightarrow{AB}$ (لأن $AM:MB=1:2$)" "\n"
  r"$\overrightarrow{OM}=\overrightarrow{OA}+\frac13\overrightarrow{AB}=2\vec{\mathbf{a}}+\vec{\mathbf{b}}-\frac23\vec{\mathbf{a}}=\frac43\vec{\mathbf{a}}+\vec{\mathbf{b}}$",
  truth=2*va + R(1, 3)*(3*vb-2*va), figure=figure('u6e1q5', fig_triangle, 3.8, 2.6)),
IndexQ('u6e1q6', L2, 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=2\hat{i}-3\hat{j}+\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $4\hat{i}+\hat{j}-2\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((4, 1, -2), (2, -3, 1)), line_opt((2, -3, 1), (4, 1, -2)), line_opt((4, 1, -2), (-3, 2, 1)), line_opt((1, 4, -2), (2, -3, 1))],
  r"معادلة المستقيم: $\vec{\mathbf{r}}=\vec{\mathbf{r}}_0+t\vec{\mathbf{v}}$ ، حيث $\vec{\mathbf{r}}_0=\langle 4,1,-2\rangle$ متجه موقع نقطة عليه، و $\vec{\mathbf{v}}=\langle 2,-3,1\rangle$ متجه اتجاهه.",
  truth=lambda vals: only(vals, lambda ln: on_line((4, 1, -2), ln) and par(ln[1], (2, -3, 1)))),
Q('u6e1q7', L2, 'medium',
  r"النقطة الواقعة على المستقيم الذي له المعادلة المتجهة: $\vec{\mathbf{r}}=\langle 1,\,-2,\,3\rangle+t\langle 2,\,1,\,-1\rangle$ ، والإحداثي $z$ لها $-1$ ، هي:",
  [pt_opt(9, 2, -1), pt_opt(-7, -6, 7), pt_opt(7, 1, 0), pt_opt(9, -2, -1)],
  r"$z=3-t=-1 \Rightarrow t=4$ ، فتكون النقطة $(1+8,\ -2+4,\ -1)=(9,\,2,\,-1)$",
  truth=lambda: T3(V(1, -2, 3)+solve(3-t+1, t)[0]*V(2, 1, -1))),
Q('u6e1q8', L2, 'medium',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 1,1,0\rangle+t\langle 2,-1,3\rangle$ و $\vec{\mathbf{r}}_2=\langle 3,0,4\rangle+s\langle -4,2,-6\rangle$ هي أنّهما:",
  rel_opts('parallel'),
  r"$\langle -4,2,-6\rangle=-2\langle 2,-1,3\rangle$ ، فمتجها الاتجاه متوازيان، والمستقيمان إمّا متوازيان أو منطبقان." "\n"
  r"المتجه بين النقطتين $(1,1,0)$ و $(3,0,4)$ هو $\langle 2,-1,4\rangle$ ، وهو لا يوازي $\langle 2,-1,3\rangle$ ، فالنقطة $(3,0,4)$ لا تقع على $\vec{\mathbf{r}}_1$" "\n"
  r"إذن المستقيمان متوازيان.",
  truth=classify((1, 1, 0), (2, -1, 3), (3, 0, 4), (-4, 2, -6))),
Q('u6e1q9', L2, 'hard',
  r"إحداثيات نقطة تقاطع المستقيمين: $\vec{\mathbf{r}}_1=\langle 2,1,0\rangle+t\langle 1,2,-1\rangle$ و $\vec{\mathbf{r}}_2=\langle 7,4,0\rangle+s\langle 3,-1,2\rangle$ هي:",
  [pt_opt(4, 5, -2), pt_opt(7, 4, 0), pt_opt(3, 3, -1), pt_opt(1, 6, -4)],
  r"نساوي الإحداثيات: $2+t=7+3s$ ، $1+2t=4-s$ ، $-t=2s$" "\n"
  r"من الثالثة: $t=-2s$ ، وبالتعويض في الأولى: $2-2s=7+3s \Rightarrow s=-1,\ t=2$" "\n"
  r"تحقق في الثانية: $1+4=5=4+1$ ✔ ، ونقطة التقاطع $\langle 2,1,0\rangle+2\langle 1,2,-1\rangle=(4,\,5,\,-2)$",
  truth=lambda: inter((2, 1, 0), (1, 2, -1), (7, 4, 0), (3, -1, 2))),
Q('u6e1q10', L3, 'easy',
  r"إذا كان المتجهان: $\vec{\mathbf{u}}=\langle 3,\,-1,\,2\rangle$ و $\vec{\mathbf{v}}=\langle 1,\,4,\,k\rangle$ متعامدين، فإنّ قيمة $k$ هي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2)), O('2', 2), O(r'\frac{7}{2}', R(7, 2))],
  r"المتجهان متعامدان إذا كان $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=0$: $3-4+2k=0 \Rightarrow k=\frac12$",
  truth=lambda: solve(V(3, -1, 2).dot(V(1, 4, k)), k)[0]),
Q('u6e1q11', L3, 'medium',
  r"إذا كان: $\vec{\mathbf{a}}=\langle 2,\,1,\,-1\rangle$ ، $\vec{\mathbf{b}}=\langle 1,\,-1,\,2\rangle$ ، فإنّ قياس الزاوية بين المتجهين $(\vec{\mathbf{a}}-\vec{\mathbf{b}})$ و $(\vec{\mathbf{a}}+\vec{\mathbf{b}})$ هو:",
  [O(r'\frac{\pi}{2}', P/2), O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{4}', P/4), O(r'\frac{\pi}{6}', P/6)],
  r"$\vec{\mathbf{a}}-\vec{\mathbf{b}}=\langle 1,2,-3\rangle$ ، $\vec{\mathbf{a}}+\vec{\mathbf{b}}=\langle 3,0,1\rangle$" "\n"
  r"الضرب القياسي $=3+0-3=0$ ، إذن الزاوية $\frac{\pi}{2}$" "\n"
  r"(ملاحظة: $(\vec{\mathbf{a}}-\vec{\mathbf{b}})\cdot(\vec{\mathbf{a}}+\vec{\mathbf{b}})=|\vec{\mathbf{a}}|^2-|\vec{\mathbf{b}}|^2=6-6=0$)",
  truth=ang(V(2, 1, -1)-V(1, -1, 2), V(2, 1, -1)+V(1, -1, 2))),
Q('u6e1q12', L3, 'hard',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{BA}=\langle 2,\,-1,\,2\rangle$ ، $\overrightarrow{BC}=\langle 4,\,4,\,-2\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O('9', 9), O('18', 18), O('6', 6), O('12', 12)],
  r"$\overrightarrow{BA}\cdot\overrightarrow{BC}=8-4-4=0$ ، إذن الزاوية $B$ قائمة" "\n"
  r"$|\overrightarrow{BA}|=3$ ، $|\overrightarrow{BC}|=\sqrt{16+16+4}=6$ ، والمساحة $=\frac12(3)(6)=9$",
  truth=R(1, 2)*V(2, -1, 2).norm()*V(4, 4, -2).norm()*sin(ang(V(2, -1, 2), V(4, 4, -2)))),
]

# ============================================================== Exam 2
E2 = [
Q('u6e2q1', L1, 'easy',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 1,\,-2,\,4\rangle$ ، $\vec{\mathbf{w}}=\langle 3,\,0,\,-1\rangle$ ، فإنّ $3\vec{\mathbf{v}}-2\vec{\mathbf{w}}$ يساوي:",
  [vec_opt(-3, -6, 14), vec_opt(-3, -6, 10), vec_opt(9, -6, 10), vec_opt(-3, 6, 14)],
  r"$3\vec{\mathbf{v}}=\langle 3,-6,12\rangle$ ، $2\vec{\mathbf{w}}=\langle 6,0,-2\rangle$ ، الفرق $\langle -3,\,-6,\,14\rangle$",
  truth=T3(3*V(1, -2, 4)-2*V(3, 0, -1))),
Q('u6e2q2', L1, 'medium',
  r"إذا كان المتجه $\vec{\mathbf{u}}=\langle a,\,6,\,-3\rangle$ يوازي المتجه $\vec{\mathbf{v}}=\langle 2,\,-4,\,b\rangle$ ، فإنّ قيمة $a+b$ هي:",
  [O('-1', -1), O('1', 1), O('-5', -5), O('5', 5)],
  r"المتجهان متوازيان: $\vec{\mathbf{u}}=k\vec{\mathbf{v}}$ ، من المركبة الثانية: $6=-4k \Rightarrow k=-\frac32$" "\n"
  r"$a=-\frac32(2)=-3$ ، و $-3=-\frac32b \Rightarrow b=2$ ، إذن $a+b=-1$",
  truth=lambda: (lambda s_: s_[a]+s_[b])(solve(list(V(a, 6, -3).cross(V(2, -4, b))), [a, b], dict=True)[0])),
Q('u6e2q3', L1, 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle 2,\,a-1,\,4\rangle$ ، $\overrightarrow{AC}=\langle 3,\,6,\,6\rangle$ ، فإنّ قيمة $a$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('5', 5), O('4', 4), O('3', 3), O('9', 9)],
  r"تقع النقاط على استقامة واحدة إذا توازى $\overrightarrow{AB}$ و $\overrightarrow{AC}$: $\overrightarrow{AB}=\frac23\overrightarrow{AC}$ (من المركبتين الأولى والثالثة)" "\n"
  r"$a-1=\frac23(6)=4 \Rightarrow a=5$",
  truth=lambda: solve(V(2, a-1, 4).cross(V(3, 6, 6))[2], a)[0]),
Q('u6e2q4', L1, 'hard',
  r"في متوازي المستطيلات الآتي، أحد رؤوسه نقطة الأصل $O$ ، وأحرفه $\overline{OP}$ و $\overline{OR}$ و $\overline{OS}$ على المحاور $x$ و $y$ و $z$ على الترتيب. إذا كانت إحداثيات الرأس $U$ هي $(4,\,6,\,3)$ ، فإنّ إحداثيات نقطة منتصف القطعة $\overline{PV}$ هي:",
  [pt_opt(2, 3, R(3, 2)), pt_opt(2, 3, 3), pt_opt(4, 6, 3), pt_opt(2, 0, R(3, 2))],
  r"من الشكل: $P(4,0,0)$ على المحور $x$ ، و $V(0,6,3)$ (فوق $R(0,6,0)$ بارتفاع $3$)" "\n"
  r"منتصف $\overline{PV}$: $\left(\dfrac{4+0}{2},\ \dfrac{0+6}{2},\ \dfrac{0+3}{2}\right)=\left(2,\,3,\,\frac32\right)$",
  truth=T3((V(4, 0, 0)+V(0, 6, 3))/2), figure=figure('u6e2q4', fig_box, 4.2, 2.8)),
Q('u6e2q5', L1, 'medium',
  r"إذا كان: $\vec{\mathbf{v}}=\langle c,\,-2,\,4\rangle$ ، وكان: $|\vec{\mathbf{v}}|=6$ ، فإنّ قيم $c$ هي:",
  [O(r'\pm 4', FiniteSet(4, -4), 'set'), O('4', FiniteSet(4), 'set'), O(r'\pm 2\sqrt{14}', FiniteSet(2*sqrt(14), -2*sqrt(14)), 'set'), O(r'\pm 16', FiniteSet(16, -16), 'set')],
  r"$\sqrt{c^2+4+16}=6 \Rightarrow c^2+20=36 \Rightarrow c^2=16 \Rightarrow c=\pm4$",
  truth=lambda: FiniteSet(*solve(x**2+20-36, x))),
IndexQ('u6e2q6', L2, 'easy',
  r"المعادلة المتجهة للمستقيم المارّ بالنقطتين: $A(3,\,-1,\,2)$ و $B(5,\,2,\,-2)$ هي:",
  [line_opt((3, -1, 2), (2, 3, -4)), line_opt((3, -1, 2), (5, 2, -2)), line_opt((2, 3, -4), (3, -1, 2)), line_opt((3, -1, 2), (8, 1, 0))],
  r"متجه الاتجاه $\overrightarrow{AB}=\langle 5-3,\,2+1,\,-2-2\rangle=\langle 2,\,3,\,-4\rangle$ ، والمستقيم يمرّ بـ $A$:" "\n"
  r"$\vec{\mathbf{r}}=\langle 3,-1,2\rangle+t\langle 2,3,-4\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((3, -1, 2), ln) and on_line((5, 2, -2), ln))),
Q('u6e2q7', L2, 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 6,\,-2,\,5\rangle+t\langle 3,\,1,\,-2\rangle$ معادلة متجهة للمستقيم $l$ ، فإنّ قيمة $t$ التي تُقابل نقطة تقاطع المستقيم $l$ مع المستوى $yz$ هي:",
  [O('-2', -2), O('2', 2), O(r'\frac{5}{2}', R(5, 2)), O('-3', -3)],
  r"على المستوى $yz$ يكون $x=0$: $6+3t=0 \Rightarrow t=-2$",
  truth=lambda: solve(6+3*t, t)[0]),
Q('u6e2q8', L2, 'hard',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 1,0,2\rangle+t\langle 1,1,1\rangle$ و $\vec{\mathbf{r}}_2=\langle 2,3,1\rangle+s\langle 2,-1,1\rangle$ هي أنّهما:",
  rel_opts('skew'),
  r"متجها الاتجاه غير متوازيين، فالمستقيمان إمّا متقاطعان أو متخالفان. نساوي الإحداثيات:" "\n"
  r"$1+t=2+2s$ ، $t=3-s$ ، $2+t=1+s$" "\n"
  r"من الثانية والثالثة: $2+3-s=1+s \Rightarrow s=2,\ t=1$ ، وبالتعويض في الأولى: $2\ne6$" "\n"
  r"لا يوجد حلّ مشترك، إذن المستقيمان متخالفان.",
  truth=classify((1, 0, 2), (1, 1, 1), (2, 3, 1), (2, -1, 1))),
Q('u6e2q9', L3, 'hard',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 1,\,0,\,2\rangle+t\langle 1,\,2,\,-1\rangle$ معادلة متجهة للمستقيم $l$ ، والنقطة $P(4,\,5,\,3)$ غير واقعة عليه، فإنّ إحداثيات مسقط العمود من النقطة $P$ على المستقيم $l$ هي:",
  [pt_opt(3, 4, 0), pt_opt(1, 0, 2), pt_opt(2, 2, 1), pt_opt(5, 8, -2)],
  r"نفرض المسقط $Q=(1+t,\ 2t,\ 2-t)$ ، فيكون $\overrightarrow{PQ}=\langle t-3,\ 2t-5,\ -t-1\rangle$ عموديًّا على $\langle 1,2,-1\rangle$:" "\n"
  r"$(t-3)+2(2t-5)-(-t-1)=0 \Rightarrow 6t-12=0 \Rightarrow t=2$ ، إذن $Q=(3,\,4,\,0)$",
  truth=lambda: (lambda tt: T3(V(1, 0, 2)+tt*V(1, 2, -1)))(solve((V(1, 0, 2)+t*V(1, 2, -1)-V(4, 5, 3)).dot(V(1, 2, -1)), t)[0])),
Q('u6e2q10', L3, 'easy',
  r"إذا كان: $|\vec{\mathbf{a}}|=4$ ، $|\vec{\mathbf{b}}|=5$ ، وقياس الزاوية بينهما $120^\circ$ ، فإنّ $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}$ يساوي:",
  [O('-10', -10), O('10', 10), O(r'-10\sqrt{3}', -10*sqrt(3)), O('20', 20)],
  r"$\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=|\vec{\mathbf{a}}||\vec{\mathbf{b}}|\cos\theta=4(5)\cos120^\circ=20\left(-\frac12\right)=-10$",
  truth=4*5*cos(2*pi/3)),
Q('u6e2q11', L3, 'medium',
  r"إذا كان قياس الزاوية بين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو $60^\circ$ ، وكان: $|\vec{\mathbf{a}}|=6$ ، $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=12$ ، فإنّ مقدار $\vec{\mathbf{b}}$ هو:",
  [O('4', 4), O('2', 2), O('8', 8), O(r'\frac{4\sqrt{3}}{3}', 4*sqrt(3)/3)],
  r"$12=6|\vec{\mathbf{b}}|\cos60^\circ=3|\vec{\mathbf{b}}| \Rightarrow |\vec{\mathbf{b}}|=4$",
  truth=12/(6*cos(pi/3))),
Q('u6e2q12', L3, 'medium',
  r"إذا كان المتجه: $\vec{\mathbf{v}}=3\hat{i}+c\hat{j}+2\hat{k}$ يُعامد المتجه: $\vec{\mathbf{w}}=2\hat{i}-\hat{j}+d\hat{k}$ ، حيث $c,\ d$ ثابتان، فإنّ $c-2d$ تساوي:",
  [O('6', 6), O('-6', -6), O('3', 3), O('-3', -3)],
  r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=6-c+2d=0 \Rightarrow c-2d=6$",
  truth=lambda: (lambda dd: simplify(solve(V(3, c, 2).dot(V(2, -1, dd)), c)[0] - 2*dd))(Symbol('dd'))),
]

# ============================================================== Exam 3
E3 = [
Q('u6e3q1', L1, 'easy',
  r"إحداثيات نقطة منتصف القطعة المستقيمة الواصلة بين النقطتين: $A(-2,\,5,\,1)$ و $B(4,\,-1,\,7)$ هي:",
  [pt_opt(1, 2, 4), pt_opt(2, 4, 8), pt_opt(3, -3, 3), pt_opt(-3, 3, -3)],
  r"$M=\left(\dfrac{-2+4}{2},\ \dfrac{5-1}{2},\ \dfrac{1+7}{2}\right)=(1,\,2,\,4)$",
  truth=T3((V(-2, 5, 1)+V(4, -1, 7))/2)),
Q('u6e3q2', L1, 'easy',
  r"إذا كانت: $A(3,\,-2,\,5)$ ، $B(-1,\,4,\,2)$ ، فإنّ الصورة الإحداثية للمتجه $\overrightarrow{BA}$ هي:",
  [vec_opt(4, -6, 3), vec_opt(-4, 6, -3), vec_opt(2, 2, 7), vec_opt(-2, -2, -7)],
  r"$\overrightarrow{BA}=A-B=\langle 3+1,\,-2-4,\,5-2\rangle=\langle 4,\,-6,\,3\rangle$ (لاحظ الترتيب: نهاية المتجه ناقص بدايته)",
  truth=T3(V(3, -2, 5)-V(-1, 4, 2))),
Q('u6e3q3', L1, 'medium',
  r"$ABCD$ متوازي أضلاع، فيه: $A(2,\,-1,\,3)$ ، $B(5,\,1,\,0)$ ، $C(4,\,4,\,2)$. إحداثيات الرأس $D$ هي:",
  [pt_opt(1, 2, 5), pt_opt(7, 6, -1), pt_opt(3, -4, 1), pt_opt(1, 2, -5)],
  r"في متوازي الأضلاع $\overrightarrow{AD}=\overrightarrow{BC}=\langle -1,\,3,\,2\rangle$" "\n" r"$D=A+\overrightarrow{BC}=(2-1,\ -1+3,\ 3+2)=(1,\,2,\,5)$",
  truth=T3(V(2, -1, 3)+V(4, 4, 2)-V(5, 1, 0))),
Q('u6e3q4', L1, 'hard',
  r"في الشكل الآتي $OABC$ متوازي أضلاع، فيه: $\overrightarrow{OA}=2\vec{\mathbf{a}}$ ، $\overrightarrow{OC}=3\vec{\mathbf{c}}$. إذا كانت $M$ منتصف الضلع $\overline{CB}$ ، وكانت $P$ نقطة على القطر $\overline{OB}$ بحيث $OP:PB=2:1$ ، فإنّ المتجه $\overrightarrow{PM}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{c}}$ هو:",
  [O(vtex(-R(1, 3)*va+vc), -R(1, 3)*va+vc), O(vtex(R(1, 3)*va-vc), R(1, 3)*va-vc), O(vtex(R(7, 3)*va+5*vc), R(7, 3)*va+5*vc), O(vtex(-R(1, 3)*va+5*vc), -R(1, 3)*va+5*vc)],
  r"$\overrightarrow{OM}=\overrightarrow{OC}+\frac12\overrightarrow{CB}=3\vec{\mathbf{c}}+\frac12(2\vec{\mathbf{a}})=\vec{\mathbf{a}}+3\vec{\mathbf{c}}$" "\n"
  r"$\overrightarrow{OP}=\frac23\overrightarrow{OB}=\frac23(2\vec{\mathbf{a}}+3\vec{\mathbf{c}})=\frac43\vec{\mathbf{a}}+2\vec{\mathbf{c}}$" "\n"
  r"$\overrightarrow{PM}=\overrightarrow{OM}-\overrightarrow{OP}=-\frac13\vec{\mathbf{a}}+\vec{\mathbf{c}}$",
  truth=(va + 3*vc) - R(2, 3)*(2*va + 3*vc), figure=figure('u6e3q4', fig_parallelogram, 3.8, 2.4)),
Q('u6e3q5', L1, 'medium',
  r"إذا وقعت النقاط: $P(1,\,2,\,3)$ ، $Q(3,\,h,\,7)$ ، $R(4,\,8,\,k)$ على مستقيم واحد، فإنّ قيمة $h+k$ هي:",
  [O('15', 15), O('12', 12), O('9', 9), O('18', 18)],
  r"$\overrightarrow{PQ}=\langle 2,\,h-2,\,4\rangle$ ، $\overrightarrow{PR}=\langle 3,\,6,\,k-3\rangle$ ، ويجب أن يكون $\overrightarrow{PQ}=\frac23\overrightarrow{PR}$" "\n"
  r"$h-2=4 \Rightarrow h=6$ ، و $4=\frac23(k-3) \Rightarrow k=9$ ، إذن $h+k=15$",
  truth=lambda: (lambda s_: s_[x]+s_[y])(solve(list(V(2, x-2, 4).cross(V(3, 6, y-3))), [x, y], dict=True)[0])),
Q('u6e3q6', L2, 'easy',
  r"النقطة الواقعة على المستقيم: $\vec{\mathbf{r}}=\langle -1,\,4,\,2\rangle+t\langle 2,\,-1,\,3\rangle$ ، والإحداثي $y$ لها يساوي $1$ ، هي:",
  [pt_opt(5, 1, 11), pt_opt(-7, 1, -7), pt_opt(5, 1, -7), pt_opt(1, 1, 5)],
  r"$y=4-t=1 \Rightarrow t=3$ ، فالنقطة $(-1+6,\ 1,\ 2+9)=(5,\,1,\,11)$",
  truth=lambda: T3(V(-1, 4, 2)+solve(4-t-1, t)[0]*V(2, -1, 3))),
IndexQ('u6e3q7', L2, 'medium',
  r"معادلة المستقيم المارّ بالنقطة $(1,\,-1,\,2)$ ، والموازي للمستقيم: $\vec{\mathbf{r}}=\langle 0,\,3,\,1\rangle+t\langle 4,\,-2,\,1\rangle$ ، هي:",
  [line_opt((1, -1, 2), (4, -2, 1)), line_opt((0, 3, 1), (1, -1, 2)), line_opt((1, -1, 2), (0, 3, 1)), line_opt((4, -2, 1), (1, -1, 2))],
  r"المستقيمان المتوازيان لهما متجه الاتجاه نفسه $\langle 4,-2,1\rangle$ ، والمستقيم المطلوب يمرّ بالنقطة $(1,-1,2)$",
  truth=lambda vals: only(vals, lambda ln: on_line((1, -1, 2), ln) and par(ln[1], (4, -2, 1)))),
Q('u6e3q8', L2, 'hard',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 2,-1,0\rangle+t\langle 1,3,-2\rangle$ و $\vec{\mathbf{r}}_2=\langle 4,5,-4\rangle+s\langle -2,-6,4\rangle$ هي أنّهما:",
  rel_opts('coincident'),
  r"$\langle -2,-6,4\rangle=-2\langle 1,3,-2\rangle$ ، فمتجها الاتجاه متوازيان." "\n"
  r"النقطة $(4,5,-4)$ تقع على $\vec{\mathbf{r}}_1$ عند $t=2$: $\langle 2+2,\,-1+6,\,0-4\rangle=\langle 4,5,-4\rangle$ ✔" "\n" r"إذن المستقيمان منطبقان.",
  truth=classify((2, -1, 0), (1, 3, -2), (4, 5, -4), (-2, -6, 4))),
Q('u6e3q9', L2, 'hard',
  r"إحداثيات نقطة تقاطع المستقيمين: $\vec{\mathbf{r}}_1=\langle 1,0,-2\rangle+t\langle 2,-1,3\rangle$ و $\vec{\mathbf{r}}_2=\langle -3,-3,-7\rangle+s\langle 1,2,1\rangle$ هي:",
  [pt_opt(-1, 1, -5), pt_opt(3, -1, 1), pt_opt(-3, -3, -7), pt_opt(1, 0, -2)],
  r"$1+2t=-3+s$ ، $-t=-3+2s$ ، $-2+3t=-7+s$" "\n"
  r"بطرح الأولى من الثالثة: $-3+t=-4 \Rightarrow t=-1$ ، ومنه $s=2$ ، وتحقق في الثانية: $1=-3+4$ ✔" "\n"
  r"نقطة التقاطع: $\langle 1,0,-2\rangle-\langle 2,-1,3\rangle=(-1,\,1,\,-5)$",
  truth=lambda: inter((1, 0, -2), (2, -1, 3), (-3, -3, -7), (1, 2, 1))),
Q('u6e3q10', L3, 'easy',
  r"إذا كان: $\vec{\mathbf{a}}=\langle 2,\,-3,\,1\rangle$ ، $\vec{\mathbf{b}}=\langle 4,\,1,\,-2\rangle$ ، فإنّ $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}$ يساوي:",
  [O('3', 3), O('-3', -3), O('11', 11), O('7', 7)],
  r"$\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=2(4)+(-3)(1)+1(-2)=8-3-2=3$",
  truth=V(2, -3, 1).dot(V(4, 1, -2))),
Q('u6e3q11', L3, 'medium',
  r"قياس الزاوية بين المتجهين: $\langle 1,\,-1,\,0\rangle$ و $\langle 0,\,1,\,-1\rangle$ هو:",
  [O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{5\pi}{6}', 5*P/6)],
  r"$\cos\theta=\dfrac{0-1+0}{\sqrt2\cdot\sqrt2}=-\dfrac12 \Rightarrow \theta=\dfrac{2\pi}{3}$ (الزاوية بين متجهين قد تكون منفرجة)",
  truth=ang((1, -1, 0), (0, 1, -1))),
Q('u6e3q12', L3, 'hard',
  r"إذا كانت $M,\ N,\ P$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{MN}=\langle 1,\,4,\,-2\rangle$ ، $\overrightarrow{PN}=\langle 3,\,-1,\,2\rangle$ ، فإنّ $\overrightarrow{MN}\cdot\overrightarrow{MP}$ يساوي:",
  [O('26', 26), O('16', 16), O('-5', -5), O('10', 10)],
  r"$\overrightarrow{MP}=\overrightarrow{MN}+\overrightarrow{NP}=\overrightarrow{MN}-\overrightarrow{PN}=\langle -2,\,5,\,-4\rangle$" "\n"
  r"$\overrightarrow{MN}\cdot\overrightarrow{MP}=-2+20+8=26$",
  truth=V(1, 4, -2).dot(V(1, 4, -2)-V(3, -1, 2))),
]

exams = [dict(id='u6-e1', title='الاختبار الأول', questions=E1),
         dict(id='u6-e2', title='الاختبار الثاني', questions=E2),
         dict(id='u6-e3', title='الاختبار الثالث', questions=E3)]
build(meta, exams, 'u6')
