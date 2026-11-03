"""Semester-2 mock papers 6-10 (n6q1..n10q30), same layout as papers 1-5: U5 (integration) items 1-16,
U6 (vectors) items 17-25, U7 (statistics) items 26-30, lesson by lesson. Every item is modelled on a named official
ministry item (the comment above each Q gives it: 2026 = paper of 2 July 2026, gen 2008, items 26-50; 2026r = 2026
repeaters paper 2; 2023, 2024, 2025 = summer paper 2 and 2023s, 2024s, 2025s = supplementary paper 2): same skill,
same stem structure, same kind of function and numbers, same option grid, never harder -- new function, numbers or
context. The pattern of each slot was chosen so that the five papers spread the ideas of the 2023-2026 semester-2
papers (previous-ministry/ANALYSIS.md, section 5); section 9 there maps every item to its model."""
from s2_helpers import *
from u5_helpers import vt_graph as vt5, region as region5
from u6_helpers import iso_box, pair_opt, poly_fig, plane_pts, sign_panels, solve_k, ijk, ijk_opt
from u7_helpers import emp_fig, emp, ztable, zclosest, spinner_fig
import numpy as np

# ================================================================== PAPER 6
ap6 = Symbol('a', positive=True)


def area_kx6(f_, lo, hi, xlim, ylim, ticks, label):
    """2026r #6 drawing: a decreasing curve in the first quadrant (arrowheads at both ends), the region under it from
    x = lo to x = hi shaded, only the x marks in ticks ({value: label}) shown. hi is drawn schematically (its label is
    the letter a), so the figure does not give the answer away."""
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        ff = lambdify(x, f_, 'numpy')
        x_top = float(solve(f_ - (ylim[1] - 0.4), x)[0])
        xs = np.linspace(x_top, xlim[1] - 0.25, 400)
        ax.plot(xs, ff(xs), color='#1f5fbf', lw=1.8)
        for i_, j_ in ((5, 0), (-6, -1)):
            ax.annotate('', xy=(xs[j_], ff(xs[j_])), xytext=(xs[i_], ff(xs[i_])),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.4, mutation_scale=12))
        xr = np.linspace(lo, hi, 200)
        ax.fill_between(xr, ff(xr), 0*xr, color='#9cc3ef', alpha=0.85)
        ax.plot([hi, hi], [0, float(ff(hi))], color='#444', lw=1)
        ax.plot([lo, lo], [0, float(ff(lo))], color='#444', lw=1)
        ax.set_xticks(list(ticks)); ax.set_xticklabels(list(ticks.values()))
        ax.set_yticks([])
        ax.text(*label, color='#1f5fbf', fontsize=12)
    return draw


def loop_fig6(pts, arrows):
    """2023s #16 drawing: three arrows head to tail around a triangle, each labelled with its vector (no vertex
    letters, no coordinates). arrows: [(start, end, label, (dx, dy))] with start/end keys of pts."""
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        for s_, e_, lab, off in arrows:
            (x1, y1), (x2, y2) = pts[s_], pts[e_]
            ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.8, mutation_scale=18, shrinkA=0, shrinkB=0))
            ax.text((x1 + x2)/2 + off[0], (y1 + y2)/2 + off[1], lab, fontsize=15, color='#1f5fbf', ha='center', va='center')
        xs = [q_[0] for q_ in pts.values()]; ys = [q_[1] for q_ in pts.values()]
        ax.set_xlim(min(xs) - 0.9, max(xs) + 0.9); ax.set_ylim(min(ys) - 0.8, max(ys) + 0.5)
    return draw


def named_line6(nm, p_, d_):
    """a line option r = p + t d written with its own vector name (the ministry names the four options r, m, n, p)"""
    return O(r'\vec{\mathbf{' + nm + r'}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')


vt6 = [(0, 2), (1, 0), (2, -2), (3, 0), (4, 2), (6, 2)]
tri6 = {'P': (0, 0), 'Q': (5, 0), 'S': (2, 3)}          # u = PQ, v = QS, w = SP: a closed loop
u6v, v6v, w6v = (Matrix(tri6['Q']) - Matrix(tri6['P']), Matrix(tri6['S']) - Matrix(tri6['Q']), Matrix(tri6['P']) - Matrix(tri6['S']))

P6 = [
# ---------------- unit 5
# 2026 #26: integral of a trig quotient of x/n; options = -ln|cos| (tan) vs ln|sin| (cot) x coefficient 3 (divided by the inner 1/3) vs 1/3 (multiplied)
Q('n6q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\tan\frac{x}{3}', tan(x/3))),
  [A(r'-3\ln|\cos\frac{x}{3}|+C', -3*log(cos(x/3))), A(r'3\ln|\sin\frac{x}{3}|+C', 3*log(sin(x/3))),
   A(r'-\frac{1}{3}\ln|\cos\frac{x}{3}|+C', -log(cos(x/3))/3), A(r'\frac{1}{3}\ln|\sin\frac{x}{3}|+C', log(sin(x/3))/3)],
  r"$\tan\frac x3=\dfrac{\sin\frac x3}{\cos\frac x3}$ ، والبسط يساوي $-3$ مضروبًا في مشتقة المقام، إذن $\displaystyle\int\tan\frac x3\,dx=-3\ln\left|\cos\frac x3\right|+C$",
  truth=tan(x/3), tag='تكامل الاقترانات المثلثية'),
# 2023s #1: definite integral of a^x on [-1, 1]; options = divided by ln a or not x numerator a - 1/a (both limits) vs 1 - 1/a (a^0 used for a^1)
Q('n6q2', U5[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{-1}^{1}«0»\,dx$ تساوي:", (r'5^{x}', 5**x)),
  [O(r'\frac{24}{5\ln 5}', R(24, 5)/log(5)), O(r'\frac{4}{5\ln 5}', R(4, 5)/log(5)), O(r'\frac{24}{5}', R(24, 5)), O(r'\frac{4}{5}', R(4, 5))],
  r"$\displaystyle\int_{-1}^{1}5^xdx=\left[\frac{5^x}{\ln5}\right]_{-1}^{1}=\frac{5-\frac15}{\ln5}=\frac{24}{5\ln5}$",
  truth=ig(5**x, (x, -1, 1)), tag='التكامل المحدود للاقتران الأسي'),
# 2026 #28: a squared trig function over an interval = a pi (power reduction); options = +-1/4, +-1/2 (the 1/2 of the identity dropped; sign)
Q('n6q3', U5[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{\frac{\pi}{2}}«0»\,dx=a\pi$ ، فإنّ قيمة الثابت $a$ هي:", (r'\cos^{2}2x', cos(2*x)**2)),
  [O(r'\frac{1}{4}', R(1, 4)), O(r'-\frac{1}{4}', -R(1, 4)), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2))],
  r"$\cos^22x=\dfrac{1+\cos4x}{2}$ ، و $\displaystyle\int_0^{\pi/2}\frac{1+\cos4x}{2}dx=\left[\frac x2+\frac{\sin4x}{8}\right]_0^{\pi/2}=\frac{\pi}{4}$ ، إذن $a=\frac14$",
  truth=ig(cos(2*x)**2, (x, 0, pi/2))/pi, tag='تكامل باستعمال تقليص القوة'),
# 2023 #5: f' = (cubic + constant)/x split term by term, and f(1) -> f; options = the x^2 term left un-integrated, sign of the constant, sign of the ln term
IndexQ('n6q4', U5[1], 'medium',
  F(r"إذا كان: $f'(x)=«0»$ ، وكان: $f(1)=7$ ، فإنّ قاعدة الاقتران $f$ هي:", (r'\frac{6x^{3}+2}{x}', (6*x**3+2)/x)),
  [O(r'f(x)=2x^{3}+2\ln|x|+5', 2*x**3+2*log(x)+5, 'eq'), O(r'f(x)=6x^{2}+2\ln|x|+5', 6*x**2+2*log(x)+5, 'eq'),
   O(r'f(x)=2x^{3}+2\ln|x|-5', 2*x**3+2*log(x)-5, 'eq'), O(r'f(x)=2x^{3}-2\ln|x|+5', 2*x**3-2*log(x)+5, 'eq')],
  r"$f'(x)=6x^2+\dfrac2x$ ، إذن $f(x)=2x^3+2\ln|x|+C$ ، و $f(1)=2+0+C=7 \Rightarrow C=5$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, (6*x**3+2)/x, 1, 7)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
# 2026 #30: total distance for v = k trig(t) over two equal arches (one interior zero, no chain factor, as in the model);
# options = a list from nameable slips: the distance, the displacement 0, one arch only (also the amplitude), doubled
Q('n6q5', U5[1], 'medium',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ سرعته بالمتر لكل ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلية بالأمتار التي قطعها الجُسيم في الفترة $[0,\,\pi]$ هي:", (r'3\cos t', 3*cos(t))),
  [O('6', 6), O('0', 0), O('3', 3), O('12', 12)],
  r"$v=0$ عند $t=\frac{\pi}{2}$ ، و $\displaystyle\int_0^{\pi/2}3\cos t\,dt=\big[3\sin t\big]_0^{\pi/2}=3$ ، $\displaystyle\int_{\pi/2}^{\pi}3\cos t\,dt=0-3=-3$" "\n"
  r"المسافة $=3+|-3|=6\ \text{m}$",
  truth=ig(3*cos(t), (t, 0, pi/2)) + Abs(ig(3*cos(t), (t, pi/2, pi))), tag='الحركة: المسافة الكلية من السرعة'),
# 2026 #31: x^n (1 + c/x)^n = (x + c)^n, then the power rule; options = (x+c)^(n+1)/(n+1), (x+c)^n/n (power not raised),
# the bracket's power ignored (x^n + c x^(n-1) integrated) with either sign
Q('n6q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{3}\left(1+\frac{2}{x}\right)^{3}', x**3*(1+2/x)**3)),
  [A(r'\frac{1}{4}(x+2)^{4}+C', (x+2)**4/4), A(r'\frac{1}{3}(x+2)^{3}+C', (x+2)**3/3),
   A(r'\frac{1}{4}x^{4}+\frac{2}{3}x^{3}+C', x**4/4+R(2, 3)*x**3), A(r'\frac{1}{4}x^{4}-\frac{2}{3}x^{3}+C', x**4/4-R(2, 3)*x**3)],
  r"$x^3\left(1+\frac2x\right)^3=\left(x\left(1+\frac2x\right)\right)^3=(x+2)^3$ ، إذن التكامل $=\frac14(x+2)^4+C$",
  truth=x**3*(1+2/x)**3, tag='التكامل بالتعويض بعد التبسيط'),
# 2026r #10: an odd power of cos times an even power of sin (u = sin x); options = coefficients matched to the powers or swapped x sign of the second term
Q('n6q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos^{3}x\,\sin^{4}x', cos(x)**3*sin(x)**4)),
  [A(r'\frac{1}{5}\sin^{5}x-\frac{1}{7}\sin^{7}x+C', sin(x)**5/5-sin(x)**7/7), A(r'\frac{1}{7}\sin^{5}x-\frac{1}{5}\sin^{7}x+C', sin(x)**5/7-sin(x)**7/5),
   A(r'\frac{1}{5}\sin^{5}x+\frac{1}{7}\sin^{7}x+C', sin(x)**5/5+sin(x)**7/7), A(r'\frac{1}{7}\sin^{5}x+\frac{1}{5}\sin^{7}x+C', sin(x)**5/7+sin(x)**7/5)],
  r"$\cos^3x\sin^4x=(1-\sin^2x)\sin^4x\cos x$ ، وبالتعويض $u=\sin x \Rightarrow du=\cos x\,dx$:" "\n"
  r"$\displaystyle\int(u^4-u^6)du=\frac{u^5}{5}-\frac{u^7}{7}+C=\frac15\sin^5x-\frac17\sin^7x+C$",
  truth=cos(x)**3*sin(x)**4, tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
# 2023 #7: (ln x)^n / x by u = ln x; options = new power n + 1 vs n + 2 x (ln x)^k vs ln x^k
Q('n6q8', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ هو:", (r'\frac{(\ln x)^{6}}{x}', log(x)**6/x)),
  [A(r'\frac{1}{7}(\ln x)^{7}+C', log(x)**7/7), A(r'\frac{1}{8}(\ln x)^{8}+C', log(x)**8/8),
   A(r'\frac{1}{7}\ln x^{7}+C', log(x**7)/7), A(r'\frac{1}{8}\ln x^{8}+C', log(x**8)/8)],
  r"بالتعويض $u=\ln x \Rightarrow du=\dfrac{dx}{x}$: $\displaystyle\int u^6du=\frac{u^7}{7}+C=\frac17(\ln x)^7+C$",
  truth=log(x)**6/x, tag='التكامل بالتعويض: لوغاريتمات'),
# 2026r #9: definite integral of x times a cube root of (x + c)^2 by u = x + c; options = sign x x = u - c (a difference) vs u + c (a sum)
Q('n6q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{-3}^{-2}«0»\,dx$ هي:", (r'x\sqrt[3]{(x+3)^{2}}', x*((x+3)**2)**R(1, 3))),
  [O(r'-\frac{57}{40}', -R(57, 40)), O(r'\frac{57}{40}', R(57, 40)), O(r'\frac{87}{40}', R(87, 40)), O(r'-\frac{87}{40}', -R(87, 40))],
  r"بالتعويض $u=x+3$ ، $x=u-3$ ، والحدود: $x=-3\to u=0$ ، $x=-2\to u=1$" "\n"
  r"$\displaystyle\int_0^1(u-3)u^{\frac23}du=\left[\frac38u^{\frac83}-\frac95u^{\frac53}\right]_0^1=\frac38-\frac95=-\frac{57}{40}$",
  truth=Integral(x*(x+3)**R(2, 3), (x, -3, -2)).evalf(40), tag='التكامل المحدود بالتعويض'),
# 2026 #33: (x^2 + a)/(x^3 + bx) = A/x + Bx/(x^2 + b), Bx a multiple of the derivative 2x as in the model (so no 1/2 appears);
# options = which ln carries which coefficient x sign of the second term
Q('n6q10', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{2}+15}{x^{3}+3x}', (x**2+15)/(x**3+3*x))),
  [A(r'5\ln|x|-2\ln(x^{2}+3)+C', 5*log(x)-2*log(x**2+3)), A(r'5\ln|x|+2\ln(x^{2}+3)+C', 5*log(x)+2*log(x**2+3)),
   A(r'2\ln|x|-5\ln(x^{2}+3)+C', 2*log(x)-5*log(x**2+3)), A(r'2\ln|x|+5\ln(x^{2}+3)+C', 2*log(x)+5*log(x**2+3))],
  r"$\dfrac{x^2+15}{x(x^2+3)}=\dfrac{A}{x}+\dfrac{Bx+D}{x^2+3}$ ، عند $x=0$: $15=3A \Rightarrow A=5$ ، ومعامل $x^2$: $1=A+B \Rightarrow B=-4$ ، و $D=0$" "\n"
  r"$\displaystyle\int\left(\frac5x-\frac{4x}{x^2+3}\right)dx=5\ln|x|-2\ln(x^2+3)+C$",
  truth=(x**2+15)/(x**3+3*x), tag='التكامل بالكسور الجزئية: عامل تربيعي'),
# 2026r #3: improper fraction, a cubic without an x^2 term over a linear factor, quotient x^2 - cx and remainder 1 (as in the model);
# options = power rule divided or not x sign of the quotient's second term
Q('n6q11', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{3}-4x+1}{x+2}', (x**3-4*x+1)/(x+2))),
  [A(r'\frac{1}{3}x^{3}-x^{2}+\ln|x+2|+C', x**3/3-x**2+log(x+2)), A(r'\frac{1}{3}x^{3}+x^{2}+\ln|x+2|+C', x**3/3+x**2+log(x+2)),
   A(r'x^{3}-2x^{2}+\ln|x+2|+C', x**3-2*x**2+log(x+2)), A(r'x^{3}+2x^{2}+\ln|x+2|+C', x**3+2*x**2+log(x+2))],
  r"بالقسمة: $x^3-4x+1=(x+2)(x^2-2x)+1$ ، إذن المقدار $=x^2-2x+\dfrac{1}{x+2}$" "\n"
  r"بالتكامل: $\dfrac13x^3-x^2+\ln|x+2|+C$",
  truth=(x**3-4*x+1)/(x+2), tag='التكامل بالكسور الجزئية: كسر غير فعلي'),
# 2026 #34: a trig function of sqrt(x): u = sqrt(x), then by parts; options = signs of the two terms
Q('n6q12', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\sin\sqrt{x}', sin(sqrt(x)))),
  [A(r'-2\sqrt{x}\cos\sqrt{x}+2\sin\sqrt{x}+C', -2*sqrt(x)*cos(sqrt(x))+2*sin(sqrt(x))), A(r'2\sqrt{x}\cos\sqrt{x}+2\sin\sqrt{x}+C', 2*sqrt(x)*cos(sqrt(x))+2*sin(sqrt(x))),
   A(r'-2\sqrt{x}\cos\sqrt{x}-2\sin\sqrt{x}+C', -2*sqrt(x)*cos(sqrt(x))-2*sin(sqrt(x))), A(r'2\sqrt{x}\cos\sqrt{x}-2\sin\sqrt{x}+C', 2*sqrt(x)*cos(sqrt(x))-2*sin(sqrt(x)))],
  r"بالتعويض $u=\sqrt x \Rightarrow x=u^2$ ، $dx=2u\,du$: $\displaystyle\int2u\sin u\,du$" "\n"
  r"وبالأجزاء: $2\left(-u\cos u+\int\cos u\,du\right)=-2u\cos u+2\sin u+C=-2\sqrt x\cos\sqrt x+2\sin\sqrt x+C$",
  truth=sin(sqrt(x)), tag='التكامل بالتعويض ثم بالأجزاء'),
# 2023s #11: integral of x f'(x) on [0, 1] from given values, by parts; options = the right value, the boundary term only,
# f(1) - f(0) (taken as the integral of f'), f(1) - f(0) - the given integral
Q('n6q13', U5[4], 'medium',
  r"إذا كان: $\displaystyle\int_{0}^{1}f(x)\,dx=4$ ، $f(1)=9$ ، $f(0)=2$ ، فإنّ قيمة $\displaystyle\int_{0}^{1}x\,f'(x)\,dx$ تساوي:",
  [O('5', 5), O('9', 9), O('7', 7), O('3', 3)],
  r"بالأجزاء: $u=x$ ، $dv=f'(x)dx \Rightarrow v=f(x)$: $\displaystyle\int_0^1xf'(x)dx=\big[xf(x)\big]_0^1-\int_0^1f(x)dx=(1\times9-0)-4=5$",
  # an explicit f with f(0) = 2, f(1) = 9 and integral 4 on [0, 1]
  truth=ig(x*diff(2-2*x+9*x**2, x), (x, 0, 1)), tag='التكامل بالأجزاء: من قيم معطاة'),
# 2026 #35 / 2026r #6: shaded area under k/x from x = 1 to x = a equals a value -> a = e^n (figure as 2026r #6);
# options = powers of e: the right one, k not divided (e^12), the coefficient taken as the exponent (e^3), ln 1 taken as 1 (e^5)
Q('n6q14', U5[5], 'easy',
  F(r"يُبيّن التمثيل البياني الآتي منحنى الاقتران: $f(x)=«0»\ ,\ x\neq 0$. إذا كانت مساحة المنطقة المُظلَّلة هي $12$ وحدة مربعة، فإنّ قيمة الثابت $a$ هي:", (r'\frac{3}{x}', 3/x)),
  [O(r'e^{4}', E**4), O(r'e^{3}', E**3), O(r'e^{5}', E**5), O(r'e^{12}', E**12)],
  r"$\displaystyle\int_1^a\frac3x\,dx=3\big[\ln x\big]_1^a=3\ln a-3\ln1=3\ln a$" "\n" r"$3\ln a=12 \Rightarrow \ln a=4 \Rightarrow a=e^4$",
  truth=lambda: solve(ig(3/x, (x, 1, ap6)) - 12, ap6)[0],
  figure=figure('n6q14', area_kx6(3/x, 1, 5.2, (-0.5, 7.4), (-0.5, 5.4), {0: '$0$', 1: '$1$', 5.2: '$a$'}, (1.35, 3.3, r'$f(x)=\frac{3}{x}$')), 3.8, 2.8),
  tag='المساحة: إيجاد ثابت'),
# 2023 #12: velocity-time graph (a new shape: a dip below the axis, then a constant stretch), start x0 given -> final position;
# options = displacement or distance x start added or not
Q('n6q15', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة المتجهة – الزمن لجُسيم يتحرّك على المحور $x$ في الفترة الزمنية $[0,\,6]$. إذا بدأ الجُسيم حركته من $x=3$ عندما $t=0$ ، فإنّ الموقع النهائي للجُسيم هو:",
  [O('7', 7, units='m'), O('11', 11, units='m'), O('8', 8, units='m'), O('4', 4, units='m')],
  r"المساحات: $[0,1]$: $+1$ ، $[1,2]$: $-1$ ، $[2,3]$: $-1$ ، $[3,4]$: $+1$ ، $[4,6]$: $+4$ ، فالإزاحة $=6-2=4$" "\n" r"الموقع النهائي $=3+4=7\ \text{m}$",
  truth=3 + pw_integral(vt6, 0, 6), figure=figure('n6q15', vt5(vt6, 6, -2, 2), 4.0, 3.0), tag='الحركة من منحنى السرعة–الزمن'),
# 2026 #37: dy/dx = 1/(trig^2 x . trig^2 y), separable, both sides direct as in the model (sin^2 y by power reduction,
# csc^2 x -> -cot x); options = 1/4 vs 1/2 sin 2y x sign of cot x
IndexQ('n6q16', U5[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ هو:", (r'\frac{1}{\sin^{2}x\sin^{2}y}', 1/(sin(x)**2*sin(y)**2))),
  [O(r'\frac{1}{2}y-\frac{1}{4}\sin 2y=-\cot x+C', y/2-sin(2*y)/4+cot(x)-Cc, 'rel'), O(r'\frac{1}{2}y-\frac{1}{2}\sin 2y=-\cot x+C', y/2-sin(2*y)/2+cot(x)-Cc, 'rel'),
   O(r'\frac{1}{2}y-\frac{1}{4}\sin 2y=\cot x+C', y/2-sin(2*y)/4-cot(x)-Cc, 'rel'), O(r'\frac{1}{2}y-\frac{1}{2}\sin 2y=\cot x+C', y/2-sin(2*y)/2-cot(x)-Cc, 'rel')],
  r"بفصل المتغيرات: $\sin^2y\,dy=\csc^2x\,dx$ ، و $\sin^2y=\dfrac{1-\cos2y}{2}$ ، إذن $\dfrac12y-\dfrac14\sin2y=-\cot x+C$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, 1/(sin(x)**2*sin(y)**2))), tag='المعادلات التفاضلية: الحل العام'),
# ---------------- unit 6
# 2023 #15: midpoint with two unknowns, a from one coordinate first, then b; options = +-k list (a itself, a + b, sign slip)
Q('n6q17', U6[1], 'medium',
  r"إذا كانت: $A(-1,\,a,\,4)$ و $B(5,\,4,\,a+b)$ ، وكانت إحداثيات نقطة منتصف $\overline{AB}$ هي $(2,\,3,\,1)$ ، فإنّ قيمة الثابت $b$ هي:",
  [O('-4', -4), O('4', 4), O('-2', -2), O('2', 2)],
  r"من الإحداثي $y$: $\dfrac{a+4}{2}=3 \Rightarrow a=2$" "\n" r"من الإحداثي $z$: $\dfrac{4+a+b}{2}=1 \Rightarrow a+b=-2 \Rightarrow b=-4$",
  truth=lambda: solve([(a+4)/2-3, (4+a+b)/2-1], [a, b], dict=True)[0][b], tag='المتجهات: منتصف قطعة مستقيمة'),
# 2026 #39 (shared stem with 2026 #40): AB = BD -> position vector of D; options = 2B - A, A (the equation read as AB = DB), -A, -(2B - A)
Q('n6q18', U6[1], 'medium',
  r"متجه الموقع للنقطة $D$ هو:",
  [vec_opt(7, 4, -5), vec_opt(1, -2, 3), vec_opt(-1, 2, -3), vec_opt(-7, -4, 5)],
  r"$\overrightarrow{AB}=\overrightarrow{BD} \Rightarrow D=2B-A=\langle 8-1,\ 2+2,\ -2-3\rangle=\langle 7,\,4,\,-5\rangle$",
  truth=T3(2*V(4, 1, -1)-V(1, -2, 3)), tag='المتجهات: نقطة ومتجه موقع (نص مشترك)',
  lead=shared(r"إذا كانت: $A(1,\,-2,\,3),\ B(4,\,1,\,-1),\ C(\alpha,\,0,\,5)$ ، وكانت $D$ نقطة في الفضاء، حيث: $\overrightarrow{AB}=\overrightarrow{BD}$", 18, 19)),
# 2026 #40: |AC| = sqrt(n) with alpha < 0; options = negative values: the right root, the (alpha + x_A) sign slip,
# the root before adding x_A, no square root taken and the sign slip
Q('n6q19', U6[1], 'medium',
  r"إذا كان: $|\overrightarrow{AC}|=\sqrt{17}$ ، فإنّ قيمة الثابت $\alpha$ ، حيث $\alpha<0$ ، هي:",
  [O('-2', -2), O('-4', -4), O('-3', -3), O('-10', -10)],
  r"$\overrightarrow{AC}=\langle \alpha-1,\ 2,\ 2\rangle$ ، و $(\alpha-1)^2+4+4=17 \Rightarrow (\alpha-1)^2=9$" "\n"
  r"$\alpha-1=\pm3 \Rightarrow \alpha=4$ أو $\alpha=-2$ ، وبما أن $\alpha<0$ فإن $\alpha=-2$",
  truth=lambda: [r_ for r_ in solve((x-1)**2+8-17, x) if r_ < 0][0], tag='المتجهات: المقدار وإيجاد ثابت (نص مشترك)'),
# 2026 #41: cuboid in the ministry's drawing, vertex B given, midpoint of a face diagonal (CF, on the face y = 4, not AF/GA);
# options = one vertex misread each time (C read as G, F read as G, C read as D)
Q('n6q20', U6[1], 'medium',
  r"في متوازي المستطيلات الآتي، إذا كانت إحداثيات الرأس $B$ هي: $(3,\,4,\,6)$ ، فإنّ إحداثيات نقطة منتصف $\overline{CF}$ هي:",
  [pt_opt(R(3, 2), 4, 3), pt_opt(R(3, 2), 4, 0), pt_opt(0, 4, 3), pt_opt(R(3, 2), 2, 3)],
  r"من الشكل: $C(0,\,4,\,6)$ (فوق $G(0,4,0)$ بارتفاع $6$) ، و $F(3,\,4,\,0)$ (تحت $B$)" "\n"
  r"منتصف $\overline{CF}$: $\left(\dfrac{0+3}{2},\ \dfrac{4+4}{2},\ \dfrac{6+0}{2}\right)=\left(\dfrac32,\,4,\,3\right)$",
  truth=T3((V(0, 4, 6)+V(3, 4, 0))/2), figure=figure('n6q20', iso_box(3, 4, 6), 3.2, 3.6), tag='المتجهات من شكل ثلاثي الأبعاد'),
# 2023s #16: three arrows head to tail around a triangle (a closed loop, the other orientation) -> the right geometric sum;
# options = the zero-sum relation and three relations with a sign flipped (values: lhs - rhs from the drawing's coordinates)
IndexQ('n6q21', U6[1], 'easy',
  r"معتمدًا الشكل الآتي الذي يُمثّل كلًّا من المتجهات $\vec{\mathbf{u}},\ \vec{\mathbf{v}},\ \vec{\mathbf{w}}$ ، أيّ من الآتية يُمثّل جمعًا هندسيًّا صحيحًا للمتجهات؟",
  [T(r"$\vec{\mathbf{u}}=-\vec{\mathbf{v}}-\vec{\mathbf{w}}$", T3(u6v-(-v6v-w6v))), T(r"$\vec{\mathbf{w}}=\vec{\mathbf{u}}+\vec{\mathbf{v}}$", T3(w6v-(u6v+v6v))),
   T(r"$\vec{\mathbf{u}}=\vec{\mathbf{v}}+\vec{\mathbf{w}}$", T3(u6v-(v6v+w6v))), T(r"$\vec{\mathbf{v}}=\vec{\mathbf{u}}-\vec{\mathbf{w}}$", T3(v6v-(u6v-w6v)))],
  r"الأسهم متتابعة حول المثلث (رأس كل سهم عند ذيل الذي يليه) وتعود إلى نقطة البداية، فمجموعها المتجه الصفري: $\vec{\mathbf{u}}+\vec{\mathbf{v}}+\vec{\mathbf{w}}=\vec{\mathbf{0}}$ ، إذن $\vec{\mathbf{u}}=-\vec{\mathbf{v}}-\vec{\mathbf{w}}$",
  truth=lambda vals: only(vals, lambda r_: all(c_ == 0 for c_ in r_)),
  figure=figure('n6q21', loop_fig6(tri6, [('P', 'Q', r'$\vec{\mathbf{u}}$', (0, -0.4)), ('Q', 'S', r'$\vec{\mathbf{v}}$', (0.42, 0.25)),
                                          ('S', 'P', r'$\vec{\mathbf{w}}$', (-0.45, 0.2))]), 3.2, 2.2),
  tag='المتجهات: الجمع الهندسي من الشكل'),
# 2026 #38: line parallel to v through a position vector with a missing component (j), options as in the model with the
# four line names r, m, n, p: point and direction swapped x the missing component put in the wrong slot
IndexQ('n6q22', U6[2], 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=-3\hat{i}+2\hat{j}+6\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها هو: $5\hat{i}-4\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [named_line6('r', (5, 0, -4), (-3, 2, 6)), named_line6('m', (-3, 2, 6), (5, 0, -4)), named_line6('n', (0, 5, -4), (-3, 2, 6)), named_line6('p', (-3, 2, 6), (0, 5, -4))],
  r"متجه موقع النقطة $A$ هو $5\hat{i}+0\hat{j}-4\hat{k}=\langle 5,\,0,\,-4\rangle$ (لا يوجد $\hat{j}$) ، ومتجه الاتجاه $\langle -3,\,2,\,6\rangle$:" "\n"
  r"$\vec{\mathbf{r}}=\langle 5,0,-4\rangle+t\langle -3,2,6\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((5, 0, -4), ln) and par(ln[1], (-3, 2, 6))), tag='معادلة المستقيم في الفضاء'),
# 2026r #20: distance from a point to a line, the foot F given; options = |PF| or |PF|^2 x sign slip with the negative coordinate (1 - (-3) taken as 1 - 3)
Q('n6q23', U6[2], 'easy',
  r"إذا كانت: $P(2,\,-3,\,4)$ نقطة غير واقعة على المستقيم $l$ ، وكانت $F(3,\,1,\,1)$ مسقط العمود من النقطة $P$ على المستقيم $l$ ، فإنّ البُعد بين النقطة $P$ والمستقيم $l$ (بوحدات الطول) هو:",
  [O(r'\sqrt{26}', sqrt(26)), O('26', 26), O(r'\sqrt{14}', sqrt(14)), O('14', 14)],
  r"البُعد هو طول العمود $\overline{PF}$: $\overrightarrow{PF}=\langle 3-2,\ 1+3,\ 1-4\rangle=\langle 1,\,4,\,-3\rangle$" "\n" r"$|\overrightarrow{PF}|=\sqrt{1+16+9}=\sqrt{26}$",
  truth=(V(3, 1, 1)-V(2, -3, 4)).norm(), tag='بعد نقطة عن مستقيم'),
# 2026r #19: perpendicular vectors with the parameter in three components -> a quadratic; options = the right factor pair of 24 or the other pair (4, 6) x which root is negative
Q('n6q24', U6[3], 'medium',
  r"إذا كان: $\vec{\mathbf{v}}=\langle \alpha,\,5,\,3\rangle$ ، $\vec{\mathbf{w}}=\langle -\alpha,\,\alpha,\,8\rangle$ ، وكان المتجهان $\vec{\mathbf{v}}$ و $\vec{\mathbf{w}}$ متعامدين، فإنّ القيمتين المُمكنتين للثابت $\alpha$ هما:",
  [pair_opt(r'-3,\ 8', -3, 8), pair_opt(r'3,\ -8', 3, -8), pair_opt(r'-4,\ 6', -4, 6), pair_opt(r'4,\ -6', 4, -6)],
  r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=-\alpha^2+5\alpha+24=0 \Rightarrow \alpha^2-5\alpha-24=0$" "\n" r"$(\alpha-8)(\alpha+3)=0 \Rightarrow \alpha=8$ أو $\alpha=-3$",
  truth=lambda: FiniteSet(*solve(V(x, 5, 3).dot(V(-x, x, 8)), x)), tag='التعامد وإيجاد ثوابت'),
# 2023s #19: u . c with u = AB; options = AB or BA (overall sign) x a sign slip in one product ((-3)(-4) taken as -12)
Q('n6q25', U6[3], 'easy',
  r"إذا كان: $A(4,\,2,\,-1)$ ، $B(2,\,-1,\,-1)$ ، $\vec{\mathbf{c}}=\langle 1,\,-4,\,3\rangle$ ، وكان $\vec{\mathbf{u}}=\overrightarrow{AB}$ ، فإنّ $\vec{\mathbf{u}}\cdot\vec{\mathbf{c}}$ يساوي:",
  [O('10', 10), O('-10', -10), O('-14', -14), O('14', 14)],
  r"$\vec{\mathbf{u}}=\overrightarrow{AB}=\langle 2-4,\ -1-2,\ -1+1\rangle=\langle -2,\,-3,\,0\rangle$" "\n" r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{c}}=(-2)(1)+(-3)(-4)+0(3)=-2+12+0=10$",
  truth=(V(2, -1, -1)-V(4, 2, -1)).dot(V(1, -4, 3)), tag='الضرب القياسي ومتجهات بين نقاط'),
# ---------------- unit 7
# 2026 #46: ratio of two geometric probabilities -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) (p vs 1 - p x value vs reciprocal)
Q('n6q26', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $\dfrac{P(X=1)}{P(X=4)}=\dfrac{343}{125}$ ، فإنّ التوقّع للمتغيّر العشوائي $X$ هو:",
  [O(r'\frac{7}{2}', R(7, 2)), O(r'\frac{2}{7}', R(2, 7)), O(r'\frac{5}{7}', R(5, 7)), O(r'\frac{7}{5}', R(7, 5))],
  r"$\dfrac{P(X=1)}{P(X=4)}=\dfrac{p}{(1-p)^3p}=\dfrac{1}{(1-p)^3}=\dfrac{343}{125} \Rightarrow (1-p)^3=\dfrac{125}{343} \Rightarrow 1-p=\dfrac57$" "\n"
  r"$p=\dfrac27$ ، و $E(X)=\dfrac1p=\dfrac72$",
  truth=lambda: 1/[r_ for r_ in solve(geo(p, 1)/geo(p, 4)-R(343, 125), p) if r_.is_real and 0 < r_ < 1][0], tag='التوزيع الهندسي: نسبة احتمالين والتوقع'),
# 2025s #22: E(X) and p of a binomial -> n -> Var(X); options = npq, E used as n (E.p.q), q, twice the variance
Q('n6q27', U7[1], 'easy',
  r"إذا كان: $X\sim B(n,\,0.1)$ ، وكان: $E(X)=3$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [D('2.7'), D('0.27'), D('0.9'), D('5.4')],
  r"$E(X)=np=0.1n=3 \Rightarrow n=30$" "\n" r"$\text{Var}(X)=np(1-p)=30(0.1)(0.9)=2.7$",
  truth=lambda: (lambda nn: nn*R(1, 10)*R(9, 10))(solve(n*R(1, 10)-3, n)[0]), tag='توزيع ذي الحدين: التوقع والتباين'),
# 2026 #48: P(X < a) below the mean for N(mu, sigma^2), with the table shared by items 28-29; options = complement or not
# x z right (-0.75) or the variance used in z (9/144 ~ 0.06, a z not in the table, as in the model)
Q('n6q28', U7[2], 'medium',
  r"إذا كان: $X\sim N(84,\,144)$ ، فإنّ $P(X<75)$ هو:",
  [D('0.2266'), D('0.7734'), D('0.4761'), D('0.5239')],
  r"$\sigma=\sqrt{144}=12$ ، $z=\dfrac{75-84}{12}=-0.75$ ، $P(Z<-0.75)=1-P(Z<0.75)=1-0.7734=0.2266$",
  truth=1-Ph(R(3, 4)), tag='التوزيع الطبيعي: حساب احتمال', lead=ztable_note([28, 29], 0, 0.7, 0.75, 1.2, 1.25), group=2),
# 2026 #49: P(-k/c < Z < k/c) given -> k; options = the right table entry times c, the neighbouring entry times c,
# the probability looked up directly (closest entry 0.7734 -> 0.75) times c, c/z (the equation inverted)
Q('n6q29', U7[2], 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{20}<Z<\dfrac{k}{20}\right)=0.7698$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:",
  [D('24'), D('25'), D('15'), D('16.7')],
  r"$2P\left(Z<\dfrac{k}{20}\right)-1=0.7698 \Rightarrow P\left(Z<\dfrac{k}{20}\right)=\dfrac{1.7698}{2}=0.8849$" "\n" r"من الجدول: $\dfrac{k}{20}=1.2 \Rightarrow k=24$",
  truth=lambda: 20*[z_ for z_ in (0, R(7, 10), R(3, 4), R(6, 5), R(5, 4)) if 2*Ph(z_)-1 == R('0.7698')][0], tag='التوزيع الطبيعي: فترة متماثلة وإيجاد ثابت'),
# 2024s #23 / 2023 #24: probability between mu - sigma and mu + 2 sigma by the empirical rule (figure), sigma from a decimal
# variance as in 2023 #24; options = the right three-band sum, mu +- 2 sigma, mu +- sigma, one side only (mu to mu + 2 sigma)
Q('n6q30', U7[2], 'medium',
  r"إذا كان: $X\sim N(5,\,0.09)$ ، فإنّ $P(4.7<X<5.6)$ هو:" "\n" r"ملحوظة: يمكنك الاستفادة من القاعدة التجريبية المبيّنة في الشكل الآتي.",
  [D('0.815'), D('0.95'), D('0.68'), D('0.475')],
  r"$\sigma=\sqrt{0.09}=0.3$ ، و $4.7=5-0.3=\mu-\sigma$ ، و $5.6=5+0.6=\mu+2\sigma$" "\n" r"$P(4.7<X<5.6)=0.34+0.34+0.135=0.815$",
  truth=emp(-1, 2), figure=figure('n6q30', emp_fig, 4.4, 2.4), tag='التوزيع الطبيعي: القاعدة التجريبية'),
]

# ================================================================== PAPER 7
# ------------------------------------------------------------------ figures drawn like the ministry's
def vol7_fig(fig, ax):
    """2026 #36: increasing curve starting on the x-axis at x = 1 (not labelled), the full line x = e, the region
    between them shaded; only the origin 0, the line and f(x) are labelled"""
    axes_style(ax, (-0.45, 3.85), (-0.45, 2.6), ticks=False)
    f_ = lambda u_: np.sqrt(u_*np.log(u_))
    xs = np.linspace(1, 3.45, 300)
    ax.plot(xs, f_(xs), color='#1f5fbf', lw=1.8)
    ax.annotate('', xy=(xs[-1], f_(xs[-1])), xytext=(xs[-15], f_(xs[-15])),
                arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
    xr = np.linspace(1, np.e, 200)
    ax.fill_between(xr, f_(xr), 0*xr, color='#9cc3ef', alpha=0.85)
    ax.plot([np.e, np.e], [-0.35, 2.35], color='#444', lw=1.2)
    ax.text(np.e, 2.42, r'$x=e$', fontsize=11, ha='center')
    ax.text(3.3, 1.72, r'$f(x)$', color='#1f5fbf', fontsize=11)
    ax.text(-0.25, -0.32, r'$0$', fontsize=11)


def area7_fig(fig, ax):
    """2025s #3: the cubic touching the x-axis at one zero and crossing it at the other, the hump shaded, no values"""
    axes_style(ax, (-0.95, 4.75), (-3.6, 11.2), ticks=False)
    f_ = lambda u_: u_**2*(4 - u_)
    xs = np.linspace(-0.85, 4.4, 400)
    ys = f_(xs)
    ys[ys < -3.4] = np.nan
    ax.plot(xs, ys, color='#1f5fbf', lw=1.8)
    xr = np.linspace(0, 4, 200)
    ax.fill_between(xr, f_(xr), 0*xr, color='#9cc3ef', alpha=0.85)
    ax.text(3.62, 7.4, r'$f(x)$', color='#1f5fbf', fontsize=11)


def panels7(angles):
    """u6_helpers.sign_panels with the label of a small acute angle moved out of the narrow gap between the arrows"""
    base = sign_panels(angles)
    def draw(fig, ax):
        base(fig, ax)
        for i, th in enumerate(angles):
            if th < 40:
                cx, cy = (i % 2)*5.8, -(i // 2)*3.1
                for t_ in ax.texts:
                    if t_.get_text() == f'${th}^\\circ$':
                        t_.set_position((cx + 1.32*np.cos(np.radians(th/2)), cy + 1.32*np.sin(np.radians(th/2)) - 0.04))
    return draw


def bell7(intervals, ticks):
    """s2_helpers.bell with the bottom spine on the curve's axis (one axis line, values under it)"""
    base = bell(intervals, ticks)
    def draw(fig, ax):
        base(fig, ax)
        ax.spines['bottom'].set_position(('data', 0))
    return draw


# parallelogram RSTV (R top left, S top right, T bottom right, V bottom left), Y the midpoint of RT,
# Z on ST produced beyond T with TZ = 3a (k = 5/3)
pg7 = plane_pts((0.0, 0.0), (-0.12, -0.5), (0.7, 0.07),
                {'R': 0, 'S': 6*vb, 'T': 5*va + 6*vb, 'V': 5*va, 'Y': R(5, 2)*va + 3*vb, 'Z': 8*va + 6*vb})

P7 = [
# ---------------- unit 5
# 2023 #2: 1/sin^2(kx) plus the constant pi; options = cot vs tan x {minus sign and pi x} vs {plus sign and pi}
Q('n7q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\frac{1}{\sin^{2}\frac{x}{4}}+\pi', 1/sin(x/4)**2 + pi)),
  [A(r'-4\cot\frac{x}{4}+\pi x+C', -4*cot(x/4) + pi*x), A(r'4\cot\frac{x}{4}+\pi+C', 4*cot(x/4) + pi),
   A(r'-4\tan\frac{x}{4}+\pi x+C', -4*tan(x/4) + pi*x), A(r'4\tan\frac{x}{4}+\pi+C', 4*tan(x/4) + pi)],
  r"$\dfrac{1}{\sin^2\frac x4}=\csc^2\frac x4$ وتكامله $-4\cot\frac x4$ ، و $\pi$ عدد ثابت تكامله $\pi x$ ، إذن الناتج $-4\cot\frac x4+\pi x+C$",
  truth=1/sin(x/4)**2 + pi, tag='تكامل الاقترانات المثلثية'),
# 2026 #27: a^(mx+n) divided by ln a; options = exponent (chain factor 4 = 2^2 absorbed or not) x ln 2 vs (ln 2)^2
Q('n7q2', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2^{4x+3}}{\ln 2}', 2**(4*x + 3)/log(2))),
  [A(r'\frac{2^{4x+1}}{(\ln 2)^{2}}+C', 2**(4*x + 1)/log(2)**2), A(r'\frac{2^{4x+1}}{\ln 2}+C', 2**(4*x + 1)/log(2)),
   A(r'\frac{2^{4x+3}}{(\ln 2)^{2}}+C', 2**(4*x + 3)/log(2)**2), A(r'\frac{2^{4x+3}}{\ln 2}+C', 2**(4*x + 3)/log(2))],
  r"$\dfrac{1}{\ln2}\displaystyle\int2^{4x+3}dx=\frac{1}{\ln2}\cdot\frac{2^{4x+3}}{4\ln2}=\frac{2^{4x+3}}{2^2(\ln2)^2}=\frac{2^{4x+1}}{(\ln2)^2}+C$",
  truth=2**(4*x + 3)/log(2), tag='تكامل الاقتران الأسي'),
# 2023s #3: cot^2(kx) - csc^2(kx) = -1; options = -x, x (identity sign), and the two term slips of the model:
# cot^2 = 1 - csc^2 (wrong identity) and the second term added instead of subtracted
Q('n7q3', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\cot^{2}4x-\csc^{2}4x', cot(4*x)**2 - csc(4*x)**2)),
  [A(r'-x+C', -x), A(r'x+C', x), A(r'x+\frac{1}{2}\cot 4x+C', x + cot(4*x)/2), A(r'-\frac{1}{2}\cot 4x-x+C', -cot(4*x)/2 - x)],
  r"من $1+\cot^2u=\csc^2u$ يكون $\cot^24x-\csc^24x=-1$ ، إذن $\displaystyle\int(-1)\,dx=-x+C$",
  truth=cot(4*x)**2 - csc(4*x)**2, tag='تكامل باستعمال متطابقات فيثاغورس'),
# 2026 #29: dy/dx = e^(2x) - e^(-x), curve through (0, 1); options = antiderivative (sign of the e^(-x) term) x sign of the constant
IndexQ('n7q4', U5[1], 'medium',
  F(r"يُمثّل الاقتران: $\dfrac{dy}{dx}=«0»$ ميل المماس لمنحنى الاقتران $y$. إذا كان منحنى $y$ يمرّ بالنقطة $(0,\,1)$ ، فإنّ قاعدة الاقتران $y$ هي:", (r'e^{2x}-e^{-x}', exp(2*x) - exp(-x))),
  [O(r'y=\frac{1}{2}e^{2x}+e^{-x}-\frac{1}{2}', exp(2*x)/2 + exp(-x) - R(1, 2), 'eq'), O(r'y=\frac{1}{2}e^{2x}+e^{-x}+\frac{1}{2}', exp(2*x)/2 + exp(-x) + R(1, 2), 'eq'),
   O(r'y=\frac{1}{2}e^{2x}-e^{-x}+\frac{3}{2}', exp(2*x)/2 - exp(-x) + R(3, 2), 'eq'), O(r'y=\frac{1}{2}e^{2x}-e^{-x}-\frac{3}{2}', exp(2*x)/2 - exp(-x) - R(3, 2), 'eq')],
  r"$y=\displaystyle\int(e^{2x}-e^{-x})dx=\frac12e^{2x}+e^{-x}+C$ ، و $y(0)=\frac12+1+C=1 \Rightarrow C=-\frac12$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, exp(2*x) - exp(-x), 0, 1)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
# 2025s #7: v = c - (2t - 6)^2 and the initial position -> position at t = 3; options = sign of the constant,
# constant taken as the initial position (the 36 at t = 0 forgotten), the initial position not added
Q('n7q5', U5[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=«0»$ ، حيث $v$ السرعة بالمتر لكل ثانية و $t$ الزمن بالثواني. إذا كان الموقع الابتدائي للجُسيم هو $10\ \text{m}$ ، فإنّ موقع الجُسيم بعد $3$ ثوانٍ هو:", (r'16-(2t-6)^{2}', 16 - (2*t - 6)**2)),
  [O('22', 22, units='m'), O('74', 74, units='m'), O('58', 58, units='m'), O('12', 12, units='m')],
  r"$s(t)=16t-\dfrac{(2t-6)^3}{6}+C$ ، و $s(0)=36+C=10 \Rightarrow C=-26$" "\n" r"$s(3)=48-0-26=22\ \text{m}$",
  truth=10 + ig(16 - (2*t - 6)**2, (t, 0, 3)), tag='الحركة: الموقع بمعلومية الموقع الابتدائي'),
# 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2 with k = 1/2; options = coefficient (divided vs multiplied by the
# chain factor) x tan vs sec
Q('n7q6', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sin^{2}\frac{x}{2}}{\cos^{4}\frac{x}{2}}', sin(x/2)**2/cos(x/2)**4)),
  [A(r'\frac{2}{3}\tan^{3}\frac{x}{2}+C', R(2, 3)*tan(x/2)**3), A(r'\frac{1}{6}\tan^{3}\frac{x}{2}+C', tan(x/2)**3/6),
   A(r'\frac{2}{3}\sec^{3}\frac{x}{2}+C', R(2, 3)*sec(x/2)**3), A(r'\frac{1}{6}\sec^{3}\frac{x}{2}+C', sec(x/2)**3/6)],
  r"المقدار $=\tan^2\frac x2\sec^2\frac x2$ ، وبالتعويض $u=\tan\frac x2 \Rightarrow du=\frac12\sec^2\frac x2\,dx$:" "\n"
  r"$\displaystyle2\int u^2du=\frac23u^3+C=\frac23\tan^3\frac x2+C$",
  truth=sin(x/2)**2/cos(x/2)**4, tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
# 2023s #7: (linear) times the cube root of a quadratic whose derivative is minus the linear factor; options = sign x
# cube root of u^4 vs fourth root of u^3 (truth with the real cube root, as in school)
Q('n7q7', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(1-4x)\sqrt[3]{2x^{2}-x}', (1 - 4*x)*cbrt(2*x**2 - x))),
  [A(r'-\frac{3\sqrt[3]{(2x^{2}-x)^{4}}}{4}+C', -R(3, 4)*cbrt((2*x**2 - x)**4)), A(r'\frac{3\sqrt[3]{(2x^{2}-x)^{4}}}{4}+C', R(3, 4)*cbrt((2*x**2 - x)**4)),
   A(r'-\frac{3\sqrt[4]{(2x^{2}-x)^{3}}}{4}+C', -R(3, 4)*((2*x**2 - x)**3)**R(1, 4)), A(r'\frac{3\sqrt[4]{(2x^{2}-x)^{3}}}{4}+C', R(3, 4)*((2*x**2 - x)**3)**R(1, 4))],
  r"$u=2x^2-x \Rightarrow du=(4x-1)dx=-(1-4x)dx$: $\displaystyle-\int u^{\frac13}du=-\frac34u^{\frac43}+C=-\frac{3\sqrt[3]{(2x^2-x)^4}}{4}+C$",
  truth=(1 - 4*x)*real_root(2*x**2 - x, 3), tag='التكامل بالتعويض: جذور'),
# 2024 #8: definite integral of k x (1 - x)^3 by u = 1 - x; options = sign (limits) x (x = 1 - u vs 1 + u)
Q('n7q8', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'12x(1-x)^{3}', 12*x*(1 - x)**3)),
  [O(r'\frac{3}{5}', R(3, 5)), O(r'-\frac{3}{5}', -R(3, 5)), O(r'\frac{27}{5}', R(27, 5)), O(r'-\frac{27}{5}', -R(27, 5))],
  r"$u=1-x$ ، $x=1-u$ ، $dx=-du$ ، والحدود: $x=0\to u=1$ ، $x=1\to u=0$" "\n"
  r"$\displaystyle\int_1^0-12(1-u)u^3du=12\int_0^1(u^3-u^4)du=12\left(\frac14-\frac15\right)=\frac35$",
  truth=ig(12*x*(1 - x)**3, (x, 0, 1)), tag='التكامل المحدود بالتعويض'),
# 2025 #8: rate k x / sqrt(c + x^2) in context, one value given in units that must be converted (pieces -> thousands);
# options = coefficient (x2 vs x1/2 when integrating u^(-1/2)) x sign of the constant (each constant fits its coefficient)
IndexQ('n7q9', U5[2], 'hard',
  F(r"يُمثّل الاقتران $C(x)$ تكلفة إنتاج القطعة الواحدة (بالدينار) من مُنتَج معيّن، حيث $x$ عدد القطع المُنتَجة بالآلاف. إذا كان: $C'(x)=«0»$ هو معدّل التغيّر في تكلفة إنتاج القطعة الواحدة، وكانت تكلفة إنتاج القطعة الواحدة $12$ JD عندما يكون عدد القطع المُنتَجة $4000$ قطعة، فإنّ قاعدة الاقتران $C(x)$ هي:", (r'\frac{-8x}{\sqrt{9+x^{2}}}', -8*x/sqrt(9 + x**2))),
  [O(r'C(x)=-8\sqrt{9+x^{2}}+52', -8*sqrt(9 + x**2) + 52, 'eq'), O(r'C(x)=-8\sqrt{9+x^{2}}-52', -8*sqrt(9 + x**2) - 52, 'eq'),
   O(r'C(x)=-2\sqrt{9+x^{2}}+22', -2*sqrt(9 + x**2) + 22, 'eq'), O(r'C(x)=-2\sqrt{9+x^{2}}-22', -2*sqrt(9 + x**2) - 22, 'eq')],
  r"$u=9+x^2$: $\displaystyle\int\frac{-8x}{\sqrt{9+x^2}}dx=-4\int u^{-\frac12}du=-8\sqrt{9+x^2}+k$ ، و $4000$ قطعة تعني $x=4$:" "\n"
  r"$-8(5)+k=12 \Rightarrow k=52$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, -8*x/sqrt(9 + x**2), 4, 12)), tag='إيجاد الاقتران من معدّل تغيّره في سياق حياتي'),
# 2026r #7: (px + q)/(x^2 + cx) with two linear factors; options = constants swapped x sign of the second
Q('n7q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x+6}{x^{2}+2x}', (x + 6)/(x**2 + 2*x))),
  [A(r'3\ln|x|-2\ln|x+2|+C', 3*log(x) - 2*log(x + 2)), A(r'3\ln|x|+2\ln|x+2|+C', 3*log(x) + 2*log(x + 2)),
   A(r'2\ln|x|-3\ln|x+2|+C', 2*log(x) - 3*log(x + 2)), A(r'2\ln|x|+3\ln|x+2|+C', 2*log(x) + 3*log(x + 2))],
  r"$\dfrac{x+6}{x(x+2)}=\dfrac{A}{x}+\dfrac{B}{x+2}$ ، عند $x=0$: $6=2A \Rightarrow A=3$ ، عند $x=-2$: $4=-2B \Rightarrow B=-2$",
  truth=(x + 6)/(x**2 + 2*x), tag='التكامل بالكسور الجزئية: عوامل خطية'),
# 2025 #10: 1/(x^2 (x + c)) with a repeated factor; options = which log carries the minus x sign of the 1/x term
Q('n7q11', U5[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{1}{x^{2}(x+1)}', 1/(x**2*(x + 1)))),
  [A(r'\ln|x+1|-\ln|x|-\frac{1}{x}+C', log(x + 1) - log(x) - 1/x), A(r'\ln|x+1|-\ln|x|+\frac{1}{x}+C', log(x + 1) - log(x) + 1/x),
   A(r'\ln|x|-\ln|x+1|-\frac{1}{x}+C', log(x) - log(x + 1) - 1/x), A(r'\ln|x|-\ln|x+1|+\frac{1}{x}+C', log(x) - log(x + 1) + 1/x)],
  r"$\dfrac{1}{x^2(x+1)}=\dfrac{A}{x}+\dfrac{B}{x^2}+\dfrac{D}{x+1}$: عند $x=0$: $B=1$ ، عند $x=-1$: $D=1$ ، ومعامل $x^2$: $A+D=0 \Rightarrow A=-1$" "\n"
  r"$\displaystyle\int=-\ln|x|-\frac1x+\ln|x+1|+C$",
  truth=1/(x**2*(x + 1)), tag='التكامل بالكسور الجزئية: عامل مكرر'),
# 2023 #9: k x^n ln x by parts; options = power of x in the first term x sign of the second
Q('n7q12', U5[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'9x^{2}\ln x', 9*x**2*log(x))),
  [A(r'3x^{3}\ln x-x^{3}+C', 3*x**3*log(x) - x**3), A(r'3x^{2}\ln x-x^{3}+C', 3*x**2*log(x) - x**3),
   A(r'3x^{3}\ln x+x^{3}+C', 3*x**3*log(x) + x**3), A(r'3x^{2}\ln x+x^{3}+C', 3*x**2*log(x) + x**3)],
  r"بالأجزاء: $u=\ln x$ ، $dv=9x^2dx \Rightarrow v=3x^3$: $\displaystyle3x^3\ln x-\int3x^3\cdot\frac1x\,dx=3x^3\ln x-x^3+C$",
  truth=9*x**2*log(x), tag='التكامل بالأجزاء'),
# 2023s #10: x csc^2(kx) by parts; options = sign of v = -cot/k (both terms flip) x ln|sin| vs ln|cos|
Q('n7q13', U5[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\csc^{2}2x', x*csc(2*x)**2)),
  [A(r'-\frac{x}{2}\cot 2x+\frac{1}{4}\ln|\sin 2x|+C', -x/2*cot(2*x) + log(sin(2*x))/4), A(r'\frac{x}{2}\cot 2x-\frac{1}{4}\ln|\sin 2x|+C', x/2*cot(2*x) - log(sin(2*x))/4),
   A(r'-\frac{x}{2}\cot 2x+\frac{1}{4}\ln|\cos 2x|+C', -x/2*cot(2*x) + log(cos(2*x))/4), A(r'\frac{x}{2}\cot 2x-\frac{1}{4}\ln|\cos 2x|+C', x/2*cot(2*x) - log(cos(2*x))/4)],
  r"بالأجزاء: $u=x$ ، $dv=\csc^22x\,dx \Rightarrow v=-\frac12\cot2x$: $\displaystyle-\frac x2\cot2x+\frac12\int\cot2x\,dx=-\frac x2\cot2x+\frac14\ln|\sin2x|+C$",
  truth=x*csc(2*x)**2, tag='التكامل بالأجزاء'),
# 2026 #36: volume about the x-axis of the region under sqrt(x ln x) from its x-intercept (x = 1, not printed) to the
# line x = e (figure like the model); one round of parts; options = sign of the lower-limit term x v = x^2/2 vs x^2
Q('n7q14', U5[5], 'hard',
  F(r"اعتمادًا على التمثيل البياني الآتي الذي يُبيّن منحنى الاقتران: $f(x)=«0»$ ، والمستقيم $x=e$ ، فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور $x$ بالوحدات المكعبة هو:", (r'\sqrt{x\ln x}', sqrt(x*log(x)))),
  [O(r'\frac{\pi(e^{2}+1)}{4}', pi*(E**2 + 1)/4), O(r'\frac{\pi(e^{2}-1)}{4}', pi*(E**2 - 1)/4),
   O(r'\frac{\pi(e^{2}+1)}{2}', pi*(E**2 + 1)/2), O(r'\frac{\pi(e^{2}-1)}{2}', pi*(E**2 - 1)/2)],
  r"المنحنى يقطع المحور $x$ عند $x=1$ ، و $V=\pi\displaystyle\int_1^e x\ln x\,dx=\pi\left[\frac{x^2}{2}\ln x-\frac{x^2}{4}\right]_1^e=\pi\left(\frac{e^2}{4}+\frac14\right)$",
  truth=pi*ig(x*log(x), (x, 1, E)), figure=figure('n7q14', vol7_fig, 3.6, 2.8), tag='الحجوم الدورانية من الشكل'),
# 2025s #3: area under a cubic with a double zero between its zeros (figure, no numbers); x^2(4 - x) on [0, 4]
# (the blueprint's x^2(3 - x) is the mirror image of u5e7q10's region, same area 27/4); options = reciprocal pair
# and the two terms of the antiderivative taken alone
Q('n7q15', U5[5], 'medium',
  F(r"إذا كان الاقتران المُبيّن مُنحناه في الشكل الآتي هو: $f(x)=«0»$ ، فإنّ مساحة المنطقة المُظلَّلة (بالوحدات المربعة) هي:", (r'x^{2}(4-x)', x**2*(4 - x))),
  [O(r'\frac{64}{3}', R(64, 3)), O(r'\frac{3}{64}', R(3, 64)), O('64', 64), O(r'\frac{256}{3}', R(256, 3))],
  r"أصفار الاقتران $0$ (مكرّر، يمسّ المحور) و $4$ ، و $\displaystyle\int_0^4(4x^2-x^3)dx=\left[\frac{4x^3}{3}-\frac{x^4}{4}\right]_0^4=\frac{256}{3}-64=\frac{64}{3}$",
  truth=ig(x**2*(4 - x), (x, 0, 4)), figure=figure('n7q15', area7_fig, 3.6, 2.9), tag='المساحة تحت منحنى من الشكل'),
# 2026r #12: dy/dx = y times a linear polynomial through (1, 1), answer in ln|y| form; options = sign of x^2 x sign of the constant
IndexQ('n7q16', U5[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي تُحقّقه النقطة $(1,\,1)$ هو:", (r'2y-2xy', 2*y - 2*x*y)),
  [O(r'\ln|y|=2x-x^{2}-1', log(y) - 2*x + x**2 + 1, 'rel'), O(r'\ln|y|=2x-x^{2}+1', log(y) - 2*x + x**2 - 1, 'rel'),
   O(r'\ln|y|=2x+x^{2}-1', log(y) - 2*x - x**2 + 1, 'rel'), O(r'\ln|y|=2x+x^{2}+1', log(y) - 2*x - x**2 - 1, 'rel')],
  r"$\dfrac{dy}{y}=(2-2x)dx \Rightarrow \ln|y|=2x-x^2+C$ ، وعند $(1,1)$: $0=2-1+C \Rightarrow C=-1$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, 2*y - 2*x*y, (1, 1))), tag='المعادلات التفاضلية: الحل الخاص'),
# ---------------- unit 6
# 2026 #42: collinear points, AB (with the unknown) and AC given; options = right value, the constant moved with the
# wrong sign (the model's 10), the middle component matched with AC's first (the model's 3), the ratio forgotten (AB = AC)
Q('n7q17', U6[1], 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle 3,\,a+1,\,-2\rangle$ ، و $\overrightarrow{AC}=\langle 6,\,10,\,-4\rangle$ ، فإنّ قيمة $a$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('4', 4), O('6', 6), O('5', 5), O('9', 9)],
  r"$\overrightarrow{AB}=k\overrightarrow{AC}$: من المركبة الأولى $3=6k \Rightarrow k=\frac12$ (وتتحقّق في الثالثة: $-2=\frac12(-4)$)" "\n"
  r"$a+1=\frac12(10)=5 \Rightarrow a=4$",
  truth=lambda: solve(V(3, a + 1, -2).cross(V(6, 10, -4))[0], a)[0], tag='النقاط على استقامة واحدة'),
# 2026 #44: parallelogram, Y the midpoint of the diagonal RT, Z on ST produced, YZ given -> k in ST:TZ = k:1 (figure);
# options = k, the coefficient of TZ (stopped early), the coefficient of ST, the ratio read the other way
Q('n7q18', U6[1], 'hard',
  r"في الشكل الآتي $RSTV$ متوازي أضلاع. إذا كان: $\overrightarrow{RS}=6\vec{\mathbf{b}}$ ، و $\overrightarrow{RV}=5\vec{\mathbf{a}}$ ، وكانت $Y$ نقطة منتصف $\overline{RT}$ ، وكان: $ST:TZ=k:1$ ، وكان: $\overrightarrow{YZ}=3\vec{\mathbf{b}}+\frac{11}{2}\vec{\mathbf{a}}$ ، فإنّ قيمة الثابت $k$ هي:",
  [O(r'\frac{5}{3}', R(5, 3)), O('3', 3), O('5', 5), O(r'\frac{3}{5}', R(3, 5))],
  r"$\overrightarrow{YT}=\frac12\overrightarrow{RT}=\frac12(6\vec{\mathbf{b}}+5\vec{\mathbf{a}})=3\vec{\mathbf{b}}+\frac52\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{TZ}=\overrightarrow{YZ}-\overrightarrow{YT}=3\vec{\mathbf{a}}$ ، و $\overrightarrow{ST}=\overrightarrow{RV}=5\vec{\mathbf{a}}$ ، إذن $ST:TZ=5:3$ و $k=\frac53$",
  truth=lambda: solve_k((6*vb + 5*va)/2 + (5*va)/k, 3*vb + R(11, 2)*va),
  figure=figure('n7q18', poly_fig(pg7, [('S', 'T'), ('V', 'T'), ('T', 'Z'), ('R', 'T')],
                                    [('R', 'S', r'$6\vec{\mathbf{b}}$', (-0.25, 0.22)), ('R', 'V', r'$5\vec{\mathbf{a}}$', (-0.8, 0.0))],
                                    {'R': (-0.3, 0.12), 'S': (0.1, 0.1), 'T': (0.15, 0.02), 'V': (-0.3, -0.33), 'Y': (-0.12, 0.2), 'Z': (0.14, -0.22)}),
                3.8, 3.2), tag='المتجهات في الأشكال الهندسية والنسبة'),
# 2023 #17: position vector of F with PF = (3/4) PQ; options as the model: F, PQ itself, PF (P not added), P plus PF
# with a sign slip in two components
Q('n7q19', U6[1], 'medium',
  r"إذا كان متجه الموقع للنقطة $P$ هو $\langle 2,\,-3,\,5\rangle$ ، وكان متجه الموقع للنقطة $Q$ هو $\langle 6,\,5,\,-7\rangle$ ، فإنّ متجه الموقع للنقطة $F$ التي تقع على $\overline{PQ}$ ، حيث: $\overrightarrow{PF}=\frac{3}{4}\overrightarrow{PQ}$ هو:",
  [vec_opt(5, 3, -4), vec_opt(4, 8, -12), vec_opt(3, 6, -9), vec_opt(5, -9, 14)],
  r"$\overrightarrow{PQ}=\langle 4,\,8,\,-12\rangle$ ، و $\overrightarrow{PF}=\frac34\overrightarrow{PQ}=\langle 3,\,6,\,-9\rangle$" "\n"
  r"متجه موقع $F$: $\langle 2,-3,5\rangle+\langle 3,6,-9\rangle=\langle 5,\,3,\,-4\rangle$",
  truth=T3(V(2, -3, 5) + R(3, 4)*(V(6, 5, -7) - V(2, -3, 5))), tag='تقسيم قطعة مستقيمة بنسبة'),
# 2026r #15: linear combination of two vectors (2u - 3v here); options = component sign variants (as the model:
# all signs reversed = 3v - 2u, the third or the first component reversed)
Q('n7q20', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{u}}=\langle 4,\,-1,\,3\rangle$ ، و $\vec{\mathbf{v}}=\langle -2,\,3,\,5\rangle$ ، فإنّ $2\vec{\mathbf{u}}-3\vec{\mathbf{v}}$ تساوي:",
  [vec_opt(14, -11, -9), vec_opt(-14, 11, 9), vec_opt(14, -11, 9), vec_opt(-14, -11, -9)],
  r"$2\vec{\mathbf{u}}-3\vec{\mathbf{v}}=\langle 8,-2,6\rangle-\langle -6,9,15\rangle=\langle 8+6,\ -2-9,\ 6-15\rangle=\langle 14,\,-11,\,-9\rangle$",
  truth=T3(2*V(4, -1, 3) - 3*V(-2, 3, 5)), tag='العمليات على المتجهات'),
# 2025 #14: unit vector in the direction of GH from two points (|GH| = 9); options = normalised or not x GH vs HG
Q('n7q21', U6[1], 'medium',
  r"إذا كان: $G(-1,\,4,\,2),\ H(7,\,3,\,6)$ ، فإنّ متجه الوحدة الذي في اتجاه $\overrightarrow{GH}$ هو:",
  [vec_opt(R(8, 9), -R(1, 9), R(4, 9)), vec_opt(-R(8, 9), R(1, 9), -R(4, 9)), vec_opt(8, -1, 4), vec_opt(-8, 1, -4)],
  r"$\overrightarrow{GH}=\langle 8,\,-1,\,4\rangle$ ، و $|\overrightarrow{GH}|=\sqrt{64+1+16}=9$ ، فمتجه الوحدة $\left\langle\frac89,-\frac19,\frac49\right\rangle$",
  truth=T3((V(7, 3, 6) - V(-1, 4, 2))/(V(7, 3, 6) - V(-1, 4, 2)).norm()), tag='متجه الوحدة'),
# 2023 #18: a point with one unknown coordinate (3a) lies on a line; options = a vs the coordinate 3a x sign
Q('n7q22', U6[2], 'easy',
  r"إذا كانت النقطة $(3,\,-1,\,3a)$ تقع على مستقيم له معادلة متجهة هي: $\vec{\mathbf{r}}=\langle -1,\,5,\,3\rangle+t\langle 2,\,-3,\,-6\rangle$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('-3', -3), O('3', 3), O('-9', -9), O('9', 9)],
  r"من الإحداثي $x$: $-1+2t=3 \Rightarrow t=2$ ، وتحقّق في $y$: $5-3(2)=-1$ ✔" "\n" r"الإحداثي $z$: $3a=3-6(2)=-9 \Rightarrow a=-3$",
  truth=lambda: solve(list(V(3, -1, 3*a) - V(-1, 5, 3) - t*V(2, -3, -6)), [a, t], dict=True)[0][a], tag='نقطة على مستقيم وإيجاد ثابت'),
# 2024 #19: point where a line meets a coordinate plane (XY here); options = right point, the sign of t slipped,
# the points on the wrong planes (XZ, YZ)
Q('n7q23', U6[2], 'medium',
  r"إحداثيات النقطة التي تقع على المستقيم $l$ الذي له معادلة متجهة: $\vec{\mathbf{r}}=\langle -3,\,6,\,-4\rangle+t\langle 3,\,-2,\,2\rangle$ ، وتقع أيضًا في المستوى $XY$ ، هي:",
  [pt_opt(3, 2, 0), pt_opt(-9, 10, 0), pt_opt(6, 0, 2), pt_opt(0, 4, -2)],
  r"في المستوى $XY$ يكون $z=0$: $-4+2t=0 \Rightarrow t=2$" "\n" r"$x=-3+6=3$ ، $y=6-4=2$ ، والنقطة $(3,\,2,\,0)$",
  truth=lambda: T3(V(-3, 6, -4) + solve(-4 + 2*t, t)[0]*V(3, -2, 2)), tag='تقاطع مستقيم مع مستوى إحداثي'),
# 2026 #43: three points, DE and FE given -> DE . DF; options = +-(right value) (DF vs FD), +-(DE . FE used directly)
Q('n7q24', U6[3], 'hard',
  r"إذا كانت $D,\ E,\ F$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{DE}=\langle 2,\,-1,\,4\rangle$ ، و $\overrightarrow{FE}=\langle 4,\,-3,\,1\rangle$ ، فإنّ $\overrightarrow{DE}\cdot\overrightarrow{DF}$ يساوي:",
  [O('6', 6), O('-6', -6), O('15', 15), O('-15', -15)],
  r"$\overrightarrow{DF}=\overrightarrow{DE}+\overrightarrow{EF}=\overrightarrow{DE}-\overrightarrow{FE}=\langle -2,\,2,\,3\rangle$" "\n"
  r"$\overrightarrow{DE}\cdot\overrightarrow{DF}=-4-2+12=6$",
  truth=V(2, -1, 4).dot(V(2, -1, 4) - V(4, -3, 1)), tag='الضرب القياسي ومتجهات بين نقاط'),
# 2023s #20: which figure shows u . v = 0 (non-zero vectors); options = the four panels (acute, straight, obtuse, right)
IndexQ('n7q25', U6[3], 'easy',
  r"إذا كان: $\vec{\mathbf{u}},\ \vec{\mathbf{v}}$ متجهين غير صفريين، وكان $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=0$ ، فإنّ الشكل الأنسب للتعبير عن المتجهين $\vec{\mathbf{u}},\ \vec{\mathbf{v}}$ هندسيًّا من الأشكال الآتية، هو:",
  [T('الشكل (4)', pi/2), T('الشكل (1)', pi/6), T('الشكل (2)', pi), T('الشكل (3)', 3*pi/4)],
  r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=|\vec{\mathbf{u}}||\vec{\mathbf{v}}|\cos\theta=0$ والمتجهان غير صفريين، إذن $\cos\theta=0$ ، أي $\theta=90^\circ$: الشكل (4)",
  truth=lambda vals: only(vals, lambda th: cos(th) == 0),
  figure=figure('n7q25', panels7([30, 180, 135, 90]), 4.4, 3.0), tag='إشارة الضرب القياسي من الشكل'),
# ---------------- unit 7
# 2026 #47: binomial quality control, the tray is rejected if 2 or more of 5 eggs are cracked; options = cut-off
# (at least 1 vs at least 2) x event vs complement: P(X >= 2), P(X = 0), P(X <= 1), P(X >= 1)
Q('n7q26', U7[1], 'hard',
  r"يختار عامل في مزرعة دواجن عيّنة عشوائية مكوّنة من $5$ بيضات من كلّ طبق لفحصها، ويُستبعَد الطبق إذا وُجدت في العيّنة بيضتان مشروختان فأكثر. إذا كانت نسبة البيض المشروخ في إنتاج المزرعة $10\%$ ، فإنّ احتمال استبعاد الطبق هو تقريبًا:",
  [D('0.0815'), D('0.5905'), D('0.9185'), D('0.4095')],
  r"$X\sim B(5,\,0.1)$: $P(X\ge2)=1-(0.9)^5-5(0.1)(0.9)^4=1-0.59049-0.32805=0.08146\approx0.0815$",
  truth=r4(1 - binom(5, R(1, 10), 0) - binom(5, R(1, 10), 1)), tag='توزيع ذي الحدين: احتمال «على الأقل»'),
# 2025 #22: P(X > 3) = q^3 gives q, then E(X) = 1/p; options = 1/p, 1/q (p and q swapped), q/p, p itself
Q('n7q27', U7[1], 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $P(X>3)=0.216$ ، فإنّ توقّع المتغيّر العشوائي $X$ هو:",
  [O(r'\frac{5}{2}', R(5, 2)), O(r'\frac{5}{3}', R(5, 3)), O(r'\frac{3}{2}', R(3, 2)), O(r'\frac{2}{5}', R(2, 5))],
  r"$P(X>3)=(1-p)^3=0.216 \Rightarrow 1-p=0.6 \Rightarrow p=0.4$ ، و $E(X)=\dfrac{1}{0.4}=\dfrac52$",
  truth=lambda: 1/(1 - [r_ for r_ in solve(s**3 - R(216, 1000), s) if r_.is_real][0]), tag='التوزيع الهندسي: احتمال «أكبر من»'),
# 2026 #50: sigma from the percentage above a value, closest table entry, rounded to two decimals; options = sigma,
# the z-value itself, d.z, z/d
Q('n7q28', U7[2], 'hard',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(1.8,\,\sigma^2)$ على كُتل ثمار الشمّام (بالكيلوغرام) في إحدى المزارع. إذا كانت كُتل $1\%$ منها تزيد على $2.5\ \text{kg}$ ، فإنّ قيمة الانحراف المعياري لكُتل الثمار (مُقرَّبًا إلى أقرب منزلتين عشريتين) هي:" + ztable(2.32, 2.33),
  [D('0.30', 'kg'), D('2.33', 'kg'), D('1.63', 'kg'), D('3.33', 'kg')],
  r"$P(X<2.5)=0.99$ ، وأقرب قيمة في الجدول $P(Z<2.33)=0.9901$ ، إذن $z=2.33$" "\n"
  r"$\dfrac{2.5-1.8}{\sigma}=2.33 \Rightarrow \sigma=\dfrac{0.7}{2.33}\approx0.30\ \text{kg}$",
  truth=lambda: R(str(round(float(R(7, 10)/zclosest(R(99, 100), (R(232, 100), R(233, 100)))), 2))),
  tag='التوزيع الطبيعي: إيجاد الانحراف المعياري'),
# 2026r #23: shaded area between a negative and a positive z, the two P(Z < z) values given (figure); options = right,
# the negative bound taken as positive, 0.5 plus a tail (each tail)
Q('n7q29', U7[2], 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P(Z<0.62)=0.7324$ ، و $P(Z<1.34)=0.9099$ ، فإنّ مساحة المنطقة المُظلَّلة أسفل منحنى التوزيع الطبيعي المعياري المُبيَّنة في الشكل الآتي هي:",
  [D('0.6423'), D('0.1775'), D('0.5901'), D('0.7676')],
  r"$P(-0.62<Z<1.34)=P(Z<1.34)-P(Z<-0.62)=0.9099-(1-0.7324)=0.9099-0.2676=0.6423$",
  truth=Ph(R(134, 100)) - Ph(-R(62, 100)),
  figure=figure('n7q29', bell7([(-0.62, 1.34)], [-0.62, 1.34]), 4.0, 2.4), tag='التوزيع الطبيعي: مساحة من الشكل'),
# 2025s #24: symmetry, P(X > mu + c) given in context -> P(X < mu - c); options = a, 1 - a, 1 - 2a, 2a
Q('n7q30', U7[2], 'easy',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(\mu,\,\sigma^2)$ على مُدَد المكالمات الهاتفية (بالدقائق) في إحدى شركات الاتصالات. إذا كان: $P(X>\mu+3)=0.24$ ، فإنّ $P(X<\mu-3)$ هو:",
  [D('0.24'), D('0.76'), D('0.52'), D('0.48')],
  r"المنحنى متماثل حول $\mu$ ، و $\mu-3$ و $\mu+3$ على البُعد نفسه منه: $P(X<\mu-3)=P(X>\mu+3)=0.24$",
  truth=R(24, 100), tag='التوزيع الطبيعي: التماثل'),
]

# ================================================================== PAPER 8
def num(expr):
    """numerical value of a definite integral (integrands with |...| or a root of a negative-looking expression)"""
    return expr.evalf(40)


def ode_t_ok(Nt, rhs, t0, n0):
    """explicit solution N(t) of N' = rhs(t) with N(t0) = n0"""
    return same(diff(Nt, t) - rhs, 0) and same(Nt.subs(t, t0), n0)


def place(pt):
    """where a point with zero coordinates lies: 'plane-xz' (one zero), 'axis-y' (two zeros), 'space' (none)"""
    zeros = [i_ for i_, c_ in enumerate(pt) if c_ == 0]
    rest = ''.join('xyz'[i_] for i_ in range(3) if i_ not in zeros)
    return {1: 'plane-', 2: 'axis-'}.get(len(zeros), 'space') + rest


def vol8(fig, ax):
    """2026 #36 drawing: the curve and the shaded region between it and the x-axis; no values on the axes except the
    origin, so the limits come from the formula (the curve meets the axis again at x = pi)"""
    xs = np.linspace(0, np.pi, 400)
    ys = np.sqrt(np.clip(xs*np.sin(xs), 0, None))
    axes_style(ax, (-0.45, 4.1), (-0.3, 1.85), ticks=False)
    ax.fill_between(xs, ys, color='#9cc3ef', alpha=0.85)
    ax.plot(xs, ys, color='#1f5fbf', lw=1.8)
    ax.text(2.45, 1.45, r'$f(x)$', color='#1f5fbf', fontsize=12)
    ax.text(-0.27, -0.22, r'$0$', fontsize=11)


EMPNOTE = "\n" r"ملحوظة: يمكنك الاستفادة من القاعدة التجريبية المبيّنة في الشكل الآتي."
vt8 = [(0, -2), (1, -2), (3, 2), (6, 2)]
sq8 = {'A': (0, 1), 'B': (1, 1), 'C': (1, 0), 'D': (0, 0)}
pg8 = plane_pts((0, 0), (3.2, 0), (1.0, 1.8), {'A': 0, 'B': va, 'C': va + vb, 'D': vb, 'M': vb + (va - vb)/4})
DEG = {'circ': 1}

P8 = [
# ---------------- unit 5
# 2023s #2: sin of (c - kx); options = right, sign lost when dividing by -k, chain factor dropped, inner function integrated
Q('n8q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\sin(3-2x)', sin(3 - 2*x))),
  [A(r'\frac{\cos(3-2x)}{2}+C', cos(3 - 2*x)/2), A(r'-\frac{\cos(3-2x)}{2}+C', -cos(3 - 2*x)/2),
   A(r'\cos(3-2x)+C', cos(3 - 2*x)), A(r'-\cos\left(3x-x^{2}\right)+C', -cos(3*x - x**2))],
  r"$\displaystyle\int\sin(3-2x)\,dx=\frac{-\cos(3-2x)}{-2}+C=\frac{\cos(3-2x)}{2}+C$ (نقسم على معامل $x$ وهو $-2$)",
  truth=sin(3 - 2*x), tag='تكامل الاقترانات المثلثية'),
# 2026r #1: k e^(mx) + a^(mx); options = coefficient of e^(mx) (k/m or the k dropped) x chain factor m under a^(mx) (kept or lost)
Q('n8q2', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'3e^{2x}+3^{2x}', 3*exp(2*x) + 3**(2*x))),
  [A(r'\frac{3e^{2x}}{2}+\frac{3^{2x}}{2\ln 3}+C', 3*exp(2*x)/2 + 3**(2*x)/(2*log(3))),
   A(r'\frac{3e^{2x}}{2}+\frac{3^{2x}}{\ln 3}+C', 3*exp(2*x)/2 + 3**(2*x)/log(3)),
   A(r'\frac{e^{2x}}{2}+\frac{3^{2x}}{2\ln 3}+C', exp(2*x)/2 + 3**(2*x)/(2*log(3))),
   A(r'\frac{e^{2x}}{2}+\frac{3^{2x}}{\ln 3}+C', exp(2*x)/2 + 3**(2*x)/log(3))],
  r"$\displaystyle\int3e^{2x}dx=\frac{3e^{2x}}{2}$ ، و $\displaystyle\int3^{2x}dx=\frac{3^{2x}}{2\ln3}$ ، إذن الناتج $\dfrac{3e^{2x}}{2}+\dfrac{3^{2x}}{2\ln3}+C$",
  truth=3*exp(2*x) + 3**(2*x), tag='تكامل الاقتران الأسي'),
# 2023 #4: |linear| on an interval where it keeps one sign (no splitting); options = +-4, +-2 (the model's list)
Q('n8q3', U5[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{3}^{5}«0»\,dx$ هي:", (r'\left|2-x\right|', Abs(2 - x))),
  [O('4', 4), O('-4', -4), O('2', 2), O('-2', -2)],
  r"في $[3,5]$ يكون $2-x<0$ ، فـ $|2-x|=x-2$ ، و $\displaystyle\int_3^5(x-2)\,dx=\left[\frac{x^2}{2}-2x\right]_3^5=\frac52-\left(-\frac32\right)=4$",
  truth=num(Integral(Abs(2 - x), (x, 3, 5))), tag='التكامل المحدود: القيمة المطلقة'),
# 2024s #6: a count changing at k e^(rt), the initial count -> N(t); options = decimal slip in k/r (9 or 0.9) x constant
# adjusted with e^0 = 1 or not (as in the model: 0.9 with the constant of 9, 0.9 with its own constant, C = N(0))
IndexQ('n8q4', U5[1], 'medium',
  F(r"في دراسة لنموّ عدد سكّان إحدى البلدات، تبيّن أنّ عدد السكّان $P(t)$ (بالآلاف) يتغيّر بمعدّل $P'(t)=«0»$ ، حيث $t$ الزمن بالسنوات منذ بدء الدراسة. إذا كان عدد السكّان عند بدء الدراسة $20$ ألف نسمة، فإنّ قاعدة الاقتران $P(t)$ هي:", (r'0.36e^{0.04t}', R(36, 100)*exp(R(4, 100)*t))),
  [O(r'P(t)=9e^{0.04t}+11', 9*exp(R(4, 100)*t) + 11, 'eq'), O(r'P(t)=0.9e^{0.04t}+11', R(9, 10)*exp(R(4, 100)*t) + 11, 'eq'),
   O(r'P(t)=0.9e^{0.04t}+19.1', R(9, 10)*exp(R(4, 100)*t) + R(191, 10), 'eq'), O(r'P(t)=9e^{0.04t}+20', 9*exp(R(4, 100)*t) + 20, 'eq')],
  r"$P(t)=\displaystyle\int0.36e^{0.04t}dt=\frac{0.36}{0.04}e^{0.04t}+C=9e^{0.04t}+C$ ، و $P(0)=9+C=20 \Rightarrow C=11$",
  truth=lambda vals: only(vals, lambda N_: ode_t_ok(N_, R(36, 100)*exp(R(4, 100)*t), 0, 20)),
  tag='إيجاد الاقتران من معدّل تغيّره في سياق حياتي'),
# 2026r #5: total distance for v = k cos t on [0, 3pi/2]; options = right, |displacement|, the second part only, half (the model's list)
Q('n8q5', U5[1], 'medium',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ سرعته بالمتر لكلّ ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلّية بالأمتار التي قطعها الجُسيم في الفترة $\left[0,\,\frac{3\pi}{2}\right]$ هي:", (r'4\cos t', 4*cos(t))),
  [O('12', 12), O('4', 4), O('8', 8), O('6', 6)],
  r"$v=0$ عند $t=\frac{\pi}{2}$: $\displaystyle\int_0^{\pi/2}4\cos t\,dt+\left|\int_{\pi/2}^{3\pi/2}4\cos t\,dt\right|=4+|-8|=12$",
  truth=ig(4*cos(t), (t, 0, pi/2)) - ig(4*cos(t), (t, pi/2, 3*pi/2)), tag='الحركة: المسافة الكلية من السرعة'),
# 2026 #31: x^n (1 - 1/x)^n = (x - 1)^n, then the power rule; options = right, power kept (n), the bracket's power
# ignored (x^n - x^(n-1)) and its sign switch
Q('n8q6', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{6}\left(1-\frac{1}{x}\right)^{6}', x**6*(1 - 1/x)**6)),
  [A(r'\frac{1}{7}(x-1)^{7}+C', (x - 1)**7/7), A(r'\frac{1}{6}(x-1)^{6}+C', (x - 1)**6/6),
   A(r'\frac{1}{7}x^{7}-\frac{1}{6}x^{6}+C', x**7/7 - x**6/6), A(r'\frac{1}{7}x^{7}+\frac{1}{6}x^{6}+C', x**7/7 + x**6/6)],
  r"$x^6\left(1-\frac1x\right)^6=\left(x-1\right)^6$ ، إذن $\displaystyle\int(x-1)^6dx=\frac17(x-1)^7+C$",
  truth=x**6*(1 - 1/x)**6, tag='التكامل بالتعويض بعد التبسيط'),
# 2023s #8: a power of a trig function times sin 2x; options = right, sign, the other function (sin for cos), sin 2x treated as sin x
Q('n8q7', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos^{2}x\sin 2x', cos(x)**2*sin(2*x))),
  [A(r'-\frac{\cos^{4}x}{2}+C', -cos(x)**4/2), A(r'\frac{\cos^{4}x}{2}+C', cos(x)**4/2),
   A(r'-\frac{\sin^{4}x}{2}+C', -sin(x)**4/2), A(r'-\frac{\cos^{3}x}{3}+C', -cos(x)**3/3)],
  r"$\sin2x=2\sin x\cos x$ ، فالمقدار $=2\cos^3x\sin x$ ، و $u=\cos x \Rightarrow du=-\sin x\,dx$: $\displaystyle-2\int u^3du=-\frac{\cos^4x}{2}+C$",
  truth=cos(x)**2*sin(2*x), tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
# 2024s #9: e^x over a power of (c + e^x); options = sign x divided or multiplied by the new power 3
Q('n8q8', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{e^{x}}{(2+e^{x})^{4}}', exp(x)/(2 + exp(x))**4)),
  [A(r'-\frac{1}{3(2+e^{x})^{3}}+C', -1/(3*(2 + exp(x))**3)), A(r'\frac{1}{3(2+e^{x})^{3}}+C', 1/(3*(2 + exp(x))**3)),
   A(r'-\frac{3}{(2+e^{x})^{3}}+C', -3/(2 + exp(x))**3), A(r'\frac{3}{(2+e^{x})^{3}}+C', 3/(2 + exp(x))**3)],
  r"$u=2+e^x \Rightarrow du=e^xdx$: $\displaystyle\int u^{-4}du=\frac{u^{-3}}{-3}+C=-\frac{1}{3(2+e^x)^3}+C$",
  truth=exp(x)/(2 + exp(x))**4, tag='التكامل بالتعويض'),
# 2025 #6: root(a^2 x^2 - x^4) on a negative interval (|x| = -x), then substitution; options = sign (|x| taken as x) x
# the 1/2 from du = -2x dx (kept or lost)
Q('n8q9', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{-3}^{0}«0»\,dx$ هي:", (r'\sqrt{9x^{2}-x^{4}}', sqrt(9*x**2 - x**4))),
  [O('9', 9), O('-9', -9), O('18', 18), O('-18', -18)],
  r"$\sqrt{9x^2-x^4}=|x|\sqrt{9-x^2}=-x\sqrt{9-x^2}$ في $[-3,0]$" "\n"
  r"$u=9-x^2$: $\displaystyle\int_{-3}^0-x\sqrt{9-x^2}\,dx=\frac12\int_0^9u^{\frac12}du=\frac13\left[u^{\frac32}\right]_0^9=9$",
  truth=num(Integral(sqrt(9*x**2 - x**4), (x, -3, 0))), tag='التكامل المحدود بالتعويض'),
# 2026 #33: a linear and an irreducible quadratic factor (x^3 + cx), A = 4 and B = -2 (3 and -2 in the model);
# options = which log carries the coefficient x sign of the second log
Q('n8q10', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2x^{2}+20}{x^{3}+5x}', (2*x**2 + 20)/(x**3 + 5*x))),
  [A(r'4\ln|x|-\ln(x^{2}+5)+C', 4*log(x) - log(x**2 + 5)), A(r'4\ln|x|+\ln(x^{2}+5)+C', 4*log(x) + log(x**2 + 5)),
   A(r'\ln|x|-4\ln(x^{2}+5)+C', log(x) - 4*log(x**2 + 5)), A(r'\ln|x|+4\ln(x^{2}+5)+C', log(x) + 4*log(x**2 + 5))],
  r"$\dfrac{2x^2+20}{x(x^2+5)}=\dfrac{A}{x}+\dfrac{Bx+D}{x^2+5}$ ، عند $x=0$: $20=5A \Rightarrow A=4$ ، ومعامل $x^2$: $2=A+B \Rightarrow B=-2$ ، و $D=0$" "\n"
  r"$\displaystyle\int\left(\frac4x-\frac{2x}{x^2+5}\right)dx=4\ln|x|-\ln(x^2+5)+C$",
  truth=(2*x**2 + 20)/(x**3 + 5*x), tag='التكامل بالكسور الجزئية: عامل تربيعي'),
# 2024s #11: (px + q)/(x - x^2); options = partial fractions or the fake ln of the denominator, x sign of the second log
# (the inner -1 of 1 - x)
Q('n8q11', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{3x+1}{x-x^{2}}', (3*x + 1)/(x - x**2))),
  [A(r'\ln|x|-4\ln|1-x|+C', log(x) - 4*log(1 - x)), A(r'\ln|x|+4\ln|1-x|+C', log(x) + 4*log(1 - x)),
   A(r'\ln|x-x^{2}|+C', log(x - x**2)), A(r'-\ln|x-x^{2}|+C', -log(x - x**2))],
  r"$\dfrac{3x+1}{x(1-x)}=\dfrac{A}{x}+\dfrac{B}{1-x}$ ، عند $x=0$: $A=1$ ، عند $x=1$: $B=4$" "\n"
  r"و $\displaystyle\int\frac{4}{1-x}dx=-4\ln|1-x|$ ، إذن الناتج $\ln|x|-4\ln|1-x|+C$",
  truth=(3*x + 1)/(x - x**2), tag='التكامل بالكسور الجزئية: عوامل خطية'),
# 2026 #34: substitution u = root x, then by parts (cos of 2 root x here); options = sign of each of the two terms
Q('n8q12', U5[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos\left(2\sqrt{x}\right)', cos(2*sqrt(x)))),
  [A(r'\sqrt{x}\,\sin\left(2\sqrt{x}\right)+\frac{1}{2}\cos\left(2\sqrt{x}\right)+C', sqrt(x)*sin(2*sqrt(x)) + cos(2*sqrt(x))/2),
   A(r'\sqrt{x}\,\sin\left(2\sqrt{x}\right)-\frac{1}{2}\cos\left(2\sqrt{x}\right)+C', sqrt(x)*sin(2*sqrt(x)) - cos(2*sqrt(x))/2),
   A(r'-\sqrt{x}\,\sin\left(2\sqrt{x}\right)+\frac{1}{2}\cos\left(2\sqrt{x}\right)+C', -sqrt(x)*sin(2*sqrt(x)) + cos(2*sqrt(x))/2),
   A(r'-\sqrt{x}\,\sin\left(2\sqrt{x}\right)-\frac{1}{2}\cos\left(2\sqrt{x}\right)+C', -sqrt(x)*sin(2*sqrt(x)) - cos(2*sqrt(x))/2)],
  r"$u=\sqrt x$ ، $dx=2u\,du$: $\displaystyle\int2u\cos2u\,du=u\sin2u-\int\sin2u\,du=u\sin2u+\frac12\cos2u+C$" "\n"
  r"$=\sqrt x\sin\left(2\sqrt x\right)+\frac12\cos\left(2\sqrt x\right)+C$",
  truth=cos(2*sqrt(x)), tag='التكامل بالتعويض ثم بالأجزاء'),
# 2023 #11: definite integral of x a^x by parts; options = sign of the second term x the lower-limit term a^0 = 1 kept or forgotten
Q('n8q13', U5[4], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'x\,2^{x}', x*2**x)),
  [O(r'\frac{2\ln 2-1}{(\ln 2)^{2}}', (2*log(2) - 1)/log(2)**2), O(r'\frac{2\ln 2+1}{(\ln 2)^{2}}', (2*log(2) + 1)/log(2)**2),
   O(r'\frac{2\ln 2-2}{(\ln 2)^{2}}', (2*log(2) - 2)/log(2)**2), O(r'\frac{2\ln 2+2}{(\ln 2)^{2}}', (2*log(2) + 2)/log(2)**2)],
  r"بالأجزاء: $\displaystyle\int x2^xdx=\frac{x2^x}{\ln2}-\frac{2^x}{(\ln2)^2}$ ، و $\left[\dfrac{x2^x}{\ln2}-\dfrac{2^x}{(\ln2)^2}\right]_0^1=\dfrac{2}{\ln2}-\dfrac{2}{(\ln2)^2}+\dfrac{1}{(\ln2)^2}=\dfrac{2\ln2-1}{(\ln2)^2}$",
  truth=ig(x*2**x, (x, 0, 1)), tag='التكامل المحدود بالأجزاء'),
# 2024s #12: distance from a velocity-time graph (a part below the axis), the start given as a distractor; options = distance,
# displacement, final position, the area above the axis only
Q('n8q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة – الزمن لجسم يتحرّك على المحور $x$ في الفترة الزمنية $[0,\,6]$. إذا بدأ الجسم الحركة من $x=2$ عندما $t=0$ ، فإنّ المسافة التي قطعها الجسم في الفترة الزمنية المُعطاة هي:",
  [O('10', 10, units='m'), O('4', 4, units='m'), O('6', 6, units='m'), O('7', 7, units='m')],
  r"المساحة تحت محور $t$: $2(1)+\frac12(1)(2)=3$ ، وفوقه: $\frac12(1)(2)+3(2)=7$" "\n"
  r"المسافة $=3+7=10\ \text{m}$ (الموقع الابتدائي لا يدخل في حساب المسافة)",
  truth=pw_integral(vt8, 0, 6, absolute=True), figure=figure('n8q14', vt_graph(vt8, 7, -3, 3), 4.0, 3.0),
  tag='الحركة من منحنى السرعة–الزمن'),
# 2026 #36: volume about the x-axis of the region under root(f) (figure); the limits are the curve's x-intercepts, not
# printed (0 and pi here; the lower limit 1 in the model), then by parts; options = right, the product integrated factor by
# factor, the pi of the formula forgotten, both slips
Q('n8q15', U5[5], 'hard',
  F(r"اعتمادًا على التمثيل البياني الآتي الذي يُبيّن منحنى الاقتران: $f(x)=«0»$ ، فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور $x$ بالوحدات المكعّبة هو:", (r'\sqrt{x\sin x}', sqrt(x*sin(x)))),
  [O(r'\pi^{2}', pi**2), O(r'\frac{\pi^{3}}{2}', pi**3/2), O(r'\pi', pi), O(r'\frac{\pi^{2}}{2}', pi**2/2)],
  r"المنحنى يقطع المحور $x$ عند $x=0$ و $x=\pi$ ، و $V=\pi\displaystyle\int_0^{\pi}x\sin x\,dx=\pi\big[-x\cos x+\sin x\big]_0^{\pi}=\pi(\pi)=\pi^2$",
  truth=pi*ig(x*sin(x), (x, 0, pi)), figure=figure('n8q15', vol8, 3.6, 2.5), tag='الحجوم الدورانية من الشكل'),
# 2023 #13: dy = (derivative of a trig function) dx through a point; options = antiderivative (-csc x or csc x, each with the
# constant that fits the point) x sign of the constant
IndexQ('n8q16', U5[6], 'easy',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $dy=«0»\,dx$ ، الذي يُحقّق النقطة $\left(\frac{\pi}{2},\,3\right)$ هو:", (r'\csc x\cot x', csc(x)*cot(x))),
  [O(r'y=-\csc x+4', -csc(x) + 4, 'eq'), O(r'y=-\csc x-4', -csc(x) - 4, 'eq'), O(r'y=\csc x+2', csc(x) + 2, 'eq'), O(r'y=\csc x-2', csc(x) - 2, 'eq')],
  r"$y=\displaystyle\int\csc x\cot x\,dx=-\csc x+C$ ، و $3=-\csc\frac{\pi}{2}+C=-1+C \Rightarrow C=4$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, csc(x)*cot(x), pi/2, 3)), tag='المعادلات التفاضلية: الحل الخاص'),
# ---------------- unit 6
# 2024s #14: magnitude of the position vector of a midpoint; options = k root m, |OP + OQ| (not halved), and the coefficient
# and the radicand swapped in both (as in the model: 3 root 2, 2 root 3, 2 root 6, 6 root 2)
Q('n8q17', U6[1], 'medium',
  r"إذا كانت: $P(7,\,-6,\,2)$ ، $Q(-1,\,-2,\,8)$ ، وكانت $N$ نقطة منتصف $\overline{PQ}$ ، فإنّ مقدار متجه الموقع للنقطة $N$ هو:",
  [O(r'5\sqrt{2}', 5*sqrt(2)), O(r'10\sqrt{2}', 10*sqrt(2)), O(r'2\sqrt{5}', 2*sqrt(5)), O(r'2\sqrt{10}', 2*sqrt(10))],
  r"$N=\left(\dfrac{7-1}{2},\ \dfrac{-6-2}{2},\ \dfrac{2+8}{2}\right)=(3,\,-4,\,5)$ ، و $|\overrightarrow{ON}|=\sqrt{9+16+25}=\sqrt{50}=5\sqrt2$",
  truth=((V(7, -6, 2) + V(-1, -2, 8))/2).norm(), tag='المتجهات: منتصف قطعة مستقيمة'),
# 2026r #17: displacement vector from A to B; options = sign variants of the components (the subtraction order mixed between
# components; A - B itself is not offered, as in the model)
Q('n8q18', U6[1], 'easy',
  r"إذا كانت: $A(3,\,-7,\,4)$ ، $B(-2,\,5,\,-6)$ ، فإنّ متجه الإزاحة من النقطة $A$ إلى النقطة $B$ هو:",
  [vec_opt(-5, 12, -10), vec_opt(5, -12, -10), vec_opt(-5, 12, 10), vec_opt(5, 12, 10)],
  r"$\overrightarrow{AB}=B-A=\langle -2-3,\ 5+7,\ -6-4\rangle=\langle -5,\,12,\,-10\rangle$",
  truth=T3(V(-2, 5, -6) - V(3, -7, 4)), tag='المتجهات: متجه الإزاحة'),
# 2025 #17: square ABCD from three vertices (figure, no coordinates) -> D = A + C - B; options = 2A - B, A + B - C, the vertex B
Q('n8q19', U6[1], 'medium',
  r"إذا كان الشكل الآتي يُمثّل المربع $ABCD$ الذي فيه: $A(1,\,3,\,-2)$ ، $B(5,\,1,\,2)$ ، $C(9,\,5,\,0)$ ، فإنّ متجه الموقع للنقطة $D$ هو:",
  [vec_opt(5, 7, -4), vec_opt(-3, 5, -6), vec_opt(-3, -1, 0), vec_opt(5, 1, 2)],
  r"$\overrightarrow{AD}=\overrightarrow{BC} \Rightarrow D=A+C-B=\langle 1+9-5,\ 3+5-1,\ -2+0-2\rangle=\langle 5,\,7,\,-4\rangle$",
  truth=T3(V(1, 3, -2) + V(9, 5, 0) - V(5, 1, 2)),
  figure=figure('n8q19', poly_fig(sq8, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], [],
                                   {'A': (-0.13, 0.03), 'B': (0.04, 0.03), 'C': (0.04, -0.12), 'D': (-0.13, -0.12)}), 2.3, 2.2),
  tag='المتجهات: نقطة ومتجه موقع'),
# 2025 #15: PK = 1/3 KQ -> K; options = ratio 1/4 (right) or 1/3 (PK = 1/3 PQ), x K measured from P (right) or from Q;
# P and Q are placed so that the from-Q slip flips the signs of two components, the model's grid, and every distractor is
# the real result of its slip
Q('n8q20', U6[1], 'medium',
  r"إذا كان متجه الموقع للنقطة $P$ هو $\langle 4,\,-8,\,3\rangle$ ، ومتجه الموقع للنقطة $Q$ هو $\langle -4,\,8,\,3\rangle$ ، وكانت النقطة $K$ تقع على $\overline{PQ}$ بحيث أنّ: $\overrightarrow{PK}=\frac{1}{3}\overrightarrow{KQ}$ ، فإنّ متجه الموقع للنقطة $K$ هو:",
  [vec_opt(2, -4, 3), vec_opt(-2, 4, 3), vec_opt(R(4, 3), R(-8, 3), 3), vec_opt(R(-4, 3), R(8, 3), 3)],
  r"$PK:KQ=1:3 \Rightarrow \overrightarrow{PK}=\frac14\overrightarrow{PQ}=\frac14\langle -8,\,16,\,0\rangle=\langle -2,\,4,\,0\rangle$" "\n"
  r"$K=P+\overrightarrow{PK}=\langle 4-2,\ -8+4,\ 3\rangle=\langle 2,\,-4,\,3\rangle$",
  truth=T3(V(4, -8, 3) + R(1, 4)*(V(-4, 8, 3) - V(4, -8, 3))), tag='تقسيم قطعة مستقيمة بنسبة'),
# 2023s #14: a point with one zero coordinate lies in a coordinate plane; options = two planes x two axes (the axis of the
# zero coordinate is the trap)
IndexQ('n8q21', U6[1], 'easy',
  r"عند تعيين النقطة $C(-4,\,0,\,5)$ في نظام الإحداثيات ثلاثي الأبعاد، فإنّها تقع على:",
  [T(r'المستوى $xz$', 'plane-xz'), T(r'المحور $y$', 'axis-y'), T(r'المستوى $xy$', 'plane-xy'), T(r'المحور $x$', 'axis-x')],
  r"الإحداثي $y$ وحده صفر، والإحداثيان الآخران غير صفريين، فالنقطة تقع في المستوى $xz$ (ولا تقع على أيّ محور).",
  truth=lambda vals: only(vals, lambda v_: v_ == place((-4, 0, 5))), tag='نقطة في مستوى إحداثي'),
# 2025s #19: parallelogram (a and b on the sides from the bottom-left vertex), M on a diagonal in a given ratio (1:3 here,
# 3:2 there), CM = k(3a + b); options = k, -k, 1/k, -1/k
Q('n8q22', U6[1], 'hard',
  r"في متوازي الأضلاع $ABCD$ الآتي، تقع النقطة $M$ على $\overline{DB}$ ، حيث $DM:MB=1:3$ ، إذا كان: $\overrightarrow{CM}=k\left(3\vec{\mathbf{a}}+\vec{\mathbf{b}}\right)$ ، فإنّ قيمة الثابت $k$ هي:",
  [O(r'-\frac{1}{4}', R(-1, 4)), O(r'\frac{1}{4}', R(1, 4)), O('-4', -4), O('4', 4)],
  r"$\overrightarrow{CM}=\overrightarrow{CD}+\frac14\overrightarrow{DB}=-\vec{\mathbf{a}}+\frac14\left(\vec{\mathbf{a}}-\vec{\mathbf{b}}\right)=-\frac34\vec{\mathbf{a}}-\frac14\vec{\mathbf{b}}=-\frac14\left(3\vec{\mathbf{a}}+\vec{\mathbf{b}}\right)$",
  truth=lambda: solve_k((vb + (va - vb)/4) - (va + vb), k*(3*va + vb)),
  figure=figure('n8q22', poly_fig(pg8, [('B', 'C'), ('C', 'D'), ('D', 'B')],
                                   [('A', 'B', r'$\vec{\mathbf{a}}$', (-0.1, -0.38)), ('A', 'D', r'$\vec{\mathbf{b}}$', (-0.48, 0.0))],
                                   {'A': (-0.28, -0.2), 'B': (0.08, -0.2), 'C': (0.08, 0.05), 'D': (-0.2, 0.08), 'M': (0.06, 0.1)}), 3.6, 2.3),
  tag='المتجهات في الأشكال الهندسية والنسبة'),
# 2023s #18: F the foot of the perpendicular from P -> PF in terms of t (the general point of the line minus P); options =
# F - P, F + P, the constant part reversed (P - r0 + t d), P + t d
Q('n8q23', U6[2], 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 3,\,-2,\,1\rangle+t\langle 2,\,-1,\,0\rangle$ معادلة متجهة للمستقيم $l$ ، و $P(-1,\,4,\,1)$ نقطة غير واقعة عليه، وكانت النقطة $F$ هي مسقط النقطة $P$ على المستقيم $l$ ، فإنّ $\overrightarrow{PF}$ هو:",
  [O(r'\langle 4+2t,\,-6-t,\,0\rangle', Tuple(4 + 2*t, -6 - t, 0), 'vec'),
   O(r'\langle 2+2t,\,2-t,\,2\rangle', Tuple(2 + 2*t, 2 - t, 2), 'vec'),
   O(r'\langle -4+2t,\,6-t,\,0\rangle', Tuple(-4 + 2*t, 6 - t, 0), 'vec'),
   O(r'\langle -1+2t,\,4-t,\,1\rangle', Tuple(-1 + 2*t, 4 - t, 1), 'vec')],
  r"$F$ نقطة على المستقيم: $F=(3+2t,\ -2-t,\ 1)$ ، و $\overrightarrow{PF}=F-P=\langle 4+2t,\ -6-t,\ 0\rangle$",
  truth=T3(V(3, -2, 1) + t*V(2, -1, 0) - V(-1, 4, 1)), tag='مسقط العمود من نقطة على مستقيم'),
# 2026 #45: triangle from BA and BC with a zero dot product (the right angle is not stated); options = 1/2 |BA||BC|,
# without the 1/2, and two same-kind decoys (as in the model)
Q('n8q24', U6[3], 'medium',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{BA}=\langle 4,\,-7,\,-4\rangle$ ، $\overrightarrow{BC}=\langle 16,\,8,\,2\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O('81', 81), O('162', 162), O('72', 72), O('99', 99)],
  r"$\overrightarrow{BA}\cdot\overrightarrow{BC}=64-56-8=0$ ، إذن الزاوية $B$ قائمة" "\n"
  r"$|\overrightarrow{BA}|=\sqrt{81}=9$ ، $|\overrightarrow{BC}|=\sqrt{324}=18$ ، والمساحة تساوي $\frac12(9)(18)=81$",
  truth=R(1, 2)*V(4, -7, -4).norm()*V(16, 8, 2).norm()*sin(ang((4, -7, -4), (16, 8, 2))), tag='مساحة مثلث باستعمال الضرب القياسي'),
# 2025 #20: angle from the magnitudes and the dot product; options = special angles in degrees (the minus sign dropped,
# root 2 taken as 2, divided by one magnitude only)
Q('n8q25', U6[3], 'easy',
  r"إذا كان: $|\vec{\mathbf{a}}|=2$ ، $|\vec{\mathbf{b}}|=\sqrt{2}$ ، وكان: $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=-2$ ، فإنّ قياس الزاوية بين المتجهين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [O(r'135^{\circ}', 135, sym=DEG), O(r'45^{\circ}', 45, sym=DEG), O(r'120^{\circ}', 120, sym=DEG), O(r'180^{\circ}', 180, sym=DEG)],
  r"$\cos\theta=\dfrac{-2}{2\sqrt2}=-\dfrac{\sqrt2}{2} \Rightarrow \theta=135^{\circ}$",
  truth=acos(R(-2)/(2*sqrt(2)))*180/pi, tag='الزاوية بين متجهين'),
# ---------------- unit 7
# 2026r #21: repeated trials until the first success (a context), P(X = 3); options = q^2 p, q p (X = 2), q^3 p (X = 4,
# rounded as the model prints 0.073), q
Q('n8q26', U7[1], 'easy',
  r"بدأ شخص الاتّصال بخطّ خدمة العملاء في إحدى الشركات مرّة تلو الأخرى، على أن يتوقّف عند أوّل مرّة يُردّ فيها على اتّصاله. إذا كان احتمال الردّ على الاتّصال الواحد هو $0.3$ ، فإنّ احتمال أن يتوقّف الشخص بعد إجرائه $3$ اتّصالات هو:",
  [D('0.147'), D('0.21'), D('0.103'), D('0.70')],
  r"$X\sim Geo(0.3)$: $P(X=3)=(0.7)^2(0.3)=0.147$",
  truth=geo(R(3, 10), 3), tag='التوزيع الهندسي: تجربة حتى أول نجاح'),
# 2026r #22: n from E(X) and Var(X); options = E/p, E/q (p and q swapped), E/(pq), and a value checked by substitution
Q('n8q27', U7[1], 'medium',
  r"إذا كان: $X\sim B(n,\,p)$ ، وكان: $E(X)=4.8$ ، $\text{Var}(X)=2.88$ ، فإنّ قيمة $n$ هي:",
  [O('12', 12), O('8', 8), O('20', 20), O('16', 16)],
  r"$1-p=\dfrac{2.88}{4.8}=0.6 \Rightarrow p=0.4$ ، و $n=\dfrac{4.8}{0.4}=12$",
  truth=lambda: R('4.8')/(1 - R('2.88')/R('4.8')), tag='توزيع ذي الحدين: التوقع والتباين'),
# 2025s #25: sigma from the interval holding 95% (empirical rule, figure); options = sigma, sigma^2, 2 sigma (95% read as
# mu +- sigma), the width of the interval
Q('n8q28', U7[2], 'medium',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(18,\,\sigma^2)$ على أطوال أقلام الرصاص (بالسنتيمتر) التي يُنتجها أحد المصانع. إذا كانت أطوال $95\%$ منها تتراوح بين $16.8\ \text{cm}$ و $19.2\ \text{cm}$ ، فإنّ قيمة الانحراف المعياري $\sigma$ لأطوال الأقلام هي:" + EMPNOTE,
  [D('0.60', 'cm'), D('0.36', 'cm'), D('1.20', 'cm'), D('2.40', 'cm')],
  r"حسب القاعدة التجريبية تقع $95\%$ من القيم بين $\mu-2\sigma$ و $\mu+2\sigma$:" "\n"
  r"$\mu+2\sigma=19.2 \Rightarrow 18+2\sigma=19.2 \Rightarrow 2\sigma=1.2 \Rightarrow \sigma=0.6\ \text{cm}$",
  truth=(R('19.2') - 18)/2, figure=figure('n8q28', emp_fig, 4.4, 2.4), tag='التوزيع الطبيعي: القاعدة التجريبية'),
# 2026 #48: P(X > a) with a below the mean (shared table); options = P(Z < z) or its complement, x z right or with the
# decimal slip z = -0.09 (also what dividing by the variance 100 gives; Phi(0.09) is not in the table, as Phi(0.06) in the model)
Q('n8q29', U7[2], 'medium',
  r"إذا كان: $X\sim N(80,\,100)$ ، فإنّ $P(X>71)$ هو:",
  [D('0.8159'), D('0.1841'), D('0.5359'), D('0.4641')],
  r"$\sigma=10$ ، $z=\dfrac{71-80}{10}=-0.9$ ، و $P(Z>-0.9)=P(Z<0.9)=0.8159$",
  truth=1 - Ph(R(-9, 10)), tag='التوزيع الطبيعي: حساب احتمال',
  lead=ztable_note([29, 30], 0, 0.9, 0.95, 1.7, 1.75), group=2),
# 2026r #25 / 2023 #25: x from an upper-tail probability (shared table); options = mu + z sigma, the z itself, z sigma (mu
# forgotten), mu + z sigma^2 (the variance used)
Q('n8q30', U7[2], 'medium',
  r"إذا كان: $X\sim N(30,\,9)$ ، فإنّ قيمة $x$ التي تُحقّق الاحتمال $P(X>x)=0.0446$ هي:",
  [D('35.1'), D('1.7'), D('5.1'), D('45.3')],
  r"$P(X<x)=1-0.0446=0.9554=P(Z<1.7)$ ، إذن $z=1.7$ ، و $x=30+1.7(3)=35.1$",
  truth=lambda: 30 + 3*[z_ for z_ in (R(9, 10), R(95, 100), R(17, 10), R(175, 100)) if Ph(z_) == 1 - R('0.0446')][0],
  tag='التوزيع الطبيعي: إيجاد قيمة من احتمال'),
]

# ================================================================== PAPER 9
mu = Symbol('mu', positive=True)
ZS9 = (0, R('0.67'), R('0.8'), R('0.84'), R('1.4'), R('1.5'))     # the shared normal table of items 28-30


# ---------------------------------------------------------------- figures
def area_nonum(f_, a_, b_, xlim, ylim, lab):
    """2025 #3 as the ministry draws it: the shaded first-quadrant region under the curve, axes x, y and the origin 0
    only (no values on the axes; the student finds the limits from the formula)"""
    def draw(fig, ax):
        region5(f_, 0*x, a_, b_, xlim, ylim, [lab])(fig, ax)
        ax.set_xticks([]); ax.set_yticks([])
        ax.text(-0.09*(xlim[1] - xlim[0]), -0.07*(ylim[1] - ylim[0]), '$0$', fontsize=11)
    return draw


def shaded_k(f_, lo, hi, xlim, ylim, ticks, label):
    """2024s #8 as the ministry draws it: a decreasing curve with arrowheads at both ends, the region under it from lo
    to hi shaded and closed by a vertical segment; only the x ticks lo and hi are labelled (no y values)"""
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        ff = lambdify(x, f_, 'numpy')
        xs = np.linspace(xlim[0] + 0.1, xlim[1] - 0.45, 400)
        ax.plot(xs, ff(xs), color='#1f5fbf', lw=1.8)
        for x1, x2 in ((xs[1], xs[0]), (xs[-2], xs[-1])):
            ax.annotate('', xy=(x2, float(ff(x2))), xytext=(x1, float(ff(x1))),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.4, mutation_scale=12))
        xr = np.linspace(float(lo), float(hi), 200)
        ax.fill_between(xr, ff(xr), 0*xr, color='#9cc3ef', alpha=0.85)
        ax.plot([float(hi)]*2, [0, float(f_.subs(x, hi))], color='#444', lw=1)
        ax.set_xticks([float(v_) for v_ in ticks]); ax.set_xticklabels(list(ticks.values()))
        ax.set_yticks([])
        ax.text(*label, color='#1f5fbf', fontsize=12)
    return draw


def cube_fig9(s_, name, vertex, off):
    """2025 #19 as the ministry draws it: a shaded cube in the first octant with one vertex at the origin O and its
    edges on the axes (x toward the lower left, y to the right, z up), the edges at O dashed; only one more vertex is
    labelled and no numbers are written on the figure"""
    from matplotlib.patches import Polygon
    def proj(p_):
        x_, y_, z_ = p_
        return np.array([-0.7*x_ + y_, -0.5*x_ - 0.25*y_ + z_], dtype=float)
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        corner = lambda i_, j_, l_: proj((i_*s_, j_*s_, l_*s_))
        faces = [([(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)], '#e3ecf7'),
                 ([(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)], '#c9daf0'),
                 ([(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)], '#afc8e8')]
        for vs, col in faces:
            ax.add_patch(Polygon([corner(*v_) for v_ in vs], closed=True, facecolor=col, edgecolor='none', zorder=1))
        cs = [(i_, j_, l_) for i_ in (0, 1) for j_ in (0, 1) for l_ in (0, 1)]
        for p1 in cs:
            for p2 in cs:
                if p1 < p2 and sum(abs(u1 - u2) for u1, u2 in zip(p1, p2)) == 1:
                    q1, q2 = corner(*p1), corner(*p2)
                    hidden = (0, 0, 0) in (p1, p2)
                    ax.plot([q1[0], q2[0]], [q1[1], q2[1]], ls='--' if hidden else '-', color='#555' if hidden else '#333',
                            lw=1.1 if hidden else 1.4, zorder=2)
        for end, lab in (((1.55*s_, 0, 0), 'x'), ((0, 1.5*s_, 0), 'y'), ((0, 0, 1.5*s_), 'z')):
            start = proj(tuple(s_ if c_ else 0 for c_ in end))
            tip = proj(end)
            ax.plot([start[0], tip[0]], [start[1], tip[1]], color='#1f5fbf', lw=1.2, zorder=2)
            u_ = (tip - start)/np.linalg.norm(tip - start)
            ax.annotate('', xy=tip, xytext=tip - 0.12*s_*u_, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2))
            ax.text(*(tip + 0.13*s_*u_), f'${lab}$', color='#1f5fbf', fontsize=12, ha='center', va='center')
        o_ = proj((0, 0, 0))
        ax.plot(*o_, 'o', color='#555', ms=2.5, zorder=3)
        ax.text(o_[0] + 0.07*s_, o_[1] + 0.09*s_, '$O$', fontsize=11, zorder=3, color='#333')
        q_ = proj(vertex)
        ax.plot(*q_, 'o', color='#222', ms=3.5, zorder=3)
        ax.text(q_[0] + off[0]*s_, q_[1] + off[1]*s_, f'${name}$', fontsize=13, ha='center', va='center', zorder=3)
        ax.set_xlim(-1.35*s_, 1.75*s_); ax.set_ylim(-1.1*s_, 1.75*s_)
    return draw


def ln_opt(name, p_, d_):
    """a line option named like the ministry's (r, m, n, p, q): the point and the direction are checked"""
    return O(r'\vec{\mathbf{' + name + '}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')


# parallelogram DEFG (D top left, E bottom left, F bottom right, G top right), DG = 5b, DE = 8a,
# Y on EF with EY = 4YF, Z on GF produced with GF = 4FZ (D, Y, Z collinear, as in the ministry's figure)
pg9 = plane_pts((0.5, 2.6), (-0.07, -0.27), (0.85, 0.0),
                {'D': 0, 'E': 8*va, 'F': 8*va + 5*vb, 'G': 5*vb, 'Y': 8*va + 4*vb, 'Z': 10*va + 5*vb})

P9 = [
# ---------------- unit 5
# 2026 #26: integral of cot(kx); options = ln|sin| vs -ln|cos| (the antiderivative of tan) x coefficient 1/3 (divided by the chain factor) vs 3 (multiplied)
Q('n9q1', U5[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cot 3x', cot(3*x))),
  [A(r'\frac{1}{3}\ln|\sin 3x|+C', log(sin(3*x))/3), A(r'3\ln|\sin 3x|+C', 3*log(sin(3*x))),
   A(r'-\frac{1}{3}\ln|\cos 3x|+C', -log(cos(3*x))/3), A(r'-3\ln|\cos 3x|+C', -3*log(cos(3*x)))],
  r"$\displaystyle\int\cot3x\,dx=\int\frac{\cos3x}{\sin3x}\,dx=\frac13\ln|\sin3x|+C$ (نقسم على معامل $x$ وهو $3$)",
  truth=cot(3*x), tag='تكامل الاقترانات المثلثية'),
# 2026 #27: a^(mx+n) divided by ln a; options = exponent 3x+1 (chain factor 3 absorbed) vs 3x+2 (forgotten) x (ln 3)^2 vs ln 3
Q('n9q2', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{3^{3x+2}}{\ln 3}', 3**(3*x+2)/log(3))),
  [A(r'\frac{3^{3x+1}}{(\ln 3)^{2}}+C', 3**(3*x+1)/log(3)**2), A(r'\frac{3^{3x+2}}{(\ln 3)^{2}}+C', 3**(3*x+2)/log(3)**2),
   A(r'\frac{3^{3x+1}}{\ln 3}+C', 3**(3*x+1)/log(3)), A(r'\frac{3^{3x+2}}{\ln 3}+C', 3**(3*x+2)/log(3))],
  r"$\displaystyle\frac{1}{\ln3}\int3^{3x+2}dx=\frac{1}{\ln3}\cdot\frac{3^{3x+2}}{3\ln3}=\frac{3^{3x+1}}{(\ln3)^2}+C$",
  truth=3**(3*x+2)/log(3), tag='تكامل الاقتران الأسي'),
# 2025 #1: sum-to-product turns the integrand into a constant (here the sum is on top, so the constant is 2);
# options = sign x 2 vs 1 (the factor 2 of the identity forgotten)
Q('n9q3', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\cos 2x+\cos 4x}{\cos x\,\cos 3x}', (cos(2*x)+cos(4*x))/(cos(x)*cos(3*x)))),
  [A(r'2x+C', 2*x), A(r'-2x+C', -2*x), A(r'x+C', x), A(r'-x+C', -x)],
  r"$\cos4x+\cos2x=2\cos3x\cos x$ ، فالمقدار يساوي $2$ ، و $\displaystyle\int2\,dx=2x+C$",
  truth=(cos(2*x)+cos(4*x))/(cos(x)*cos(3*x)), tag='تكامل باستعمال تحويل المجموع إلى ضرب'),
# 2024 #5: f from f' = (a e^x + b)^2 and f(0); all four options pass f(0) = 13/2 and differ in the expansion or the
# integration (1/2 of e^(2x) forgotten, the 2ab term halved, the 2ab term dropped)
IndexQ('n9q4', U5[1], 'medium',
  F(r"إذا كان: $f'(x)=«0»$ ، وكان: $f(0)=\dfrac{13}{2}$ ، فإنّ قاعدة الاقتران $f$ هي:", (r'(e^{x}+3)^{2}', (exp(x)+3)**2)),
  [O(r'f(x)=\frac{1}{2}e^{2x}+6e^{x}+9x', exp(2*x)/2+6*exp(x)+9*x, 'eq'),
   O(r'f(x)=e^{2x}+6e^{x}+9x-\frac{1}{2}', exp(2*x)+6*exp(x)+9*x-R(1, 2), 'eq'),
   O(r'f(x)=\frac{1}{2}e^{2x}+3e^{x}+9x+3', exp(2*x)/2+3*exp(x)+9*x+3, 'eq'),
   O(r'f(x)=\frac{1}{2}e^{2x}+9x+6', exp(2*x)/2+9*x+6, 'eq')],
  r"$(e^x+3)^2=e^{2x}+6e^x+9$ ، إذن $f(x)=\frac12e^{2x}+6e^x+9x+C$" "\n" r"$f(0)=\frac12+6+C=\frac{13}{2}$ ، إذن $C=0$",
  truth=lambda vals: only(vals, lambda F_: ode_ok(F_, (exp(x)+3)**2, 0, R(13, 2))), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
# 2023s #4: definite integral of a piecewise function split at x = 1; options = first piece only, second piece only,
# the first piece with its sign slipped (chain factor -2)
Q('n9q5', U5[1], 'easy',
  F(r"إذا كان: $f(x)=\begin{cases}«0» & ,\ x<1\\ «1» & ,\ x\ge 1\end{cases}$ ، فإنّ قيمة $\displaystyle\int_{0}^{3}f(x)\,dx$ تساوي:",
    (r'(1-2x)^{2}', (1-2*x)**2), (r'2x+3', 2*x+3)),
  [O(r'\frac{43}{3}', R(43, 3)), O(r'\frac{1}{3}', R(1, 3)), O('14', 14), O(r'\frac{41}{3}', R(41, 3))],
  r"$\displaystyle\int_0^1(1-2x)^2dx=\left[-\frac{(1-2x)^3}{6}\right]_0^1=\frac16+\frac16=\frac13$ ، و $\displaystyle\int_1^3(2x+3)dx=\big[x^2+3x\big]_1^3=14$" "\n"
  r"المجموع $\frac13+14=\frac{43}{3}$",
  truth=ig((1-2*x)**2, (x, 0, 1)) + ig(2*x+3, (x, 1, 3)), tag='التكامل المحدود: اقتران متعدد القاعدة'),
# 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2, u = tan kx; options = coefficient 1/12 (divided by the chain factor 4 and
# the power 3) vs 4/3 (multiplied by the chain factor) x tan vs sec
Q('n9q6', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sin^{2}4x}{\cos^{4}4x}', sin(4*x)**2/cos(4*x)**4)),
  [A(r'\frac{1}{12}\tan^{3}4x+C', tan(4*x)**3/12), A(r'\frac{4}{3}\tan^{3}4x+C', 4*tan(4*x)**3/3),
   A(r'\frac{1}{12}\sec^{3}4x+C', sec(4*x)**3/12), A(r'\frac{4}{3}\sec^{3}4x+C', 4*sec(4*x)**3/3)],
  r"المقدار $=\tan^24x\sec^24x$ ، وبالتعويض $u=\tan4x$ ، $du=4\sec^24x\,dx$: $\displaystyle\frac14\int u^2du=\frac{u^3}{12}=\frac{1}{12}\tan^34x+C$",
  truth=sin(4*x)**2/cos(4*x)**4, tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
# 2025 #7: e^(kx)(1 - 1/e^x)^n = e^x (e^x - 1)^n, u = e^x - 1, definite (only the lower limit contributes);
# options = sign x power 4 vs 3 (power not raised; that slip gives the base 1 - 1/e)
Q('n9q7', U5[2], 'hard',
  F(r"قيمة: $\displaystyle\int_{-1}^{0}«0»\,dx$ هي:", (r'e^{4x}\left(1-\frac{1}{e^{x}}\right)^{3}', exp(4*x)*(1-exp(-x))**3)),
  [O(r'-\frac{1}{4}\left(\frac{1}{e}-1\right)^{4}', -(1/E-1)**4/4), O(r'-\frac{1}{4}\left(1-\frac{1}{e}\right)^{3}', -(1-1/E)**3/4),
   O(r'\frac{1}{4}\left(\frac{1}{e}-1\right)^{4}', (1/E-1)**4/4), O(r'\frac{1}{4}\left(1-\frac{1}{e}\right)^{3}', (1-1/E)**3/4)],
  r"$e^{4x}\left(1-\frac{1}{e^x}\right)^3=e^x(e^x-1)^3$ ، وبالتعويض $u=e^x-1$ ، $du=e^xdx$ ، والحدود $\frac1e-1\to0$:" "\n"
  r"$\displaystyle\int_{\frac1e-1}^{0}u^3du=0-\frac14\left(\frac1e-1\right)^4=-\frac14\left(\frac1e-1\right)^4$",
  truth=ig(exp(4*x)*(1-exp(-x))**3, (x, -1, 0)), tag='التكامل بالتعويض بعد التبسيط'),
# 2024s #3: kx/(1 - cx^2), u = 1 - cx^2; options = sign (du = -8x dx) x 1/4 vs 1/2 (derivative of 4x^2 taken as 4x)
Q('n9q8', U5[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2x}{1-4x^{2}}', 2*x/(1-4*x**2))),
  [A(r'-\frac{1}{4}\ln|1-4x^{2}|+C', -log(1-4*x**2)/4), A(r'\frac{1}{4}\ln|1-4x^{2}|+C', log(1-4*x**2)/4),
   A(r'-\frac{1}{2}\ln|1-4x^{2}|+C', -log(1-4*x**2)/2), A(r'\frac{1}{2}\ln|1-4x^{2}|+C', log(1-4*x**2)/2)],
  r"بالتعويض $u=1-4x^2$ ، $du=-8x\,dx$: $\displaystyle\int\frac{2x}{1-4x^2}dx=-\frac14\int\frac{du}{u}=-\frac14\ln|1-4x^2|+C$",
  truth=2*x/(1-4*x**2), tag='التكامل بالتعويض: لوغاريتمات'),
# 2023 #6: displacement from v = kt/(t^2 + c) (ln form); options = sign (limits subtracted the wrong way) x ln 4 vs ln 9
# (ln 12 - ln 3 taken as ln(12 - 3))
Q('n9q9', U5[2], 'medium',
  F(r"يتحرك جُسيم في مسار مستقيم، وتُعطى سرعته المتجهة بالاقتران: $v(t)=«0»$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته المتجهة بالمتر لكل ثانية. إزاحة الجُسيم بالأمتار في الفترة $[0,\,3]$ تساوي:",
    (r'\frac{4t}{t^{2}+3}', 4*t/(t**2+3))),
  [O(r'2\ln 4', 2*log(4)), O(r'-2\ln 4', -2*log(4)), O(r'2\ln 9', 2*log(9)), O(r'-2\ln 9', -2*log(9))],
  r"$\displaystyle\int_0^3\frac{4t}{t^2+3}dt=\big[2\ln(t^2+3)\big]_0^3=2\ln12-2\ln3=2\ln\frac{12}{3}=2\ln4$",
  truth=ig(4*t/(t**2+3), (t, 0, 3)), tag='الحركة: الإزاحة من السرعة'),
# 2024 #9: k/((x - a)(x + a)) by partial fractions; options = the sign of B lost, "ln of the denominator" shortcuts x6 and x3
Q('n9q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{6}{(x-3)(x+3)}', 6/((x-3)*(x+3)))),
  [A(r'\ln|x-3|-\ln|x+3|+C', log(x-3)-log(x+3)), A(r'\ln|x-3|+\ln|x+3|+C', log(x-3)+log(x+3)),
   A(r'6\ln|x^{2}-9|+C', 6*log(x**2-9)), A(r'3\ln|x^{2}-9|+C', 3*log(x**2-9))],
  r"$\dfrac{6}{(x-3)(x+3)}=\dfrac{A}{x-3}+\dfrac{B}{x+3}$: عند $x=3$: $6=6A$ ، $A=1$ ، وعند $x=-3$: $6=-6B$ ، $B=-1$" "\n"
  r"الناتج: $\ln|x-3|-\ln|x+3|+C$",
  truth=6/((x-3)*(x+3)), tag='التكامل بالكسور الجزئية: عوامل خطية'),
# 2025s #5: improper fraction, one-step division, match the coefficient a of ax^2; options = reciprocal pairs (2, 1/2), (4, 1/4)
Q('n9q11', U5[3], 'medium',
  F(r"إذا كان: $\displaystyle\int «0»\,dx=ax^{2}+3\ln|x+2|+C$ ، فإنّ قيمة الثابت $a$ هي:", (r'\frac{4x^{2}+8x+3}{x+2}', (4*x**2+8*x+3)/(x+2))),
  [O('2', 2), O(r'\frac{1}{2}', R(1, 2)), O('4', 4), O(r'\frac{1}{4}', R(1, 4))],
  r"$\dfrac{4x^2+8x+3}{x+2}=4x+\dfrac{3}{x+2}$ ، و $\displaystyle\int\left(4x+\frac{3}{x+2}\right)dx=2x^2+3\ln|x+2|+C$ ، إذن $a=2$",
  truth=lambda: (lambda qr: ig(qr[0], x).coeff(x, 2) if qr[1] == 3 else None)(div(4*x**2+8*x+3, x+2, x)),
  tag='التكامل بالكسور الجزئية: كسر غير فعلي'),
# 2023 #10: by parts, kx cos(kx); options = x sin vs x cos (v not integrated) x sign of the 1/4 term
Q('n9q12', U5[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'4x\cos 4x', 4*x*cos(4*x))),
  [A(r'x\sin 4x+\frac{1}{4}\cos 4x+C', x*sin(4*x)+cos(4*x)/4), A(r'x\sin 4x-\frac{1}{4}\cos 4x+C', x*sin(4*x)-cos(4*x)/4),
   A(r'x\cos 4x+\frac{1}{4}\sin 4x+C', x*cos(4*x)+sin(4*x)/4), A(r'x\cos 4x-\frac{1}{4}\sin 4x+C', x*cos(4*x)-sin(4*x)/4)],
  r"بالأجزاء: $u=x$ ، $dv=4\cos4x\,dx$ ، $v=\sin4x$: $\displaystyle x\sin4x-\int\sin4x\,dx=x\sin4x+\frac14\cos4x+C$",
  truth=4*x*cos(4*x), tag='التكامل بالأجزاء'),
# 2023s #9: definite integral of ln x^n by parts; options = the lower-limit value ignored, its sign slipped, the factor 3
# of ln x^3 = 3 ln x forgotten
Q('n9q13', U5[4], 'medium',
  F(r"قيمة: $\displaystyle\int_{1}^{e}«0»\,dx$ هي:", (r'\ln x^{3}', log(x**3))),
  [O('3', 3), O('0', 0), O('-3', -3), O('1', 1)],
  r"$\ln x^3=3\ln x$ ، و $\displaystyle\int\ln x\,dx=x\ln x-x$" "\n" r"$3\big[x\ln x-x\big]_1^e=3\big[(e-e)-(0-1)\big]=3$",
  truth=ig(log(x**3), (x, 1, E)), tag='التكامل المحدود بالأجزاء'),
# 2025 #3: area in the first quadrant under c - a^x (figure without numbers; the limits 0 and 2 come from the formula);
# options = divided vs multiplied by ln 3 x the lower-limit value 3^0 = 1 kept or forgotten
Q('n9q14', U5[5], 'medium',
  F(r"إذا كان الاقتران المُبيّن مُنحناه في الشكل الآتي هو: $f(x)=«0»$ ، فإنّ مساحة المنطقة المُظلَّلة بالوحدات المربعة هي:", (r'9-3^{x}', 9-3**x)),
  [O(r'18-\frac{8}{\ln 3}', 18-8/log(3)), O(r'18-\frac{9}{\ln 3}', 18-9/log(3)), O(r'18-8\ln 3', 18-8*log(3)), O(r'18-9\ln 3', 18-9*log(3))],
  r"المنحنى يقطع المحور $x$ عند $3^x=9$ ، أي $x=2$ ، فالمساحة $\displaystyle\int_0^2(9-3^x)dx=\left[9x-\frac{3^x}{\ln3}\right]_0^2$" "\n"
  r"$=\left(18-\frac{9}{\ln3}\right)-\left(0-\frac{1}{\ln3}\right)=18-\frac{8}{\ln3}$",
  truth=ig(9-3**x, (x, 0, 2)),
  figure=figure('n9q14', area_nonum(9-3**x, 0, 2, (-0.8, 2.8), (-2.6, 10.6), (1.45, 5.0, r'$f(x)$', '#1f5fbf')), 3.4, 2.9),
  tag='المساحة تحت منحنى من الشكل'),
# 2024s #8: k from the shaded area under k/(x + c) (figure with the ticks 0 and 6 only); options = k, the ratio of logs
# inverted, the lower-limit term ln 2 forgotten (k ln 8 = ln 64), both
Q('n9q15', U5[5], 'medium',
  F(r"يُبيّن الشكل الآتي منحنى الاقتران: $f(x)=«0»$ ، حيث $k>0$. إذا كانت مساحة المنطقة المُظلَّلة تساوي $\ln 64$ وحدة مربعة، فإنّ قيمة الثابت $k$ هي:", (r'\frac{k}{x+2}', k/(x+2))),
  [O('3', 3), O(r'\frac{1}{3}', R(1, 3)), O('2', 2), O(r'\frac{1}{2}', R(1, 2))],
  r"$\displaystyle\int_0^6\frac{k}{x+2}dx=k\big[\ln(x+2)\big]_0^6=k(\ln8-\ln2)=k\ln4$ ، و $k\ln4=\ln64=3\ln4$ ، إذن $k=3$",
  truth=lambda: solve(ig(k/(x+2), (x, 0, 6)) - log(64), k)[0],
  figure=figure('n9q15', shaded_k(3/(x+2), 0, 6, (-1.0, 8.0), (-0.35, 3.0), {0: '$0$', 6: '$6$'}, (1.6, 1.35, r'$f(x)=\frac{k}{x+2}$')), 3.8, 2.8),
  tag='المساحة: إيجاد ثابت'),
# 2024 #11: general solution of dy/dx = 1/(x y^n); options = variables in place vs swapped x the factor y^2 integrated vs ignored
IndexQ('n9q16', U5[6], 'medium',
  F(r"الحلّ العامّ للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»\ ,\ x>0,\ y>0$ هو:", (r'\frac{1}{xy^{2}}', 1/(x*y**2))),
  [O(r'y^{3}=\ln x^{3}+C', y**3-log(x**3)-Cc, 'rel'), O(r'y=\ln x+C', y-log(x)-Cc, 'rel'),
   O(r'x^{3}=\ln y^{3}+C', x**3-log(y**3)-Cc, 'rel'), O(r'x=\ln y+C', x-log(y)-Cc, 'rel')],
  r"بفصل المتغيرات: $y^2\,dy=\dfrac{dx}{x} \Rightarrow \dfrac{y^3}{3}=\ln x+C \Rightarrow y^3=3\ln x+C=\ln x^3+C$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, 1/(x*y**2))), tag='المعادلات التفاضلية: الحل العام'),
# ---------------- unit 6
# 2024 #20: parallel vectors with an unknown in each -> a + b; options = a + b, the sign of k slipped, a - b, one unknown (b) only
Q('n9q17', U6[1], 'medium',
  r"إذا كان: $\vec{\mathbf{u}}=\langle -4,\,2-a,\,-3\rangle$ ، $\vec{\mathbf{v}}=\langle b+2,\,-8,\,6\rangle$ ، وكان: $\vec{\mathbf{u}}\parallel\vec{\mathbf{v}}$ ، فإنّ قيمة $(a+b)$ هي:",
  [O('4', 4), O('-4', -4), O('-8', -8), O('6', 6)],
  r"$\vec{\mathbf{v}}=k\vec{\mathbf{u}}$: من المركبة الثالثة $6=-3k \Rightarrow k=-2$" "\n"
  r"$b+2=-2(-4)=8 \Rightarrow b=6$ ، و $-8=-2(2-a) \Rightarrow 2-a=4 \Rightarrow a=-2$ ، إذن $a+b=4$",
  truth=lambda: (lambda s_: s_[a] + s_[b])(solve(list(V(-4, 2-a, -3).cross(V(b+2, -8, 6))), [a, b], dict=True)[0]),
  tag='توازي المتجهات وإيجاد ثابت'),
# 2026r #18: parallelogram, Y on a side with EY = 4YF, Z on a produced side, k from the given YZ; options = consecutive integers
Q('n9q18', U6[1], 'hard',
  r"في الشكل الآتي $DEFG$ متوازي أضلاع. إذا كان: $\overrightarrow{DG}=5\vec{\mathbf{b}}$ ، و $\overrightarrow{DE}=8\vec{\mathbf{a}}$ ، وكان: $\overrightarrow{GF}=k\,\overrightarrow{FZ}$ ، وكانت النقطة $Y$ تقع على $\overline{EF}$ حيث: $EY=4YF$ ، و $\overrightarrow{YZ}=\vec{\mathbf{b}}+2\vec{\mathbf{a}}$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('4', 4), O('5', 5), O('3', 3), O('2', 2)],
  r"$\overrightarrow{YF}=\frac15\overrightarrow{EF}=\frac15(5\vec{\mathbf{b}})=\vec{\mathbf{b}}$ ، إذن $\overrightarrow{FZ}=\overrightarrow{YZ}-\overrightarrow{YF}=2\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{GF}=\overrightarrow{DE}=8\vec{\mathbf{a}}=4(2\vec{\mathbf{a}})=4\,\overrightarrow{FZ}$ ، إذن $k=4$",
  truth=lambda: solve_k((8*va + 5*vb + 8*va/k) - (8*va + R(4, 5)*5*vb), vb + 2*va),
  figure=figure('n9q18', poly_fig(pg9, [('E', 'F'), ('G', 'F'), ('F', 'Z')],
                                    [('D', 'G', r'$5\vec{\mathbf{b}}$', (-0.2, 0.18)), ('D', 'E', r'$8\vec{\mathbf{a}}$', (-0.78, 0.0))],
                                    {'D': (-0.22, 0.12), 'G': (0.1, 0.1), 'E': (-0.3, -0.3), 'F': (0.14, 0.04), 'Y': (-0.12, -0.42), 'Z': (0.12, -0.28)},
                                    thick=[('D', 'Z')]), 3.8, 2.6),
  tag='المتجهات في الأشكال الهندسية والنسبة'),
# 2024s #15: PQ = QR with an unknown coordinate -> two values; options = mirrored pairs: right, the k - (-1) sign slip,
# the x and y parts of QR forgotten, both
Q('n9q19', U6[1], 'medium',
  r"إذا كانت: $P(5,\,-1,\,2)\ ,\ Q(3,\,5,\,-1)\ ,\ R(9,\,2,\,k)$ نقاطًا في الفضاء، وكانت $\overline{PQ}=\overline{QR}$ ، فإنّ قِيَم $k$ المُمكِنة هي:",
  [pair_opt(r'-3,\ 1', -3, 1), pair_opt(r'-1,\ 3', -1, 3), pair_opt(r'-8,\ 6', -8, 6), pair_opt(r'-6,\ 8', -6, 8)],
  r"$PQ^2=(-2)^2+6^2+(-3)^2=49$ ، و $QR^2=6^2+(-3)^2+(k+1)^2=45+(k+1)^2$" "\n"
  r"$45+(k+1)^2=49 \Rightarrow (k+1)^2=4 \Rightarrow k=1$ أو $k=-3$",
  truth=lambda: (lambda w_, u_: FiniteSet(*solve(w_.dot(w_) - u_.dot(u_), k)))(V(9, 2, k) - V(3, 5, -1), V(3, 5, -1) - V(5, -1, 2)),
  tag='المتجهات: المقدار وإيجاد ثابت'),
# 2025s #15: displacement vector from C to A (A - C) with a double negative in one component; options = sign of the
# x component x the y component right or slipped (10 + (-5))
Q('n9q20', U6[1], 'easy',
  r"إذا كانت: $A(-3,\,10,\,6)\ ,\ C(0,\,-5,\,2)$ ، فإنّ متجه الإزاحة من النقطة $C$ إلى النقطة $A$ هو:",
  [vec_opt(-3, 15, 4), vec_opt(3, 15, 4), vec_opt(-3, 5, 4), vec_opt(3, 5, 4)],
  r"$\overrightarrow{CA}=A-C=\langle -3-0,\ 10-(-5),\ 6-2\rangle=\langle -3,\,15,\,4\rangle$",
  truth=T3(V(-3, 10, 6) - V(0, -5, 2)), tag='المتجهات: متجه الإزاحة'),
# 2026r #14: vector of a given magnitude in the direction of v; options = scaled vs unit vector (stopped early) x same vs
# opposite direction (all four exact)
Q('n9q21', U6[1], 'medium',
  r"المتجه الذي مقداره $21$ ، وله اتجاه المتجه $\vec{\mathbf{v}}$ نفسه، حيث: $\vec{\mathbf{v}}=\langle 3,\,-6,\,2\rangle$ هو:",
  [vec_opt(9, -18, 6), vec_opt(-9, 18, -6), vec_opt(R(3, 7), R(-6, 7), R(2, 7)), vec_opt(R(-3, 7), R(6, 7), R(-2, 7))],
  r"$|\vec{\mathbf{v}}|=\sqrt{9+36+4}=7$ ، والمتجه المطلوب $21\cdot\dfrac{\vec{\mathbf{v}}}{7}=3\vec{\mathbf{v}}=\langle 9,\,-18,\,6\rangle$",
  truth=T3(21*V(3, -6, 2)/V(3, -6, 2).norm()), tag='متجه بمقدار معلوم في اتجاه معلوم'),
# 2024s #18: line through a position vector with a missing i component, parallel to a vector; options = point and direction
# swapped x the missing component put in the wrong slot (the lines are named r, m, n, q as in the model)
IndexQ('n9q22', U6[2], 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{a}}=3\hat{i}-2\hat{j}+5\hat{k}$ ، ويمرّ بنقطة متجه الموقع لها: $\vec{\mathbf{b}}=-6\hat{j}+\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة تُمثّله هي:",
  [ln_opt('n', (0, -6, 1), (3, -2, 5)), ln_opt('r', (-6, 0, 1), (3, -2, 5)), ln_opt('m', (3, -2, 5), (-6, 0, 1)), ln_opt('q', (3, -2, 5), (0, -6, 1))],
  r"متجه موقع النقطة $-6\hat{j}+\hat{k}=\langle 0,\,-6,\,1\rangle$ (المركبة الأولى صفر)، ومتجه الاتجاه $\langle 3,\,-2,\,5\rangle$" "\n"
  r"$\vec{\mathbf{n}}=\langle 0,-6,1\rangle+t\langle 3,-2,5\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((0, -6, 1), ln) and par(ln[1], (3, -2, 5))), tag='معادلة المستقيم في الفضاء'),
# 2025 #19: line through a cube vertex read from the figure and the cube's centre; options = the vertex misread (x and y
# swapped) with the right direction, lines through M along the other space diagonals (names r, m, n, p as in the model)
IndexQ('n9q23', U6[2], 'hard',
  r"إذا كان الشكل الآتي يُمثّل مكعبًا طول ضلعه $4$ وحدات، وكانت النقطة $M$ تُمثّل مركز المكعب، فإنّ للمستقيم $l$ المارّ بالنقطتين $C$ و $M$ معادلة متجهة تُمثّله هي:",
  [ln_opt('r', (4, 0, 4), (1, -1, 1)), ln_opt('m', (0, 4, 4), (1, -1, 1)), ln_opt('n', (2, 2, 2), (1, -1, -1)), ln_opt('p', (2, 2, 2), (-1, -1, 1))],
  r"من الشكل $C(4,\,0,\,4)$ ، والمركز $M(2,\,2,\,2)$ ، و $\overrightarrow{CM}=\langle -2,\,2,\,-2\rangle\parallel\langle 1,\,-1,\,1\rangle$" "\n"
  r"$\vec{\mathbf{r}}=\langle 4,0,4\rangle+t\langle 1,-1,1\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((4, 0, 4), ln) and on_line((2, 2, 2), ln)),
  figure=figure('n9q23', cube_fig9(4, 'C', (4, 0, 4), (-0.13, 0.05)), 3.3, 3.0),
  tag='المستقيم المار بنقطتين من شكل ثلاثي الأبعاد'),
# 2026 #43: PR built from PQ and RQ, then PQ . PR; options = sign (RP used) x RQ used directly (+-PQ . RQ)
Q('n9q24', U6[3], 'hard',
  r"إذا كانت $P,\ Q,\ R$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{PQ}=\langle 1,\,3,\,-2\rangle$ ، و $\overrightarrow{RQ}=\langle 3,\,4,\,-3\rangle$ ، فإنّ $\overrightarrow{PQ}\cdot\overrightarrow{PR}$ يساوي:",
  [O('-7', -7), O('7', 7), O('21', 21), O('-21', -21)],
  r"$\overrightarrow{PR}=\overrightarrow{PQ}+\overrightarrow{QR}=\overrightarrow{PQ}-\overrightarrow{RQ}=\langle -2,\,-1,\,1\rangle$" "\n"
  r"$\overrightarrow{PQ}\cdot\overrightarrow{PR}=-2-3-2=-7$",
  truth=V(1, 3, -2).dot(V(1, 3, -2) - V(3, 4, -3)), tag='الضرب القياسي ومتجهات بين نقاط'),
# 2024s #20: |b| from the angle, the dot product and |a|; options = cos ignored, multiplied by cos instead of dividing, |a| ignored
Q('n9q25', U6[3], 'medium',
  r"إذا كان قياس الزاوية بين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو $30^\circ$ ، وكان: $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=18$ ، وكان: $|\vec{\mathbf{a}}|=4$ ، فإنّ مقدار $\vec{\mathbf{b}}$ هو:",
  [O(r'3\sqrt{3}', 3*sqrt(3)), O(r'\frac{9}{2}', R(9, 2)), O(r'\frac{9\sqrt{3}}{4}', 9*sqrt(3)/4), O(r'12\sqrt{3}', 12*sqrt(3))],
  r"$18=4|\vec{\mathbf{b}}|\cos30^\circ=2\sqrt3\,|\vec{\mathbf{b}}| \Rightarrow |\vec{\mathbf{b}}|=\dfrac{9}{\sqrt3}=3\sqrt3$",
  truth=18/(4*cos(pi/6)), tag='الضرب القياسي: إيجاد مقدار متجه'),
# ---------------- unit 7
# 2023 #22: at least n - 1 successes of n, options as expressions (n(1 - p) = 1 makes the coefficient vanish);
# options = X = n only, one ordering of the n - 1 successes, the second term written with (1 - p)^n
Q('n9q26', U7[1], 'medium',
  r"إذا كان احتمال أن يُسجّل لاعب كرة سلّة رمية حرّة يساوي $\dfrac{2}{3}$ ، وسدّد هذا اللاعب $3$ رميات حرّة متتالية، فإنّ احتمال أن يُسجّل $2$ منها على الأقل هو:",
  [O(r'\left(\frac{2}{3}\right)^{2}+\left(\frac{2}{3}\right)^{3}', R(2, 3)**2+R(2, 3)**3), O(r'\left(\frac{2}{3}\right)^{3}', R(2, 3)**3),
   O(r'\left(\frac{2}{3}\right)^{2}\cdot\frac{1}{3}', R(2, 3)**2*R(1, 3)), O(r'\left(\frac{2}{3}\right)^{2}+\left(\frac{1}{3}\right)^{3}', R(2, 3)**2+R(1, 3)**3)],
  r"$X\sim B\left(3,\frac23\right)$: $P(X=2)=\binom32\left(\frac23\right)^2\frac13=\left(\frac23\right)^2$ ، و $P(X=3)=\left(\frac23\right)^3$" "\n"
  r"$P(X\ge2)=\left(\frac23\right)^2+\left(\frac23\right)^3$",
  truth=binom(3, R(2, 3), 2) + binom(3, R(2, 3), 3), tag='توزيع ذي الحدين: احتمال «على الأقل»'),
# 2024s #21: a die with more faces thrown until an event; options = (1-p)^2 p, (1-p)^2 (the final success dropped),
# (1-p) p^2 (exponents swapped), (1-p)^3 (the third throw counted as a failure). p = 1/5 (p = 1/4 would repeat the
# option values of n4q26)
Q('n9q27', U7[1], 'easy',
  r"أُلقيَ حجر نرد منتظم ذو عشرة أوجه مُرقَّمة بالأعداد من $1$ إلى $10$ عشوائيًّا بشكل مُتكرِّر حتى ظهور عدد أكبر من $8$ ، فإنّ احتمال إلقائه $3$ مرّات هو:",
  [O(r'\frac{16}{125}', R(16, 125)), O(r'\frac{16}{25}', R(16, 25)), O(r'\frac{4}{125}', R(4, 125)), O(r'\frac{64}{125}', R(64, 125))],
  r"$p=\dfrac{2}{10}=\dfrac15$ (العددان $9$ و $10$)، و $P(X=3)=\left(\dfrac45\right)^2\cdot\dfrac15=\dfrac{16}{125}$",
  truth=geo(R(2, 10), 3), tag='التوزيع الهندسي: تجربة حتى أول نجاح'),
# 2026 #49: symmetric interval P(-k/c < Z < k/c) -> k (the one table for items 28-30, like 2026 #48-50);
# options = c z, c times a neighbouring table entry (0.84 and 0.67), c / z (the equation inverted)
Q('n9q28', U7[2], 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{6}<Z<\dfrac{k}{6}\right)=0.5762$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:",
  [D('4.8'), D('5.04'), D('4.02'), D('7.5')],
  r"$2P\left(Z<\frac k6\right)-1=0.5762 \Rightarrow P\left(Z<\frac k6\right)=0.7881$ ، ومن الجدول $\frac k6=0.8$ ، إذن $k=4.8$",
  truth=lambda: [zz*6 for zz in ZS9 if 2*Ph(zz) - 1 == R('0.5762')][0],
  lead=ztable_note([28, 29, 30], *ZS9), group=3, tag='التوزيع الطبيعي: فترة متماثلة وإيجاد ثابت'),
# 2026 #50 asked for the mean: the percentage above a value -> mu; options = mu, the sign slipped (x + z sigma),
# z not multiplied by sigma, the variance used as sigma
Q('n9q29', U7[2], 'hard',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(\mu,\,0.25)$ ، على أطوال قِطَع الكوابل (بالمتر) التي تُنتجها آلة في أحد المصانع. إذا كانت أطوال $8.08\%$ منها تزيد على $50.7\ \text{m}$ ، فإنّ قيمة الوسط الحسابي $\mu$ لأطوال القِطَع هي:",
  [D('50', 'm'), D('51.4', 'm'), D('49.3', 'm'), D('50.35', 'm')],
  r"$P(X<50.7)=1-0.0808=0.9192 \Rightarrow z=1.4$ ، و $\sigma=\sqrt{0.25}=0.5$" "\n" r"$50.7=\mu+1.4(0.5) \Rightarrow \mu=50\ \text{m}$",
  truth=lambda: [R('50.7') - zz*sqrt(R('0.25')) for zz in ZS9 if Phi4(zz) == 1 - R('0.0808')][0],
  tag='التوزيع الطبيعي: إيجاد الوسط الحسابي'),
# 2023s #25: sigma given in terms of mu, P(X > 2mu) from the table; options = z = 1.5 vs 0.67 (the factor of sigma
# inverted) x complement or the table value
Q('n9q30', U7[2], 'medium',
  r"إذا كان: $\mu>0\ ,\ X\sim N\left(\mu,\,\dfrac{4\mu^{2}}{9}\right)$ ، فإنّ قيمة $P(X>2\mu)$ تساوي:",
  [D('0.0668'), D('0.9332'), D('0.2514'), D('0.7486')],
  r"$\sigma=\dfrac{2\mu}{3}$ ، و $z=\dfrac{2\mu-\mu}{2\mu/3}=1.5$ ، إذن $P(X>2\mu)=1-0.9332=0.0668$",
  truth=lambda: 1 - Ph(simplify((2*mu - mu)/sqrt(4*mu**2/9))), tag='التوزيع الطبيعي: حساب احتمال'),
]

# ================================================================== PAPER 10
class NamedIJK(O):
    """an option that names its vector, '\\vec{r} = a i + b j + c k' (2024 #18 gives every option its own letter); the
    part after '=' is parsed as an i, j, k vector"""
    def __init__(self, name, *c_):
        super().__init__(r'\vec{\mathbf{' + name + '}}=' + ijk(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'ijk')

    def parsed(self):
        return O(self.tex.split('=', 1)[1], self.val, 'ijk').parsed()


def cube_fig10(s_, name, pt):
    """2023 #14 as the ministry draws it: a shaded cube in the first octant with its hidden back vertex at the origin (not
    labelled), x toward the lower left, y toward the lower right, z up (the three edges on the axes dashed); only the vertex
    pt is labelled and no length is written on the figure"""
    import numpy as np
    from matplotlib.patches import Polygon

    def proj(p_):
        x_, y_, z_ = p_
        return np.array([-0.7*x_ + y_, -0.5*x_ - 0.25*y_ + z_], dtype=float)

    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        s = s_
        vtx = {'O': (0, 0, 0), 'E': (s, 0, 0), 'F': (s, s, 0), 'G': (0, s, 0),
               'D': (0, 0, s), 'A': (s, 0, s), 'B': (s, s, s), 'C': (0, s, s)}
        for face, col in (('DABC', '#e4e4e4'), ('EFBA', '#c8c8c8'), ('GFBC', '#d6d6d6')):
            ax.add_patch(Polygon([proj(vtx[q_]) for q_ in face], closed=True, facecolor=col, edgecolor='none', alpha=0.9, zorder=1))
        for e in ('EF', 'FG', 'EA', 'FB', 'GC', 'DA', 'AB', 'BC', 'CD'):
            p1, p2 = proj(vtx[e[0]]), proj(vtx[e[1]])
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#444', lw=1.4, zorder=3)
        for e in ('OE', 'OG', 'OD'):
            p1, p2 = proj(vtx[e[0]]), proj(vtx[e[1]])
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#444', lw=1.2, ls='--', zorder=2)
        seen = [proj(v_) for v_ in vtx.values()]
        for v_, lab in (('E', 'x'), ('G', 'y'), ('D', 'z')):
            p1 = proj(vtx[v_]); u_ = p1/np.linalg.norm(p1); p2 = p1 + 0.45*s*u_
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#1f5fbf', lw=1.2, zorder=3)
            ax.annotate('', xy=p2, xytext=p2 - 0.1*s*u_, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2))
            ax.text(*(p2 + 0.1*s*u_), f'${lab}$', color='#1f5fbf', fontsize=13, ha='center', va='center')
            seen.append(p2 + 0.1*s*u_)
        q_ = proj(pt)
        ax.plot(*q_, 'o', color='#222', ms=3.5, zorder=4)
        lab = q_ + np.array([0.11, 0.05])*s
        ax.text(*lab, f'${name}$', fontsize=13, ha='center', va='center', zorder=4)
        seen.append(lab)
        xs, ys = [p_[0] for p_ in seen], [p_[1] for p_ in seen]
        pad = 0.08*s
        ax.set_xlim(min(xs) - pad, max(xs) + pad); ax.set_ylim(min(ys) - pad, max(ys) + pad)
    return draw


vt10 = [(0, 0), (1, -2), (3, -2), (4, 0), (6, 4), (7, 4), (8, 0)]
D10 = pw_integral(vt10, 0, 8)                     # signed area = displacement
H10 = (0, 6, 6)                                   # the labelled vertex of the cube in item 19
N10 = lambda t_: -R(1, 2)*exp(-t_/2)/(1 + exp(-t_/2))**2   # item 9: rate of change of the number of subscribers


P10 = [
# ---------------------------------------------------------------- unit 5: integration
# 2024s #2: 1/(sin^2 x cos^2 x) = 4 csc^2 2x -> -2 cot 2x (here 3x inside: 4 csc^2 6x); options = tan vs cot x sign
Q('n10q1', U5[1], 'medium',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ هو:", (r'\frac{1}{\sin^{2}3x\cos^{2}3x}', 1/(sin(3*x)**2*cos(3*x)**2))),
  [A(r'-\frac{2}{3}\cot 6x+C', -R(2, 3)*cot(6*x)), A(r'\frac{2}{3}\cot 6x+C', R(2, 3)*cot(6*x)),
   A(r'\frac{2}{3}\tan 6x+C', R(2, 3)*tan(6*x)), A(r'-\frac{2}{3}\tan 6x+C', -R(2, 3)*tan(6*x))],
  r"$\sin3x\cos3x=\frac12\sin6x$ ، إذن $\sin^23x\cos^23x=\frac14\sin^26x$ والمقدار $=4\csc^26x$" "\n"
  r"$\displaystyle\int4\csc^26x\,dx=-\frac46\cot6x+C=-\frac23\cot6x+C$",
  truth=1/(sin(3*x)**2*cos(3*x)**2), tag='تكامل باستعمال متطابقات ضعف الزاوية'),
# 2026r #4: definite integral of k/(ax + b) giving k ln m, the lower limit not giving ln 1 = 0; options = k ln m values:
# lower limit dropped (= chain factor forgotten, as in the model), ln 9 - ln 3 taken as ln 6, chain factor multiplied
Q('n10q2', U5[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{2}^{5}«0»\,dx$ هي:", (r'\frac{8}{2x-1}', 8/(2*x - 1))),
  [O(r'4\ln 3', 4*log(3)), O(r'4\ln 9', 4*log(9)), O(r'4\ln 6', 4*log(6)), O(r'16\ln 3', 16*log(3))],
  r"$\displaystyle\int\frac{8}{2x-1}dx=\frac82\ln|2x-1|=4\ln|2x-1|$" "\n"
  r"$4\big[\ln|2x-1|\big]_2^5=4(\ln9-\ln3)=4\ln3$",
  truth=ig(8/(2*x - 1), (x, 2, 5)), tag='التكامل المحدود: ناتج لوغاريتمي'),
# 2026 #28: definite integral of sin^2 (power reduction) = a pi; options = +-1/6, +-1/3 (the 1/2 of the identity dropped)
Q('n10q3', U5[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{\frac{\pi}{3}}«0»\,dx=a\pi$ ، فإنّ قيمة الثابت $a$ هي:", (r'\sin^{2}3x', sin(3*x)**2)),
  [O(r'\frac{1}{6}', R(1, 6)), O(r'-\frac{1}{6}', -R(1, 6)), O(r'\frac{1}{3}', R(1, 3)), O(r'-\frac{1}{3}', -R(1, 3))],
  r"$\sin^23x=\dfrac{1-\cos6x}{2}$ ، و $\displaystyle\int_0^{\pi/3}\frac{1-\cos6x}{2}dx=\left[\frac x2-\frac{\sin6x}{12}\right]_0^{\pi/3}=\frac{\pi}{6}$ ، إذن $a=\frac16$",
  truth=ig(sin(3*x)**2, (x, 0, pi/3))/pi, tag='تكامل باستعمال تقليص القوة'),
# 2026 #29: dy/dx = e^(kx) - e^(-x) through (0, 2); options = the right antiderivative (1/4 e^(4x) + e^(-x)) or the model's
# wrong one (3/4 e^(4x) - e^(-x), coefficient and constant swapped, sign of e^(-x) slipped) x sign of the constant
IndexQ('n10q4', U5[1], 'medium',
  F(r"يُمثّل الاقتران: $\dfrac{dy}{dx}=«0»$ ميل المماس لمنحنى الاقتران $y$. إذا كان منحنى $y$ يمرّ بالنقطة $(0,\,2)$ ، فإنّ قاعدة الاقتران $y$ هي:", (r'e^{4x}-e^{-x}', exp(4*x) - exp(-x))),
  [O(r'y=\frac{1}{4}e^{4x}+e^{-x}+\frac{3}{4}', exp(4*x)/4 + exp(-x) + R(3, 4), 'eq'), O(r'y=\frac{3}{4}e^{4x}-e^{-x}+\frac{1}{4}', R(3, 4)*exp(4*x) - exp(-x) + R(1, 4), 'eq'),
   O(r'y=\frac{1}{4}e^{4x}+e^{-x}-\frac{3}{4}', exp(4*x)/4 + exp(-x) - R(3, 4), 'eq'), O(r'y=\frac{3}{4}e^{4x}-e^{-x}-\frac{1}{4}', R(3, 4)*exp(4*x) - exp(-x) - R(1, 4), 'eq')],
  r"$y=\displaystyle\int(e^{4x}-e^{-x})dx=\frac14e^{4x}+e^{-x}+C$ ، و $y(0)=2 \Rightarrow \frac14+1+C=2 \Rightarrow C=\frac34$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, exp(4*x) - exp(-x), 0, 2)), tag='إيجاد الاقتران بمعلومية مشتقته ونقطة'),
# 2024 #6: displacement for v = A cos(t/k) on an interval ending at t/k = 2pi/3; options = sign x sqrt3 or not
# (antiderivative sign slip, cosine kept instead of integrated, sin(2pi/3) taken as 1/2)
Q('n10q5', U5[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=«0»$ ، حيث $v$ السرعة بالمتر لكل ثانية، و $t$ الزمن بالثواني. إنّ إزاحة الجُسيم بالأمتار في الفترة $[0,\,4\pi]$ ، هي:", (r'3\cos\left(\frac{t}{6}\right)', 3*cos(t/6))),
  [O(r'9\sqrt{3}', 9*sqrt(3)), O(r'-9\sqrt{3}', -9*sqrt(3)), O('-9', -9), O('9', 9)],
  r"$\displaystyle\int_0^{4\pi}3\cos\frac t6\,dt=\left[18\sin\frac t6\right]_0^{4\pi}=18\sin\frac{2\pi}{3}-0=18\cdot\frac{\sqrt3}{2}=9\sqrt3$",
  truth=ig(3*cos(t/6), (t, 0, 4*pi)), tag='الحركة: الإزاحة من السرعة'),
# 2025s #8: (x^2 - 2x + 1)^3 / x^8 = (1 - 1/x)^6 / x^2, u = 1 - 1/x (here (x + 1)^4 / x^6, u = 1 + 1/x);
# options = power 5 vs 4 (power not raised) x sign
Q('n10q6', U5[2], 'medium',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ هو:", (r'\frac{(x^{2}+2x+1)^{2}}{x^{6}}', (x**2 + 2*x + 1)**2/x**6)),
  [A(r'-\frac{1}{5}\left(1+\frac{1}{x}\right)^{5}+C', -(1 + 1/x)**5/5), A(r'\frac{1}{5}\left(1+\frac{1}{x}\right)^{5}+C', (1 + 1/x)**5/5),
   A(r'-\frac{1}{4}\left(1+\frac{1}{x}\right)^{4}+C', -(1 + 1/x)**4/4), A(r'\frac{1}{4}\left(1+\frac{1}{x}\right)^{4}+C', (1 + 1/x)**4/4)],
  r"$\dfrac{(x+1)^4}{x^6}=\dfrac{(x+1)^4}{x^4}\cdot\dfrac{1}{x^2}=\left(1+\dfrac1x\right)^4\dfrac{1}{x^2}$ ، و $u=1+\frac1x \Rightarrow du=-\frac{dx}{x^2}$" "\n"
  r"$\displaystyle-\int u^4du=-\frac{u^5}{5}+C=-\frac15\left(1+\frac1x\right)^5+C$",
  truth=(x**2 + 2*x + 1)**2/x**6, tag='التكامل بالتعويض بعد التبسيط'),
# 2025 #9: tan x sec^3 x = sec^2 x (sec x tan x), u = sec x, definite; options = the cube computed (8 vs 2) x sign of the
# lower-limit term
Q('n10q7', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\frac{\pi}{3}}«0»\,dx$ هي:", (r'\tan x\sec^{3}x', tan(x)*sec(x)**3)),
  [O(r'\frac{7}{3}', R(7, 3)), O(r'\frac{1}{3}', R(1, 3)), O('3', 3), O('1', 1)],
  r"$u=\sec x \Rightarrow du=\sec x\tan x\,dx$ ، و $\tan x\sec^3x\,dx=\sec^2x\cdot\sec x\tan x\,dx=u^2du$" "\n"
  r"$\left[\dfrac{\sec^3x}{3}\right]_0^{\pi/3}=\dfrac{2^3-1^3}{3}=\dfrac73$",
  truth=lambda: Integral(tan(x)*sec(x)**3, (x, 0, pi/3)).evalf(40), tag='التكامل بالتعويض: قوى الاقترانات المثلثية'),
# 2025s #6: substitution whose du is the whole numerator (sin 2x = derivative of 4 + sin^2 x), definite; options = logs of
# simple numbers (lower-limit value ln 4 dropped, limits reversed, ln 5 - ln 4 taken as ln(5 - 4) = 0)
Q('n10q8', U5[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\frac{\pi}{2}}«0»\,dx$ هي:", (r'\frac{\sin 2x}{4+\sin^{2}x}', sin(2*x)/(4 + sin(x)**2))),
  [O(r'\ln\frac{5}{4}', log(R(5, 4))), O(r'\ln 5', log(5)), O(r'\ln\frac{4}{5}', log(R(4, 5))), O('0', 0)],
  r"$u=4+\sin^2x \Rightarrow du=2\sin x\cos x\,dx=\sin2x\,dx$ ، والحدود: $x=0\to u=4$ ، $x=\frac{\pi}{2}\to u=5$" "\n"
  r"$\displaystyle\int_4^5\frac{du}{u}=\ln5-\ln4=\ln\frac54$",
  truth=ig(sin(2*x)/(4 + sin(x)**2), (x, 0, pi/2)), tag='التكامل المحدود بالتعويض'),
# 2025s #9: a quantity from its rate -k e^(-kt)/(1 + e^(-kt))^2 and its starting value (drug concentration in the model;
# newspaper subscribers here), u = 1 + e^(-kt); options = sign of the fraction x the constant (right constant for the wrong
# sign, or the constant's sign flipped)
Q('n10q9', U5[2], 'hard',
  F(r"يُمثّل الاقتران $N(t)$ عدد مشتركي إحدى الصحف الورقية (بالآلاف) بعد $t$ شهرًا من إطلاق نسختها الإلكترونية. إذا كان عدد المشتركين لحظة إطلاق النسخة الإلكترونية $2.5$ ألف مشترك، وأخذ يتغيّر بمعدّل $N'(t)=«0»$ ، فإنّ قاعدة الاقتران $N(t)$ هي:",
    (r'\frac{-0.5\,e^{-0.5t}}{(1+e^{-0.5t})^{2}}', N10(t))),
  [O(r'\frac{-1}{1+e^{-0.5t}}+3', -1/(1 + exp(-t/2)) + 3), O(r'\frac{-1}{1+e^{-0.5t}}-3', -1/(1 + exp(-t/2)) - 3),
   O(r'\frac{1}{1+e^{-0.5t}}+2', 1/(1 + exp(-t/2)) + 2), O(r'\frac{1}{1+e^{-0.5t}}-2', 1/(1 + exp(-t/2)) - 2)],
  r"$u=1+e^{-0.5t} \Rightarrow du=-0.5e^{-0.5t}dt$ ، إذن $N(t)=\displaystyle\int\frac{du}{u^2}=-\frac1u+K=\frac{-1}{1+e^{-0.5t}}+K$" "\n"
  r"$N(0)=-\frac12+K=2.5 \Rightarrow K=3$",
  truth=R(5, 2) + ig(N10(s), (s, 0, t)), tag='إيجاد الاقتران من معدّل تغيّره في سياق حياتي'),
# 2025s #10: partial fractions with two distinct linear factors; options = B from a sign slip (6 + 3 -> 6 - 3) x sign of A
Q('n10q10', U5[3], 'easy',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ هو:", (r'\frac{2x+3}{x^{2}-3x}', (2*x + 3)/(x**2 - 3*x))),
  [A(r'3\ln|x-3|-\ln|x|+C', 3*log(x - 3) - log(x)), A(r'3\ln|x-3|+\ln|x|+C', 3*log(x - 3) + log(x)),
   A(r'\ln|x-3|-\ln|x|+C', log(x - 3) - log(x)), A(r'\ln|x-3|+\ln|x|+C', log(x - 3) + log(x))],
  r"$\dfrac{2x+3}{x(x-3)}=\dfrac{A}{x}+\dfrac{B}{x-3}$ ، عند $x=0$: $3=-3A \Rightarrow A=-1$ ، عند $x=3$: $9=3B \Rightarrow B=3$" "\n"
  r"الناتج: $3\ln|x-3|-\ln|x|+C$",
  truth=(2*x + 3)/(x**2 - 3*x), tag='التكامل بالكسور الجزئية: عوامل خطية'),
# 2025 #2: improper rational function, one-step division x + c/(x - a); options = x^2/2 vs x^2 x sign of the ln term
Q('n10q11', U5[3], 'medium',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ هو:", (r'\frac{x^{2}-4x+5}{x-4}', (x**2 - 4*x + 5)/(x - 4))),
  [A(r'\frac{x^{2}}{2}+5\ln|x-4|+C', x**2/2 + 5*log(x - 4)), A(r'\frac{x^{2}}{2}-5\ln|x-4|+C', x**2/2 - 5*log(x - 4)),
   A(r'x^{2}+5\ln|x-4|+C', x**2 + 5*log(x - 4)), A(r'x^{2}-5\ln|x-4|+C', x**2 - 5*log(x - 4))],
  r"$x^2-4x+5=x(x-4)+5$ ، إذن $\dfrac{x^2-4x+5}{x-4}=x+\dfrac{5}{x-4}$" "\n"
  r"$\displaystyle\int\left(x+\frac{5}{x-4}\right)dx=\frac{x^2}{2}+5\ln|x-4|+C$",
  truth=(x**2 - 4*x + 5)/(x - 4), tag='التكامل بالكسور الجزئية: كسر غير فعلي'),
# 2024 #10: ln of a root -> k ln x, then the integral of ln x by parts; options = sign of the x term x the factor 3/2 on
# both terms or only on x ln x
Q('n10q12', U5[4], 'easy',
  F(r"ناتج: $\displaystyle\int«0»\,dx$ ، هو:", (r'\ln\sqrt{x^{3}}', log(sqrt(x**3)))),
  [A(r'\frac{3}{2}x\ln x-\frac{3}{2}x+C', R(3, 2)*x*log(x) - R(3, 2)*x), A(r'\frac{3}{2}x\ln x+\frac{3}{2}x+C', R(3, 2)*x*log(x) + R(3, 2)*x),
   A(r'\frac{3}{2}x\ln x-x+C', R(3, 2)*x*log(x) - x), A(r'\frac{3}{2}x\ln x+x+C', R(3, 2)*x*log(x) + x)],
  r"$\ln\sqrt{x^3}=\ln x^{\frac32}=\frac32\ln x$ ، وبالأجزاء: $\displaystyle\int\ln x\,dx=x\ln x-x$" "\n"
  r"الناتج: $\frac32(x\ln x-x)+C=\frac32x\ln x-\frac32x+C$",
  truth=log(sqrt(x**3)), tag='التكامل بالأجزاء'),
# 2023s #11: integral of x f'(x) on [0, 1] by parts from given values (the model's own form: the integral of f is
# handed over); options = right, the boundary term only, f(1) - f(0) taken as the answer, f(1) - f(0) - the given integral
Q('n10q13', U5[4], 'medium',
  r"إذا كان: $\displaystyle\int_{0}^{1}f(x)\,dx=2$ ، $f(1)=6$ ، $f(0)=1$ ، فإنّ قيمة $\displaystyle\int_{0}^{1}x\,f'(x)\,dx$ تساوي:",
  [O('4', 4), O('6', 6), O('5', 5), O('3', 3)],
  r"بالأجزاء: $u=x$ ، $dv=f'(x)dx \Rightarrow v=f(x)$: $\displaystyle\int_0^1xf'(x)dx=\big[xf(x)\big]_0^1-\int_0^1f(x)dx=(1\times6-0)-2=4$",
  # an explicit f with f(0) = 1, f(1) = 6 and integral 2 on [0, 1]
  truth=ig(x*diff(1-4*x+9*x**2, x), (x, 0, 1)), tag='التكامل بالأجزاء: من قيم معطاة'),
# 2025 #11: displacement from a piecewise-linear v-t graph, answered with its direction; the start x0 is not needed;
# options = displacement 4 vs distance 16 x right/left
IndexQ('n10q14', U5[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة – الزمن لجسم يتحرّك على المحور $x$ في الفترة $[0,\,8]$ ، إذا بدأ الجسم الحركة من $x=3$ عندما $t=0$ ، فإنّ إزاحة الجسم في الفترة الزمنية المعطاة هي:",
  [T(r"$4\ \text{m}$ إلى اليمين", (4, 1)), T(r"$4\ \text{m}$ إلى اليسار", (4, -1)),
   T(r"$16\ \text{m}$ إلى اليمين", (16, 1)), T(r"$16\ \text{m}$ إلى اليسار", (16, -1))],
  r"المساحة تحت محور $t$ في $[0,4]$: $\frac12(4+2)(2)=6$ ، وفوقه في $[4,8]$: $\frac12(4+1)(4)=10$" "\n"
  r"الإزاحة $=10-6=4$ ، موجبة، إذن $4\ \text{m}$ إلى اليمين",
  truth=lambda vals: only(vals, lambda v_: v_ == (abs(D10), sign(D10))),
  figure=figure('n10q14', vt_graph(vt10, 8, -2, 4), 4.2, 3.0), tag='الحركة من منحنى السرعة–الزمن'),
# 2026r #8: area under x e^(c x^2) from 0 (substitution); options = factor 1/4 kept vs dropped x -+1 (e^0 = 1)
Q('n10q15', U5[5], 'medium',
  F(r"مساحة المنطقة المحصورة بين منحنى الاقتران: $y=«0»$ والمحور $x$ والمستقيمين: $x=0\ ,\ x=1$ هي:", (r'x\,e^{2x^{2}}', x*exp(2*x**2))),
  [O(r'\frac{1}{4}(e^{2}-1)', (E**2 - 1)/4), O(r'\frac{1}{4}(e^{2}+1)', (E**2 + 1)/4), O(r'e^{2}-1', E**2 - 1), O(r'e^{2}+1', E**2 + 1)],
  r"المنحنى فوق المحور $x$ في $[0,1]$ ، و $u=2x^2 \Rightarrow du=4x\,dx$" "\n"
  r"$\displaystyle\int_0^1xe^{2x^2}dx=\frac14\left[e^{2x^2}\right]_0^1=\frac14(e^2-1)$",
  truth=ig(x*exp(2*x**2), (x, 0, 1)), tag='المساحة بين منحنى والمحور x'),
# 2024 #13: dy/dx = e^(ax + by) through (0, 0), separated; options = chain factor divided vs multiplied x sign of the
# constant; one of them passes through (0, 0) but fails the equation (the model's trap)
IndexQ('n10q16', U5[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ ، الذي يُحقّق النقطة $(0,\,0)$ ، هو:", (r'e^{(2x-y)}', exp(2*x - y))),
  [O(r'2e^{y}=e^{2x}+1', 2*exp(y) - exp(2*x) - 1, 'rel'), O(r'2e^{y}=e^{2x}-1', 2*exp(y) - exp(2*x) + 1, 'rel'),
   O(r'e^{y}=2e^{2x}-1', exp(y) - 2*exp(2*x) + 1, 'rel'), O(r'e^{y}=2e^{2x}+1', exp(y) - 2*exp(2*x) - 1, 'rel')],
  r"$e^{2x-y}=\dfrac{e^{2x}}{e^y} \Rightarrow e^ydy=e^{2x}dx \Rightarrow e^y=\frac12e^{2x}+C$" "\n"
  r"$(0,0)$: $1=\frac12+C \Rightarrow C=\frac12$ ، إذن $2e^y=e^{2x}+1$",
  truth=lambda vals: only(vals, lambda F_: ode_rel_ok(F_, exp(2*x - y), (0, 0))), tag='المعادلات التفاضلية: الحل الخاص'),
# ---------------------------------------------------------------- unit 6: vectors
# 2026r #13: endpoint B from A and the midpoint N; options = 2N - A, A - 2N, and A - 2N in one component
Q('n10q17', U6[1], 'easy',
  r"إذا كانت: $A(-1,\,4,\,-5)$ ، وكانت: $N(3,\,0,\,-2)$ نقطة منتصف $\overline{AB}$ ، فإنّ إحداثيات النقطة $B$ هي:",
  [pt_opt(7, -4, 1), pt_opt(-7, 4, -1), pt_opt(-7, -4, 1), pt_opt(7, -4, -1)],
  r"$N$ منتصف $\overline{AB}$ ، إذن $B=2N-A=(6-(-1),\ 0-4,\ -4-(-5))=(7,\,-4,\,1)$",
  truth=T3(2*V(3, 0, -2) - V(-1, 4, -5)), tag='المتجهات: منتصف قطعة مستقيمة'),
# 2025s #18: parallel vectors, unknown component; options = sign x multiplied vs divided by the factor 2
Q('n10q18', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{a}}=\langle 4,\,-1,\,3\rangle,\ \vec{\mathbf{b}}=\langle \alpha,\,2,\,-6\rangle$ ، فإنّ قيمة الثابت $\alpha$ التي تجعل المتجهين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ متوازيين هي:",
  [O('-8', -8), O('8', 8), O('-2', -2), O('2', 2)],
  r"من المركبتين الثانية والثالثة: $2=-2(-1)$ و $-6=-2(3)$ ، إذن $\vec{\mathbf{b}}=-2\vec{\mathbf{a}}$ و $\alpha=-2(4)=-8$",
  truth=lambda: [s_ for s_ in solve(V(4, -1, 3).cross(V(Symbol('al'), 2, -6))[2], Symbol('al'))
                 if V(4, -1, 3).cross(V(s_, 2, -6)) == zeros(3, 1)][0], tag='توازي المتجهات وإيجاد ثابت'),
# 2023 #14: coordinates of one labelled vertex of a cube read from the ministry's drawing (the vertex above the y-axis end
# here, above the x-axis end in the model); options = other vertices of the cube (x/y swapped, the one below it, the front one)
Q('n10q19', U6[1], 'medium',
  r"اعتمادًا على الشكل الآتي الذي يُمثّل مكعّبًا طول ضلعه $6\ \text{cm}$ ، فإنّ إحداثيات النقطة $H$ هي:",
  [pt_opt(0, 6, 6), pt_opt(6, 0, 6), pt_opt(0, 6, 0), pt_opt(6, 6, 6)],
  r"الرأس $H$ فوق الرأس الواقع على المحور $y$ ، وهو $(0,6,0)$ ، على ارتفاع $6$ ، إذن $H(0,\,6,\,6)$",
  truth=Tuple(*H10), figure=figure('n10q19', cube_fig10(6, 'H', H10), 3.2, 3.2), tag='المتجهات من شكل ثلاثي الأبعاد'),
# 2025s #14: 2f - g in i, j, k with a vanishing component (3f - g and the j component here, since u6e5q1 asks 2f - g);
# options = the vanishing component kept (0) vs slipped (3(3) + 9 = 18) x sign of the rest (g - 3f)
Q('n10q20', U6[1], 'easy',
  r"إذا كان: $\vec{\mathbf{f}}=" + ijk(2, 3, -2) + r",\ \vec{\mathbf{g}}=" + ijk(-3, 9, 5) + r"$ ، فإنّ $3\vec{\mathbf{f}}-\vec{\mathbf{g}}$ هو:",
  [ijk_opt(9, 0, -11), ijk_opt(-9, 0, 11), ijk_opt(9, 18, -11), ijk_opt(-9, 18, 11)],
  r"$3\vec{\mathbf{f}}-\vec{\mathbf{g}}=(6+3)\hat{i}+(9-9)\hat{j}+(-6-5)\hat{k}=9\hat{i}-11\hat{k}$",
  truth=T3(3*V(2, 3, -2) - V(-3, 9, 5)), tag='العمليات على المتجهات'),
# 2024 #18: vector of a given magnitude along v (|v| an integer), each option named with its own letter; options = 3v (right),
# the unit vector, v/|v|^2 times the magnitude (root forgotten), v divided by the magnitude
Q('n10q21', U6[1], 'medium',
  r"إذا كان: $\vec{\mathbf{v}}=" + ijk(1, 4, -8) + r"$ ، فإنّ المتجه الذي له اتجاه $\vec{\mathbf{v}}$ نفسه، ومقداره $27$ ، هو:",
  [NamedIJK('r', 3, 12, -24), NamedIJK('u', R(1, 9), R(4, 9), -R(8, 9)), NamedIJK('n', R(1, 3), R(4, 3), -R(8, 3)),
   NamedIJK('w', R(1, 27), R(4, 27), -R(8, 27))],
  r"$|\vec{\mathbf{v}}|=\sqrt{1+16+64}=9$ ، والمطلوب $27\cdot\dfrac{\vec{\mathbf{v}}}{9}=3\vec{\mathbf{v}}=3\hat{i}+12\hat{j}-24\hat{k}$",
  truth=T3(27*V(1, 4, -8)/V(1, 4, -8).norm()), tag='متجه بمقدار معلوم في اتجاه معلوم'),
# 2025 #16: p a - q b = given vector, a has a zero component that hands over q at once -> p + q; options = sum vs
# difference x sign
Q('n10q22', U6[1], 'medium',
  r"إذا كان: $\vec{\mathbf{a}}=\langle 3,\,0,\,-1\rangle,\ \vec{\mathbf{b}}=\langle 1,\,1,\,2\rangle$ ، وكان: $p\vec{\mathbf{a}}-q\vec{\mathbf{b}}=\langle 1,\,-5,\,-12\rangle$ ، فإنّ قيمة $p+q$ هي:",
  [O('7', 7), O('-7', -7), O('3', 3), O('-3', -3)],
  r"المركبة الثانية: $0-q=-5 \Rightarrow q=5$ ، والأولى: $3p-5=1 \Rightarrow p=2$ (والثالثة: $-2-10=-12$ ✔) ، إذن $p+q=7$",
  truth=lambda: (lambda pq: (lambda sol: sol[pq[0]] + sol[pq[1]])(
      solve(list(pq[0]*V(3, 0, -1) - pq[1]*V(1, 1, 2) - V(1, -5, -12)), list(pq), dict=True)[0]))(symbols('p_ q_')),
  tag='المتجهات: إيجاد معاملين'),
# 2024s #19: a point whose coordinates all contain a lies on a line -> a; options = +-1, +-2
Q('n10q23', U6[2], 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 1,\,-3,\,2\rangle+t\,\langle 2,\,1,\,-1\rangle$ تُمثّل معادلة متجهة للمستقيم $l$ ، وكانت النقطة: $(1-a,\,a,\,a+3)$ تقع على المستقيم $l$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('-2', -2), O('2', 2), O('1', 1), O('-1', -1)],
  r"$1+2t=1-a$ ، $-3+t=a$ ، $2-t=a+3$" "\n"
  r"من الثانية والثالثة: $t=a+3$ و $t=-1-a$ ، إذن $a+3=-1-a \Rightarrow a=-2$ ، $t=1$ ، وتتحقّق الأولى: $3=3$ ✔",
  truth=lambda: solve(list(V(1, -3, 2) + t*V(2, 1, -1) - V(1 - a, a, a + 3)), [t, a], dict=True)[0][a],
  tag='نقطة على مستقيم وإيجاد ثابت'),
# 2026 #45: triangle area from two side vectors, the right angle not stated (at A here, at B in the model);
# options = (1/2)|AB||AC|, without 1/2, the two lengths added, |AB| taken as the sum of its components (the model's list)
Q('n10q24', U6[3], 'medium',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{AB}=\langle 6,\,2,\,-3\rangle$ ، و $\overrightarrow{AC}=\langle 4,\,6,\,12\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O('49', 49), O('98', 98), O('21', 21), O('35', 35)],
  r"$\overrightarrow{AB}\cdot\overrightarrow{AC}=24+12-36=0$ ، إذن الزاوية $A$ قائمة" "\n"
  r"$|\overrightarrow{AB}|=\sqrt{49}=7$ ، $|\overrightarrow{AC}|=\sqrt{196}=14$ ، والمساحة $=\frac12(7)(14)=49$",
  truth=R(1, 2)*V(6, 2, -3).norm()*V(4, 6, 12).norm()*sin(ang((6, 2, -3), (4, 6, 12))), tag='مساحة مثلث باستعمال الضرب القياسي'),
# 2023 #19: perpendicular vectors, linear in c; options = right, sign slip, first components equated, a sign slip in one product
Q('n10q25', U6[3], 'easy',
  r"إذا كان: $\vec{\mathbf{u}}=\langle 5,\,-6,\,2\rangle$ ، $\vec{\mathbf{v}}=\langle 2c,\,3,\,-11\rangle$ متعامدين، فإنّ قيمة الثابت $c$ هي:",
  [O('4', 4), O('-4', -4), O(r'\frac{5}{2}', R(5, 2)), O(r'\frac{2}{5}', R(2, 5))],
  r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=10c-18-22=0 \Rightarrow 10c=40 \Rightarrow c=4$",
  truth=lambda: solve(V(5, -6, 2).dot(V(2*c, 3, -11)), c)[0], tag='التعامد وإيجاد ثوابت'),
# ---------------------------------------------------------------- unit 7: statistics
# 2026 #47: quality control, a box rejected when the sample has defective items (one or more here, two or more in the
# model); options = P(X >= 1), P(X = 0), P(X = 1), P(X >= 2)
Q('n10q26', U7[1], 'medium',
  r"يختار قسم ضبط الجودة في أحد مصانع الهواتف الذكية عيّنة عشوائية مكوّنة من $4$ شاشات من كلّ صندوق لفحصها، ويُرفَض الصندوق إذا وُجدت في العيّنة شاشة معيبة واحدة فأكثر. إذا كانت نسبة الشاشات المعيبة في إنتاج المصنع $10\%$ ، فإنّ احتمال رفض الصندوق هو:",
  [D('0.3439'), D('0.6561'), D('0.2916'), D('0.0523')],
  r"$X\sim B(4,\,0.1)$ ، و $P(X\ge1)=1-P(X=0)=1-(0.9)^4=1-0.6561=0.3439$",
  truth=r4(1 - binom(4, R(1, 10), 0)), tag='توزيع ذي الحدين: احتمال «على الأقل»'),
# 2025s #21: spinner of congruent sectors (figure), X = spins until the pointer first stops on a given kind of sector -> E(X);
# options = 1/p, p, q/p, 1/q
Q('n10q27', U7[1], 'easy',
  r"يُمثّل الشكل الآتي قرصًا مُقسّمًا إلى خمسة قطاعات دائرية متطابقة. إذا دلّ المتغيّر العشوائي $X$ على عدد مرّات تدوير مؤشّر القرص حتى يقف عند قطاع يحمل عددًا فرديًّا أوّل مرّة، فإنّ قيمة $E(X)$ هي:",
  [O(r'\frac{5}{3}', R(5, 3)), O(r'\frac{3}{5}', R(3, 5)), O(r'\frac{2}{3}', R(2, 3)), O(r'\frac{5}{2}', R(5, 2))],
  r"الأعداد الفردية $1,3,5$: ثلاثة قطاعات من خمسة متطابقة، $p=\dfrac35$ ، و $X\sim Geo\left(\frac35\right)$ ، $E(X)=\dfrac1p=\dfrac53$",
  truth=1/R(3, 5), figure=figure('n10q27', spinner_fig([str(i_) for i_ in range(1, 6)], pointer_deg=50), 2.6, 2.6),
  tag='التوزيع الهندسي: التوقع والاحتمال'),
# 2024 #23: empirical rule in words, one side of the mean (figure); "less than the mean by more than one sigma" = below
# mu - sigma here; options = 16 %, 34 % (mu - sigma .. mu), 84 % (the complement), 13.5 % (one band only)
Q('n10q28', U7[2], 'easy',
  r"اعتمادًا على القاعدة التجريبية في الشكل الآتي، إذا اتّخذ التمثيل البياني لكتل مجموعة من المواليد الجُدد شكل المنحنى الطبيعي بوسط حسابي $\mu$ ، وانحراف معياري $\sigma$ ، فإنّ النسبة المئوية للمواليد الذين تقلّ كتلهم عن الوسط الحسابي بأكثر من انحراف معياري واحد، هي:",
  [O(r'16\%', 16), O(r'34\%', 34), O(r'84\%', 84), O(r'13.5\%', R(27, 2))],
  r"تقلّ عن الوسط بأكثر من $\sigma$ ← أقلّ من $\mu-\sigma$: $13.5\%+2.35\%+0.15\%=16\%$ (أو $50\%-34\%$)",
  truth=100*(R(1, 2) - emp(-1, 0)), figure=figure('n10q28', emp_fig, 4.4, 2.4), tag='التوزيع الطبيعي: القاعدة التجريبية'),
# 2025s #23: probability below a value under the mean in context, mean and SD in words, with the table; options = right, the
# table value, the table value - 0.5, 0.5 + the tail
Q('n10q29', U7[2], 'medium',
  r"توصّلت دراسة إلى أنّ مُدد الرحلات الجوية بين مدينتين تتبع توزيعًا طبيعيًّا وسطه الحسابي $150$ دقيقة، وانحرافه المعياري $8$ دقائق. إذا اختيرت رحلة عشوائيًّا، فإنّ احتمال أن تقلّ مدّتها عن $138$ دقيقة هو:",
  [D('0.0668'), D('0.9332'), D('0.4332'), D('0.5668')],
  r"$z=\dfrac{138-150}{8}=-1.5$ ، و $P(Z<-1.5)=1-P(Z<1.5)=1-0.9332=0.0668$",
  truth=Ph(R(138 - 150, 8)), tag='التوزيع الطبيعي: حساب احتمال',
  lead=ztable_note([29, 30], 0, 0.25, 0.5, 1, 1.5, 2), group=2),
# 2024 #25: P(-a < Z < b) from the table; options = right, -a treated as +a, from 0, the neighbouring column with the sign
# ignored
Q('n10q30', U7[2], 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، فإنّ $P(-0.25<Z<2)$ يساوي:",
  [D('0.5759'), D('0.3785'), D('0.4772'), D('0.2857')],
  r"$P(-0.25<Z<2)=P(Z<2)-P(Z<-0.25)=0.9772-(1-0.5987)=0.9772-0.4013=0.5759$",
  truth=Ph(2) - Ph(-R(1, 4)), tag='التوزيع الطبيعي: حساب احتمال'),
]
