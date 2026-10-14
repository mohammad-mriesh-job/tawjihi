"""Five full mock papers for semester 2 (units 5-7), in the format of the official
half-year trial of 19 May 2026: 30 items / 90 minutes,
U5 (integration) items 1-16, U6 (vectors) items 17-25, U7 (statistics) items 26-30."""
from qb import *
import numpy as np

R = Rational
P = pi
U5 = {i: f'u5-l{i}' for i in range(1, 7)}
U6 = {1: 'u6-l1', 2: 'u6-l2', 3: 'u6-l3'}
U7 = {1: 'u7-l1', 2: 'u7-l2'}
ig = integrate
yp = Symbol('yp')
Cc = Symbol('C')

# ------------------------------------------------------------------ helpers (integration)
def A(tex, F_):
    assert tex.rstrip().endswith('+C'), tex
    return O(tex, F_, 'anti')
def ode_ok(Yx, rhs, x0, y0):
    return same(diff(Yx, x) - rhs.subs(y, Yx), 0) and same(Yx.subs(x, x0), y0)
def ode_rel_ok(Fxy, rhs, pt=None):
    """implicit (possibly general, with C) solution F(x,y)=0 of y'=rhs"""
    dydx = -diff(Fxy, x)/diff(Fxy, y)
    if not same(dydx - rhs, 0):
        return False
    return pt is None or same(Fxy.subs({x: pt[0], y: pt[1]}), 0)

def region(f_, g_, a_, b_, xlim, ylim, labels=()):
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        xs = np.linspace(xlim[0], xlim[1], 400)
        ff = lambdify(x, f_, 'numpy'); gg = lambdify(x, g_, 'numpy')
        with np.errstate(all='ignore'):
            ax.plot(xs, ff(xs) + 0*xs, color='#1f5fbf', lw=1.8)
            if g_ != 0:
                ax.plot(xs, gg(xs) + 0*xs, color='#d04a1a', lw=1.8)
            xr = np.linspace(float(a_), float(b_), 200)
            ax.fill_between(xr, ff(xr) + 0*xr, gg(xr) + 0*xr, color='#9cc3ef', alpha=0.85)
        for (tx_, ty_, s_, col) in labels:
            ax.text(tx_, ty_, s_, color=col, fontsize=11)
    return draw

def vt_graph(pts, tmax, vmin, vmax):
    def draw(fig, ax):
        axes_style(ax, (-0.4, tmax + 0.8), (vmin - 0.8, vmax + 1), xlabel=r't\,(\mathrm{s})', ylabel=r'v\,(\mathrm{m/s})', grid=True)
        ax.set_xticks(range(0, tmax + 1)); ax.set_yticks(range(vmin, vmax + 1))
        tx_, vy_ = zip(*pts)
        ax.plot(tx_, vy_, color='#1f5fbf', lw=2)
    return draw
def pw_integral(pts, a_, b_, absolute=False):
    tt = symbols('tt')
    tot = 0
    for (t1, v1), (t2, v2) in zip(pts, pts[1:]):
        seg = R(v1) + R(v2 - v1, t2 - t1)*(tt - t1)
        lo, hi = max(a_, t1), min(b_, t2)
        if lo < hi:
            tot += ig(Abs(seg) if absolute else seg, (tt, lo, hi))
    return tot

# ------------------------------------------------------------------ helpers (vectors)
V = lambda *c_: Matrix(c_)
T3 = lambda m_: Tuple(*list(m_))
def vt(*c_): return r'\langle ' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + r'\rangle'
def vec_opt(*c_): return O(vt(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'vec')
def pt_opt(*c_): return O('(' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + ')', Tuple(*[sympify(q_) for q_ in c_]), 'tuple')
def line_opt(p_, d_): return O(r'\vec{\mathbf{r}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')
def par(u_, v_): return Matrix(u_).cross(Matrix(v_)) == zeros(3, 1)
def on_line(pt_, ln): return par(Matrix(pt_) - Matrix(ln[0]), Matrix(ln[1]))
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
va, vb, vc = symbols('a b c')
def vtex(expr):
    expr = expand(expr); out = ''
    for sym_, name in ((va, 'a'), (vb, 'b'), (vc, 'c')):
        cf = expr.coeff(sym_)
        if cf == 0:
            continue
        sign = '-' if cf < 0 else ('+' if out else '')
        mag = abs(cf)
        out += f'{sign}{"" if mag == 1 else latex(mag)}' + r'\vec{\mathbf{' + name + '}}'
    return out
def vopt(expr): return O(vtex(expr), expr)

def fig_box(dx, dy, dz):
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        proj = lambda x_, y_, z_: (y_ - 0.55*x_, z_ - 0.35*x_)
        vtx = {'O': (0, 0, 0), 'P': (dx, 0, 0), 'Q': (dx, dy, 0), 'R': (0, dy, 0), 'S': (0, 0, dz), 'T': (dx, 0, dz), 'U': (dx, dy, dz), 'V': (0, dy, dz)}
        for e in ['OP', 'PQ', 'QR', 'RO', 'OS', 'PT', 'QU', 'RV', 'ST', 'TU', 'UV', 'VS']:
            a1, a2 = proj(*vtx[e[0]]), proj(*vtx[e[1]])
            ax.plot([a1[0], a2[0]], [a1[1], a2[1]], ls='--' if e in ('OP', 'RO', 'OS') else '-', color='#555', lw=1.3)
        for start, end, lab in [((dx, 0, 0), (dx*1.6, 0, 0), 'x'), ((0, dy, 0), (0, dy*1.35, 0), 'y'), ((0, 0, dz), (0, 0, dz*1.5), 'z')]:
            a1, a2 = proj(*start), proj(*end)
            ax.plot([a1[0], a2[0]], [a1[1], a2[1]], color='#1f5fbf', lw=1.2)
            ax.annotate('', xy=a2, xytext=(a1[0] + 0.8*(a2[0] - a1[0]), a1[1] + 0.8*(a2[1] - a1[1])),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2), annotation_clip=False)
            ax.text(a2[0] + 0.1, a2[1] + 0.1, f'${lab}$', color='#1f5fbf', fontsize=12)
            ax.plot([a2[0] - 0.3, a2[0] + 0.5], [a2[1] - 0.3, a2[1] + 0.5], alpha=0)
        for k_, p_ in vtx.items():
            q_ = proj(*p_); ax.plot(*q_, 'o', color='#222', ms=3); ax.text(q_[0] + 0.12, q_[1] + 0.12, f'${k_}$', fontsize=12)
        ax.autoscale(); ax.margins(0.08)
    return draw

def fig_poly(points, edges, arrows, labels, extra_dashed=()):
    """generic vector diagram: points {name:(x,y)}, edges [(A,B)], arrows [(A,B,label,(dx,dy))]"""
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        for a1, b1 in edges:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
        for a1, b1 in extra_dashed:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#888', lw=1.2, ls='--')
        for a1, b1, lab, off in arrows:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
            ax.annotate('', xy=(x1 + 0.6*(x2 - x1), y1 + 0.6*(y2 - y1)), xytext=(x1 + 0.45*(x2 - x1), y1 + 0.45*(y2 - y1)), arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
            ax.text((x1 + x2)/2 + off[0], (y1 + y2)/2 + off[1], lab, fontsize=12, color='#1f5fbf')
        for nm, (px, py) in points.items():
            ax.plot(px, py, 'o', color='#222', ms=3.5)
            d_ = labels.get(nm, (0.12, 0.12))
            ax.text(px + d_[0], py + d_[1], f'${nm}$', fontsize=13)
        ax.margins(0.1)
    return draw

# ------------------------------------------------------------------ helpers (statistics)
def Phi4(z0):
    z0 = nsimplify(z0)
    return R(str(round(float(N((1 + erf(z0/sqrt(2)))/2, 30)), 4)))
def Ph(z0):
    z0 = nsimplify(z0)
    return Phi4(z0) if z0 >= 0 else 1 - Phi4(-z0)
def ztable_lead(items, *zs):
    zs = sorted({nsimplify(q_) for q_ in zs})
    head = ' & '.join(f'{float(q_):g}' for q_ in zs)
    row = ' & '.join(f'{float(Phi4(q_)):.4f}' for q_ in zs)
    nums = ' و '.join(f'({i_})' for i_ in items)
    return (rf"❖ يمكنك الاستفادة من الجدول الآتي الذي يُمثّل بعضًا من قيم جدول التوزيع الطبيعي المعياري للإجابة عن الفقرات {nums} الآتية:"
            r"$$\begin{array}{|c|" + 'c|'*len(zs) + r"}\hline z & " + head + r"\\ \hline P(Z<z) & " + row + r"\\ \hline\end{array}$$")
def binom(n_, p_, k_): return binomial(n_, k_)*p_**k_*(1-p_)**(n_-k_)
def geo(p_, k_): return (1-p_)**(k_-1)*p_
def r4(v_): return R(str(round(float(v_), 4)))
def bell(intervals, ticks):
    def draw(fig, ax):
        xs = np.linspace(-3.6, 3.6, 400); f_ = lambda u_: np.exp(-u_**2/2)/np.sqrt(2*np.pi)
        ax.plot(xs, f_(xs), color='#1f5fbf', lw=1.8)
        for a_, b_ in intervals:
            xr = np.linspace(a_, b_, 200); ax.fill_between(xr, f_(xr), color='#9cc3ef', alpha=0.9)
        for xv in ticks:
            ax.plot([xv, xv], [0, f_(xv)], color='#1f5fbf', lw=1, ls='--')
        ax.axhline(0, color='black', lw=0.8); ax.set_yticks([])
        ax.set_xticks(ticks); ax.set_xticklabels([f'{q_:g}' for q_ in ticks])
        for side in ('top', 'right', 'left'):
            ax.spines[side].set_visible(False)
        ax.text(3.4, -0.05, '$Z$', fontsize=12); ax.set_ylim(-0.02, 0.45)
    return draw
def shared(stem, a_, b_): return rf"❖ {stem} ، فاعتمد ذلك للإجابة عن الفقرتين ({a_}) و ({b_}) الآتيتين:"

# ================================================================== PAPER 1
P1 = [
Q('n1q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{1}{1-\cos^{2}\frac{x}{3}}', 1/(1-cos(x/3)**2))),
  [A(r'-3\cot\frac{x}{3}+C', -3*cot(x/3)), A(r'3\cot\frac{x}{3}+C', 3*cot(x/3)), A(r'-\frac{1}{3}\cot\frac{x}{3}+C', -cot(x/3)/3), A(r'3\tan\frac{x}{3}+C', 3*tan(x/3))],
  r"$1-\cos^2\frac x3=\sin^2\frac x3$ ، إذن المقدار $=\csc^2\frac x3$ ، و $\displaystyle\int\csc^2\frac x3\,dx=-3\cot\frac x3+C$",
  truth=1/(1-cos(x/3)**2), tag='تكامل الاقترانات المثلثية'),
Q('n1q2', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'3^{x}\cdot 9^{x}', 3**x*9**x)),
  [A(r'\frac{27^{x}}{\ln 27}+C', 27**x/log(27)), A(r'27^{x}\ln 27+C', 27**x*log(27)), A(r'\frac{3^{x}\cdot 9^{x}}{(\ln 3)(\ln 9)}+C', 3**x*9**x/(log(3)*log(9))), A(r'\frac{27^{x+1}}{x+1}+C', 27**(x+1)/(x+1))],
  r"$3^x\cdot9^x=(3\cdot9)^x=27^x$ ، و $\displaystyle\int27^xdx=\frac{27^x}{\ln27}+C$",
  truth=3**x*9**x, tag='تكامل الاقتران الأسي'),
Q('n1q3', U5[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{2\pi}«0»\,dx=a\pi$ ، فإنّ قيمة الثابت $a$ هي:", (r'\sin^{2}\frac{x}{2}', sin(x/2)**2)),
  [O('1', 1), O(r'\frac{1}{2}', R(1, 2)), O('2', 2), O(r'\frac{1}{4}', R(1, 4))],
  r"$\sin^2\frac x2=\dfrac{1-\cos x}{2}$ ، و $\displaystyle\int_0^{2\pi}\frac{1-\cos x}{2}dx=\left[\frac x2-\frac{\sin x}{2}\right]_0^{2\pi}=\pi$ ، إذن $a=1$",
  truth=ig(sin(x/2)**2, (x, 0, 2*pi))/pi, tag='تكامل باستعمال تقليص القوة'),
IndexQ('n1q4', U5[1], 'medium',
  F(r"يُمثّل الاقتران: $f'(x)=«0»$ ميل المماس لمنحنى الاقتران $f(x)$. إذا كان منحنى $f(x)$ يمرّ بالنقطة $(0,\,3)$ ، فإنّ قاعدة الاقتران $f(x)$ هي:", (r'e^{2x}-2\sin x', exp(2*x)-2*sin(x))),
  [O(r'f(x)=\frac{1}{2}e^{2x}+2\cos x+\frac{1}{2}', exp(2*x)/2+2*cos(x)+R(1, 2), 'eq'), O(r'f(x)=\frac{1}{2}e^{2x}-2\cos x+\frac{9}{2}', exp(2*x)/2-2*cos(x)+R(9, 2), 'eq'),
   O(r'f(x)=2e^{2x}+2\cos x-1', 2*exp(2*x)+2*cos(x)-1, 'eq'), O(r'f(x)=\frac{1}{2}e^{2x}+2\cos x+3', exp(2*x)/2+2*cos(x)+3, 'eq')],
  r"$f(x)=\displaystyle\int(e^{2x}-2\sin x)dx=\frac12e^{2x}+2\cos x+C$" "\n" r"$f(0)=3 \Rightarrow \frac12+2+C=3 \Rightarrow C=\frac12$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, exp(2*x)-2*sin(x), 0, 3)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
Q('n1q5', U5[1], 'hard',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ سرعته بالمتر لكل ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلية بالأمتار التي قطعها الجُسيم في الفترة $[0,\,\pi]$ هي:", (r'4\cos 2t', 4*cos(2*t))),
  [O('8', 8), O('0', 0), O('4', 4), O('2', 2)],
  r"$v(t)=0$ عند $t=\frac{\pi}{4}$ و $t=\frac{3\pi}{4}$ ، فالمسافة $=\displaystyle\int_0^{\pi}|4\cos2t|\,dt$" "\n"
  r"$=\left[2\sin2t\right]_0^{\pi/4}+\left|\left[2\sin2t\right]_{\pi/4}^{3\pi/4}\right|+\left|\left[2\sin2t\right]_{3\pi/4}^{\pi}\right|=2+4+2=8$ (أما الإزاحة فتساوي $0$)",
  truth=ig(4*cos(2*t), (t, 0, pi/4))-ig(4*cos(2*t), (t, pi/4, 3*pi/4))+ig(4*cos(2*t), (t, 3*pi/4, pi)), tag='الحركة: المسافة الكلية من السرعة'),
Q('n1q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{e^{\frac{1}{x}}}{x^{2}}', exp(1/x)/x**2)),
  [A(r'-e^{\frac{1}{x}}+C', -exp(1/x)), A(r'e^{\frac{1}{x}}+C', exp(1/x)), A(r'-\frac{e^{\frac{1}{x}}}{x}+C', -exp(1/x)/x), A(r'\frac{e^{\frac{1}{x}}}{x^{3}}+C', exp(1/x)/x**3)],
  r"بالتعويض $u=\dfrac1x \Rightarrow du=-\dfrac{1}{x^2}dx$: $\displaystyle-\int e^udu=-e^u+C=-e^{\frac1x}+C$",
  truth=exp(1/x)/x**2, tag='التكامل بالتعويض'),
Q('n1q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\cos^{3}x}{\sin^{2}x}', cos(x)**3/sin(x)**2)),
  [A(r'-\csc x-\sin x+C', -csc(x)-sin(x)), A(r'\csc x+\sin x+C', csc(x)+sin(x)), A(r'-\csc x+\sin x+C', -csc(x)+sin(x)), A(r'-\cot x-\sin x+C', -cot(x)-sin(x))],
  r"$\cos^3x=(1-\sin^2x)\cos x$ ، وبالتعويض $u=\sin x \Rightarrow du=\cos x\,dx$:" "\n" r"$\displaystyle\int\frac{1-u^2}{u^2}du=\int(u^{-2}-1)du=-\frac1u-u+C=-\csc x-\sin x+C$",
  truth=cos(x)**3/sin(x)**2, tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
Q('n1q8', U5[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x(2-x)^{4}', x*(2-x)**4)),
  [A(r'\frac{(2-x)^{6}}{6}-\frac{2(2-x)^{5}}{5}+C', (2-x)**6/6-2*(2-x)**5/5), A(r'\frac{2(2-x)^{5}}{5}-\frac{(2-x)^{6}}{6}+C', 2*(2-x)**5/5-(2-x)**6/6),
   A(r'\frac{(2-x)^{6}}{6}+\frac{2(2-x)^{5}}{5}+C', (2-x)**6/6+2*(2-x)**5/5), A(r'-\frac{x^{2}(2-x)^{5}}{10}+C', -x**2*(2-x)**5/10)],
  r"بالتعويض $u=2-x \Rightarrow x=2-u$ ، $dx=-du$:" "\n"
  r"$\displaystyle-\int(2-u)u^4du=-\left(\frac{2u^5}{5}-\frac{u^6}{6}\right)+C=\frac{(2-x)^6}{6}-\frac{2(2-x)^5}{5}+C$",
  truth=x*(2-x)**4, tag='التكامل بالتعويض: قوى مقدار خطي'),
Q('n1q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{1}^{2}«0»\,dx$ هي:", (r'x(x-1)^{4}', x*(x-1)**4)),
  [O(r'\frac{11}{30}', R(11, 30)), O(r'\frac{1}{30}', R(1, 30)), O(r'\frac{1}{5}', R(1, 5)), O(r'\frac{7}{30}', R(7, 30))],
  r"بالتعويض $u=x-1$ ، $x=u+1$ ، والحدود: $x=1\to u=0$ ، $x=2\to u=1$" "\n" r"$\displaystyle\int_0^1(u+1)u^4du=\left[\frac{u^6}{6}+\frac{u^5}{5}\right]_0^1=\frac16+\frac15=\frac{11}{30}$",
  truth=ig(x*(x-1)**4, (x, 1, 2)), tag='التكامل المحدود بالتعويض'),
Q('n1q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{5x-1}{x^{2}-x-2}', (5*x-1)/(x**2-x-2))),
  [A(r'3\ln|x-2|+2\ln|x+1|+C', 3*log(x-2)+2*log(x+1)), A(r'2\ln|x-2|+3\ln|x+1|+C', 2*log(x-2)+3*log(x+1)), A(r'3\ln|x-2|-2\ln|x+1|+C', 3*log(x-2)-2*log(x+1)), A(r'3\ln|x+2|+2\ln|x-1|+C', 3*log(x+2)+2*log(x-1))],
  r"$x^2-x-2=(x-2)(x+1)$ ، و $\dfrac{5x-1}{(x-2)(x+1)}=\dfrac{A}{x-2}+\dfrac{B}{x+1}$" "\n" r"عند $x=2$: $9=3A \Rightarrow A=3$ ، عند $x=-1$: $-6=-3B \Rightarrow B=2$",
  truth=(5*x-1)/(x**2-x-2), tag='التكامل بالكسور الجزئية: عوامل خطية'),
Q('n1q11', U5[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{2}+8}{x^{3}+4x}', (x**2+8)/(x**3+4*x))),
  [A(r'2\ln|x|-\frac{1}{2}\ln(x^{2}+4)+C', 2*log(x)-log(x**2+4)/2), A(r'2\ln|x|+\frac{1}{2}\ln(x^{2}+4)+C', 2*log(x)+log(x**2+4)/2),
   A(r'2\ln|x|-\ln(x^{2}+4)+C', 2*log(x)-log(x**2+4)), A(r'8\ln|x|-\frac{7}{2}\ln(x^{2}+4)+C', 8*log(x)-R(7, 2)*log(x**2+4))],
  r"$\dfrac{x^2+8}{x(x^2+4)}=\dfrac{A}{x}+\dfrac{Bx+D}{x^2+4}$ ، عند $x=0$: $8=4A \Rightarrow A=2$ ، ومعامل $x^2$: $1=A+B \Rightarrow B=-1$ ، و $D=0$" "\n"
  r"$\displaystyle\int\left(\frac2x-\frac{x}{x^2+4}\right)dx=2\ln|x|-\frac12\ln(x^2+4)+C$",
  truth=(x**2+8)/(x**3+4*x), tag='التكامل بالكسور الجزئية: عامل تربيعي'),
Q('n1q12', U5[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\sin 3x', x*sin(3*x))),
  [A(r'-\frac{x}{3}\cos 3x+\frac{1}{9}\sin 3x+C', -x/3*cos(3*x)+sin(3*x)/9), A(r'-\frac{x}{3}\cos 3x-\frac{1}{9}\sin 3x+C', -x/3*cos(3*x)-sin(3*x)/9),
   A(r'\frac{x}{3}\cos 3x+\frac{1}{9}\sin 3x+C', x/3*cos(3*x)+sin(3*x)/9), A(r'-3x\cos 3x+9\sin 3x+C', -3*x*cos(3*x)+9*sin(3*x))],
  r"بالأجزاء: $u=x$ ، $dv=\sin3x\,dx \Rightarrow v=-\frac13\cos3x$" "\n" r"$\displaystyle-\frac x3\cos3x+\int\frac13\cos3x\,dx=-\frac x3\cos3x+\frac19\sin3x+C$",
  truth=x*sin(3*x), tag='التكامل بالأجزاء'),
Q('n1q13', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos\sqrt{x}', cos(sqrt(x)))),
  [A(r'2\sqrt{x}\sin\sqrt{x}+2\cos\sqrt{x}+C', 2*sqrt(x)*sin(sqrt(x))+2*cos(sqrt(x))), A(r'2\sqrt{x}\sin\sqrt{x}-2\cos\sqrt{x}+C', 2*sqrt(x)*sin(sqrt(x))-2*cos(sqrt(x))),
   A(r'-2\sqrt{x}\sin\sqrt{x}+2\cos\sqrt{x}+C', -2*sqrt(x)*sin(sqrt(x))+2*cos(sqrt(x))), A(r'\sqrt{x}\sin\sqrt{x}+\cos\sqrt{x}+C', sqrt(x)*sin(sqrt(x))+cos(sqrt(x)))],
  r"بالتعويض $u=\sqrt x \Rightarrow x=u^2$ ، $dx=2u\,du$: $\displaystyle\int2u\cos u\,du$" "\n" r"ثم بالأجزاء: $2(u\sin u+\cos u)+C=2\sqrt x\sin\sqrt x+2\cos\sqrt x+C$",
  truth=cos(sqrt(x)), tag='التكامل بالتعويض ثم بالأجزاء'),
Q('n1q14', U5[5], 'medium',
  F(r"إذا كانت مساحة المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ ، والمحور $x$ ، والمستقيمين: $x=0,\ x=\ln a$ تساوي $4$ وحدات مربعة، حيث $a>1$ ، فإنّ قيمة الثابت $a$ هي:", (r'e^{\frac{x}{2}}', exp(x/2))),
  [O('9', 9), O('3', 3), O(r'e^{3}', E**3), O('81', 81)],
  r"$\displaystyle\int_0^{\ln a}e^{\frac x2}dx=\left[2e^{\frac x2}\right]_0^{\ln a}=2\sqrt a-2=4 \Rightarrow \sqrt a=3 \Rightarrow a=9$",
  truth=lambda: [r_ for r_ in solve(ig(exp(x/2), (x, 0, log(a)))-4, a) if r_ > 1][0], tag='المساحة: إيجاد ثابت'),
Q('n1q15', U5[5], 'hard',
  F(r"اعتمادًا على التمثيل البياني الآتي الذي يُبيّن منحنى الاقتران: $f(x)=«0»$ ، والمستقيم $x=1$ ، فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور $x$ بالوحدات المكعبة هو:", (r'\sqrt{xe^{x}}', sqrt(x*exp(x)))),
  [O(r'\pi', P), O(r'\pi e', P*E), O(r'\pi(e-1)', P*(E-1)), O(r'2\pi', 2*P)],
  r"$\displaystyle V=\pi\int_0^1\left(\sqrt{xe^x}\right)^2dx=\pi\int_0^1xe^x\,dx$ ، وبالأجزاء: $\displaystyle\int xe^xdx=(x-1)e^x$" "\n" r"$V=\pi\big[(x-1)e^x\big]_0^1=\pi(0-(-1))=\pi$",
  truth=pi*ig(x*exp(x), (x, 0, 1)), figure=figure('n1q15', region(sqrt(x*exp(x)), 0*x, 0, 1, (-0.4, 1.6), (-0.3, 2.2), [(1.05, 1.9, r'$f(x)$', '#1f5fbf')]), 3.4, 2.8), tag='الحجوم الدورانية من الشكل'),
IndexQ('n1q16', U5[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ هو:", (r'e^{x}\cos^{2}y', exp(x)*cos(y)**2)),
  [O(r'\tan y=e^{x}+C', tan(y)-exp(x)-Cc, 'rel'), O(r'\sec y=e^{x}+C', sec(y)-exp(x)-Cc, 'rel'), O(r'\tan y=-e^{x}+C', tan(y)+exp(x)-Cc, 'rel'), O(r'-\cot y=e^{x}+C', -cot(y)-exp(x)-Cc, 'rel')],
  r"بفصل المتغيرات: $\dfrac{dy}{\cos^2y}=e^xdx \Rightarrow \displaystyle\int\sec^2y\,dy=\int e^xdx \Rightarrow \tan y=e^x+C$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, exp(x)*cos(y)**2)), tag='المعادلات التفاضلية: الحل العام'),
# ---------------- unit 6
IndexQ('n1q17', U6[2], 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=-\hat{i}+4\hat{j}+2\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $3\hat{i}-2\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((3, 0, -2), (-1, 4, 2)), line_opt((-1, 4, 2), (3, 0, -2)), line_opt((3, -2, 0), (-1, 4, 2)), line_opt((0, 3, -2), (-1, 4, 2))],
  r"متجه موقع النقطة $A$ هو $\langle 3,0,-2\rangle$ (لا يوجد $\hat j$ ، فمركبته الثانية صفر) ، ومتجه الاتجاه $\langle -1,4,2\rangle$" "\n" r"$\vec{\mathbf{r}}=\langle 3,0,-2\rangle+t\langle -1,4,2\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((3, 0, -2), ln) and par(ln[1], (-1, 4, 2))), tag='معادلة المستقيم في الفضاء'),
Q('n1q18', U6[1], 'medium',
  r"متجه الموقع للنقطة $D$ هو:",
  [vec_opt(8, 3, -5), vec_opt(-8, -3, 5), vec_opt(3, 2, -4), vec_opt(R(7, 2), 0, 1)],
  r"$\overrightarrow{AB}=\overrightarrow{BD} \Rightarrow D=2B-A=\langle 10-2,\ 2+1,\ -2-3\rangle=\langle 8,\,3,\,-5\rangle$",
  truth=T3(2*V(5, 1, -1)-V(2, -1, 3)), tag='المتجهات: نقطة ومتجه موقع (نص مشترك)',
  lead=shared(r"إذا كانت: $A(2,-1,3),\ B(5,1,-1),\ C(a,0,1)$ ، وكانت $D$ نقطة في الفضاء، حيث: $\overrightarrow{AB}=\overrightarrow{BD}$", 18, 19)),
Q('n1q19', U6[1], 'medium',
  r"إذا كان: $|\overrightarrow{AC}|=3$ ، حيث $a>2$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('4', 4), O('0', 0), O('2', 2), O('6', 6)],
  r"$\overrightarrow{AC}=\langle a-2,\ 1,\ -2\rangle$ ، و $(a-2)^2+1+4=9 \Rightarrow (a-2)^2=4 \Rightarrow a=4$ أو $a=0$ ، وبما أن $a>2$ فإن $a=4$",
  truth=lambda: [r_ for r_ in solve((x-2)**2+1+4-9, x) if r_ > 2][0], tag='المتجهات: المقدار وإيجاد ثابت (نص مشترك)'),
Q('n1q20', U6[1], 'medium',
  r"في متوازي المستطيلات الآتي، أحد رؤوسه نقطة الأصل $O$ ، وأحرفه $\overline{OP}$ و $\overline{OR}$ و $\overline{OS}$ على المحاور $x$ و $y$ و $z$ على الترتيب. إذا كانت إحداثيات الرأس $U$ هي $(2,\,5,\,4)$ ، فإنّ متجه الموقع لنقطة منتصف القطعة $\overline{RT}$ هو:",
  [vec_opt(1, R(5, 2), 2), vec_opt(2, 5, 4), vec_opt(1, R(5, 2), 0), vec_opt(-1, R(5, 2), 2)],
  r"من الشكل: $R(0,5,0)$ ، $T(2,0,4)$" "\n" r"منتصف $\overline{RT}$: $\left(\dfrac{0+2}{2},\ \dfrac{5+0}{2},\ \dfrac{0+4}{2}\right)=\left(1,\ \frac52,\ 2\right)$",
  truth=T3((V(0, 5, 0)+V(2, 0, 4))/2), figure=figure('n1q20', fig_box(2, 5, 4), 4.2, 2.9), tag='المتجهات من شكل ثلاثي الأبعاد'),
Q('n1q21', U6[1], 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle 2,\,3,\,b+1\rangle$ ، $\overrightarrow{AC}=\langle -4,\,-6,\,10\rangle$ ، فإنّ قيمة $b$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('-6', -6), O('4', 4), O('-4', -4), O('6', 6)],
  r"يجب أن يكون $\overrightarrow{AB}=k\,\overrightarrow{AC}$: من المركبة الأولى $k=-\frac12$ (وتحقق الثانية: $3=-\frac12(-6)$ ✔)" "\n" r"$b+1=-\frac12(10)=-5 \Rightarrow b=-6$",
  truth=lambda: solve(V(2, 3, b+1).cross(V(-4, -6, 10))[0], b)[0], tag='النقاط على استقامة واحدة'),
Q('n1q22', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 1,\,2,\,-1\rangle$ ، $\vec{\mathbf{w}}=\langle 0,\,1,\,2\rangle$ ، فإنّ متجه الوحدة في اتجاه المتجه $2\vec{\mathbf{v}}-\vec{\mathbf{w}}$ هو:",
  [vec_opt(2/sqrt(29), 3/sqrt(29), -4/sqrt(29)), vec_opt(R(2, 29), R(3, 29), -R(4, 29)), vec_opt(-2/sqrt(29), -3/sqrt(29), 4/sqrt(29)), vec_opt(2/sqrt(21), 3/sqrt(21), -4/sqrt(21))],
  r"$2\vec{\mathbf{v}}-\vec{\mathbf{w}}=\langle 2,4,-2\rangle-\langle 0,1,2\rangle=\langle 2,3,-4\rangle$ ، ومقداره $\sqrt{4+9+16}=\sqrt{29}$" "\n" r"متجه الوحدة: $\left\langle \frac{2}{\sqrt{29}},\frac{3}{\sqrt{29}},\frac{-4}{\sqrt{29}}\right\rangle$",
  truth=T3((2*V(1, 2, -1)-V(0, 1, 2))/sqrt(29)), tag='متجه الوحدة'),
Q('n1q23', U6[2], 'hard',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 1,2,-1\rangle+t\langle 2,-1,1\rangle$ معادلة متجهة للمستقيم $l_1$ ، وكانت: $\vec{\mathbf{r}}=\langle 5,-5,8\rangle+u\langle 1,2,-3\rangle$ معادلة متجهة للمستقيم $l_2$ ، فإنّ إحداثيات نقطة تقاطع المستقيمين هي:",
  [pt_opt(7, -1, 2), pt_opt(5, -5, 8), pt_opt(3, 1, 0), pt_opt(6, -3, 5)],
  r"$1+2t=5+u$ ، $2-t=-5+2u$ ، $-1+t=8-3u$" "\n" r"من الأولى: $u=2t-4$ ، وبالتعويض في الثالثة: $-1+t=8-6t+12 \Rightarrow t=3,\ u=2$ ، وتحقق في الثانية: $-1=-1$ ✔" "\n" r"نقطة التقاطع: $\langle 1,2,-1\rangle+3\langle 2,-1,1\rangle=(7,-1,2)$",
  truth=lambda: inter((1, 2, -1), (2, -1, 1), (5, -5, 8), (1, 2, -3)), tag='نقطة تقاطع مستقيمين'),
Q('n1q24', U6[3], 'medium',
  r"إذا كان المتجه: $\vec{\mathbf{v}}=3\hat{i}+c\hat{j}-2\hat{k}$ يُعامد المتجه: $\vec{\mathbf{w}}=d\hat{i}+2\hat{j}+4\hat{k}$ ، حيث $c,\ d$ ثابتان، فإنّ $3d+2c$ تساوي:",
  [O('8', 8), O('-8', -8), O('4', 4), O('12', 12)],
  r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=3d+2c-8=0 \Rightarrow 3d+2c=8$",
  truth=lambda: (lambda dd: simplify(3*dd+2*solve(V(3, c, -2).dot(V(dd, 2, 4)), c)[0]))(Symbol('dd')), tag='التعامد وإيجاد ثوابت'),
Q('n1q25', U6[3], 'hard',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{BA}=\langle 2,\,1,\,-2\rangle$ ، $\overrightarrow{BC}=\langle 2,\,2,\,3\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O(r'\frac{3\sqrt{17}}{2}', 3*sqrt(17)/2), O(r'3\sqrt{17}', 3*sqrt(17)), O(r'\frac{9}{2}', R(9, 2)), O(r'\frac{17}{2}', R(17, 2))],
  r"$\overrightarrow{BA}\cdot\overrightarrow{BC}=4+2-6=0$ ، إذن الزاوية $B$ قائمة" "\n" r"$|\overrightarrow{BA}|=3$ ، $|\overrightarrow{BC}|=\sqrt{17}$ ، والمساحة $=\frac12(3)(\sqrt{17})=\dfrac{3\sqrt{17}}{2}$",
  truth=R(1, 2)*V(2, 1, -2).norm()*V(2, 2, 3).norm()*sin(ang((2, 1, -2), (2, 2, 3))), tag='مساحة مثلث باستعمال الضرب القياسي'),
# ---------------- unit 7
Q('n1q26', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $\dfrac{P(X=1)}{P(X=3)}=\dfrac{9}{4}$ ، فإنّ التوقّع للمتغيّر العشوائي $X$ هو:",
  [O('3', 3), O(r'\frac{1}{3}', R(1, 3)), O(r'\frac{3}{2}', R(3, 2)), O(r'\frac{2}{3}', R(2, 3))],
  r"$\dfrac{P(X=1)}{P(X=3)}=\dfrac{p}{(1-p)^2p}=\dfrac{1}{(1-p)^2}=\dfrac94 \Rightarrow 1-p=\frac23 \Rightarrow p=\frac13$ ، و $E(X)=\frac1p=3$",
  truth=lambda: 1/[r_ for r_ in solve(1/(1-p)**2-R(9, 4), p) if 0 < r_ < 1][0], tag='التوزيع الهندسي: نسبة احتمالين والتوقع'),
Q('n1q27', U7[1], 'hard',
  r"يختار قسم ضبط الجودة في أحد المصانع عيّنة عشوائية مكوّنة من $6$ قطع من كل شحنة لفحصها، وتُرفَض الشحنة إذا وُجدت في العيّنة قطعتان معيبتان فأكثر. إذا كانت نسبة القطع المعيبة في إنتاج المصنع $5\%$ ، فإنّ احتمال رفض الشحنة هو تقريبًا:",
  [D('0.0328'), D('0.9672'), D('0.2321'), D('0.7351')],
  r"$X\sim B(6,\,0.05)$: $P(X\ge2)=1-P(X=0)-P(X=1)=1-(0.95)^6-6(0.05)(0.95)^5$" "\n" r"$\approx1-0.7351-0.2321=0.0328$",
  truth=r4(1-binom(6, R(5, 100), 0)-binom(6, R(5, 100), 1)), tag='توزيع ذي الحدين: احتمال «على الأقل»'),
Q('n1q28', U7[2], 'medium',
  r"إذا كان: $X\sim N(64,\,100)$ ، فإنّ $P(X<59)$ يساوي:",
  [D('0.3085'), D('0.6915'), D('0.1915'), D('0.3830')],
  r"$\sigma=10$ ، $z=\dfrac{59-64}{10}=-0.5$ ، $P(Z<-0.5)=1-P(Z<0.5)=1-0.6915=0.3085$",
  truth=Ph(-R(1, 2)), tag='التوزيع الطبيعي: حساب احتمال', lead=ztable_lead([28, 29, 30], 0.4, 0.5, 0.75, 1.5, 1.88), group=3),
Q('n1q29', U7[2], 'hard',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{10}<Z<\dfrac{k}{10}\right)=0.5468$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:",
  [D('7.5'), D('0.75'), D('75'), D('5.468')],
  r"$2P\left(Z<\frac{k}{10}\right)-1=0.5468 \Rightarrow P\left(Z<\frac{k}{10}\right)=0.7734$" "\n" r"من الجدول: $\frac{k}{10}=0.75 \Rightarrow k=7.5$",
  truth=lambda: [zz*10 for zz in (R(4, 10), R(5, 10), R(75, 100), R(15, 10), R(188, 100)) if 2*Ph(zz)-1 == R('0.5468')][0], tag='التوزيع الطبيعي: فترة متماثلة وإيجاد ثابت'),
Q('n1q30', U7[2], 'hard',
  r"تتوزّع علامات طلبة في امتحان توزيعًا طبيعيًّا: $X\sim N(50,\,\sigma^{2})$. إذا كانت علامات $6.68\%$ من الطلبة تزيد على $62$ ، فإنّ قيمة الانحراف المعياري للعلامات هي:",
  [O('8', 8), O('12', 12), D('1.5'), D('18')],
  r"$P(X>62)=0.0668 \Rightarrow P(X<62)=0.9332=P(Z<1.5)$" "\n" r"$\dfrac{62-50}{\sigma}=1.5 \Rightarrow \sigma=8$",
  truth=12/R(15, 10), tag='التوزيع الطبيعي: إيجاد الانحراف المعياري'),
]
# ================================================================== PAPER 2
vt2 = [(0, 0), (1, 3), (4, 3), (6, -3), (8, -3), (9, 0)]
P2 = [
Q('n2q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'e^{x}-\sec x\tan x+\frac{1}{x^{2}}', exp(x)-sec(x)*tan(x)+1/x**2)),
  [A(r'e^{x}-\sec x-\frac{1}{x}+C', exp(x)-sec(x)-1/x), A(r'e^{x}+\sec x-\frac{1}{x}+C', exp(x)+sec(x)-1/x), A(r'e^{x}-\sec x+\frac{1}{x}+C', exp(x)-sec(x)+1/x), A(r'e^{x}-\tan x-\frac{1}{x}+C', exp(x)-tan(x)-1/x)],
  r"$\displaystyle\int\sec x\tan x\,dx=\sec x$ ، و $\displaystyle\int x^{-2}dx=-x^{-1}$ ، إذن الناتج $e^x-\sec x-\dfrac1x+C$",
  truth=exp(x)-sec(x)*tan(x)+1/x**2, tag='تكامل الاقترانات المثلثية'),
Q('n2q2', U5[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{a}«0»\,dx=\sqrt{3}$ ، حيث $0<a<\dfrac{\pi}{2}$ ، فإنّ قيمة الثابت $a$ هي:", (r'\sec^{2}x', sec(x)**2)),
  [O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{\pi}{4}', P/4), O(r'\frac{5\pi}{12}', 5*P/12)],
  r"$\displaystyle\int_0^a\sec^2x\,dx=\big[\tan x\big]_0^a=\tan a=\sqrt3$ ، وبما أن $0<a<\frac{\pi}{2}$ فإن $a=\dfrac{\pi}{3}$",
  truth=lambda: [r_ for r_ in solve(tan(a)-sqrt(3), a) if 0 < r_ < P/2][0], tag='التكامل المحدود: إيجاد ثابت'),
Q('n2q3', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(\sin^{2}x-\cos^{2}x)', sin(x)**2-cos(x)**2)),
  [A(r'-\frac{1}{2}\sin 2x+C', -sin(2*x)/2), A(r'\frac{1}{2}\sin 2x+C', sin(2*x)/2), A(r'-2\sin 2x+C', -2*sin(2*x)), A(r'\frac{\sin^{3}x-\cos^{3}x}{3}+C', (sin(x)**3-cos(x)**3)/3)],
  r"$\sin^2x-\cos^2x=-\cos2x$ ، إذن $\displaystyle\int-\cos2x\,dx=-\frac12\sin2x+C$",
  truth=sin(x)**2-cos(x)**2, tag='تكامل باستعمال متطابقات ضعف الزاوية'),
Q('n2q4', U5[1], 'hard',
  r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=\begin{cases}2t+1, & 0\le t\le3\\ 10-t, & t>3\end{cases}$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. إذا انطلق الجسم من نقطة الأصل، فإنّ موقعه بعد $6$ ثوانٍ من بدء الحركة هو:",
  [D('28.5', 'm'), D('12', 'm'), D('16.5', 'm'), D('30', 'm')],
  r"$s(6)=\displaystyle\int_0^3(2t+1)dt+\int_3^6(10-t)dt=\big[t^2+t\big]_0^3+\left[10t-\frac{t^2}{2}\right]_3^6$" "\n" r"$=12+(42-25.5)=12+16.5=28.5\ \text{m}$",
  truth=ig(2*t+1, (t, 0, 3))+ig(10-t, (t, 3, 6)), tag='الحركة: الموقع من سرعة متعددة القاعدة'),
IndexQ('n2q5', U5[1], 'easy',
  r"منحنى يمرّ بالنقطة $(1,\,3)$ ، وميل المماس له عند أيّ نقطة $(x,y)$ يُعطى بالعلاقة: $\dfrac{dy}{dx}=6x^{2}-4x+1$. معادلة المنحنى هي:",
  [O('y=2x^{3}-2x^{2}+x+2', 2*x**3-2*x**2+x+2, 'eq'), O('y=2x^{3}-2x^{2}+x+3', 2*x**3-2*x**2+x+3, 'eq'), O('y=6x^{3}-4x^{2}+x', 6*x**3-4*x**2+x, 'eq'), O('y=12x-4', 12*x-4, 'eq')],
  r"$y=\displaystyle\int(6x^2-4x+1)dx=2x^3-2x^2+x+C$ ، وبالتعويض بالنقطة $(1,3)$: $3=2-2+1+C \Rightarrow C=2$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, 6*x**2-4*x+1, 1, 3)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
Q('n2q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\,2^{x^{2}}', x*2**(x**2))),
  [A(r'\frac{2^{x^{2}}}{2\ln 2}+C', 2**(x**2)/(2*log(2))), A(r'\frac{2^{x^{2}}}{\ln 2}+C', 2**(x**2)/log(2)), A(r'2^{x^{2}}\ln 2+C', 2**(x**2)*log(2)), A(r'\frac{x^{2}}{2}2^{x^{2}}+C', x**2/2*2**(x**2))],
  r"بالتعويض $u=x^2 \Rightarrow du=2x\,dx$: $\displaystyle\frac12\int2^udu=\frac{2^u}{2\ln2}+C=\frac{2^{x^2}}{2\ln2}+C$",
  truth=x*2**(x**2), tag='التكامل بالتعويض'),
Q('n2q7', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos^{4}x\sin x', cos(x)**4*sin(x))),
  [A(r'-\frac{\cos^{5}x}{5}+C', -cos(x)**5/5), A(r'\frac{\cos^{5}x}{5}+C', cos(x)**5/5), A(r'-\frac{\sin^{5}x}{5}+C', -sin(x)**5/5), A(r'-4\cos^{3}x\sin^{2}x+C', -4*cos(x)**3*sin(x)**2)],
  r"بالتعويض $u=\cos x \Rightarrow du=-\sin x\,dx$: $\displaystyle-\int u^4du=-\frac{u^5}{5}+C=-\frac{\cos^5x}{5}+C$",
  truth=cos(x)**4*sin(x), tag='التكامل بالتعويض: اقترانات مثلثية'),
Q('n2q8', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ ، حيث $x>1$ ، هو:", (r'\frac{1}{x\ln x}', 1/(x*log(x)))),
  [A(r'\ln(\ln x)+C', log(log(x))), A(r'\frac{(\ln x)^{2}}{2}+C', log(x)**2/2), A(r'\frac{1}{\ln x}+C', 1/log(x)), A(r'(\ln x)^{2}+C', log(x)**2)],
  r"بالتعويض $u=\ln x \Rightarrow du=\frac1xdx$: $\displaystyle\int\frac{du}{u}=\ln|u|+C=\ln(\ln x)+C$ (لأن $\ln x>0$)",
  truth=1/(x*log(x)), tag='التكامل بالتعويض: لوغاريتمات'),
Q('n2q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'\frac{x^{2}}{(x^{3}+1)^{2}}', x**2/(x**3+1)**2)),
  [O(r'\frac{1}{6}', R(1, 6)), O(r'\frac{1}{3}', R(1, 3)), O(r'-\frac{1}{6}', -R(1, 6)), O(r'\frac{1}{2}', R(1, 2))],
  r"بالتعويض $u=x^3+1 \Rightarrow du=3x^2dx$ ، والحدود $1\to2$:" "\n" r"$\displaystyle\frac13\int_1^2u^{-2}du=\frac13\left[-\frac1u\right]_1^2=\frac13\left(-\frac12+1\right)=\frac16$",
  truth=ig(x**2/(x**3+1)**2, (x, 0, 1)), tag='التكامل المحدود بالتعويض'),
Q('n2q10', U5[3], 'medium',
  F(r"قيمة: $\displaystyle\int_{3}^{4}«0»\,dx$ هي:", (r'\frac{5}{(x-2)(x+3)}', 5/((x-2)*(x+3)))),
  [O(r'\ln\frac{12}{7}', log(R(12, 7))), O(r'\ln\frac{7}{12}', log(R(7, 12))), O(r'\ln 12', log(12)), O(r'\ln\frac{2}{7}', log(R(2, 7)))],
  r"$\dfrac{5}{(x-2)(x+3)}=\dfrac{1}{x-2}-\dfrac{1}{x+3}$" "\n" r"$\big[\ln|x-2|-\ln|x+3|\big]_3^4=(\ln2-\ln7)-(0-\ln6)=\ln\dfrac{2\cdot6}{7}=\ln\dfrac{12}{7}$",
  truth=ig(5/((x-2)*(x+3)), (x, 3, 4)), tag='التكامل المحدود بالكسور الجزئية'),
Q('n2q11', U5[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{3}+2x^{2}+3}{x^{2}+2x}', (x**3+2*x**2+3)/(x**2+2*x))),
  [A(r'\frac{x^{2}}{2}+\frac{3}{2}\ln|x|-\frac{3}{2}\ln|x+2|+C', x**2/2+R(3, 2)*log(x)-R(3, 2)*log(x+2)), A(r'\frac{x^{2}}{2}-\frac{3}{2}\ln|x|+\frac{3}{2}\ln|x+2|+C', x**2/2-R(3, 2)*log(x)+R(3, 2)*log(x+2)),
   A(r'\frac{x^{2}}{2}+3\ln|x|-3\ln|x+2|+C', x**2/2+3*log(x)-3*log(x+2)), A(r'\frac{3}{2}\ln|x|-\frac{3}{2}\ln|x+2|+C', R(3, 2)*log(x)-R(3, 2)*log(x+2))],
  r"الكسر غير فعلي: $x^3+2x^2+3=x(x^2+2x)+3$ ، إذن المقدار $=x+\dfrac{3}{x(x+2)}=x+\dfrac{3/2}{x}-\dfrac{3/2}{x+2}$" "\n" r"بالتكامل: $\dfrac{x^2}{2}+\frac32\ln|x|-\frac32\ln|x+2|+C$",
  truth=(x**3+2*x**2+3)/(x**2+2*x), tag='التكامل بالكسور الجزئية: كسر غير فعلي'),
Q('n2q12', U5[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(2x+1)e^{x}', (2*x+1)*exp(x))),
  [A(r'(2x-1)e^{x}+C', (2*x-1)*exp(x)), A(r'(2x+1)e^{x}+C', (2*x+1)*exp(x)), A(r'(2x+3)e^{x}+C', (2*x+3)*exp(x)), A(r'(x^{2}+x)e^{x}+C', (x**2+x)*exp(x))],
  r"بالأجزاء: $u=2x+1 \Rightarrow du=2\,dx$ ، $dv=e^xdx \Rightarrow v=e^x$" "\n" r"$(2x+1)e^x-\displaystyle\int2e^xdx=(2x+1)e^x-2e^x+C=(2x-1)e^x+C$",
  truth=(2*x+1)*exp(x), tag='التكامل بالأجزاء'),
Q('n2q13', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{3}\sin(x^{2})', x**3*sin(x**2))),
  [A(r'-\frac{1}{2}x^{2}\cos(x^{2})+\frac{1}{2}\sin(x^{2})+C', -x**2*cos(x**2)/2+sin(x**2)/2), A(r'\frac{1}{2}x^{2}\cos(x^{2})+\frac{1}{2}\sin(x^{2})+C', x**2*cos(x**2)/2+sin(x**2)/2),
   A(r'-x^{2}\cos(x^{2})+\sin(x^{2})+C', -x**2*cos(x**2)+sin(x**2)), A(r'-\frac{1}{2}x^{2}\cos(x^{2})-\frac{1}{2}\sin(x^{2})+C', -x**2*cos(x**2)/2-sin(x**2)/2)],
  r"بالتعويض $u=x^2 \Rightarrow du=2x\,dx$: $\displaystyle\int x^2\sin(x^2)\,x\,dx=\frac12\int u\sin u\,du$" "\n"
  r"وبالأجزاء: $\displaystyle\frac12\left(-u\cos u+\int\cos u\,du\right)=\frac12(-u\cos u+\sin u)+C=-\frac12x^2\cos(x^2)+\frac12\sin(x^2)+C$",
  truth=x**3*sin(x**2), tag='التكامل بالتعويض ثم بالأجزاء'),
Q('n2q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة–الزمن لجسم يتحرّك على المحور $x$ في الفترة الزمنية $[0,\,9]$. إذا بدأ الجسم الحركة من $x=2$ عندما $t=0$ ، فإنّ موقعه النهائي هو:",
  [O('x=5', 5, 'eq'), O('x=3', 3, 'eq'), O('x=23', 23, 'eq'), O('x=21', 21, 'eq')],
  r"الإزاحة = المساحات فوق المحور ناقص المساحات تحته:" "\n"
  r"$[0,1]$: $1.5$ ، $[1,4]$: $9$ ، $[4,5]$: $1.5$ ، $[5,6]$: $-1.5$ ، $[6,8]$: $-6$ ، $[8,9]$: $-1.5$ ، والمجموع $3$" "\n" r"الموقع النهائي $=2+3=5$",
  truth=lambda: 2 + pw_integral(vt2, 0, 9), figure=figure('n2q14', vt_graph(vt2, 9, -3, 3), 4.2, 3.0), tag='الحركة من منحنى السرعة–الزمن'),
Q('n2q15', U5[5], 'medium',
  F(r"مساحة المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ (بالوحدات المربعة) هي:", (r'x^{2}', x**2), (r'6-x', 6-x)),
  [O(r'\frac{125}{6}', R(125, 6)), O(r'\frac{125}{3}', R(125, 3)), O(r'\frac{61}{6}', R(61, 6)), O(r'\frac{64}{3}', R(64, 3))],
  r"نقاط التقاطع: $x^2=6-x \Rightarrow x^2+x-6=0 \Rightarrow x=-3,\ x=2$ ، وفي الفترة $6-x\ge x^2$" "\n"
  r"$\displaystyle\int_{-3}^{2}(6-x-x^2)dx=\left[6x-\frac{x^2}{2}-\frac{x^3}{3}\right]_{-3}^{2}=\frac{22}{3}+\frac{27}{2}=\frac{125}{6}$",
  truth=ig(6-x-x**2, (x, -3, 2)), tag='المساحة بين منحنيين'),
IndexQ('n2q16', U5[6], 'medium',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ ، حيث $y>0$ ، الذي يُحقّق الشرط الأوّلي $y(0)=2$ هو:", (r'y\cos x', y*cos(x))),
  [O(r'y=2e^{\sin x}', 2*exp(sin(x)), 'eq'), O(r'y=e^{\sin x}+1', exp(sin(x))+1, 'eq'), O(r'y=2e^{-\sin x}', 2*exp(-sin(x)), 'eq'), O(r'y=2+\sin x', 2+sin(x), 'eq')],
  r"بفصل المتغيرات: $\dfrac{dy}{y}=\cos x\,dx \Rightarrow \ln y=\sin x+C$ ، و $y(0)=2 \Rightarrow C=\ln2$" "\n" r"$\ln y=\sin x+\ln2 \Rightarrow y=2e^{\sin x}$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, y*cos(x), 0, 2)), tag='المعادلات التفاضلية: الحل الخاص'),
Q('n2q17', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 2,\,-6,\,3\rangle$ ، فإنّ متجه الوحدة في عكس اتجاه المتجه $\vec{\mathbf{v}}$ هو:",
  [vec_opt(-R(2, 7), R(6, 7), -R(3, 7)), vec_opt(R(2, 7), -R(6, 7), R(3, 7)), vec_opt(-2, 6, -3), vec_opt(-R(2, 49), R(6, 49), -R(3, 49))],
  r"$|\vec{\mathbf{v}}|=\sqrt{4+36+9}=7$ ، ومتجه الوحدة في عكس الاتجاه $-\dfrac{\vec{\mathbf{v}}}{7}=\left\langle -\frac27,\frac67,-\frac37\right\rangle$",
  truth=T3(-V(2, -6, 3)/7), tag='متجه الوحدة'),
Q('n2q18', U6[1], 'hard',
  r"في الشكل الآتي $OAB$ مثلث فيه: $\overrightarrow{OA}=4\vec{\mathbf{a}}$ ، $\overrightarrow{OB}=2\vec{\mathbf{b}}$ ، والنقطة $M$ تقع على الضلع $\overline{AB}$ بحيث $AM:MB=3:1$. المتجه $\overrightarrow{OM}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [vopt(va+R(3, 2)*vb), vopt(3*va+R(1, 2)*vb), vopt(R(3, 2)*va+vb), vopt(va+3*vb)],
  r"$\overrightarrow{AB}=2\vec{\mathbf{b}}-4\vec{\mathbf{a}}$ ، و $\overrightarrow{AM}=\frac34\overrightarrow{AB}$" "\n" r"$\overrightarrow{OM}=4\vec{\mathbf{a}}+\frac34(2\vec{\mathbf{b}}-4\vec{\mathbf{a}})=\vec{\mathbf{a}}+\frac32\vec{\mathbf{b}}$",
  truth=4*va+R(3, 4)*(2*vb-4*va),
  figure=figure('n2q18', fig_poly({'O': (0, 0), 'A': (2, 3.4), 'B': (6, 0), 'M': (2 + 0.75*4, 3.4 - 0.75*3.4)}, [('A', 'B')], [('O', 'A', r'$4\vec{\mathbf{a}}$', (-0.9, 0.1)), ('O', 'B', r'$2\vec{\mathbf{b}}$', (0, -0.5)), ],
                                    {'O': (-0.35, -0.3), 'A': (-0.1, 0.2), 'B': (0.1, -0.3), 'M': (0.15, 0.1)}, extra_dashed=[('O', 'M')]), 3.8, 2.6), tag='المتجهات في الأشكال الهندسية والنسبة'),
Q('n2q19', U6[1], 'medium',
  r"إذا كان: $\vec{\mathbf{s}}=\langle 1,\,-2,\,4\rangle$ ، $\vec{\mathbf{k}}=\langle 2,\,b,\,-1\rangle$ ، وكان المتجه $3\vec{\mathbf{s}}-\vec{\mathbf{k}}$ يوازي المتجه $\langle -1,\,2,\,-13\rangle$ ، فإنّ قيمة الثابت $b$ هي:",
  [O('-4', -4), O('4', 4), O('-8', -8), O('8', 8)],
  r"$3\vec{\mathbf{s}}-\vec{\mathbf{k}}=\langle 1,\ -6-b,\ 13\rangle$ ، ومن المركبتين الأولى والثالثة: $3\vec{\mathbf{s}}-\vec{\mathbf{k}}=-1\times\langle -1,2,-13\rangle$" "\n" r"إذن المركبة الثانية: $-6-b=-1(2)=-2 \Rightarrow b=-4$",
  truth=lambda: solve((3*V(1, -2, 4)-V(2, b, -1)).cross(V(-1, 2, -13))[0], b)[0], tag='توازي المتجهات وإيجاد ثابت'),
Q('n2q20', U6[1], 'medium',
  r"$ABCD$ متوازي أضلاع، فيه: $A(1,\,-2,\,3)$ ، $B(4,\,0,\,1)$ ، $C(6,\,3,\,2)$. إحداثيات الرأس $D$ هي:",
  [pt_opt(3, 1, 4), pt_opt(9, 5, 0), pt_opt(-1, -5, 2), pt_opt(3, 1, -4)],
  r"$\overrightarrow{AD}=\overrightarrow{BC}=\langle 2,3,1\rangle$ ، إذن $D=A+\langle 2,3,1\rangle=(3,\,1,\,4)$",
  truth=T3(V(1, -2, 3)+V(6, 3, 2)-V(4, 0, 1)), tag='متوازي الأضلاع في الفضاء'),
Q('n2q21', U6[2], 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 2,\,5,\,-8\rangle+t\langle 1,\,-1,\,4\rangle$ معادلة متجهة للمستقيم $l$ ، فإنّ إحداثيات نقطة تقاطع المستقيم $l$ مع المستوى $xy$ هي:",
  [pt_opt(4, 3, 0), pt_opt(0, 7, -16), pt_opt(3, 4, -4), pt_opt(4, 3, 8)],
  r"على المستوى $xy$ يكون $z=0$: $-8+4t=0 \Rightarrow t=2$ ، فالنقطة $(2+2,\ 5-2,\ 0)=(4,3,0)$",
  truth=lambda: T3(V(2, 5, -8)+solve(-8+4*t, t)[0]*V(1, -1, 4)), tag='تقاطع مستقيم مع مستوى إحداثي'),
Q('n2q22', U6[2], 'hard',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 1,1,2\rangle+t\langle 1,0,-1\rangle$ و $\vec{\mathbf{r}}_2=\langle 2,3,0\rangle+s\langle 0,1,1\rangle$ هي أنّهما:",
  rel_opts('skew'),
  r"متجها الاتجاه غير متوازيين. نساوي الإحداثيات: $1+t=2$ ، $1=3+s$ ، $2-t=s$" "\n" r"من الأولى $t=1$ ، ومن الثانية $s=-2$ ، وبالتعويض في الثالثة: $1\ne-2$ ، إذن المستقيمان متخالفان",
  truth=classify((1, 1, 2), (1, 0, -1), (2, 3, 0), (0, 1, 1)), tag='العلاقة بين مستقيمين'),
Q('n2q23', U6[2], 'hard',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 0,\,1,\,-1\rangle+t\langle 1,\,1,\,2\rangle$ معادلة متجهة للمستقيم $l$ ، والنقطة $P(4,\,1,\,6)$ غير واقعة عليه، فإنّ إحداثيات مسقط العمود من النقطة $P$ على المستقيم $l$ هي:",
  [pt_opt(3, 4, 5), pt_opt(4, 5, 7), pt_opt(2, 3, 3), pt_opt(1, 2, 1)],
  r"نفرض المسقط $Q=(t,\ 1+t,\ -1+2t)$ ، و $\overrightarrow{PQ}=\langle t-4,\ t,\ 2t-7\rangle$ عمودي على $\langle 1,1,2\rangle$:" "\n" r"$(t-4)+t+2(2t-7)=0 \Rightarrow 6t=18 \Rightarrow t=3$ ، إذن $Q=(3,4,5)$",
  truth=lambda: (lambda tt: T3(V(0, 1, -1)+tt*V(1, 1, 2)))(solve((V(0, 1, -1)+t*V(1, 1, 2)-V(4, 1, 6)).dot(V(1, 1, 2)), t)[0]), tag='مسقط العمود من نقطة على مستقيم'),
Q('n2q24', U6[3], 'easy',
  r"قياس الزاوية بين المتجهين: $\langle 1,\,1,\,0\rangle$ و $\langle 1,\,0,\,1\rangle$ هو:",
  [O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{\pi}{4}', P/4), O(r'\frac{2\pi}{3}', 2*P/3)],
  r"$\cos\theta=\dfrac{1+0+0}{\sqrt2\cdot\sqrt2}=\dfrac12 \Rightarrow \theta=\frac{\pi}{3}$",
  truth=ang((1, 1, 0), (1, 0, 1)), tag='الزاوية بين متجهين'),
Q('n2q25', U6[3], 'medium',
  r"إذا كانت $M,\ N,\ P$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{MN}=\langle 2,\,-1,\,3\rangle$ ، $\overrightarrow{NP}=\langle 0,\,3,\,-1\rangle$ ، فإنّ $\overrightarrow{NM}\cdot\overrightarrow{MP}$ يساوي:",
  [O('-8', -8), O('8', 8), O('-6', -6), O('12', 12)],
  r"$\overrightarrow{MP}=\overrightarrow{MN}+\overrightarrow{NP}=\langle 2,2,2\rangle$ ، و $\overrightarrow{NM}=-\overrightarrow{MN}=\langle -2,1,-3\rangle$" "\n" r"$\overrightarrow{NM}\cdot\overrightarrow{MP}=-4+2-6=-8$",
  truth=(-V(2, -1, 3)).dot(V(2, -1, 3)+V(0, 3, -1)), tag='الضرب القياسي ومتجهات بين نقاط'),
Q('n2q26', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان التوقّع $E(X)=\frac{5}{2}$ ، فإنّ $P(X=3)$ يساوي:",
  [D('0.144'), D('0.096'), D('0.216'), D('0.4')],
  r"$E(X)=\frac1p=\frac52 \Rightarrow p=0.4$" "\n" r"$P(X=3)=(1-p)^2p=(0.6)^2(0.4)=0.144$",
  truth=geo(R(2, 5), 3), tag='التوزيع الهندسي: التوقع والاحتمال'),
Q('n2q27', U7[1], 'hard',
  r"إذا كان: $X\sim B(n,\,p)$ ، وكان: $E(X)=2$ ، $\text{Var}(X)=1.6$ ، فإنّ $P(X=1)$ يساوي تقريبًا:",
  [D('0.2684'), D('0.1074'), D('0.3020'), D('0.6242')],
  r"$\dfrac{\text{Var}(X)}{E(X)}=\dfrac{np(1-p)}{np}=1-p=0.8 \Rightarrow p=0.2$ ، و $n=\dfrac{2}{0.2}=10$" "\n" r"$P(X=1)=\binom{10}{1}(0.2)(0.8)^9\approx0.2684$",
  truth=lambda: (lambda pp: r4(binom(int(2/pp), pp, 1)))(1-R(16, 10)/2), tag='توزيع ذي الحدين: التوقع والتباين'),
Q('n2q28', U7[2], 'medium',
  r"يُمثّل الشكل الآتي منحنى التوزيع الطبيعي المعياري. إذا علمت أنّ: $P(Z<-1.8)=0.0359$ ، فإنّ مساحة المنطقة المُظلَّلة هي:",
  [D('0.9282'), D('0.4641'), D('0.9641'), D('0.0718')],
  r"المنطقة المظلّلة بين $z=-1.8$ و $z=1.8$ ، والطرفان المتبقّيان متماثلان:" "\n" r"$P(-1.8<Z<1.8)=1-2(0.0359)=0.9282$",
  truth=1-2*R('0.0359'), figure=figure('n2q28', bell([(-1.8, 1.8)], [-1.8, 0, 1.8]), 4.0, 2.3), tag='التوزيع الطبيعي: مساحة من الشكل'),
Q('n2q29', U7[2], 'medium',
  r"إذا كان: $X\sim N(72,\,64)$ ، فإنّ $P(68<X<84)$ يساوي:",
  [D('0.6247'), D('0.2417'), D('0.4332'), D('0.8664')],
  r"$\sigma=8$ ، $z_1=\dfrac{68-72}{8}=-0.5$ ، $z_2=\dfrac{84-72}{8}=1.5$" "\n" r"$P(-0.5<Z<1.5)=0.9332-(1-0.6915)=0.6247$",
  truth=Ph(R(3, 2))-Ph(-R(1, 2)), tag='التوزيع الطبيعي: حساب احتمال', lead=ztable_lead([29, 30], 0.5, 1, 1.5, 2), group=2),
Q('n2q30', U7[2], 'hard',
  r"يُعبّئ مصنع أكياس سكر تتوزّع كتلها توزيعًا طبيعيًّا وسطه الحسابي $1000\ \text{g}$. إذا تبيّن أنّ $1587$ كيسًا من أصل $10000$ كيس تزيد كتلتها على $1012\ \text{g}$ ، فإنّ الانحراف المعياري للكتل هو:",
  [D('12', 'g'), D('6', 'g'), D('24', 'g'), D('8', 'g')],
  r"$P(X>1012)=\dfrac{1587}{10000}=0.1587 \Rightarrow P(X<1012)=0.8413=P(Z<1)$" "\n" r"$\dfrac{1012-1000}{\sigma}=1 \Rightarrow \sigma=12\ \text{g}$",
  truth=lambda: [12/zz for zz in (R(1, 2), 1, R(3, 2), 2) if 1-Ph(zz) == R('0.1587')][0], tag='التوزيع الطبيعي: إيجاد الانحراف المعياري'),
]
# ================================================================== PAPER 3
pg3 = {'O': (0, 0), 'A': (4, 0), 'C': (1.5, 2.6), 'B': (5.5, 2.6), 'P': (4 + 1.5/3, 2.6/3), 'Q': (0.75, 1.3)}
P3 = [
Q('n3q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\sec^{2}x-\csc^{2}x', sec(x)**2-csc(x)**2)),
  [A(r'\tan x+\cot x+C', tan(x)+cot(x)), A(r'\tan x-\cot x+C', tan(x)-cot(x)), A(r'-\tan x+\cot x+C', -tan(x)+cot(x)), A(r'\sec x+\csc x+C', sec(x)+csc(x))],
  r"$\displaystyle\int\sec^2x\,dx=\tan x$ ، و $\displaystyle\int\csc^2x\,dx=-\cot x$ ، إذن الناتج $\tan x-(-\cot x)+C=\tan x+\cot x+C$",
  truth=sec(x)**2-csc(x)**2, tag='تكامل الاقترانات المثلثية'),
Q('n3q2', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'2^{5x}', 2**(5*x))),
  [A(r'\frac{2^{5x}}{5\ln 2}+C', 2**(5*x)/(5*log(2))), A(r'\frac{2^{5x}}{\ln 2}+C', 2**(5*x)/log(2)), A(r'5\cdot 2^{5x}\ln 2+C', 5*2**(5*x)*log(2)), A(r'\frac{2^{5x+1}}{5x+1}+C', 2**(5*x+1)/(5*x+1))],
  r"$\displaystyle\int a^{kx}dx=\frac{a^{kx}}{k\ln a}+C$ ، إذن $\displaystyle\int2^{5x}dx=\frac{2^{5x}}{5\ln2}+C$",
  truth=2**(5*x), tag='تكامل الاقتران الأسي'),
Q('n3q3', U5[1], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\frac{\pi}{4}}«0»\,dx$ هي:", (r'(1-2\sin^{2}x)', 1-2*sin(x)**2)),
  [O(r'\frac{1}{2}', R(1, 2)), O('1', 1), O(r'\frac{\pi}{4}-\frac{1}{2}', P/4-R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2))],
  r"$1-2\sin^2x=\cos2x$ ، إذن $\displaystyle\int_0^{\pi/4}\cos2x\,dx=\left[\frac12\sin2x\right]_0^{\pi/4}=\frac12\sin\frac{\pi}{2}-0=\frac12$",
  truth=ig(1-2*sin(x)**2, (x, 0, P/4)), tag='تكامل باستعمال متطابقات ضعف الزاوية'),
IndexQ('n3q4', U5[1], 'medium',
  r"إذا كان: $f'(x)=\dfrac{3}{x}+2e^{-x}$ ، حيث $x>0$ ، وكان $f(1)=1$ ، فإنّ قاعدة الاقتران $f(x)$ هي:",
  [O(r'f(x)=3\ln x-2e^{-x}+1+\frac{2}{e}', 3*log(x)-2*exp(-x)+1+2/E, 'eq'), O(r'f(x)=3\ln x-2e^{-x}+1', 3*log(x)-2*exp(-x)+1, 'eq'),
   O(r'f(x)=3\ln x+2e^{-x}+1-\frac{2}{e}', 3*log(x)+2*exp(-x)+1-2/E, 'eq'), O(r'f(x)=3\ln x-2e^{-x}+1-\frac{2}{e}', 3*log(x)-2*exp(-x)+1-2/E, 'eq')],
  r"$f(x)=\displaystyle\int\left(\frac3x+2e^{-x}\right)dx=3\ln x-2e^{-x}+C$" "\n" r"$f(1)=0-\dfrac2e+C=1 \Rightarrow C=1+\dfrac2e$",
  truth=lambda vals: only(vals, lambda F_: same(diff(F_, x)-(3/x+2*exp(-x)), 0) and same(F_.subs(x, 1), 1)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
Q('n3q5', U5[1], 'hard',
  r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=3t^{2}-12$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. المسافة الكلية التي قطعها الجسم في الفترة الزمنية $[0,\,3]$ هي:",
  [D('23', 'm'), D('9', 'm'), D('16', 'm'), D('7', 'm')],
  r"$v(t)=0 \Rightarrow t=2$ ، والسرعة سالبة في $[0,2)$ وموجبة في $(2,3]$" "\n"
  r"$\displaystyle\int_0^2(3t^2-12)dt=\big[t^3-12t\big]_0^2=-16$ ، $\displaystyle\int_2^3(3t^2-12)dt=-9-(-16)=7$" "\n" r"المسافة $=|-16|+7=23\ \text{m}$",
  truth=-ig(3*t**2-12, (t, 0, 2))+ig(3*t**2-12, (t, 2, 3)), tag='الحركة: المسافة الكلية من السرعة'),
Q('n3q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{e^{x}}{(1+e^{x})^{2}}', exp(x)/(1+exp(x))**2)),
  [A(r'-\frac{1}{1+e^{x}}+C', -1/(1+exp(x))), A(r'\frac{1}{1+e^{x}}+C', 1/(1+exp(x))), A(r'\ln(1+e^{x})+C', log(1+exp(x))), A(r'-\frac{1}{(1+e^{x})^{2}}+C', -1/(1+exp(x))**2)],
  r"بالتعويض $u=1+e^x \Rightarrow du=e^xdx$: $\displaystyle\int u^{-2}du=-u^{-1}+C=-\frac{1}{1+e^x}+C$",
  truth=exp(x)/(1+exp(x))**2, tag='التكامل بالتعويض'),
Q('n3q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sec^{2}x}{\sqrt{\tan x}}', sec(x)**2/sqrt(tan(x)))),
  [A(r'2\sqrt{\tan x}+C', 2*sqrt(tan(x))), A(r'\frac{1}{2}\sqrt{\tan x}+C', sqrt(tan(x))/2), A(r'\frac{2}{3}\sqrt{\tan^{3}x}+C', R(2, 3)*sqrt(tan(x)**3)), A(r'2\sqrt{\sec x}+C', 2*sqrt(sec(x)))],
  r"بالتعويض $u=\tan x \Rightarrow du=\sec^2x\,dx$: $\displaystyle\int u^{-\frac12}du=2u^{\frac12}+C=2\sqrt{\tan x}+C$",
  truth=sec(x)**2/sqrt(tan(x)), tag='التكامل بالتعويض: اقترانات مثلثية'),
Q('n3q8', U5[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{1}{x^{2}}\left(1+\frac{1}{x}\right)^{3}', (1+1/x)**3/x**2)),
  [A(r'-\frac{(1+\frac{1}{x})^{4}}{4}+C', -(1+1/x)**4/4), A(r'\frac{(1+\frac{1}{x})^{4}}{4}+C', (1+1/x)**4/4), A(r'-\frac{(1+\frac{1}{x})^{3}}{3}+C', -(1+1/x)**3/3), A(r'-\frac{(x+1)^{4}}{4x^{2}}+C', -(x+1)**4/(4*x**2))],
  r"بالتعويض $u=1+\dfrac1x \Rightarrow du=-\dfrac{1}{x^2}dx$: $\displaystyle-\int u^3du=-\frac{u^4}{4}+C=-\frac14\left(1+\frac1x\right)^4+C$",
  truth=(1+1/x)**3/x**2, tag='التكامل بالتعويض'),
Q('n3q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{1}^{e}«0»\,dx$ هي:", (r'\frac{(1+\ln x)^{2}}{x}', (1+log(x))**2/x)),
  [O(r'\frac{7}{3}', R(7, 3)), O(r'\frac{8}{3}', R(8, 3)), O(r'\frac{1}{3}', R(1, 3)), O('7', 7)],
  r"بالتعويض $u=1+\ln x \Rightarrow du=\frac1xdx$ ، والحدود $1\to2$: $\displaystyle\int_1^2u^2du=\left[\frac{u^3}{3}\right]_1^2=\frac83-\frac13=\frac73$",
  truth=ig((1+log(x))**2/x, (x, 1, E)), tag='التكامل المحدود بالتعويض'),
Q('n3q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{4x-2}{x^{2}-1}', (4*x-2)/(x**2-1))),
  [A(r'\ln|x-1|+3\ln|x+1|+C', log(x-1)+3*log(x+1)), A(r'3\ln|x-1|+\ln|x+1|+C', 3*log(x-1)+log(x+1)), A(r'\ln|x-1|-3\ln|x+1|+C', log(x-1)-3*log(x+1)), A(r'2\ln|x^{2}-1|+C', 2*log(x**2-1))],
  r"$\dfrac{4x-2}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1}$: عند $x=1$: $2=2A \Rightarrow A=1$ ، وعند $x=-1$: $-6=-2B \Rightarrow B=3$" "\n" r"الناتج: $\ln|x-1|+3\ln|x+1|+C$",
  truth=(4*x-2)/(x**2-1), tag='التكامل بالكسور الجزئية: عوامل خطية'),
Q('n3q11', U5[3], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'\frac{2x+3}{(x+1)^{2}}', (2*x+3)/(x+1)**2)),
  [O(r'2\ln 2+\frac{1}{2}', 2*log(2)+R(1, 2)), O(r'2\ln 2-\frac{1}{2}', 2*log(2)-R(1, 2)), O(r'\ln 2+\frac{1}{2}', log(2)+R(1, 2)), O(r'2\ln 2+1', 2*log(2)+1)],
  r"$\dfrac{2x+3}{(x+1)^2}=\dfrac{A}{x+1}+\dfrac{B}{(x+1)^2}$: $2x+3=A(x+1)+B \Rightarrow A=2,\ B=1$" "\n"
  r"$\displaystyle\int_0^1\left(\frac{2}{x+1}+\frac{1}{(x+1)^2}\right)dx=\left[2\ln|x+1|-\frac{1}{x+1}\right]_0^1=2\ln2-\frac12+1=2\ln2+\frac12$",
  truth=ig((2*x+3)/(x+1)**2, (x, 0, 1)), tag='التكامل بالكسور الجزئية: عامل مكرر'),
Q('n3q12', U5[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ ، حيث $x>0$ ، هو:", (r'\ln(x^{2})', 2*log(x))),
  [A(r'2x\ln x-2x+C', 2*x*log(x)-2*x), A(r'2x\ln x+2x+C', 2*x*log(x)+2*x), A(r'2x\ln x-x+C', 2*x*log(x)-x), A(r'x\ln x-x+C', x*log(x)-x)],
  r"$\ln(x^2)=2\ln x$ ، وبالأجزاء: $u=\ln x$ ، $dv=dx$: $\displaystyle2\left(x\ln x-\int x\cdot\frac1xdx\right)=2x\ln x-2x+C$",
  truth=2*log(x), tag='التكامل بالأجزاء'),
Q('n3q13', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'e^{x}\cos 2x', exp(x)*cos(2*x))),
  [A(r'\frac{1}{5}e^{x}(\cos 2x+2\sin 2x)+C', exp(x)*(cos(2*x)+2*sin(2*x))/5), A(r'\frac{1}{5}e^{x}(\cos 2x-2\sin 2x)+C', exp(x)*(cos(2*x)-2*sin(2*x))/5),
   A(r'\frac{1}{5}e^{x}(2\cos 2x+\sin 2x)+C', exp(x)*(2*cos(2*x)+sin(2*x))/5), A(r'\frac{1}{3}e^{x}(\cos 2x+2\sin 2x)+C', exp(x)*(cos(2*x)+2*sin(2*x))/3)],
  r"بالأجزاء مرتين (نرمز للتكامل بـ $I$): $I=e^x\cos2x+2\displaystyle\int e^x\sin2x\,dx=e^x\cos2x+2\left(e^x\sin2x-2I\right)$" "\n" r"$5I=e^x\cos2x+2e^x\sin2x \Rightarrow I=\dfrac15e^x(\cos2x+2\sin2x)+C$",
  truth=exp(x)*cos(2*x), tag='التكامل بالأجزاء: تكرار التكامل'),
Q('n3q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران: $f(x)=\dfrac{2x}{x^{2}+1}$. مساحة المنطقة المُظلَّلة المحصورة بين منحنى الاقتران $f(x)$ والمحور $x$ والمستقيم $x=2$ (بالوحدات المربعة) هي:",
  [O(r'\ln 5', log(5)), O(r'2\ln 5', 2*log(5)), O(r'\frac{1}{2}\ln 5', log(5)/2), O(r'\ln 3', log(3))],
  r"المنحنى يمرّ بنقطة الأصل، و $f(x)\ge0$ في $[0,2]$:" "\n" r"$\displaystyle\int_0^2\frac{2x}{x^2+1}dx=\big[\ln(x^2+1)\big]_0^2=\ln5-\ln1=\ln5$",
  truth=ig(2*x/(x**2+1), (x, 0, 2)), figure=figure('n3q14', region(2*x/(x**2+1), 0*x, 0, 2, (-0.6, 3.4), (-0.4, 1.5), [(2.5, 0.95, r'$f(x)$', '#1f5fbf')]), 3.4, 2.4), tag='المساحة تحت منحنى من الشكل'),
Q('n3q15', U5[5], 'hard',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنى الاقتران $f(x)=«0»$ والمستقيم $y=5$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'9-x^{2}', 9-x**2)),
  [O(r'\frac{704\pi}{5}', 704*P/5), O(r'\frac{512\pi}{15}', 512*P/15), O(r'\frac{32\pi}{3}', 32*P/3), O(r'\frac{1408\pi}{5}', 1408*P/5)],
  r"التقاطع: $9-x^2=5 \Rightarrow x=\pm2$ ، وفي الفترة $9-x^2\ge5>0$ ، فالحجم بطريقة الحلقات:" "\n"
  r"$V=\pi\displaystyle\int_{-2}^{2}\big((9-x^2)^2-5^2\big)dx=\pi\int_{-2}^{2}(x^4-18x^2+56)dx=2\pi\left(\frac{32}{5}-48+112\right)=\frac{704\pi}{5}$",
  truth=P*ig((9-x**2)**2-25, (x, -2, 2)), tag='الحجوم الدورانية: طريقة الحلقات'),
IndexQ('n3q16', U5[6], 'medium',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ ، حيث $y>0$ ، الذي يُحقّق الشرط الأوّلي $y(0)=1$ هو:", (r'\frac{\sec^{2}x}{2y}', sec(x)**2/(2*y))),
  [O(r'y=\sqrt{\tan x+1}', sqrt(tan(x)+1), 'eq'), O(r'y=\tan x+1', tan(x)+1, 'eq'), O(r'y=\sqrt{\tan x}+1', sqrt(tan(x))+1, 'eq'), O(r'y=\sqrt{2\tan x+1}', sqrt(2*tan(x)+1), 'eq')],
  r"بفصل المتغيرات: $2y\,dy=\sec^2x\,dx \Rightarrow y^2=\tan x+C$ ، و $y(0)=1 \Rightarrow C=1$" "\n" r"$y^2=\tan x+1$ ، وبما أن $y>0$: $y=\sqrt{\tan x+1}$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, sec(x)**2/(2*y), 0, 1)), tag='المعادلات التفاضلية: الحل الخاص'),
Q('n3q17', U6[1], 'medium',
  r"إذا كانت: $A(-1,\,4,\,2)$ ، $B(3,\,1,\,2)$ ، وكانت $C$ نقطة في الفضاء بحيث: $\overrightarrow{AB}=2\overrightarrow{BC}$ ، فإنّ إحداثيات النقطة $C$ هي:",
  [pt_opt(5, -R(1, 2), 2), pt_opt(11, -5, 2), pt_opt(1, R(5, 2), 2), pt_opt(7, -2, 2)],
  r"$\overrightarrow{AB}=\langle 4,-3,0\rangle$ ، إذن $\overrightarrow{BC}=\frac12\overrightarrow{AB}=\left\langle 2,-\frac32,0\right\rangle$" "\n" r"$C=B+\overrightarrow{BC}=\left(5,\ -\frac12,\ 2\right)$",
  truth=T3(V(3, 1, 2)+(V(3, 1, 2)-V(-1, 4, 2))/2), tag='المتجهات: نقطة ومتجه موقع'),
Q('n3q18', U6[1], 'easy',
  r"في متوازي المستطيلات الآتي، أحد رؤوسه نقطة الأصل $O$ ، وأحرفه $\overline{OP}$ و $\overline{OR}$ و $\overline{OS}$ على المحاور $x$ و $y$ و $z$ على الترتيب. إذا كانت إحداثيات الرأس $U$ هي $(3,\,4,\,2)$ ، فإنّ الصورة الإحداثية للمتجه $\overrightarrow{TR}$ هي:",
  [vec_opt(-3, 4, -2), vec_opt(3, -4, 2), vec_opt(3, 4, 2), vec_opt(-3, 4, 2)],
  r"من الشكل: $T(3,0,2)$ ، $R(0,4,0)$ ، إذن $\overrightarrow{TR}=R-T=\langle 0-3,\ 4-0,\ 0-2\rangle=\langle -3,4,-2\rangle$",
  truth=T3(V(0, 4, 0)-V(3, 0, 2)), figure=figure('n3q18', fig_box(3, 4, 2), 4.2, 2.6), tag='المتجهات من شكل ثلاثي الأبعاد'),
Q('n3q19', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{u}}=\langle c,\,2c,\,-2\rangle$ ، وكان $|\vec{\mathbf{u}}|=3$ ، حيث $c<0$ ، فإنّ قيمة الثابت $c$ هي:",
  [O('-1', -1), O('1', 1), O(r'-\sqrt{\frac{5}{3}}', -sqrt(R(5, 3))), O(r'-\sqrt{5}', -sqrt(5))],
  r"$c^2+4c^2+4=9 \Rightarrow 5c^2=5 \Rightarrow c=\pm1$ ، وبما أن $c<0$ فإن $c=-1$",
  truth=lambda: [r_ for r_ in solve(V(c, 2*c, -2).dot(V(c, 2*c, -2))-9, c) if r_ < 0][0], tag='المتجهات: المقدار وإيجاد ثابت'),
Q('n3q20', U6[1], 'hard',
  r"في الشكل الآتي $OABC$ متوازي أضلاع، فيه: $\overrightarrow{OA}=\vec{\mathbf{a}}$ ، $\overrightarrow{OC}=\vec{\mathbf{c}}$. إذا كانت النقطة $P$ تقع على $\overline{AB}$ بحيث $AP:PB=1:2$ ، وكانت $Q$ منتصف $\overline{OC}$ ، فإنّ $\overrightarrow{PQ}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{c}}$ هو:",
  [vopt(-va+vc/6), vopt(va-vc/6), vopt(-va+R(5, 6)*vc), vopt(-va-vc/6)],
  r"$\overrightarrow{AB}=\overrightarrow{OC}=\vec{\mathbf{c}}$ ، إذن $\overrightarrow{OP}=\vec{\mathbf{a}}+\frac13\vec{\mathbf{c}}$ ، و $\overrightarrow{OQ}=\frac12\vec{\mathbf{c}}$" "\n" r"$\overrightarrow{PQ}=\overrightarrow{OQ}-\overrightarrow{OP}=\frac12\vec{\mathbf{c}}-\vec{\mathbf{a}}-\frac13\vec{\mathbf{c}}=-\vec{\mathbf{a}}+\frac16\vec{\mathbf{c}}$",
  truth=vc/2-(va+vc/3),
  figure=figure('n3q20', fig_poly(pg3, [('A', 'B'), ('B', 'C')], [('O', 'A', r'$\vec{\mathbf{a}}$', (0, -0.45)), ('O', 'C', r'$\vec{\mathbf{c}}$', (0.2, -0.4))],
                                  {'O': (-0.35, -0.3), 'A': (0.05, -0.4), 'B': (0.12, 0.08), 'C': (-0.15, 0.15), 'P': (0.15, -0.1), 'Q': (-0.45, 0.05)}, extra_dashed=[('P', 'Q')]), 3.8, 2.4),
  tag='المتجهات في الأشكال الهندسية والنسبة'),
IndexQ('n3q21', U6[2], 'medium',
  r"معادلة متجهة للمستقيم المارّ بالنقطتين: $A(2,\,-3,\,1)$ و $B(-1,\,0,\,4)$ هي:",
  [line_opt((-1, 0, 4), (1, -1, -1)), line_opt((2, -3, 1), (1, -3, 5)), line_opt((-1, 0, 4), (2, -3, 1)), line_opt((2, -3, 1), (-1, -1, 1))],
  r"$\overrightarrow{AB}=\langle -3,3,3\rangle=-3\langle 1,-1,-1\rangle$ ، فيمكن أخذ متجه الاتجاه $\langle 1,-1,-1\rangle$ والنقطة $B$:" "\n" r"$\vec{\mathbf{r}}=\langle -1,0,4\rangle+t\langle 1,-1,-1\rangle$ (وتتحقق: عند $t=3$ نحصل على $A$)",
  truth=lambda vals: only(vals, lambda ln: on_line((2, -3, 1), ln) and on_line((-1, 0, 4), ln)), tag='معادلة المستقيم في الفضاء'),
Q('n3q22', U6[2], 'hard',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 0,1,2\rangle+t\langle 2,-2,1\rangle$ و $\vec{\mathbf{r}}_2=\langle 4,-3,4\rangle+s\langle -4,4,-2\rangle$ هي أنّهما:",
  rel_opts('coincident'),
  r"$\langle -4,4,-2\rangle=-2\langle 2,-2,1\rangle$ ، فالمستقيمان متوازيان أو منطبقان" "\n" r"النقطة $(4,-3,4)$ من $l_2$ تقع على $l_1$ عند $t=2$: $(0+4,\ 1-4,\ 2+2)=(4,-3,4)$ ✔ ، إذن المستقيمان منطبقان",
  truth=classify((0, 1, 2), (2, -2, 1), (4, -3, 4), (-4, 4, -2)), tag='العلاقة بين مستقيمين'),
Q('n3q23', U6[2], 'medium',
  r"إذا كانت النقطة $(k,\,-1,\,7)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle 1,\,3,\,-1\rangle+t\langle 2,\,-2,\,4\rangle$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('5', 5), O('3', 3), O('-3', -3), O('9', 9)],
  r"من المركبة الثانية: $3-2t=-1 \Rightarrow t=2$ ، وتتحقق الثالثة: $-1+4(2)=7$ ✔" "\n" r"$k=1+2(2)=5$",
  truth=lambda: (lambda tt: 1+2*tt if -1+4*tt == 7 else None)(solve(3-2*t+1, t)[0]), tag='نقطة على مستقيم وإيجاد ثابت'),
Q('n3q24', U6[3], 'medium',
  r"إذا كان: $\langle 1,\,-2,\,2\rangle$ و $\langle 2,\,2,\,-1\rangle$ متجهي اتجاه لمستقيمين متقاطعين، فإنّ جيب تمام الزاوية الحادة بين المستقيمين هو:",
  [O(r'\frac{4}{9}', R(4, 9)), O(r'-\frac{4}{9}', -R(4, 9)), O(r'\frac{4}{3}', R(4, 3)), O(r'\frac{2}{9}', R(2, 9))],
  r"$\langle 1,-2,2\rangle\cdot\langle 2,2,-1\rangle=2-4-2=-4$ ، ومقدار كل منهما $3$" "\n" r"جيب تمام الزاوية الحادة بين المستقيمين $=\dfrac{|-4|}{3\times3}=\dfrac49$",
  truth=Abs(V(1, -2, 2).dot(V(2, 2, -1)))/(V(1, -2, 2).norm()*V(2, 2, -1).norm()), tag='الزاوية بين مستقيمين'),
Q('n3q25', U6[3], 'easy',
  r"إذا كان المتجه: $\vec{\mathbf{v}}=\langle a,\,1,\,2\rangle$ عموديًّا على المتجه: $\langle 1,\,2,\,-2\rangle$ ، فإنّ $|\vec{\mathbf{v}}|$ يساوي:",
  [O('3', 3), O(r'\sqrt{5}', sqrt(5)), O('9', 9), O(r'\sqrt{21}', sqrt(21))],
  r"$a+2-4=0 \Rightarrow a=2$ ، إذن $|\vec{\mathbf{v}}|=\sqrt{4+1+4}=3$",
  truth=lambda: V(solve(V(a, 1, 2).dot(V(1, 2, -2)), a)[0], 1, 2).norm(), tag='التعامد وإيجاد ثوابت'),
Q('n3q26', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $P(X>2)=0.36$ ، فإنّ $P(X=2)$ يساوي:",
  [D('0.24'), D('0.16'), D('0.4'), D('0.096')],
  r"$P(X>2)=(1-p)^2=0.36 \Rightarrow 1-p=0.6 \Rightarrow p=0.4$" "\n" r"$P(X=2)=(1-p)p=(0.6)(0.4)=0.24$",
  truth=lambda: geo([r_ for r_ in solve((1-p)**2-R(36, 100), p) if 0 < r_ < 1][0], 2), tag='التوزيع الهندسي: احتمال «أكبر من»'),
Q('n3q27', U7[1], 'medium',
  r"إذا كان: $X\sim B(3,\,0.6)$ ، فإنّ $P(X\ge2)$ يساوي:",
  [D('0.648'), D('0.352'), D('0.432'), D('0.216')],
  r"$P(X\ge2)=P(X=2)+P(X=3)=\binom32(0.6)^2(0.4)+(0.6)^3=0.432+0.216=0.648$",
  truth=binom(3, R(3, 5), 2)+binom(3, R(3, 5), 3), tag='توزيع ذي الحدين: احتمال «على الأقل»'),
Q('n3q28', U7[2], 'medium',
  r"إذا كان: $X\sim N(40,\,16)$ ، فإنّ $P(X>45)$ يساوي:",
  [D('0.1056'), D('0.8944'), D('0.3944'), D('0.1587')],
  r"$\sigma=4$ ، $z=\dfrac{45-40}{4}=1.25$ ، $P(Z>1.25)=1-0.8944=0.1056$",
  truth=1-Ph(R(5, 4)), tag='التوزيع الطبيعي: حساب احتمال', lead=ztable_lead([28, 29, 30], 0.25, 0.5, 1, 1.25, 2), group=3),
Q('n3q29', U7[2], 'hard',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P(a<Z<1)=0.44$ ، فإنّ قيمة الثابت $a$ هي:",
  [D('-0.25'), D('0.25'), D('-0.5'), D('0.5')],
  r"$P(Z<1)-P(Z<a)=0.44 \Rightarrow P(Z<a)=0.8413-0.44=0.4013$" "\n" r"وبما أن $0.4013<0.5$ فإن $a$ سالبة: $P(Z<-a)=1-0.4013=0.5987 \Rightarrow -a=0.25 \Rightarrow a=-0.25$",
  truth=lambda: [-zz for zz in (R(1, 4), R(1, 2), 1, R(5, 4), 2) if Ph(1)-Ph(-zz) == R('0.44')][0], tag='التوزيع الطبيعي: إيجاد قيمة من احتمال'),
Q('n3q30', U7[2], 'hard',
  r"تتوزّع أعمار نوع من البطاريات توزيعًا طبيعيًّا: $X\sim N(\mu,\,25)$ بالساعات. إذا كان: $P(X<48)=0.0228$ ، فإنّ قيمة الوسط الحسابي $\mu$ هي:",
  [O('58', 58), O('38', 38), O('53', 53), O('43', 43)],
  r"$P(X<48)=0.0228=1-0.9772=P(Z<-2)$ ، و $\sigma=5$" "\n" r"$\dfrac{48-\mu}{5}=-2 \Rightarrow \mu=58$",
  truth=lambda: solve((48-Symbol('mu'))/5+2, Symbol('mu'))[0], tag='التوزيع الطبيعي: إيجاد الوسط الحسابي'),
]
# ================================================================== PAPER 4
vt4 = [(0, 4), (2, 0), (4, -2), (6, -2), (7, 0)]
tr4 = {'O': (0, 0), 'A': (1.2, 3.4), 'B': (6, 0), 'N': (4.5, 0), 'M': (3.6, 1.7)}
mu_, sg_ = symbols('mu_ sg_')
P4 = [
Q('n4q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\tan 2x', tan(2*x))),
  [A(r'-\frac{1}{2}\ln|\cos 2x|+C', -log(cos(2*x))/2), A(r'\frac{1}{2}\ln|\cos 2x|+C', log(cos(2*x))/2), A(r'-2\ln|\cos 2x|+C', -2*log(cos(2*x))), A(r'\frac{1}{2}\ln|\sin 2x|+C', log(sin(2*x))/2)],
  r"$\displaystyle\int\tan2x\,dx=\int\frac{\sin2x}{\cos2x}dx=-\frac12\ln|\cos2x|+C$",
  truth=tan(2*x), tag='تكامل الاقترانات المثلثية'),
Q('n4q2', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(3^{x}+3^{-x})^{2}', (3**x+3**(-x))**2)),
  [A(r'\frac{9^{x}}{\ln 9}+2x-\frac{9^{-x}}{\ln 9}+C', 9**x/log(9)+2*x-9**(-x)/log(9)), A(r'\frac{9^{x}}{\ln 9}+2x+\frac{9^{-x}}{\ln 9}+C', 9**x/log(9)+2*x+9**(-x)/log(9)),
   A(r'\frac{9^{x}}{\ln 9}-\frac{9^{-x}}{\ln 9}+C', 9**x/log(9)-9**(-x)/log(9)), A(r'\frac{(3^{x}+3^{-x})^{3}}{3}+C', (3**x+3**(-x))**3/3)],
  r"$(3^x+3^{-x})^2=9^x+2+9^{-x}$ ، و $\displaystyle\int9^{-x}dx=-\frac{9^{-x}}{\ln9}$" "\n" r"الناتج: $\dfrac{9^x}{\ln9}+2x-\dfrac{9^{-x}}{\ln9}+C$",
  truth=(3**x+3**(-x))**2, tag='تكامل الاقتران الأسي'),
Q('n4q3', U5[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{0}^{\frac{\pi}{2}}«0»\,dx$ هي:", (r'(\cos x+\sin 2x)', cos(x)+sin(2*x))),
  [O('2', 2), O('1', 1), O('3', 3), O('0', 0)],
  r"$\left[\sin x-\frac12\cos2x\right]_0^{\pi/2}=\left(1-\frac12(-1)\right)-\left(0-\frac12\right)=\frac32+\frac12=2$",
  truth=ig(cos(x)+sin(2*x), (x, 0, P/2)), tag='التكامل المحدود لاقترانات مثلثية'),
IndexQ('n4q4', U5[1], 'easy',
  r"إذا كان: $f'(x)=2\cos 2x-3x^{2}$ ، وكان منحنى الاقتران $f(x)$ يمرّ بالنقطة $(0,\,5)$ ، فإنّ قاعدة الاقتران $f(x)$ هي:",
  [O(r'f(x)=\sin 2x-x^{3}+5', sin(2*x)-x**3+5, 'eq'), O(r'f(x)=4\sin 2x-x^{3}+5', 4*sin(2*x)-x**3+5, 'eq'),
   O(r'f(x)=-\sin 2x-x^{3}+5', -sin(2*x)-x**3+5, 'eq'), O(r'f(x)=\sin 2x-x^{3}+4', sin(2*x)-x**3+4, 'eq')],
  r"$f(x)=\displaystyle\int(2\cos2x-3x^2)dx=\sin2x-x^3+C$" "\n" r"$f(0)=0-0+C=5 \Rightarrow C=5$",
  truth=lambda vals: only(vals, lambda F_: same(diff(F_, x)-(2*cos(2*x)-3*x**2), 0) and same(F_.subs(x, 0), 5)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
Q('n4q5', U5[1], 'hard',
  r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=2\sin t$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. المسافة الكلية التي قطعها الجسم في الفترة الزمنية $\left[0,\,\dfrac{3\pi}{2}\right]$ هي:",
  [D('6', 'm'), D('2', 'm'), D('4', 'm'), D('8', 'm')],
  r"$v(t)\ge0$ في $[0,\pi]$ و $v(t)<0$ في $\left(\pi,\frac{3\pi}{2}\right]$" "\n"
  r"$\displaystyle\int_0^{\pi}2\sin t\,dt=\big[-2\cos t\big]_0^{\pi}=4$ ، $\displaystyle\int_{\pi}^{3\pi/2}2\sin t\,dt=0-2=-2$" "\n" r"المسافة $=4+|-2|=6\ \text{m}$",
  truth=ig(2*sin(t), (t, 0, P))-ig(2*sin(t), (t, P, 3*P/2)), tag='الحركة: المسافة الكلية من السرعة'),
Q('n4q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2x+1}{(x^{2}+x+3)^{2}}', (2*x+1)/(x**2+x+3)**2)),
  [A(r'-\frac{1}{x^{2}+x+3}+C', -1/(x**2+x+3)), A(r'\frac{1}{x^{2}+x+3}+C', 1/(x**2+x+3)), A(r'\ln(x^{2}+x+3)+C', log(x**2+x+3)), A(r'-\frac{1}{3(x^{2}+x+3)^{3}}+C', -1/(3*(x**2+x+3)**3))],
  r"بالتعويض $u=x^2+x+3 \Rightarrow du=(2x+1)dx$: $\displaystyle\int u^{-2}du=-\frac1u+C=-\frac{1}{x^2+x+3}+C$",
  truth=(2*x+1)/(x**2+x+3)**2, tag='التكامل بالتعويض'),
Q('n4q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\sin^{3}x', sin(x)**3)),
  [A(r'-\cos x+\frac{\cos^{3}x}{3}+C', -cos(x)+cos(x)**3/3), A(r'\cos x-\frac{\cos^{3}x}{3}+C', cos(x)-cos(x)**3/3), A(r'-\cos x-\frac{\cos^{3}x}{3}+C', -cos(x)-cos(x)**3/3), A(r'\frac{\sin^{4}x}{4}+C', sin(x)**4/4)],
  r"$\sin^3x=(1-\cos^2x)\sin x$ ، وبالتعويض $u=\cos x \Rightarrow du=-\sin x\,dx$:" "\n" r"$\displaystyle-\int(1-u^2)du=-u+\frac{u^3}{3}+C=-\cos x+\frac{\cos^3x}{3}+C$",
  truth=sin(x)**3, tag='التكامل بالتعويض: اقترانات مثلثية'),
Q('n4q8', U5[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x}{\sqrt{x+4}}', x/sqrt(x+4))),
  [A(r'\frac{2}{3}(x+4)^{\frac{3}{2}}-8\sqrt{x+4}+C', R(2, 3)*(x+4)**R(3, 2)-8*sqrt(x+4)), A(r'\frac{2}{3}(x+4)^{\frac{3}{2}}+8\sqrt{x+4}+C', R(2, 3)*(x+4)**R(3, 2)+8*sqrt(x+4)),
   A(r'\frac{2}{3}(x+4)^{\frac{3}{2}}-4\sqrt{x+4}+C', R(2, 3)*(x+4)**R(3, 2)-4*sqrt(x+4)), A(r'2x\sqrt{x+4}+C', 2*x*sqrt(x+4))],
  r"بالتعويض $u=x+4 \Rightarrow x=u-4,\ dx=du$:" "\n" r"$\displaystyle\int\frac{u-4}{\sqrt u}du=\int\left(u^{\frac12}-4u^{-\frac12}\right)du=\frac23u^{\frac32}-8u^{\frac12}+C=\frac23(x+4)^{\frac32}-8\sqrt{x+4}+C$",
  truth=x/sqrt(x+4), tag='التكامل بالتعويض: جذور'),
Q('n4q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\frac{\pi}{6}}«0»\,dx$ هي:", (r'\frac{\cos x}{1+\sin x}', cos(x)/(1+sin(x)))),
  [O(r'\ln\frac{3}{2}', log(R(3, 2))), O(r'\ln\frac{2}{3}', log(R(2, 3))), O(r'\ln 3', log(3)), O(r'\frac{1}{2}', R(1, 2))],
  r"بالتعويض $u=1+\sin x \Rightarrow du=\cos x\,dx$ ، والحدود $1\to\frac32$: $\big[\ln|u|\big]_1^{3/2}=\ln\dfrac32$",
  truth=ig(cos(x)/(1+sin(x)), (x, 0, P/6)), tag='التكامل المحدود بالتعويض'),
Q('n4q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x+9}{(x-3)(x+1)}', (x+9)/((x-3)*(x+1)))),
  [A(r'3\ln|x-3|-2\ln|x+1|+C', 3*log(x-3)-2*log(x+1)), A(r'-2\ln|x-3|+3\ln|x+1|+C', -2*log(x-3)+3*log(x+1)), A(r'3\ln|x-3|+2\ln|x+1|+C', 3*log(x-3)+2*log(x+1)), A(r'3\ln|x+3|-2\ln|x-1|+C', 3*log(x+3)-2*log(x-1))],
  r"$\dfrac{x+9}{(x-3)(x+1)}=\dfrac{A}{x-3}+\dfrac{B}{x+1}$: عند $x=3$: $12=4A \Rightarrow A=3$ ، وعند $x=-1$: $8=-4B \Rightarrow B=-2$" "\n" r"الناتج: $3\ln|x-3|-2\ln|x+1|+C$",
  truth=(x+9)/((x-3)*(x+1)), tag='التكامل بالكسور الجزئية: عوامل خطية'),
Q('n4q11', U5[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2x^{2}-x+1}{x(x-1)^{2}}', (2*x**2-x+1)/(x*(x-1)**2))),
  [A(r'\ln|x|+\ln|x-1|-\frac{2}{x-1}+C', log(x)+log(x-1)-2/(x-1)), A(r'\ln|x|+\ln|x-1|+\frac{2}{x-1}+C', log(x)+log(x-1)+2/(x-1)),
   A(r'\ln|x|-\ln|x-1|-\frac{2}{x-1}+C', log(x)-log(x-1)-2/(x-1)), A(r'\ln|x|+2\ln|x-1|-\frac{1}{x-1}+C', log(x)+2*log(x-1)-1/(x-1))],
  r"$\dfrac{2x^2-x+1}{x(x-1)^2}=\dfrac{A}{x}+\dfrac{B}{x-1}+\dfrac{D}{(x-1)^2}$: عند $x=0$: $A=1$ ، وعند $x=1$: $D=2$ ، ومقارنة معامل $x^2$: $A+B=2 \Rightarrow B=1$" "\n"
  r"الناتج: $\ln|x|+\ln|x-1|-\dfrac{2}{x-1}+C$",
  truth=(2*x**2-x+1)/(x*(x-1)**2), tag='التكامل بالكسور الجزئية: عامل مكرر'),
Q('n4q12', U5[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'xe^{-x}', x*exp(-x))),
  [A(r'-xe^{-x}-e^{-x}+C', -x*exp(-x)-exp(-x)), A(r'-xe^{-x}+e^{-x}+C', -x*exp(-x)+exp(-x)), A(r'xe^{-x}-e^{-x}+C', x*exp(-x)-exp(-x)), A(r'-\frac{x^{2}}{2}e^{-x}+C', -x**2/2*exp(-x))],
  r"بالأجزاء: $u=x$ ، $dv=e^{-x}dx \Rightarrow v=-e^{-x}$: $\displaystyle-xe^{-x}+\int e^{-x}dx=-xe^{-x}-e^{-x}+C$",
  truth=x*exp(-x), tag='التكامل بالأجزاء'),
Q('n4q13', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ ، حيث $x>0$ ، هو:", (r'\sin(\ln x)', sin(log(x)))),
  [A(r'\frac{x}{2}(\sin(\ln x)-\cos(\ln x))+C', x/2*(sin(log(x))-cos(log(x)))), A(r'\frac{x}{2}(\sin(\ln x)+\cos(\ln x))+C', x/2*(sin(log(x))+cos(log(x)))),
   A(r'\frac{x}{2}(\cos(\ln x)-\sin(\ln x))+C', x/2*(cos(log(x))-sin(log(x)))), A(r'-x\cos(\ln x)+C', -x*cos(log(x)))],
  r"بالأجزاء مرتين (نرمز للتكامل بـ $I$): $I=x\sin(\ln x)-\displaystyle\int\cos(\ln x)dx=x\sin(\ln x)-\big(x\cos(\ln x)+I\big)$" "\n" r"$2I=x\sin(\ln x)-x\cos(\ln x) \Rightarrow I=\dfrac x2\big(\sin(\ln x)-\cos(\ln x)\big)+C$",
  truth=sin(log(x)), tag='التكامل بالأجزاء: تكرار التكامل'),
Q('n4q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة–الزمن لجسم يتحرّك في مسار مستقيم في الفترة الزمنية $[0,\,7]$. المسافة الكلية التي قطعها الجسم في هذه الفترة هي:",
  [D('11', 'm'), D('3', 'm'), D('-3', 'm'), D('7', 'm')],
  r"المسافة = مجموع المساحات (كلها موجبة):" "\n" r"$[0,2]$: $\frac12(2)(4)=4$ ، $[2,4]$: $\frac12(2)(2)=2$ ، $[4,6]$: $2\times2=4$ ، $[6,7]$: $\frac12(1)(2)=1$" "\n" r"المسافة $=4+2+4+1=11\ \text{m}$ (أما الإزاحة فهي $4-7=-3$)",
  truth=lambda: pw_integral(vt4, 0, 7, absolute=True), figure=figure('n4q14', vt_graph(vt4, 7, -2, 4), 4.0, 3.0), tag='الحركة من منحنى السرعة–الزمن'),
Q('n4q15', U5[5], 'hard',
  F(r"مساحة المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ في الفترة $\left[0,\,\dfrac{\pi}{2}\right]$ (بالوحدات المربعة) هي:", (r'\sin x', sin(x)), (r'\cos x', cos(x))),
  [O(r'2\sqrt{2}-2', 2*sqrt(2)-2), O(r'2\sqrt{2}', 2*sqrt(2)), O(r'\sqrt{2}-1', sqrt(2)-1), O('0', 0)],
  r"يتقاطع المنحنيان عند $x=\frac{\pi}{4}$ ، و $\cos x\ge\sin x$ في $\left[0,\frac{\pi}{4}\right]$ ، و $\sin x\ge\cos x$ في $\left[\frac{\pi}{4},\frac{\pi}{2}\right]$" "\n"
  r"$\displaystyle\int_0^{\pi/4}(\cos x-\sin x)dx+\int_{\pi/4}^{\pi/2}(\sin x-\cos x)dx=(\sqrt2-1)+(\sqrt2-1)=2\sqrt2-2$",
  truth=ig(cos(x)-sin(x), (x, 0, P/4))+ig(sin(x)-cos(x), (x, P/4, P/2)), tag='المساحة بين منحنيين متقاطعين'),
IndexQ('n4q16', U5[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ هو:", (r'e^{y}\cos x', exp(y)*cos(x))),
  [O(r'-e^{-y}=\sin x+C', -exp(-y)-sin(x)-Cc, 'rel'), O(r'e^{-y}=\sin x+C', exp(-y)-sin(x)-Cc, 'rel'), O(r'e^{y}=\sin x+C', exp(y)-sin(x)-Cc, 'rel'), O(r'-e^{-y}=-\sin x+C', -exp(-y)+sin(x)-Cc, 'rel')],
  r"بفصل المتغيرات: $e^{-y}dy=\cos x\,dx \Rightarrow \displaystyle\int e^{-y}dy=\int\cos x\,dx \Rightarrow -e^{-y}=\sin x+C$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, exp(y)*cos(x))), tag='المعادلات التفاضلية: الحل العام'),
IndexQ('n4q17', U6[2], 'easy',
  r"معادلة متجهة للمستقيم المارّ بالنقطة $(-1,\,0,\,2)$ ويوازي المستقيم: $\vec{\mathbf{r}}=\langle 3,\,1,\,-4\rangle+s\langle 2,\,-1,\,0\rangle$ هي:",
  [line_opt((-1, 0, 2), (-4, 2, 0)), line_opt((-1, 0, 2), (3, 1, -4)), line_opt((3, 1, -4), (-1, 0, 2)), line_opt((2, -1, 0), (-1, 0, 2))],
  r"المستقيمان متوازيان، فمتجه الاتجاه $\langle 2,-1,0\rangle$ أو أيّ مضاعف له مثل $\langle -4,2,0\rangle$ ، والنقطة $(-1,0,2)$:" "\n" r"$\vec{\mathbf{r}}=\langle -1,0,2\rangle+t\langle -4,2,0\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((-1, 0, 2), ln) and par(ln[1], (2, -1, 0))), tag='معادلة مستقيم يوازي مستقيمًا معلومًا'),
Q('n4q18', U6[1], 'easy',
  r"متجه الوحدة في اتجاه المتجه $\overrightarrow{PQ}$ هو:",
  [vec_opt(1/sqrt(6), 2/sqrt(6), 1/sqrt(6)), vec_opt(1, 2, 1), vec_opt(R(1, 6), R(1, 3), R(1, 6)), vec_opt(-1/sqrt(6), -2/sqrt(6), -1/sqrt(6))],
  r"$\overrightarrow{PQ}=\langle 2,4,2\rangle$ ، و $|\overrightarrow{PQ}|=\sqrt{4+16+4}=2\sqrt6$" "\n" r"متجه الوحدة: $\dfrac{1}{2\sqrt6}\langle 2,4,2\rangle=\left\langle \frac{1}{\sqrt6},\frac{2}{\sqrt6},\frac{1}{\sqrt6}\right\rangle$",
  truth=T3((V(3, 4, 0)-V(1, 0, -2))/(V(3, 4, 0)-V(1, 0, -2)).norm()), tag='متجه الوحدة (نص مشترك)',
  lead=shared(r"إذا كانت: $P(1,\,0,\,-2)$ ، $Q(3,\,4,\,0)$ ، $R(\beta,\,2,\,1)$ ثلاث نقاط في الفضاء، حيث $\beta$ ثابت", 18, 19)),
Q('n4q19', U6[3], 'medium',
  r"إذا كان: $\overrightarrow{PR}\perp\overrightarrow{PQ}$ ، فإنّ قيمة الثابت $\beta$ هي:",
  [O('-6', -6), O('6', 6), O('-7', -7), O('-4', -4)],
  r"$\overrightarrow{PR}=\langle \beta-1,\ 2,\ 3\rangle$ ، $\overrightarrow{PQ}=\langle 2,4,2\rangle$" "\n" r"$\overrightarrow{PR}\cdot\overrightarrow{PQ}=2(\beta-1)+8+6=0 \Rightarrow 2\beta=-12 \Rightarrow \beta=-6$",
  truth=lambda: solve((V(b, 2, 1)-V(1, 0, -2)).dot(V(3, 4, 0)-V(1, 0, -2)), b)[0], tag='التعامد وإيجاد ثوابت (نص مشترك)'),
Q('n4q20', U6[1], 'hard',
  r"في الشكل الآتي $OAB$ مثلث فيه: $\overrightarrow{OA}=6\vec{\mathbf{a}}$ ، $\overrightarrow{OB}=4\vec{\mathbf{b}}$. إذا كانت النقطة $N$ تقع على $\overline{OB}$ بحيث $ON:NB=3:1$ ، وكانت $M$ منتصف $\overline{AB}$ ، فإنّ $\overrightarrow{MN}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [vopt(-3*va+vb), vopt(3*va-vb), vopt(-3*va-vb), vopt(-6*va+3*vb)],
  r"$\overrightarrow{ON}=\frac34(4\vec{\mathbf{b}})=3\vec{\mathbf{b}}$ ، $\overrightarrow{OM}=\frac12(6\vec{\mathbf{a}}+4\vec{\mathbf{b}})=3\vec{\mathbf{a}}+2\vec{\mathbf{b}}$" "\n" r"$\overrightarrow{MN}=\overrightarrow{ON}-\overrightarrow{OM}=-3\vec{\mathbf{a}}+\vec{\mathbf{b}}$",
  truth=R(3, 4)*4*vb-(6*va+4*vb)/2,
  figure=figure('n4q20', fig_poly(tr4, [('A', 'B')], [('O', 'A', r'$6\vec{\mathbf{a}}$', (-0.95, 0.05)), ('O', 'B', r'$4\vec{\mathbf{b}}$', (0, -0.5))],
                                  {'O': (-0.35, -0.3), 'A': (-0.1, 0.2), 'B': (0.1, -0.3), 'N': (-0.1, -0.45), 'M': (0.15, 0.1)}, extra_dashed=[('M', 'N')]), 3.8, 2.6),
  tag='المتجهات في الأشكال الهندسية والنسبة'),
Q('n4q21', U6[1], 'medium',
  r"المتجه الذي مقداره $6$ وحدات ، واتجاهه عكس اتجاه المتجه $\langle 2,\,-1,\,2\rangle$ هو:",
  [vec_opt(-4, 2, -4), vec_opt(4, -2, 4), vec_opt(-12, 6, -12), vec_opt(-2, 1, -2)],
  r"$|\langle 2,-1,2\rangle|=3$ ، ومتجه الوحدة في عكس اتجاهه $\left\langle -\frac23,\frac13,-\frac23\right\rangle$" "\n" r"المتجه المطلوب $=6\left\langle -\frac23,\frac13,-\frac23\right\rangle=\langle -4,2,-4\rangle$",
  truth=T3(-6*V(2, -1, 2)/V(2, -1, 2).norm()), tag='متجه بمقدار معلوم في اتجاه معلوم'),
Q('n4q22', U6[2], 'hard',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 3,-1,4\rangle+t\langle 1,1,-2\rangle$ معادلة متجهة للمستقيم $l_1$ ، وكانت: $\vec{\mathbf{r}}=\langle -4,-2,3\rangle+s\langle 2,0,1\rangle$ معادلة متجهة للمستقيم $l_2$ ، فإنّ إحداثيات نقطة تقاطع المستقيمين هي:",
  [pt_opt(2, -2, 6), pt_opt(4, 0, 2), pt_opt(-2, -2, 5), pt_opt(2, -2, 2)],
  r"$3+t=-4+2s$ ، $-1+t=-2$ ، $4-2t=3+s$" "\n" r"من الثانية: $t=-1$ ، ومن الأولى: $s=3$ ، وتتحقق الثالثة: $6=6$ ✔" "\n" r"نقطة التقاطع: $\langle 3,-1,4\rangle-\langle 1,1,-2\rangle=(2,-2,6)$",
  truth=lambda: inter((3, -1, 4), (1, 1, -2), (-4, -2, 3), (2, 0, 1)), tag='نقطة تقاطع مستقيمين'),
Q('n4q23', U6[2], 'medium',
  r"إذا كان المستقيم: $\vec{\mathbf{r}}=\langle 1,0,5\rangle+t\langle 2,\,a,\,-4\rangle$ يوازي المستقيم: $\vec{\mathbf{r}}=\langle 0,2,-1\rangle+s\langle -1,\,3,\,b\rangle$ ، فإنّ $a+b$ يساوي:",
  [O('-4', -4), O('4', 4), O('-8', -8), O('8', 8)],
  r"متجها الاتجاه متوازيان: $\langle 2,a,-4\rangle=k\langle -1,3,b\rangle$ ، من المركبة الأولى $k=-2$" "\n" r"$a=-2(3)=-6$ ، و $-4=-2b \Rightarrow b=2$ ، إذن $a+b=-4$",
  truth=lambda: (lambda sol: sol[a]+sol[b])(solve(list(V(2, a, -4).cross(V(-1, 3, b))), [a, b], dict=True)[0]), tag='توازي مستقيمين وإيجاد ثوابت'),
Q('n4q24', U6[3], 'hard',
  r"إذا كان: $|\vec{\mathbf{a}}|=2$ ، $|\vec{\mathbf{b}}|=3$ ، $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=-1$ ، فإنّ $(2\vec{\mathbf{a}}-\vec{\mathbf{b}})\cdot(\vec{\mathbf{a}}+3\vec{\mathbf{b}})$ يساوي:",
  [O('-24', -24), O('-34', -34), O('-14', -14), O('20', 20)],
  r"$(2\vec{\mathbf{a}}-\vec{\mathbf{b}})\cdot(\vec{\mathbf{a}}+3\vec{\mathbf{b}})=2|\vec{\mathbf{a}}|^2+6\,\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}-\vec{\mathbf{b}}\cdot\vec{\mathbf{a}}-3|\vec{\mathbf{b}}|^2$" "\n" r"$=2(4)+5(-1)-3(9)=8-5-27=-24$",
  truth=lambda: (lambda aa, ab, bb: 2*aa+6*ab-ab-3*bb)(4, -1, 9), tag='خصائص الضرب القياسي'),
Q('n4q25', U6[3], 'medium',
  r"إذا كانت: $A(3,\,1,\,0)$ ، $B(2,\,1,\,-1)$ ، $C(2,\,0,\,-2)$ رؤوس المثلث $ABC$ ، فإنّ قياس الزاوية $ABC$ هو:",
  [O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{3}', P/3), O(r'\frac{5\pi}{6}', 5*P/6), O(r'\frac{\pi}{6}', P/6)],
  r"الزاوية $ABC$ بين المتجهين $\overrightarrow{BA}=\langle 1,0,1\rangle$ و $\overrightarrow{BC}=\langle 0,-1,-1\rangle$" "\n" r"$\cos\theta=\dfrac{0+0-1}{\sqrt2\cdot\sqrt2}=-\dfrac12 \Rightarrow \theta=\dfrac{2\pi}{3}$",
  truth=ang(V(3, 1, 0)-V(2, 1, -1), V(2, 0, -2)-V(2, 1, -1)), tag='الزاوية بين متجهين: زاوية في مثلث'),
Q('n4q26', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان التوقّع $E(X)=4$ ، فإنّ $P(X\ge3)$ يساوي:",
  [O(r'\frac{9}{16}', R(9, 16)), O(r'\frac{27}{64}', R(27, 64)), O(r'\frac{7}{16}', R(7, 16)), O(r'\frac{9}{64}', R(9, 64))],
  r"$E(X)=\frac1p=4 \Rightarrow p=\frac14$" "\n" r"$P(X\ge3)=P(X>2)=(1-p)^2=\left(\frac34\right)^2=\frac{9}{16}$",
  truth=1-geo(R(1, 4), 1)-geo(R(1, 4), 2), tag='التوزيع الهندسي: احتمال «أكبر من»'),
Q('n4q27', U7[1], 'medium',
  r"إذا كان احتمال نجاح لاعب في إصابة هدف في كل محاولة $0.2$ ، وحاول $5$ محاولات مستقلة، فإنّ احتمال أن يُصيب الهدف مرة واحدة على الأكثر هو تقريبًا:",
  [D('0.7373'), D('0.2627'), D('0.4096'), D('0.3277')],
  r"$X\sim B(5,\,0.2)$: $P(X\le1)=(0.8)^5+5(0.2)(0.8)^4=0.32768+0.4096\approx0.7373$",
  truth=r4(binom(5, R(1, 5), 0)+binom(5, R(1, 5), 1)), tag='توزيع ذي الحدين: احتمال «على الأكثر»'),
Q('n4q28', U7[2], 'medium',
  r"يُمثّل الشكل الآتي منحنى التوزيع الطبيعي المعياري. إذا علمت أنّ: $P(Z<-2.3)=0.0107$ ، فإنّ مساحة المنطقة المُظلَّلة هي:",
  [D('0.0214'), D('0.0107'), D('0.9786'), D('0.4893')],
  r"المنطقة المظلّلة طرفان متماثلان: $P(Z<-2.3)+P(Z>2.3)=2(0.0107)=0.0214$",
  truth=2*R('0.0107'), figure=figure('n4q28', bell([(-3.6, -2.3), (2.3, 3.6)], [-2.3, 0, 2.3]), 4.0, 2.3), tag='التوزيع الطبيعي: مساحة من الشكل'),
Q('n4q29', U7[2], 'medium',
  r"إذا كان: $X\sim N(200,\,400)$ ، فإنّ $P(176<X<224)$ يساوي:",
  [D('0.7698'), D('0.3849'), D('0.8849'), D('0.6826')],
  r"$\sigma=20$ ، $z=\dfrac{176-200}{20}=-1.2$ ، $z=\dfrac{224-200}{20}=1.2$" "\n" r"$P(-1.2<Z<1.2)=2P(Z<1.2)-1=2(0.8849)-1=0.7698$",
  truth=Ph(R(6, 5))-Ph(-R(6, 5)), tag='التوزيع الطبيعي: حساب احتمال', lead=ztable_lead([29, 30], 0.8, 1, 1.2, 1.5), group=2),
Q('n4q30', U7[2], 'hard',
  r"إذا كان: $X\sim N(\mu,\,\sigma^{2})$ ، وكان: $P(X<70)=0.8413$ ، $P(X<45)=0.0668$ ، فإنّ قيمتي $\mu$ و $\sigma$ هما:",
  [O(r'\mu=60,\ \sigma=10', Tuple(60, 10), 'pairs'), O(r'\mu=50,\ \sigma=20', Tuple(50, 20), 'pairs'), O(r'\mu=55,\ \sigma=15', Tuple(55, 15), 'pairs'), O(r'\mu=62.5,\ \sigma=7.5', Tuple(R(125, 2), R(15, 2)), 'pairs')],
  r"$P(X<70)=0.8413=P(Z<1) \Rightarrow \dfrac{70-\mu}{\sigma}=1$" "\n" r"$P(X<45)=0.0668=1-0.9332=P(Z<-1.5) \Rightarrow \dfrac{45-\mu}{\sigma}=-1.5$" "\n"
  r"بالطرح: $25=2.5\sigma \Rightarrow \sigma=10$ ، ثم $\mu=70-10=60$",
  truth=lambda: (lambda sol: Tuple(sol[mu_], sol[sg_]))(solve([70-mu_-1*sg_, 45-mu_+R(3, 2)*sg_], [mu_, sg_])), tag='التوزيع الطبيعي: إيجاد الوسط والانحراف'),
]
# ================================================================== PAPER 5 (hardest)
pg5 = {'U': (0, 0), 'V': (4, 0), 'X': (1.2, 2.4), 'W': (5.2, 2.4), 'Y': (2.6, 1.2), 'Z': (6.2, 2.4)}
kk = Symbol('kk')
P5 = [
Q('n5q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(1+\tan^{2}3x)', 1+tan(3*x)**2)),
  [A(r'\frac{1}{3}\tan 3x+C', tan(3*x)/3), A(r'\tan 3x+C', tan(3*x)), A(r'3\tan 3x+C', 3*tan(3*x)), A(r'x+\frac{1}{3}\tan 3x+C', x+tan(3*x)/3)],
  r"$1+\tan^23x=\sec^23x$ ، إذن $\displaystyle\int\sec^23x\,dx=\frac13\tan3x+C$",
  truth=1+tan(3*x)**2, tag='تكامل الاقترانات المثلثية'),
Q('n5q2', U5[1], 'hard',
  F(r"إذا كان: $\displaystyle\int_{0}^{\ln a}«0»\,dx=\frac{8}{3}$ ، حيث $a>1$ ، فإنّ قيمة الثابت $a$ هي:", (r'(e^{x}+e^{-x})', exp(x)+exp(-x))),
  [O('3', 3), O(r'\frac{1}{3}', R(1, 3)), O('9', 9), O(r'e^{3}', exp(3))],
  r"$\big[e^x-e^{-x}\big]_0^{\ln a}=a-\dfrac1a-0=\dfrac83 \Rightarrow 3a^2-8a-3=0 \Rightarrow (3a+1)(a-3)=0$" "\n" r"وبما أن $a>1$ فإن $a=3$",
  truth=lambda: [r_ for r_ in solve(ig(exp(x)+exp(-x), (x, 0, log(a)))-R(8, 3), a) if r_.is_real and r_ > 1][0], tag='التكامل المحدود: إيجاد ثابت'),
Q('n5q3', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos^{2}3x', cos(3*x)**2)),
  [A(r'\frac{x}{2}+\frac{\sin 6x}{12}+C', x/2+sin(6*x)/12), A(r'\frac{x}{2}-\frac{\sin 6x}{12}+C', x/2-sin(6*x)/12), A(r'\frac{x}{2}+\frac{\sin 6x}{6}+C', x/2+sin(6*x)/6), A(r'\frac{\cos^{3}3x}{9}+C', cos(3*x)**3/9)],
  r"$\cos^23x=\dfrac{1+\cos6x}{2}$ ، إذن $\displaystyle\int\left(\frac12+\frac12\cos6x\right)dx=\frac x2+\frac{\sin6x}{12}+C$",
  truth=cos(3*x)**2, tag='تكامل باستعمال تقليص القوة'),
IndexQ('n5q4', U5[1], 'hard',
  r"إذا كان: $f''(x)=6x+e^{x}$ ، وكان: $f'(0)=2$ ، $f(0)=3$ ، فإنّ قاعدة الاقتران $f(x)$ هي:",
  [O(r'f(x)=x^{3}+e^{x}+x+2', x**3+exp(x)+x+2, 'eq'), O(r'f(x)=x^{3}+e^{x}+2x+2', x**3+exp(x)+2*x+2, 'eq'), O(r'f(x)=x^{3}+e^{x}+x+3', x**3+exp(x)+x+3, 'eq'), O(r'f(x)=x^{3}+e^{x}+2', x**3+exp(x)+2, 'eq')],
  r"$f'(x)=3x^2+e^x+C_1$ ، و $f'(0)=1+C_1=2 \Rightarrow C_1=1$" "\n" r"$f(x)=x^3+e^x+x+C_2$ ، و $f(0)=1+C_2=3 \Rightarrow C_2=2$",
  truth=lambda vals: only(vals, lambda F_: same(diff(F_, x, 2)-(6*x+exp(x)), 0) and same(diff(F_, x).subs(x, 0), 2) and same(F_.subs(x, 0), 3)), tag='إيجاد الاقتران من مشتقته الثانية'),
Q('n5q5', U5[1], 'hard',
  r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=6t-3t^{2}$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. المسافة الكلية التي قطعها الجسم في الفترة الزمنية $[0,\,3]$ هي:",
  [D('8', 'm'), D('0', 'm'), D('4', 'm'), D('12', 'm')],
  r"$v(t)=3t(2-t)=0 \Rightarrow t=2$ ، والسرعة موجبة في $(0,2)$ وسالبة في $(2,3]$" "\n"
  r"$\displaystyle\int_0^2(6t-3t^2)dt=\big[3t^2-t^3\big]_0^2=4$ ، $\displaystyle\int_2^3(6t-3t^2)dt=0-4=-4$" "\n" r"المسافة $=4+|-4|=8\ \text{m}$ (والإزاحة صفر)",
  truth=ig(6*t-3*t**2, (t, 0, 2))-ig(6*t-3*t**2, (t, 2, 3)), tag='الحركة: المسافة الكلية من السرعة'),
Q('n5q6', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sqrt{1+\sqrt{x}}}{\sqrt{x}}', sqrt(1+sqrt(x))/sqrt(x))),
  [A(r'\frac{4}{3}(1+\sqrt{x})^{\frac{3}{2}}+C', R(4, 3)*(1+sqrt(x))**R(3, 2)), A(r'\frac{2}{3}(1+\sqrt{x})^{\frac{3}{2}}+C', R(2, 3)*(1+sqrt(x))**R(3, 2)),
   A(r'\frac{1}{3}(1+\sqrt{x})^{\frac{3}{2}}+C', R(1, 3)*(1+sqrt(x))**R(3, 2)), A(r'4\sqrt{1+\sqrt{x}}+C', 4*sqrt(1+sqrt(x)))],
  r"بالتعويض $u=1+\sqrt x \Rightarrow du=\dfrac{dx}{2\sqrt x}$: $\displaystyle2\int u^{\frac12}du=\frac43u^{\frac32}+C=\frac43(1+\sqrt x)^{\frac32}+C$",
  truth=sqrt(1+sqrt(x))/sqrt(x), tag='التكامل بالتعويض: جذور'),
Q('n5q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sin 2x}{\sqrt{1+\sin^{2}x}}', sin(2*x)/sqrt(1+sin(x)**2))),
  [A(r'2\sqrt{1+\sin^{2}x}+C', 2*sqrt(1+sin(x)**2)), A(r'\sqrt{1+\sin^{2}x}+C', sqrt(1+sin(x)**2)), A(r'\frac{1}{2}\sqrt{1+\sin^{2}x}+C', sqrt(1+sin(x)**2)/2), A(r'\ln(1+\sin^{2}x)+C', log(1+sin(x)**2))],
  r"بالتعويض $u=1+\sin^2x \Rightarrow du=2\sin x\cos x\,dx=\sin2x\,dx$: $\displaystyle\int u^{-\frac12}du=2\sqrt u+C=2\sqrt{1+\sin^2x}+C$",
  truth=sin(2*x)/sqrt(1+sin(x)**2), tag='التكامل بالتعويض: اقترانات مثلثية'),
Q('n5q8', U5[2], 'hard',
  F(r"قيمة: $\displaystyle\int_{1}^{5}«0»\,dx$ هي:", (r'\frac{x}{\sqrt{2x-1}}', x/sqrt(2*x-1))),
  [O(r'\frac{16}{3}', R(16, 3)), O(r'\frac{32}{3}', R(32, 3)), O(r'\frac{8}{3}', R(8, 3)), O(r'\frac{14}{3}', R(14, 3))],
  r"بالتعويض $u=2x-1 \Rightarrow x=\frac{u+1}{2}$ ، $dx=\frac{du}{2}$ ، والحدود $1\to9$:" "\n"
  r"$\displaystyle\frac14\int_1^9\frac{u+1}{\sqrt u}du=\frac14\left[\frac23u^{\frac32}+2u^{\frac12}\right]_1^9=\frac14\left(24-\frac83\right)=\frac{16}{3}$",
  truth=ig(x/sqrt(2*x-1), (x, 1, 5)), tag='التكامل المحدود بالتعويض'),
Q('n5q9', U5[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\tan^{3}x', tan(x)**3)),
  [A(r'\frac{\tan^{2}x}{2}+\ln|\cos x|+C', tan(x)**2/2+log(cos(x))), A(r'\frac{\tan^{2}x}{2}-\ln|\cos x|+C', tan(x)**2/2-log(cos(x))), A(r'\frac{\tan^{4}x}{4}+C', tan(x)**4/4), A(r'\frac{\tan^{2}x}{2}+\ln|\sin x|+C', tan(x)**2/2+log(sin(x)))],
  r"$\tan^3x=\tan x(\sec^2x-1)=\tan x\sec^2x-\tan x$" "\n" r"$\displaystyle\int\tan x\sec^2x\,dx=\frac{\tan^2x}{2}$ (بالتعويض $u=\tan x$) ، و $\displaystyle\int\tan x\,dx=-\ln|\cos x|$" "\n" r"الناتج: $\dfrac{\tan^2x}{2}+\ln|\cos x|+C$",
  truth=tan(x)**3, tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
Q('n5q10', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{3}-2x}{x^{2}-1}', (x**3-2*x)/(x**2-1))),
  [A(r'\frac{x^{2}}{2}-\frac{1}{2}\ln|x^{2}-1|+C', x**2/2-log(x**2-1)/2), A(r'\frac{x^{2}}{2}+\frac{1}{2}\ln|x^{2}-1|+C', x**2/2+log(x**2-1)/2),
   A(r'\frac{x^{2}}{2}-\ln|x^{2}-1|+C', x**2/2-log(x**2-1)), A(r'\frac{x^{2}}{2}-\frac{1}{2}\ln|x-1|+\frac{1}{2}\ln|x+1|+C', x**2/2-log(x-1)/2+log(x+1)/2)],
  r"بالقسمة: $x^3-2x=x(x^2-1)-x$ ، إذن المقدار $=x-\dfrac{x}{x^2-1}=x-\dfrac{1/2}{x-1}-\dfrac{1/2}{x+1}$" "\n" r"بالتكامل: $\dfrac{x^2}{2}-\frac12\ln|x-1|-\frac12\ln|x+1|+C=\dfrac{x^2}{2}-\frac12\ln|x^2-1|+C$",
  truth=(x**3-2*x)/(x**2-1), tag='التكامل بالكسور الجزئية: كسر غير فعلي'),
Q('n5q11', U5[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{2}+2}{x^{3}-x}', (x**2+2)/(x**3-x))),
  [A(r'-2\ln|x|+\frac{3}{2}\ln|x^{2}-1|+C', -2*log(x)+R(3, 2)*log(x**2-1)), A(r'2\ln|x|-\frac{3}{2}\ln|x^{2}-1|+C', 2*log(x)-R(3, 2)*log(x**2-1)),
   A(r'-2\ln|x|+3\ln|x^{2}-1|+C', -2*log(x)+3*log(x**2-1)), A(r'-2\ln|x|+\frac{3}{2}\ln|x-1|-\frac{3}{2}\ln|x+1|+C', -2*log(x)+R(3, 2)*log(x-1)-R(3, 2)*log(x+1))],
  r"$x^3-x=x(x-1)(x+1)$ ، و $\dfrac{x^2+2}{x(x-1)(x+1)}=\dfrac{A}{x}+\dfrac{B}{x-1}+\dfrac{D}{x+1}$" "\n"
  r"عند $x=0$: $2=-A \Rightarrow A=-2$ ، عند $x=1$: $3=2B \Rightarrow B=\frac32$ ، عند $x=-1$: $3=2D \Rightarrow D=\frac32$" "\n"
  r"الناتج: $-2\ln|x|+\frac32\ln|x-1|+\frac32\ln|x+1|+C=-2\ln|x|+\frac32\ln|x^2-1|+C$",
  truth=(x**2+2)/(x**3-x), tag='التكامل بالكسور الجزئية: عوامل خطية'),
Q('n5q12', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'e^{\sqrt{x}}', exp(sqrt(x)))),
  [A(r'2\sqrt{x}e^{\sqrt{x}}-2e^{\sqrt{x}}+C', 2*sqrt(x)*exp(sqrt(x))-2*exp(sqrt(x))), A(r'2\sqrt{x}e^{\sqrt{x}}+2e^{\sqrt{x}}+C', 2*sqrt(x)*exp(sqrt(x))+2*exp(sqrt(x))),
   A(r'\sqrt{x}e^{\sqrt{x}}-e^{\sqrt{x}}+C', sqrt(x)*exp(sqrt(x))-exp(sqrt(x))), A(r'2e^{\sqrt{x}}+C', 2*exp(sqrt(x)))],
  r"بالتعويض $u=\sqrt x \Rightarrow x=u^2,\ dx=2u\,du$: $\displaystyle\int2ue^udu$ ، وبالأجزاء: $2\left(ue^u-e^u\right)+C$" "\n" r"$=2\sqrt xe^{\sqrt x}-2e^{\sqrt x}+C$",
  truth=exp(sqrt(x)), tag='التكامل بالتعويض ثم بالأجزاء'),
Q('n5q13', U5[4], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'x^{2}e^{x}', x**2*exp(x))),
  [O('e-2', E-2), O('5e-2', 5*E-2), O('e', E), O('e-1', E-1)],
  r"بالأجزاء مرتين: $\displaystyle\int x^2e^xdx=x^2e^x-2\int xe^xdx=x^2e^x-2(xe^x-e^x)=e^x(x^2-2x+2)$" "\n" r"$\big[e^x(x^2-2x+2)\big]_0^1=e(1)-2=e-2$",
  truth=ig(x**2*exp(x), (x, 0, 1)), tag='التكامل المحدود بالأجزاء'),
Q('n5q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران: $f(x)=\ln x$. مساحة المنطقة المُظلَّلة المحصورة بين منحنى الاقتران $f(x)$ والمحور $x$ والمستقيم $x=e$ (بالوحدات المربعة) هي:",
  [O('1', 1), O('e-1', E-1), O('e', E), O('e-2', E-2)],
  r"المنحنى يقطع المحور $x$ عند $x=1$ ، وبالأجزاء: $\displaystyle\int_1^e\ln x\,dx=\big[x\ln x-x\big]_1^e=(e-e)-(0-1)=1$",
  truth=ig(log(x), (x, 1, E)), figure=figure('n5q14', region(log(x), 0*x, 1, E, (-0.3, 3.4), (-1.2, 1.5), [(2.95, 1.2, r'$f(x)$', '#1f5fbf')]), 3.4, 2.6), tag='المساحة تحت منحنى من الشكل'),
Q('n5q15', U5[5], 'hard',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'\sqrt{x}', sqrt(x)), (r'x^{2}', x**2)),
  [O(r'\frac{3\pi}{10}', 3*P/10), O(r'\frac{9\pi}{70}', 9*P/70), O(r'\frac{\pi}{3}', P/3), O(r'\frac{7\pi}{10}', 7*P/10)],
  r"التقاطع: $\sqrt x=x^2 \Rightarrow x=0,\ x=1$ ، و $\sqrt x\ge x^2$ في $[0,1]$ ، فبطريقة الحلقات:" "\n" r"$V=\pi\displaystyle\int_0^1\big((\sqrt x)^2-(x^2)^2\big)dx=\pi\left[\frac{x^2}{2}-\frac{x^5}{5}\right]_0^1=\frac{3\pi}{10}$",
  truth=P*ig(x-x**4, (x, 0, 1)), tag='الحجوم الدورانية: طريقة الحلقات'),
IndexQ('n5q16', U5[6], 'hard',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ هو:", (r'\frac{\sin^{2}x}{\cos^{2}y}', sin(x)**2/cos(y)**2)),
  [O(r'\frac{y}{2}+\frac{\sin 2y}{4}=\frac{x}{2}-\frac{\sin 2x}{4}+C', y/2+sin(2*y)/4-x/2+sin(2*x)/4-Cc, 'rel'), O(r'\frac{y}{2}-\frac{\sin 2y}{4}=\frac{x}{2}+\frac{\sin 2x}{4}+C', y/2-sin(2*y)/4-x/2-sin(2*x)/4-Cc, 'rel'),
   O(r'\tan y=\frac{x}{2}-\frac{\sin 2x}{4}+C', tan(y)-x/2+sin(2*x)/4-Cc, 'rel'), O(r'\frac{y}{2}+\frac{\sin 2y}{4}=\frac{x}{2}+\frac{\sin 2x}{4}+C', y/2+sin(2*y)/4-x/2-sin(2*x)/4-Cc, 'rel')],
  r"بفصل المتغيرات: $\cos^2y\,dy=\sin^2x\,dx$ ، وباستعمال $\cos^2y=\dfrac{1+\cos2y}{2}$ و $\sin^2x=\dfrac{1-\cos2x}{2}$:" "\n" r"$\dfrac y2+\dfrac{\sin2y}{4}=\dfrac x2-\dfrac{\sin2x}{4}+C$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, sin(x)**2/cos(y)**2)), tag='المعادلات التفاضلية: الحل العام'),
Q('n5q17', U6[1], 'medium',
  r"إذا كانت: $A(1,\,-2,\,3)$ ، $B(3,\,-1,\,1)$ ، وكانت النقطة $C$ تقع على $\overline{AB}$ بحيث $AC:CB=2:1$ ، فإنّ إحداثيات النقطة $C$ هي:",
  [pt_opt(R(7, 3), -R(4, 3), R(5, 3)), pt_opt(R(5, 3), -R(5, 3), R(7, 3)), pt_opt(2, -R(3, 2), 2), pt_opt(5, 0, -1)],
  r"$\overrightarrow{AB}=\langle 2,1,-2\rangle$ ، و $\overrightarrow{AC}=\frac23\overrightarrow{AB}=\left\langle \frac43,\frac23,-\frac43\right\rangle$" "\n" r"$C=A+\overrightarrow{AC}=\left(\frac73,\ -\frac43,\ \frac53\right)$",
  truth=T3(V(1, -2, 3)+R(2, 3)*(V(3, -1, 1)-V(1, -2, 3))), tag='تقسيم قطعة مستقيمة بنسبة'),
Q('n5q18', U6[1], 'medium',
  r"في المكعب الآتي، أحد رؤوسه نقطة الأصل $O$ ، وأحرفه $\overline{OP}$ و $\overline{OR}$ و $\overline{OS}$ على المحاور $x$ و $y$ و $z$ على الترتيب، وطول حرفه $4$ وحدات. متجه الوحدة في اتجاه $\overrightarrow{PV}$ هو:",
  [vec_opt(-1/sqrt(3), 1/sqrt(3), 1/sqrt(3)), vec_opt(1/sqrt(3), -1/sqrt(3), -1/sqrt(3)), vec_opt(-1, 1, 1), vec_opt(-1/sqrt(3), 1/sqrt(3), -1/sqrt(3))],
  r"من الشكل: $P(4,0,0)$ ، $V(0,4,4)$ ، إذن $\overrightarrow{PV}=\langle -4,4,4\rangle$ ، ومقداره $4\sqrt3$" "\n" r"متجه الوحدة: $\left\langle -\frac{1}{\sqrt3},\frac{1}{\sqrt3},\frac{1}{\sqrt3}\right\rangle$",
  truth=T3((V(0, 4, 4)-V(4, 0, 0))/(V(0, 4, 4)-V(4, 0, 0)).norm()), figure=figure('n5q18', fig_box(4, 4, 4), 3.8, 3.2), tag='المتجهات من شكل ثلاثي الأبعاد'),
Q('n5q19', U6[1], 'hard',
  r"في الشكل الآتي $UVWX$ متوازي أضلاع، فيه: $\overrightarrow{UV}=2\vec{\mathbf{a}}$ ، $\overrightarrow{UX}=6\vec{\mathbf{b}}$ ، والنقطة $Y$ منتصف القطر $\overline{UW}$ ، والنقطة $Z$ تقع على امتداد $\overline{XW}$ بحيث $XW:WZ=k:1$. إذا كان: $\overrightarrow{YZ}=\frac{3}{2}\vec{\mathbf{a}}+3\vec{\mathbf{b}}$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('4', 4), O('2', 2), O(r'\frac{1}{4}', R(1, 4)), O('3', 3)],
  r"$\overrightarrow{UY}=\frac12(2\vec{\mathbf{a}}+6\vec{\mathbf{b}})=\vec{\mathbf{a}}+3\vec{\mathbf{b}}$ ، و $\overrightarrow{XW}=2\vec{\mathbf{a}}$ ، فـ $\overrightarrow{WZ}=\frac{2}{k}\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{UZ}=6\vec{\mathbf{b}}+2\vec{\mathbf{a}}+\frac2k\vec{\mathbf{a}}$ ، و $\overrightarrow{YZ}=\overrightarrow{UZ}-\overrightarrow{UY}=\left(1+\frac2k\right)\vec{\mathbf{a}}+3\vec{\mathbf{b}}$" "\n" r"$1+\frac2k=\frac32 \Rightarrow k=4$",
  truth=lambda: solve((6*vb+2*va+2*va/kk-(va+3*vb)-(R(3, 2)*va+3*vb)).coeff(va), kk)[0],
  figure=figure('n5q19', fig_poly(pg5, [('V', 'W'), ('X', 'W'), ('W', 'Z')], [('U', 'V', r'$2\vec{\mathbf{a}}$', (0, -0.5)), ('U', 'X', r'$6\vec{\mathbf{b}}$', (-0.85, 0.05))],
                                  {'U': (-0.35, -0.3), 'V': (0.05, -0.4), 'W': (-0.1, 0.18), 'X': (-0.2, 0.18), 'Y': (0.05, -0.38), 'Z': (0.1, 0.15)}, extra_dashed=[('U', 'W'), ('Y', 'Z')]), 4.0, 2.2),
  tag='المتجهات في الأشكال الهندسية والنسبة'),
Q('n5q20', U6[3], 'medium',
  r"إذا كان: $\vec{\mathbf{u}}=\langle 2,\,-1,\,3\rangle$ ، $\vec{\mathbf{v}}=\langle 1,\,1,\,0\rangle$ ، فإنّ قيمة الثابت $k$ التي تجعل المتجه $\vec{\mathbf{u}}+k\vec{\mathbf{v}}$ عموديًّا على المتجه $\vec{\mathbf{v}}$ هي:",
  [O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2)), O('-1', -1), O('2', 2)],
  r"$(\vec{\mathbf{u}}+k\vec{\mathbf{v}})\cdot\vec{\mathbf{v}}=\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}+k|\vec{\mathbf{v}}|^2=(2-1+0)+2k=0 \Rightarrow k=-\frac12$",
  truth=lambda: solve((V(2, -1, 3)+kk*V(1, 1, 0)).dot(V(1, 1, 0)), kk)[0], tag='التعامد وإيجاد ثوابت'),
Q('n5q21', U6[2], 'medium',
  r"العلاقة بين المستقيمين: $\vec{\mathbf{r}}_1=\langle 1,0,1\rangle+t\langle 1,1,0\rangle$ و $\vec{\mathbf{r}}_2=\langle 2,3,1\rangle+s\langle 0,1,0\rangle$ هي أنّهما:",
  rel_opts('intersect'),
  r"متجها الاتجاه غير متوازيين. نساوي الإحداثيات: $1+t=2$ ، $t=3+s$ ، $1=1$" "\n" r"من الأولى $t=1$ ، ومن الثانية $s=-2$ ، والثالثة متحققة، إذن المستقيمان متقاطعان في النقطة $(2,1,1)$",
  truth=classify((1, 0, 1), (1, 1, 0), (2, 3, 1), (0, 1, 0)), tag='العلاقة بين مستقيمين'),
Q('n5q22', U6[2], 'hard',
  r"بُعد النقطة $P(5,\,2,\,3)$ عن المستقيم: $\vec{\mathbf{r}}=\langle 2,\,-1,\,0\rangle+t\langle 1,\,-1,\,1\rangle$ هو:",
  [O(r'2\sqrt{6}', 2*sqrt(6)), O(r'\sqrt{6}', sqrt(6)), O('24', 24), O(r'\sqrt{29}', sqrt(29))],
  r"نفرض مسقط العمود $Q=(2+t,\ -1-t,\ t)$ ، و $\overrightarrow{PQ}=\langle t-3,\ -3-t,\ t-3\rangle\perp\langle 1,-1,1\rangle$:" "\n"
  r"$(t-3)+(3+t)+(t-3)=0 \Rightarrow t=1$ ، فـ $Q=(3,-2,1)$ ، والبعد $|\overrightarrow{PQ}|=|\langle -2,-4,-2\rangle|=\sqrt{24}=2\sqrt6$",
  truth=lambda: (lambda tt: (V(2, -1, 0)+tt*V(1, -1, 1)-V(5, 2, 3)).norm())(solve((V(2, -1, 0)+t*V(1, -1, 1)-V(5, 2, 3)).dot(V(1, -1, 1)), t)[0]), tag='بعد نقطة عن مستقيم'),
Q('n5q23', U6[3], 'hard',
  r"النقطة $D$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle 5,\,1,\,0\rangle+t\langle 1,\,1,\,2\rangle$ بحيث يكون $\overrightarrow{OD}$ عموديًّا على المستقيم، حيث $O$ نقطة الأصل. إحداثيات النقطة $D$ هي:",
  [pt_opt(4, 0, -2), pt_opt(6, 2, 2), pt_opt(5, 1, 0), pt_opt(3, -1, -4)],
  r"$\overrightarrow{OD}=\langle 5+t,\ 1+t,\ 2t\rangle$ ، و $\overrightarrow{OD}\cdot\langle 1,1,2\rangle=0$:" "\n" r"$5+t+1+t+4t=0 \Rightarrow 6t=-6 \Rightarrow t=-1$ ، إذن $D=(4,0,-2)$",
  truth=lambda: (lambda tt: T3(V(5, 1, 0)+tt*V(1, 1, 2)))(solve((V(5, 1, 0)+t*V(1, 1, 2)).dot(V(1, 1, 2)), t)[0]), tag='مسقط العمود من نقطة على مستقيم'),
Q('n5q24', U6[3], 'hard',
  r"إذا كان: $|\vec{\mathbf{a}}|=2$ ، $|\vec{\mathbf{b}}|=4$ ، $|\vec{\mathbf{a}}+\vec{\mathbf{b}}|=2\sqrt{7}$ ، فإنّ قياس الزاوية بين المتجهين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [O(r'\frac{\pi}{3}', P/3), O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{\pi}{4}', P/4)],
  r"$|\vec{\mathbf{a}}+\vec{\mathbf{b}}|^2=|\vec{\mathbf{a}}|^2+2\,\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}+|\vec{\mathbf{b}}|^2 \Rightarrow 28=4+2\,\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}+16 \Rightarrow \vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=4$" "\n" r"$\cos\theta=\dfrac{4}{2\times4}=\dfrac12 \Rightarrow \theta=\dfrac{\pi}{3}$",
  truth=acos((28-4-16)/R(2)/(2*4)), tag='خصائص الضرب القياسي'),
Q('n5q25', U6[3], 'hard',
  r"إذا كان قياس الزاوية بين المتجهين: $\langle 1,\,k,\,1\rangle$ و $\langle 1,\,0,\,1\rangle$ هو $\dfrac{\pi}{4}$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:",
  [O(r'\sqrt{2}', sqrt(2)), O('2', 2), O(r'\sqrt{6}', sqrt(6)), O('1', 1)],
  r"$\cos\frac{\pi}{4}=\dfrac{2}{\sqrt{2+k^2}\cdot\sqrt2}=\dfrac{1}{\sqrt2} \Rightarrow \sqrt{2+k^2}=2 \Rightarrow k^2=2 \Rightarrow k=\sqrt2$",
  truth=lambda: [r_ for r_ in solve(2/(sqrt(2+kk**2)*sqrt(2))-1/sqrt(2), kk) if r_ > 0][0], tag='الزاوية بين متجهين: إيجاد ثابت'),
Q('n5q26', U7[1], 'hard',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $\dfrac{P(X=3)}{P(X=6)}=\dfrac{64}{27}$ ، فإنّ التوقّع $E(X)$ يساوي:",
  [O('4', 4), O(r'\frac{4}{3}', R(4, 3)), O(r'\frac{1}{4}', R(1, 4)), O(r'\frac{3}{4}', R(3, 4))],
  r"$\dfrac{P(X=3)}{P(X=6)}=\dfrac{(1-p)^2p}{(1-p)^5p}=\dfrac{1}{(1-p)^3}=\dfrac{64}{27} \Rightarrow 1-p=\frac34 \Rightarrow p=\frac14$" "\n" r"$E(X)=\dfrac1p=4$",
  truth=lambda: 1/[r_ for r_ in solve(geo(p, 3)/geo(p, 6)-R(64, 27), p) if r_.is_real and 0 < r_ < 1][0], tag='التوزيع الهندسي: نسبة احتمالين والتوقع'),
Q('n5q27', U7[1], 'hard',
  r"إذا كان: $X\sim B(5,\,p)$ ، حيث $0<p<1$ ، وكان: $P(X=1)=P(X=2)$ ، فإنّ تباين المتغيّر العشوائي $X$ هو:",
  [O(r'\frac{10}{9}', R(10, 9)), O(r'\frac{5}{3}', R(5, 3)), O(r'\frac{5}{9}', R(5, 9)), O(r'\frac{2}{3}', R(2, 3))],
  r"$\binom51p(1-p)^4=\binom52p^2(1-p)^3 \Rightarrow 5(1-p)=10p \Rightarrow p=\frac13$" "\n" r"$\text{Var}(X)=np(1-p)=5\times\frac13\times\frac23=\frac{10}{9}$",
  truth=lambda: (lambda pp: 5*pp*(1-pp))([r_ for r_ in solve(binom(5, p, 1)-binom(5, p, 2), p) if 0 < r_ < 1][0]), tag='توزيع ذي الحدين: معادلة احتمالين والتباين'),
Q('n5q28', U7[2], 'hard',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{20}<Z<\dfrac{k}{20}\right)=0.1586$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('4', 4), O('2', 2), D('0.2'), O('5', 5)],
  r"$2P\left(Z<\frac{k}{20}\right)-1=0.1586 \Rightarrow P\left(Z<\frac{k}{20}\right)=0.5793$" "\n" r"من الجدول: $\frac{k}{20}=0.2 \Rightarrow k=4$",
  truth=lambda: [zz*20 for zz in (R(1, 10), R(1, 5), R(1, 4), R(7, 4)) if 2*Ph(zz)-1 == R('0.1586')][0], tag='التوزيع الطبيعي: فترة متماثلة وإيجاد ثابت',
  lead=ztable_lead([28, 29, 30], 0.1, 0.2, 0.25, 1.75), group=3),
Q('n5q29', U7[2], 'hard',
  r"تتوزّع أطوال قطع معدنية توزيعًا طبيعيًّا: $X\sim N(500,\,\sigma^{2})$ بالمليمتر. إذا كانت أطوال $4.01\%$ من القطع تزيد على $535\ \text{mm}$ ، فإنّ قيمة الانحراف المعياري $\sigma$ هي:",
  [D('20', 'mm'), D('35', 'mm'), D('400', 'mm'), D('1.75', 'mm')],
  r"$P(X>535)=0.0401 \Rightarrow P(X<535)=0.9599=P(Z<1.75)$" "\n" r"$\dfrac{535-500}{\sigma}=1.75 \Rightarrow \sigma=20\ \text{mm}$",
  truth=lambda: [35/zz for zz in (R(1, 10), R(1, 5), R(1, 4), R(7, 4)) if 1-Ph(zz) == R('0.0401')][0], tag='التوزيع الطبيعي: إيجاد الانحراف المعياري'),
Q('n5q30', U7[2], 'hard',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، فإنّ احتمال أن تقع قيمة $Z$ خارج الفترة $(-0.25,\,1.75)$ يساوي:",
  [D('0.4414'), D('0.5586'), D('0.3612'), D('0.4599')],
  r"$P(Z<-0.25)+P(Z>1.75)=(1-0.5987)+(1-0.9599)=0.4013+0.0401=0.4414$",
  truth=Ph(-R(1, 4))+1-Ph(R(7, 4)), tag='التوزيع الطبيعي: حساب احتمال'),
]

papers = [dict(id='s2-m1', model=1, title='النموذج (1)', minutes=90, questions=P1),
          dict(id='s2-m2', model=2, title='النموذج (2)', minutes=90, questions=P2),
          dict(id='s2-m3', model=3, title='النموذج (3)', minutes=90, questions=P3),
          dict(id='s2-m4', model=4, title='النموذج (4)', minutes=90, questions=P4),
          dict(id='s2-m5', model=5, title='النموذج (5)', minutes=90, questions=P5)]

SKILLS = {
  'تكامل الاقترانات الخاصة': ['تكامل الاقترانات المثلثية', 'تكامل الاقتران الأسي', 'تكامل باستعمال متطابقات ضعف الزاوية', 'تكامل باستعمال تقليص القوة'],
  'التكامل المحدود وإيجاد الثوابت': ['التكامل المحدود: إيجاد ثابت', 'التكامل المحدود لاقترانات مثلثية'],
  'الاقتران من مشتقته (الشروط الأولية)': ['إيجاد الاقتران بمعلومية مشتقته ونقطة', 'إيجاد الاقتران من مشتقته الثانية'],
  'تطبيقات الحركة': ['الحركة: الموقع من سرعة متعددة القاعدة', 'الحركة: المسافة الكلية من السرعة', 'الحركة من منحنى السرعة–الزمن'],
  'التكامل بالتعويض': ['التكامل بالتعويض', 'التكامل بالتعويض: اقترانات مثلثية', 'التكامل بالتعويض: لوغاريتمات', 'التكامل بالتعويض: جذور', 'التكامل بالتعويض: قوى مقدار خطي', 'التكامل بالتعويض: قوى الاقترانات المثلثية', 'التكامل المحدود بالتعويض'],
  'التكامل بالكسور الجزئية': ['التكامل بالكسور الجزئية: عوامل خطية', 'التكامل بالكسور الجزئية: عامل مكرر', 'التكامل بالكسور الجزئية: عامل تربيعي', 'التكامل بالكسور الجزئية: كسر غير فعلي', 'التكامل المحدود بالكسور الجزئية'],
  'التكامل بالأجزاء': ['التكامل بالأجزاء', 'التكامل بالأجزاء: تكرار التكامل', 'التكامل بالتعويض ثم بالأجزاء', 'التكامل المحدود بالأجزاء'],
  'المساحات والحجوم': ['المساحة بين منحنيين', 'المساحة بين منحنيين متقاطعين', 'المساحة تحت منحنى من الشكل', 'المساحة: إيجاد ثابت', 'الحجوم الدورانية من الشكل', 'الحجوم الدورانية: طريقة الحلقات'],
  'المعادلات التفاضلية': ['المعادلات التفاضلية: الحل العام', 'المعادلات التفاضلية: الحل الخاص'],
  'المتجهات: المقدار والوحدة والنقاط': ['متجه الوحدة', 'متجه الوحدة (نص مشترك)', 'متجه بمقدار معلوم في اتجاه معلوم', 'المتجهات: المقدار وإيجاد ثابت', 'المتجهات: المقدار وإيجاد ثابت (نص مشترك)', 'المتجهات: نقطة ومتجه موقع', 'المتجهات: نقطة ومتجه موقع (نص مشترك)', 'تقسيم قطعة مستقيمة بنسبة', 'متوازي الأضلاع في الفضاء'],
  'التوازي والاستقامة': ['توازي المتجهات وإيجاد ثابت', 'النقاط على استقامة واحدة'],
  'المتجهات في الأشكال': ['المتجهات في الأشكال الهندسية والنسبة', 'المتجهات من شكل ثلاثي الأبعاد'],
  'المستقيمات في الفضاء': ['معادلة المستقيم في الفضاء', 'معادلة مستقيم يوازي مستقيمًا معلومًا', 'نقطة على مستقيم وإيجاد ثابت', 'تقاطع مستقيم مع مستوى إحداثي', 'العلاقة بين مستقيمين', 'نقطة تقاطع مستقيمين', 'توازي مستقيمين وإيجاد ثوابت'],
  'الضرب القياسي والزوايا': ['الزاوية بين متجهين', 'الزاوية بين متجهين: إيجاد ثابت', 'الزاوية بين متجهين: زاوية في مثلث', 'الزاوية بين مستقيمين', 'الضرب القياسي ومتجهات بين نقاط', 'خصائص الضرب القياسي', 'مساحة مثلث باستعمال الضرب القياسي'],
  'التعامد والمسقط والبعد': ['التعامد وإيجاد ثوابت', 'التعامد وإيجاد ثوابت (نص مشترك)', 'مسقط العمود من نقطة على مستقيم', 'بعد نقطة عن مستقيم'],
  'التوزيع الهندسي وتوزيع ذي الحدين': ['التوزيع الهندسي: التوقع والاحتمال', 'التوزيع الهندسي: احتمال «أكبر من»', 'التوزيع الهندسي: نسبة احتمالين والتوقع', 'توزيع ذي الحدين: احتمال «على الأقل»', 'توزيع ذي الحدين: احتمال «على الأكثر»', 'توزيع ذي الحدين: التوقع والتباين', 'توزيع ذي الحدين: معادلة احتمالين والتباين'],
  'التوزيع الطبيعي': ['التوزيع الطبيعي: حساب احتمال', 'التوزيع الطبيعي: مساحة من الشكل', 'التوزيع الطبيعي: فترة متماثلة وإيجاد ثابت', 'التوزيع الطبيعي: إيجاد قيمة من احتمال', 'التوزيع الطبيعي: إيجاد الانحراف المعياري', 'التوزيع الطبيعي: إيجاد الوسط الحسابي', 'التوزيع الطبيعي: إيجاد الوسط والانحراف'],
}
PATTERN_TO_SKILL = {pt: sk for sk, pts in SKILLS.items() for pt in pts}
assert len(PATTERN_TO_SKILL) == sum(len(v_) for v_ in SKILLS.values())
for paper in papers:
    for q_ in paper['questions']:
        assert q_.tag in PATTERN_TO_SKILL, f'{q_.id}: pattern {q_.tag} not grouped'
        q_.pattern, q_.tag = q_.tag, PATTERN_TO_SKILL[q_.tag]

if __name__ == '__main__':
    meta = dict(id='s2', title='امتحانات تجريبية — الفصل الثاني', subtitle='الوحدات 5–7 · 30 فقرة · 90 دقيقة')
    build_mock(meta, papers, 's2', seed=2027)
