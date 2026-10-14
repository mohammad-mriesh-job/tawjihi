from qb import *

L = {i: f'u5-l{i}' for i in range(1, 7)}
meta = dict(id='u5', number=5, semester=2, title='التكامل',
    description='تكامل الاقترانات الأسية واللوغاريتمية والمثلثية وتطبيقاته في الحركة، التكامل بالتعويض وبالكسور الجزئية وبالأجزاء، المساحات والحجوم الدورانية، والمعادلات التفاضلية.',
    lessons=[dict(id=L[1], title='تكامل اقترانات خاصة'), dict(id=L[2], title='التكامل بالتعويض'),
             dict(id=L[3], title='التكامل بالكسور الجزئية'), dict(id=L[4], title='التكامل بالأجزاء'),
             dict(id=L[5], title='المساحات والحجوم'), dict(id=L[6], title='المعادلات التفاضلية')])
R = Rational
P = pi
ig = integrate
C = r'+C'
def A(tex, F_):
    """antiderivative option: displayed LaTeX (must end with +C) and the antiderivative F"""
    assert tex.rstrip().endswith('+C'), tex
    return O(tex, F_, 'anti')
def ode_ok(Yx, rhs, x0, y0):
    """explicit solution y=Y(x) satisfies y'=rhs(x,y) and y(x0)=y0"""
    return same(diff(Yx, x) - rhs.subs(y, Yx), 0) and same(Yx.subs(x, x0), y0)
def ode_ok_rel(Fxy, rhs, x0, y0):
    """implicit solution F(x,y)=0 satisfies y'=rhs and passes (x0,y0)"""
    dydx = -diff(Fxy, x)/diff(Fxy, y)
    if not same(Fxy.subs({x: x0, y: y0}), 0):
        return False
    return same(dydx - rhs, 0) or same(simplify((dydx - rhs).subs(y, solve(Fxy, y)[-1])), 0)

def region(f_, g_, a_, b_, xlim, ylim, labels=(), fill='#9cc3ef'):
    import numpy as np
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        xs = np.linspace(xlim[0], xlim[1], 400)
        ff = lambdify(x, f_, 'numpy'); gg = lambdify(x, g_, 'numpy')
        ax.plot(xs, ff(xs) + 0*xs, color='#1f5fbf', lw=1.8)
        if g_ != 0:
            ax.plot(xs, gg(xs) + 0*xs, color='#d04a1a', lw=1.8)
        xr = np.linspace(float(a_), float(b_), 200)
        ax.fill_between(xr, ff(xr) + 0*xr, gg(xr) + 0*xr, color=fill, alpha=0.8)
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

# ============================================================== Exam 1
E1 = [
Q('u5e1q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'2e^{x}-\frac{3}{x}+\sec^{2}x', 2*exp(x)-3/x+sec(x)**2)),
  [A(r'2e^{x}-3\ln|x|+\tan x+C', 2*exp(x)-3*log(x)+tan(x)), A(r'2e^{x}+\frac{3}{x^{2}}+\tan x+C', 2*exp(x)+3/x**2+tan(x)),
   A(r'2e^{x}-3\ln|x|-\tan x+C', 2*exp(x)-3*log(x)-tan(x)), A(r'2xe^{x}-3\ln|x|+\tan x+C', 2*x*exp(x)-3*log(x)+tan(x))],
  r"$\displaystyle\int e^x\,dx=e^x$ ، $\displaystyle\int\frac1x\,dx=\ln|x|$ ، $\displaystyle\int\sec^2x\,dx=\tan x$" "\n"
  r"إذن الناتج $2e^x-3\ln|x|+\tan x+C$",
  truth=2*exp(x)-3/x+sec(x)**2),
Q('u5e1q2', L[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{\ln a}«0»\,dx=30$ ، حيث $a>0$ ، فإنّ قيمة الثابت $a$ هي:", (r'4e^{2x}', 4*exp(2*x))),
  [O('4', 4), O('2', 2), O('16', 16), O(r'\sqrt{15}', sqrt(15))],
  r"$\displaystyle\int_0^{\ln a}4e^{2x}dx=\big[2e^{2x}\big]_0^{\ln a}=2e^{2\ln a}-2=2a^2-2$" "\n"
  r"$2a^2-2=30 \Rightarrow a^2=16 \Rightarrow a=4$ (لأن $a>0$)",
  truth=lambda: [r_ for r_ in solve(ig(4*exp(2*x), (x, 0, log(a)))-30, a) if r_.is_positive][0]),
Q('u5e1q3', L[1], 'medium',
  F(r"يُمثّل الاقتران: $f'(x)=«0»$ ميل المماس لمنحنى الاقتران $f(x)$. إذا كان منحنى $f(x)$ يمرّ بالنقطة $(0,\,4)$ ، فإنّ قاعدة الاقتران $f(x)$ هي:", (r'6x-e^{-x}', 6*x-exp(-x))),
  [O(r'f(x)=3x^{2}+e^{-x}+3', 3*x**2+exp(-x)+3, 'eq'), O(r'f(x)=3x^{2}-e^{-x}+5', 3*x**2-exp(-x)+5, 'eq'),
   O(r'f(x)=3x^{2}+e^{-x}+4', 3*x**2+exp(-x)+4, 'eq'), O(r'f(x)=6x^{2}+e^{-x}+3', 6*x**2+exp(-x)+3, 'eq')],
  r"$f(x)=\displaystyle\int(6x-e^{-x})dx=3x^2+e^{-x}+C$" "\n" r"$f(0)=4 \Rightarrow 0+1+C=4 \Rightarrow C=3$",
  truth=lambda: (lambda F_: F_ + 4 - F_.subs(x, 0))(ig(6*x-exp(-x), x))),
Q('u5e1q4', L[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{2}e^{x^{3}}', x**2*exp(x**3))),
  [A(r'\frac{1}{3}e^{x^{3}}+C', exp(x**3)/3), A(r'3e^{x^{3}}+C', 3*exp(x**3)), A(r'e^{x^{3}}+C', exp(x**3)), A(r'\frac{x^{3}}{3}e^{x^{3}}+C', x**3*exp(x**3)/3)],
  r"بالتعويض $u=x^3 \Rightarrow du=3x^2dx$: $\displaystyle\frac13\int e^u\,du=\frac13e^{x^3}+C$",
  truth=x**2*exp(x**3)),
Q('u5e1q5', L[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\sqrt{x-1}', x*sqrt(x-1))),
  [A(r'\frac{2}{5}(x-1)^{\frac{5}{2}}+\frac{2}{3}(x-1)^{\frac{3}{2}}+C', R(2, 5)*(x-1)**R(5, 2)+R(2, 3)*(x-1)**R(3, 2)),
   A(r'\frac{2}{5}(x-1)^{\frac{5}{2}}-\frac{2}{3}(x-1)^{\frac{3}{2}}+C', R(2, 5)*(x-1)**R(5, 2)-R(2, 3)*(x-1)**R(3, 2)),
   A(r'\frac{x^{2}}{2}\cdot\frac{2}{3}(x-1)^{\frac{3}{2}}+C', x**2/2*R(2, 3)*(x-1)**R(3, 2)),
   A(r'\frac{2}{3}x(x-1)^{\frac{3}{2}}+C', R(2, 3)*x*(x-1)**R(3, 2))],
  r"بالتعويض $u=x-1 \Rightarrow x=u+1$ ، $dx=du$:" "\n"
  r"$\displaystyle\int(u+1)\sqrt u\,du=\int\left(u^{\frac32}+u^{\frac12}\right)du=\frac25u^{\frac52}+\frac23u^{\frac32}+C$" "\n"
  r"$=\frac25(x-1)^{\frac52}+\frac23(x-1)^{\frac32}+C$",
  truth=x*sqrt(x-1)),
Q('u5e1q6', L[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{5x+4}{(x-1)(x+2)}', (5*x+4)/((x-1)*(x+2)))),
  [A(r'3\ln|x-1|+2\ln|x+2|+C', 3*log(x-1)+2*log(x+2)), A(r'2\ln|x-1|+3\ln|x+2|+C', 2*log(x-1)+3*log(x+2)),
   A(r'3\ln|x-1|-2\ln|x+2|+C', 3*log(x-1)-2*log(x+2)), A(r'5\ln|(x-1)(x+2)|+C', 5*log((x-1)*(x+2)))],
  r"$\dfrac{5x+4}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$ ، عند $x=1$: $9=3A \Rightarrow A=3$ ، عند $x=-2$: $-6=-3B \Rightarrow B=2$" "\n"
  r"إذن التكامل $=3\ln|x-1|+2\ln|x+2|+C$",
  truth=(5*x+4)/((x-1)*(x+2))),
Q('u5e1q7', L[3], 'hard',
  F(r"قيمة: $\displaystyle\int_{2}^{3}«0»\,dx$ هي:", (r'\frac{x^{2}+1}{x^{2}-1}', (x**2+1)/(x**2-1))),
  [O(r'1+\ln\frac{3}{2}', 1+log(R(3, 2))), O(r'1+\ln\frac{2}{3}', 1+log(R(2, 3))), O(r'\ln\frac{3}{2}', log(R(3, 2))), O(r'1+\ln 6', 1+log(6))],
  r"الكسر غير فعلي: $\dfrac{x^2+1}{x^2-1}=1+\dfrac{2}{x^2-1}=1+\dfrac{1}{x-1}-\dfrac{1}{x+1}$" "\n"
  r"$\big[x+\ln|x-1|-\ln|x+1|\big]_2^3=(3+\ln2-\ln4)-(2+0-\ln3)=1+\ln\dfrac{2\cdot3}{4}=1+\ln\dfrac32$",
  truth=ig((x**2+1)/(x**2-1), (x, 2, 3))),
Q('u5e1q8', L[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'xe^{3x}', x*exp(3*x))),
  [A(r'\frac{x}{3}e^{3x}-\frac{1}{9}e^{3x}+C', x/3*exp(3*x)-exp(3*x)/9), A(r'\frac{x}{3}e^{3x}-\frac{1}{3}e^{3x}+C', x/3*exp(3*x)-exp(3*x)/3),
   A(r'3xe^{3x}-9e^{3x}+C', 3*x*exp(3*x)-9*exp(3*x)), A(r'\frac{x^{2}}{6}e^{3x}+C', x**2/6*exp(3*x))],
  r"بالأجزاء: $u=x$ ، $dv=e^{3x}dx \Rightarrow v=\frac13e^{3x}$" "\n"
  r"$\displaystyle\frac{x}{3}e^{3x}-\int\frac13e^{3x}dx=\frac{x}{3}e^{3x}-\frac19e^{3x}+C$",
  truth=x*exp(3*x)),
Q('u5e1q9', L[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\sec^{2}x', x*sec(x)**2)),
  [A(r'x\tan x+\ln|\cos x|+C', x*tan(x)+log(cos(x))), A(r'x\tan x-\ln|\cos x|+C', x*tan(x)-log(cos(x))),
   A(r'x\tan x+\ln|\sin x|+C', x*tan(x)+log(sin(x))), A(r'\frac{x^{2}}{2}\tan x+C', x**2/2*tan(x))],
  r"بالأجزاء: $u=x$ ، $dv=\sec^2x\,dx \Rightarrow v=\tan x$" "\n"
  r"$\displaystyle x\tan x-\int\tan x\,dx=x\tan x-(-\ln|\cos x|)+C=x\tan x+\ln|\cos x|+C$",
  truth=x*sec(x)**2),
Q('u5e1q10', L[5], 'medium',
  F(r"اعتمادًا على الشكل الآتي الذي يُبيّن منحنى الاقتران: $f(x)=«0»$ ، فإنّ مساحة المنطقة المُظلَّلة (بالوحدات المربعة) هي:", (r'x^{2}-4x', x**2-4*x)),
  [O(r'\frac{32}{3}', R(32, 3)), O(r'-\frac{32}{3}', -R(32, 3)), O(r'\frac{16}{3}', R(16, 3)), O(r'\frac{64}{3}', R(64, 3))],
  r"المنطقة تحت محور $x$ بين نقطتي التقاطع $x=0$ و $x=4$ ، فالمساحة $=\left|\displaystyle\int_0^4(x^2-4x)dx\right|$" "\n"
  r"$=\left|\left[\frac{x^3}{3}-2x^2\right]_0^4\right|=\left|\frac{64}{3}-32\right|=\frac{32}{3}$ (المساحة لا تكون سالبة)",
  truth=Abs(ig(x**2-4*x, (x, 0, 4))),
  figure=figure('u5e1q10', region(x**2-4*x, 0*x, 0, 4, (-1, 5.4), (-4.8, 3.2), [(4.5, 1.6, r'$f(x)$', '#1f5fbf')]), 3.6, 3.0)),
Q('u5e1q11', L[5], 'hard',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ والمحور $x$ في الفترة $\left[0,\,\frac{\pi}{2}\right]$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'\sqrt{\cos x}', sqrt(cos(x)))),
  [O(r'\pi', P), O(r'2\pi', 2*P), O(r'\frac{\pi}{2}', P/2), O(r'\pi^{2}', P**2)],
  r"$V=\pi\displaystyle\int_0^{\pi/2}\left(\sqrt{\cos x}\right)^2dx=\pi\int_0^{\pi/2}\cos x\,dx=\pi\big[\sin x\big]_0^{\pi/2}=\pi(1-0)=\pi$",
  truth=pi*ig(cos(x), (x, 0, pi/2))),
IndexQ('u5e1q12', L[6], 'medium',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي يُحقّق الشرط الأوّلي $y(0)=1$ هو:", (r'xy^{2}', x*y**2)),
  [O(r'y=\frac{2}{2-x^{2}}', 2/(2-x**2), 'eq'), O(r'y=\frac{2}{2+x^{2}}', 2/(2+x**2), 'eq'),
   O(r'y=\frac{1}{1-x^{2}}', 1/(1-x**2), 'eq'), O(r'y=1-\frac{x^{2}}{2}', 1-x**2/2, 'eq')],
  r"بفصل المتغيرات: $\dfrac{dy}{y^2}=x\,dx \Rightarrow -\dfrac1y=\dfrac{x^2}{2}+C$" "\n"
  r"$y(0)=1 \Rightarrow -1=C$ ، إذن $-\dfrac1y=\dfrac{x^2}{2}-1=\dfrac{x^2-2}{2} \Rightarrow y=\dfrac{2}{2-x^2}$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, x*y**2, 0, 1))),
]

# ============================================================== Exam 2
E2 = [
Q('u5e2q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\cot^{2}x+3', cot(x)**2+3)),
  [A(r'-\cot x+2x+C', -cot(x)+2*x), A(r'-\cot x+3x+C', -cot(x)+3*x), A(r'\cot x+2x+C', cot(x)+2*x), A(r'-\csc x+2x+C', -csc(x)+2*x)],
  r"$\cot^2x=\csc^2x-1$ ، إذن $\displaystyle\int(\csc^2x-1+3)dx=\int(\csc^2x+2)dx=-\cot x+2x+C$",
  truth=cot(x)**2+3),
Q('u5e2q2', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'3^{2x+1}', 3**(2*x+1))),
  [A(r'\frac{3^{2x+1}}{2\ln 3}+C', 3**(2*x+1)/(2*log(3))), A(r'\frac{3^{2x+1}}{\ln 3}+C', 3**(2*x+1)/log(3)),
   A(r'2\cdot3^{2x+1}\ln 3+C', 2*3**(2*x+1)*log(3)), A(r'\frac{3^{2x+1}}{(\ln 3)^{2}}+C', 3**(2*x+1)/log(3)**2)],
  r"$\displaystyle\int a^{kx+b}dx=\frac{a^{kx+b}}{k\ln a}+C$ ، إذن الناتج $\dfrac{3^{2x+1}}{2\ln3}+C$",
  truth=3**(2*x+1)),
Q('u5e2q3', L[1], 'hard',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ بالمتر لكل ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلية بالأمتار التي قطعها الجُسيم في الفترة $[0,\,3]$ هي:", (r't^{2}-4t+3', t**2-4*t+3)),
  [O(r'\frac{8}{3}', R(8, 3)), O('0', 0), O(r'\frac{4}{3}', R(4, 3)), O('3', 3)],
  r"$v(t)=(t-1)(t-3)$ موجبة في $(0,1)$ وسالبة في $(1,3)$" "\n"
  r"$\displaystyle\int_0^1v\,dt=\left[\frac{t^3}{3}-2t^2+3t\right]_0^1=\frac43$ ، $\displaystyle\int_1^3v\,dt=0-\frac43=-\frac43$" "\n"
  r"المسافة $=\frac43+\left|-\frac43\right|=\frac83\ \text{m}$ (لاحظ أن الإزاحة $=0$)",
  truth=ig(Abs(t**2-4*t+3), (t, 0, 3))),
Q('u5e2q4', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\cos x}{(1+\sin x)^{2}}', cos(x)/(1+sin(x))**2)),
  [A(r'-\frac{1}{1+\sin x}+C', -1/(1+sin(x))), A(r'\frac{1}{1+\sin x}+C', 1/(1+sin(x))),
   A(r'\ln|1+\sin x|+C', log(1+sin(x))), A(r'-\frac{2}{(1+\sin x)^{3}}+C', -2/(1+sin(x))**3)],
  r"بالتعويض $u=1+\sin x \Rightarrow du=\cos x\,dx$: $\displaystyle\int u^{-2}du=-u^{-1}+C=-\frac{1}{1+\sin x}+C$",
  truth=cos(x)/(1+sin(x))**2),
Q('u5e2q5', L[2], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\pi/3}«0»\,dx$ هي:", (r'\frac{\sin x}{\cos^{2}x}', sin(x)/cos(x)**2)),
  [O('1', 1), O('2', 2), O('-1', -1), O(r'\frac{1}{2}', R(1, 2))],
  r"بالتعويض $u=\cos x \Rightarrow du=-\sin x\,dx$ ، أو بملاحظة أن $\dfrac{\sin x}{\cos^2x}=\sec x\tan x$:" "\n"
  r"$\big[\sec x\big]_0^{\pi/3}=\sec\frac{\pi}{3}-\sec0=2-1=1$",
  truth=ig(sin(x)/cos(x)**2, (x, 0, pi/3))),
Q('u5e2q6', L[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{3x+1}{x^{2}-1}', (3*x+1)/(x**2-1))),
  [A(r'2\ln|x-1|+\ln|x+1|+C', 2*log(x-1)+log(x+1)), A(r'\ln|x-1|+2\ln|x+1|+C', log(x-1)+2*log(x+1)),
   A(r'2\ln|x-1|-\ln|x+1|+C', 2*log(x-1)-log(x+1)), A(r'\frac{3}{2}\ln|x^{2}-1|+C', R(3, 2)*log(x**2-1))],
  r"$\dfrac{3x+1}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1}$ ، عند $x=1$: $4=2A \Rightarrow A=2$ ، عند $x=-1$: $-2=-2B \Rightarrow B=1$",
  truth=(3*x+1)/(x**2-1)),
Q('u5e2q7', L[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2x^{2}+3}{x^{3}+3x}', (2*x**2+3)/(x**3+3*x))),
  [A(r'\ln|x|+\frac{1}{2}\ln(x^{2}+3)+C', log(x)+log(x**2+3)/2), A(r'\ln|x|+\ln(x^{2}+3)+C', log(x)+log(x**2+3)),
   A(r'\ln|x|-\frac{1}{2}\ln(x^{2}+3)+C', log(x)-log(x**2+3)/2), A(r'2\ln|x|+\frac{1}{2}\ln(x^{2}+3)+C', 2*log(x)+log(x**2+3)/2)],
  r"$x^3+3x=x(x^2+3)$ ، و $2x^2+3=A(x^2+3)+(Bx+C)x$: عند $x=0$: $A=1$ ، ثم $B=1$ ، $C=0$" "\n"
  r"$\displaystyle\int\left(\frac1x+\frac{x}{x^2+3}\right)dx=\ln|x|+\frac12\ln(x^2+3)+C$",
  truth=(2*x**2+3)/(x**3+3*x)),
Q('u5e2q8', L[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\ln(2x)', log(2*x))),
  [A(r'x\ln(2x)-x+C', x*log(2*x)-x), A(r'x\ln(2x)-2x+C', x*log(2*x)-2*x), A(r'\frac{1}{2x}+C', 1/(2*x)), A(r'2x\ln(2x)-x+C', 2*x*log(2*x)-x)],
  r"بالأجزاء: $u=\ln(2x) \Rightarrow du=\frac1xdx$ ، $dv=dx \Rightarrow v=x$" "\n"
  r"$\displaystyle x\ln(2x)-\int x\cdot\frac1x\,dx=x\ln(2x)-x+C$",
  truth=log(2*x)),
Q('u5e2q9', L[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{2}\cos x', x**2*cos(x))),
  [A(r'x^{2}\sin x+2x\cos x-2\sin x+C', x**2*sin(x)+2*x*cos(x)-2*sin(x)), A(r'x^{2}\sin x-2x\cos x+2\sin x+C', x**2*sin(x)-2*x*cos(x)+2*sin(x)),
   A(r'x^{2}\sin x+2x\cos x+2\sin x+C', x**2*sin(x)+2*x*cos(x)+2*sin(x)), A(r'-x^{2}\sin x+2x\cos x-2\sin x+C', -x**2*sin(x)+2*x*cos(x)-2*sin(x))],
  r"بالأجزاء مرتين (أو بالجدول): $u=x^2$ ، $dv=\cos x\,dx$" "\n"
  r"$\displaystyle\int x^2\cos x\,dx=x^2\sin x-\int2x\sin x\,dx=x^2\sin x-\left(-2x\cos x+2\sin x\right)$" "\n"
  r"$=x^2\sin x+2x\cos x-2\sin x+C$",
  truth=x**2*cos(x)),
Q('u5e2q10', L[5], 'medium',
  F(r"مساحة المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ (بالوحدات المربعة) هي:", (r'2x', 2*x), (r'x^{2}-3', x**2-3)),
  [O(r'\frac{32}{3}', R(32, 3)), O(r'\frac{16}{3}', R(16, 3)), O('9', 9), O(r'\frac{64}{3}', R(64, 3))],
  r"نقاط التقاطع: $x^2-3=2x \Rightarrow x^2-2x-3=0 \Rightarrow x=-1,\ x=3$ ، وفي $(-1,3)$ يكون $2x\ge x^2-3$" "\n"
  r"$\displaystyle A=\int_{-1}^{3}(2x-x^2+3)dx=\left[x^2-\frac{x^3}{3}+3x\right]_{-1}^{3}=9-\left(-\frac53\right)=\frac{32}{3}$",
  truth=ig(2*x-(x**2-3), (x, -1, 3))),
Q('u5e2q11', L[5], 'hard',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'\sqrt{x}', sqrt(x)), (r'x', x)),
  [O(r'\frac{\pi}{6}', P/6), O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{2}', P/2), O(r'\frac{\pi}{12}', P/12)],
  r"نقاط التقاطع: $\sqrt x=x \Rightarrow x=0,\ x=1$ ، وفي $(0,1)$ يكون $\sqrt x>x$ (المنحنى الخارجي $\sqrt x$)" "\n"
  r"$\displaystyle V=\pi\int_0^1\left((\sqrt x)^2-x^2\right)dx=\pi\int_0^1(x-x^2)dx=\pi\left(\frac12-\frac13\right)=\frac{\pi}{6}$",
  truth=pi*ig(x-x**2, (x, 0, 1))),
Q('u5e2q12', L[6], 'medium',
  r"يتغيّر عدد البكتيريا $P$ في مزرعة وفق المعادلة التفاضلية $\dfrac{dP}{dt}=kP$ ، حيث $t$ الزمن بالساعات. إذا كان العدد الابتدائي $200$ ، وأصبح بعد $3$ ساعات $1600$ ، فإنّ عدد البكتيريا بعد $5$ ساعات هو:",
  [O('6400', 6400), O('3200', 3200), O('4000', 4000), O('12800', 12800)],
  r"الحل العام: $P=P_0e^{kt}=200e^{kt}$ ، و $P(3)=1600 \Rightarrow e^{3k}=8 \Rightarrow e^{k}=2$" "\n"
  r"إذن $P(t)=200\cdot2^t$ ، و $P(5)=200(32)=6400$",
  truth=lambda: (lambda kk: 200*exp(kk*5))([r_ for r_ in solve(200*exp(3*k)-1600, k) if r_.is_real][0])),
]

# ============================================================== Exam 3
vt_pts = [(0, 0), (2, 4), (4, 4), (6, -4), (8, 0)]
E3 = [
Q('u5e3q1', L[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{1}^{e}«0»\,dx$ هي:", (r'\frac{x+1}{x}', (x+1)/x)),
  [O('e', E), O('e-1', E-1), O('e+1', E+1), O('1', 1)],
  r"$\displaystyle\int_1^e\left(1+\frac1x\right)dx=\big[x+\ln x\big]_1^e=(e+1)-(1+0)=e$",
  truth=ig((x+1)/x, (x, 1, E))),
Q('u5e3q2', L[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{\pi/2}«0»\,dx=a\pi$ ، فإنّ قيمة الثابت $a$ هي:", (r'\cos^{2}x', cos(x)**2)),
  [O(r'\frac{1}{4}', R(1, 4)), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{4}', -R(1, 4)), O('1', 1)],
  r"$\cos^2x=\dfrac{1+\cos2x}{2}$ ، إذن $\displaystyle\int_0^{\pi/2}\frac{1+\cos2x}{2}dx=\left[\frac x2+\frac{\sin2x}{4}\right]_0^{\pi/2}=\frac{\pi}{4}$" "\n"
  r"$a\pi=\dfrac{\pi}{4} \Rightarrow a=\dfrac14$",
  truth=ig(cos(x)**2, (x, 0, pi/2))/pi),
Q('u5e3q3', L[1], 'hard',
  r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=\begin{cases}3t^{2}, & 0\le t\le2\\ 12, & t>2\end{cases}$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. إذا انطلق الجسم من نقطة الأصل، فإنّ موقعه بعد $5$ ثوانٍ من بدء الحركة هو:",
  [O('44', 44, units='m'), O('36', 36, units='m'), O('75', 75, units='m'), O('48', 48, units='m')],
  r"$s(5)=s(0)+\displaystyle\int_0^5v(t)dt=0+\int_0^2 3t^2dt+\int_2^5 12\,dt$" "\n"
  r"$=\big[t^3\big]_0^2+12(5-2)=8+36=44\ \text{m}$",
  truth=ig(3*t**2, (t, 0, 2))+ig(12, (t, 2, 5))),
Q('u5e3q4', L[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{e^{x}}{e^{x}+3}', exp(x)/(exp(x)+3))),
  [A(r'\ln(e^{x}+3)+C', log(exp(x)+3)), A(r'e^{x}\ln(e^{x}+3)+C', exp(x)*log(exp(x)+3)),
   A(r'\frac{1}{e^{x}+3}+C', 1/(exp(x)+3)), A(r'x+\ln 3+C', x+log(3))],
  r"البسط مشتقة المقام: $\displaystyle\int\frac{f'(x)}{f(x)}dx=\ln|f(x)|+C=\ln(e^x+3)+C$ (لأن $e^x+3>0$)",
  truth=exp(x)/(exp(x)+3)),
Q('u5e3q5', L[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sin 2x}{1+\cos^{2}x}', sin(2*x)/(1+cos(x)**2))),
  [A(r'-\ln(1+\cos^{2}x)+C', -log(1+cos(x)**2)), A(r'\ln(1+\cos^{2}x)+C', log(1+cos(x)**2)),
   A(r'-2\ln(1+\cos^{2}x)+C', -2*log(1+cos(x)**2)), A(r'-\frac{1}{2}\ln(1+\cos^{2}x)+C', -log(1+cos(x)**2)/2)],
  r"بالتعويض $u=1+\cos^2x \Rightarrow du=-2\sin x\cos x\,dx=-\sin2x\,dx$" "\n"
  r"$\displaystyle\int\frac{-du}{u}=-\ln|u|+C=-\ln(1+\cos^2x)+C$",
  truth=sin(2*x)/(1+cos(x)**2)),
Q('u5e3q6', L[3], 'medium',
  F(r"قيمة: $\displaystyle\int_{3}^{4}«0»\,dx$ هي:", (r'\frac{2x-1}{(x-1)(x-2)}', (2*x-1)/((x-1)*(x-2)))),
  [O(r'\ln\frac{16}{3}', log(R(16, 3))), O(r'\ln\frac{3}{16}', log(R(3, 16))), O(r'\ln 16', log(16)), O(r'4\ln 2+\ln 3', 4*log(2)+log(3))],
  r"$\dfrac{2x-1}{(x-1)(x-2)}=\dfrac{-1}{x-1}+\dfrac{3}{x-2}$ (عند $x=1$: $A=-1$ ، عند $x=2$: $B=3$)" "\n"
  r"$\big[-\ln|x-1|+3\ln|x-2|\big]_3^4=(-\ln3+3\ln2)-(-\ln2+0)=4\ln2-\ln3=\ln\dfrac{16}{3}$",
  truth=ig((2*x-1)/((x-1)*(x-2)), (x, 3, 4))),
Q('u5e3q7', L[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{3}}{x^{2}-1}', x**3/(x**2-1))),
  [A(r'\frac{x^{2}}{2}+\frac{1}{2}\ln|x^{2}-1|+C', x**2/2+log(x**2-1)/2), A(r'\frac{x^{2}}{2}+\ln|x^{2}-1|+C', x**2/2+log(x**2-1)),
   A(r'\frac{x^{2}}{2}-\frac{1}{2}\ln|x^{2}-1|+C', x**2/2-log(x**2-1)/2), A(r'\frac{x^{4}}{4}\ln|x^{2}-1|+C', x**4/4*log(x**2-1))],
  r"الكسر غير فعلي: $x^3=x(x^2-1)+x$ ، إذن $\dfrac{x^3}{x^2-1}=x+\dfrac{x}{x^2-1}=x+\dfrac{1/2}{x-1}+\dfrac{1/2}{x+1}$" "\n"
  r"$\displaystyle\int=\frac{x^2}{2}+\frac12\ln|x-1|+\frac12\ln|x+1|+C=\frac{x^2}{2}+\frac12\ln|x^2-1|+C$",
  truth=x**3/(x**2-1)),
Q('u5e3q8', L[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x\cos 2x', x*cos(2*x))),
  [A(r'\frac{x}{2}\sin 2x+\frac{1}{4}\cos 2x+C', x/2*sin(2*x)+cos(2*x)/4), A(r'\frac{x}{2}\sin 2x-\frac{1}{4}\cos 2x+C', x/2*sin(2*x)-cos(2*x)/4),
   A(r'2x\sin 2x+4\cos 2x+C', 2*x*sin(2*x)+4*cos(2*x)), A(r'\frac{x^{2}}{2}\sin 2x+C', x**2/2*sin(2*x))],
  r"بالأجزاء: $u=x$ ، $dv=\cos2x\,dx \Rightarrow v=\frac12\sin2x$" "\n"
  r"$\displaystyle\frac x2\sin2x-\int\frac12\sin2x\,dx=\frac x2\sin2x+\frac14\cos2x+C$",
  truth=x*cos(2*x)),
Q('u5e3q9', L[4], 'hard',
  F(r"قيمة: $\displaystyle\int_{1}^{e}«0»\,dx$ هي:", (r'x\ln x', x*log(x))),
  [O(r'\frac{e^{2}+1}{4}', (E**2+1)/4), O(r'\frac{e^{2}-1}{4}', (E**2-1)/4), O(r'\frac{e^{2}}{4}', E**2/4), O(r'\frac{e^{2}+1}{2}', (E**2+1)/2)],
  r"بالأجزاء: $u=\ln x$ ، $dv=x\,dx$: $\displaystyle\int x\ln x\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}$" "\n"
  r"$\left[\frac{x^2}{2}\ln x-\frac{x^2}{4}\right]_1^e=\left(\frac{e^2}{2}-\frac{e^2}{4}\right)-\left(0-\frac14\right)=\dfrac{e^2+1}{4}$",
  truth=ig(x*log(x), (x, 1, E))),
Q('u5e3q10', L[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة–الزمن لجسم يتحرّك على المحور $x$ في الفترة الزمنية $[0,\,8]$. المسافة الكلية التي قطعها الجسم في هذه الفترة هي:",
  [O('20', 20, units='m'), O('8', 8, units='m'), O('16', 16, units='m'), O('12', 12, units='m')],
  r"المسافة الكلية = مجموع المساحات (كلها موجبة) بين المنحنى ومحور $t$:" "\n"
  r"$[0,2]$: مثلث $=\frac12(2)(4)=4$ ، $[2,4]$: مستطيل $=8$ ، $[4,5]$: مثلث $=2$ ، $[5,6]$: مثلث تحت المحور $=2$ ، $[6,8]$: مثلث تحت المحور $=4$" "\n"
  r"المسافة $=4+8+2+2+4=20\ \text{m}$ (أما الإزاحة فهي $4+8+2-2-4=8\ \text{m}$)",
  truth=lambda: pw_integral(vt_pts, 0, 8, absolute=True), figure=figure('u5e3q10', vt_graph(vt_pts, 8, -4, 4), 4.2, 3.0)),
Q('u5e3q11', L[5], 'medium',
  F(r"إذا كانت مساحة المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ ، والمحور $x$ ، والمستقيمين: $x=1,\ x=a$ تساوي $12$ وحدة مربعة، حيث $a>1$ ، فإنّ قيمة الثابت $a$ هي:", (r'\frac{6}{x}', 6/x)),
  [O(r'e^{2}', E**2), O('e', E), O(r'e^{3}', E**3), O(r'e^{6}', E**6)],
  r"$\displaystyle\int_1^a\frac6x\,dx=\big[6\ln x\big]_1^a=6\ln a=12 \Rightarrow \ln a=2 \Rightarrow a=e^2$",
  truth=lambda: solve(ig(6/x, (x, 1, a))-12, a)[0]),
IndexQ('u5e3q12', L[6], 'hard',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي يُحقّق الشرط الأوّلي $y(0)=\ln 2$ هو:", (r'e^{x-y}', exp(x-y))),
  [O(r'y=\ln(e^{x}+1)', log(exp(x)+1), 'eq'), O(r'y=\ln(e^{x}+2)', log(exp(x)+2), 'eq'),
   O(r'y=x+\ln 2', x+log(2), 'eq'), O(r'y=\ln(2e^{x})-x', log(2*exp(x))-x, 'eq')],
  r"$\dfrac{dy}{dx}=\dfrac{e^x}{e^y} \Rightarrow e^y\,dy=e^x\,dx \Rightarrow e^y=e^x+C$" "\n"
  r"$y(0)=\ln2 \Rightarrow 2=1+C \Rightarrow C=1$ ، إذن $e^y=e^x+1 \Rightarrow y=\ln(e^x+1)$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, exp(x-y), 0, log(2)))),
]

# ============================================================== Exam 4
E4 = [
Q('u5e4q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\sqrt{x}+\frac{1}{\sqrt{x}}', sqrt(x)+1/sqrt(x))),
  [A(r'\frac{2}{3}x^{\frac{3}{2}}+2\sqrt{x}+C', R(2, 3)*x**R(3, 2)+2*sqrt(x)), A(r'\frac{3}{2}x^{\frac{3}{2}}+2\sqrt{x}+C', R(3, 2)*x**R(3, 2)+2*sqrt(x)),
   A(r'\frac{2}{3}x^{\frac{3}{2}}+\frac{1}{2}\sqrt{x}+C', R(2, 3)*x**R(3, 2)+sqrt(x)/2), A(r'\frac{2}{3}x^{\frac{3}{2}}-2\sqrt{x}+C', R(2, 3)*x**R(3, 2)-2*sqrt(x))],
  r"$\displaystyle\int\left(x^{\frac12}+x^{-\frac12}\right)dx=\frac{x^{\frac32}}{\frac32}+\frac{x^{\frac12}}{\frac12}+C=\frac23x^{\frac32}+2\sqrt x+C$",
  truth=sqrt(x)+1/sqrt(x)),
Q('u5e4q2', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(\sin x+\cos x)^{2}', (sin(x)+cos(x))**2)),
  [A(r'x-\frac{1}{2}\cos 2x+C', x-cos(2*x)/2), A(r'x+\frac{1}{2}\cos 2x+C', x+cos(2*x)/2),
   A(r'x-\cos 2x+C', x-cos(2*x)), A(r'\frac{(\sin x+\cos x)^{3}}{3}+C', (sin(x)+cos(x))**3/3)],
  r"$(\sin x+\cos x)^2=\sin^2x+2\sin x\cos x+\cos^2x=1+\sin2x$" "\n"
  r"$\displaystyle\int(1+\sin2x)dx=x-\frac12\cos2x+C$",
  truth=(sin(x)+cos(x))**2),
Q('u5e4q3', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{e^{2x}-1}{e^{x}}', (exp(2*x)-1)/exp(x))),
  [A(r'e^{x}+e^{-x}+C', exp(x)+exp(-x)), A(r'e^{x}-e^{-x}+C', exp(x)-exp(-x)), A(r'e^{x}-x+C', exp(x)-x), A(r'e^{2x}-x+C', exp(2*x)-x)],
  r"نقسم كل حد على $e^x$: $\dfrac{e^{2x}-1}{e^x}=e^x-e^{-x}$" "\n"
  r"$\displaystyle\int(e^x-e^{-x})dx=e^x+e^{-x}+C$",
  truth=(exp(2*x)-1)/exp(x)),
Q('u5e4q4', L[2], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{(\ln x)^{3}}{x}', log(x)**3/x)),
  [A(r'\frac{(\ln x)^{4}}{4}+C', log(x)**4/4), A(r'(\ln x)^{4}+C', log(x)**4), A(r'\frac{3(\ln x)^{2}}{x}+C', 3*log(x)**2/x), A(r'\frac{(\ln x)^{4}}{4x}+C', log(x)**4/(4*x))],
  r"بالتعويض $u=\ln x \Rightarrow du=\frac1xdx$: $\displaystyle\int u^3du=\frac{u^4}{4}+C=\frac{(\ln x)^4}{4}+C$",
  truth=log(x)**3/x),
Q('u5e4q5', L[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{3}\sqrt{x^{2}+1}', x**3*sqrt(x**2+1))),
  [A(r'\frac{1}{5}(x^{2}+1)^{\frac{5}{2}}-\frac{1}{3}(x^{2}+1)^{\frac{3}{2}}+C', (x**2+1)**R(5, 2)/5-(x**2+1)**R(3, 2)/3),
   A(r'\frac{1}{5}(x^{2}+1)^{\frac{5}{2}}+\frac{1}{3}(x^{2}+1)^{\frac{3}{2}}+C', (x**2+1)**R(5, 2)/5+(x**2+1)**R(3, 2)/3),
   A(r'\frac{2}{5}(x^{2}+1)^{\frac{5}{2}}-\frac{2}{3}(x^{2}+1)^{\frac{3}{2}}+C', R(2, 5)*(x**2+1)**R(5, 2)-R(2, 3)*(x**2+1)**R(3, 2)),
   A(r'\frac{x^{4}}{4}\cdot\frac{2}{3}(x^{2}+1)^{\frac{3}{2}}+C', x**4/4*R(2, 3)*(x**2+1)**R(3, 2))],
  r"بالتعويض $u=x^2+1 \Rightarrow du=2x\,dx$ ، و $x^2=u-1$:" "\n"
  r"$\displaystyle\int x^2\sqrt{x^2+1}\cdot x\,dx=\frac12\int(u-1)\sqrt u\,du=\frac12\left(\frac25u^{\frac52}-\frac23u^{\frac32}\right)+C$" "\n"
  r"$=\frac15(x^2+1)^{\frac52}-\frac13(x^2+1)^{\frac32}+C$",
  truth=x**3*sqrt(x**2+1)),
Q('u5e4q6', L[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{4}{x^{2}-4x}', 4/(x**2-4*x))),
  [A(r'\ln|x-4|-\ln|x|+C', log(x-4)-log(x)), A(r'\ln|x|-\ln|x-4|+C', log(x)-log(x-4)),
   A(r'4\ln|x-4|-4\ln|x|+C', 4*log(x-4)-4*log(x)), A(r'\ln|x^{2}-4x|+C', log(x**2-4*x))],
  r"$\dfrac{4}{x(x-4)}=\dfrac{A}{x}+\dfrac{B}{x-4}$ ، عند $x=0$: $4=-4A \Rightarrow A=-1$ ، عند $x=4$: $4=4B \Rightarrow B=1$" "\n"
  r"التكامل $=-\ln|x|+\ln|x-4|+C$",
  truth=4/(x**2-4*x)),
Q('u5e4q7', L[3], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'\frac{x+3}{x^{2}+3x+2}', (x+3)/(x**2+3*x+2))),
  [O(r'\ln\frac{8}{3}', log(R(8, 3))), O(r'\ln\frac{3}{8}', log(R(3, 8))), O(r'\ln 4', log(4)), O(r'\ln\frac{4}{3}', log(R(4, 3)))],
  r"$x^2+3x+2=(x+1)(x+2)$ ، و $\dfrac{x+3}{(x+1)(x+2)}=\dfrac{2}{x+1}-\dfrac{1}{x+2}$" "\n"
  r"$\big[2\ln|x+1|-\ln|x+2|\big]_0^1=(2\ln2-\ln3)-(0-\ln2)=3\ln2-\ln3=\ln\dfrac83$",
  truth=ig((x+3)/(x**2+3*x+2), (x, 0, 1))),
Q('u5e4q8', L[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{2}e^{x}', x**2*exp(x))),
  [A(r'e^{x}(x^{2}-2x+2)+C', exp(x)*(x**2-2*x+2)), A(r'e^{x}(x^{2}+2x+2)+C', exp(x)*(x**2+2*x+2)),
   A(r'e^{x}(x^{2}-2x-2)+C', exp(x)*(x**2-2*x-2)), A(r'\frac{x^{3}}{3}e^{x}+C', x**3/3*exp(x))],
  r"بالأجزاء مرتين: $\displaystyle\int x^2e^xdx=x^2e^x-\int2xe^xdx=x^2e^x-(2xe^x-2e^x)$" "\n"
  r"$=e^x(x^2-2x+2)+C$",
  truth=x**2*exp(x)),
Q('u5e4q9', L[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'e^{2x}\cos x', exp(2*x)*cos(x))),
  [A(r'\frac{e^{2x}}{5}(2\cos x+\sin x)+C', exp(2*x)/5*(2*cos(x)+sin(x))), A(r'\frac{e^{2x}}{5}(2\cos x-\sin x)+C', exp(2*x)/5*(2*cos(x)-sin(x))),
   A(r'\frac{e^{2x}}{3}(2\cos x+\sin x)+C', exp(2*x)/3*(2*cos(x)+sin(x))), A(r'\frac{e^{2x}}{5}(\cos x+2\sin x)+C', exp(2*x)/5*(cos(x)+2*sin(x)))],
  r"بالأجزاء مرتين (تكامل دوري): نفرض $I=\displaystyle\int e^{2x}\cos x\,dx$" "\n"
  r"$I=e^{2x}\sin x-\displaystyle\int2e^{2x}\sin x\,dx=e^{2x}\sin x-2\left(-e^{2x}\cos x+\int2e^{2x}\cos x\,dx\right)$" "\n"
  r"$I=e^{2x}\sin x+2e^{2x}\cos x-4I \Rightarrow 5I=e^{2x}(2\cos x+\sin x)$",
  truth=exp(2*x)*cos(x)),
Q('u5e4q10', L[5], 'medium',
  F(r"اعتمادًا على الشكل الآتي الذي يُبيّن منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ ، فإنّ مساحة المنطقة المُظلَّلة (بالوحدات المربعة) هي:", (r'6-x^{2}', 6-x**2), (r'x+4', x+4)),
  [O(r'\frac{9}{2}', R(9, 2)), O('9', 9), O(r'\frac{7}{6}', R(7, 6)), O(r'\frac{10}{3}', R(10, 3))],
  r"نقاط التقاطع: $6-x^2=x+4 \Rightarrow x^2+x-2=0 \Rightarrow x=-2,\ x=1$" "\n"
  r"$\displaystyle A=\int_{-2}^{1}\big((6-x^2)-(x+4)\big)dx=\int_{-2}^{1}(2-x-x^2)dx=\left[2x-\frac{x^2}{2}-\frac{x^3}{3}\right]_{-2}^{1}=\frac76+\frac{10}{3}=\frac92$",
  truth=ig(6-x**2-(x+4), (x, -2, 1)),
  figure=figure('u5e4q10', region(6-x**2, x+4, -2, 1, (-3, 2.6), (-1, 7), [(1.3, 5.6, r'$g(x)$', '#d04a1a'), (-2.95, 2.4, r'$f(x)$', '#1f5fbf')]), 3.6, 3.2)),
Q('u5e4q11', L[5], 'hard',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'5-x^{2}', 5-x**2), (r'x+3', x+3)),
  [O(r'\frac{153\pi}{5}', 153*P/5), O(r'\frac{9\pi}{2}', 9*P/2), O(r'\frac{81\pi}{4}', 81*P/4), O(r'\frac{168\pi}{5}', 168*P/5)],
  r"نقاط التقاطع: $5-x^2=x+3 \Rightarrow x=-2,\ x=1$ ، وفي الفترة يكون $5-x^2\ge x+3\ge0$ (طريقة الحلقات)" "\n"
  r"$\displaystyle V=\pi\int_{-2}^{1}\left((5-x^2)^2-(x+3)^2\right)dx=\pi\int_{-2}^{1}(x^4-11x^2-6x+16)dx$" "\n"
  r"$=\pi\left[\frac{x^5}{5}-\frac{11x^3}{3}-3x^2+16x\right]_{-2}^{1}=\pi\left(\frac{143}{15}+\frac{316}{15}\right)=\frac{153\pi}{5}$",
  truth=pi*ig((5-x**2)**2-(x+3)**2, (x, -2, 1)),
  figure=figure('u5e4q11', region(5-x**2, x+3, -2, 1, (-3, 2.6), (-1.5, 6), [(1.2, 4.5, r'$g(x)$', '#d04a1a'), (-2.95, 1.6, r'$f(x)$', '#1f5fbf')]), 3.6, 3.2)),
IndexQ('u5e4q12', L[6], 'medium',
  F(r"الحلّ الخاص للمعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ ، حيث $y>0$ ، الذي يُحقّق الشرط الأوّلي $y(0)=3$ هو:", (r'\frac{2x+1}{2y}', (2*x+1)/(2*y))),
  [O('y^{2}=x^{2}+x+9', y**2-x**2-x-9, 'rel'), O('y^{2}=x^{2}+x+3', y**2-x**2-x-3, 'rel'),
   O('y^{2}=2x^{2}+x+9', y**2-2*x**2-x-9, 'rel'), O('y=x^{2}+x+3', y-x**2-x-3, 'rel')],
  r"بفصل المتغيرات: $2y\,dy=(2x+1)dx \Rightarrow y^2=x^2+x+C$" "\n" r"$y(0)=3 \Rightarrow 9=C$ ، إذن $y^2=x^2+x+9$",
  truth=lambda vals: only(vals, lambda F_: ode_ok_rel(F_, (2*x+1)/(2*y), 0, 3))),
]

exams = [dict(id=f'u5-e{i+1}', title=tt, questions=qq) for i, (tt, qq) in enumerate(
    [('الاختبار الأول', E1), ('الاختبار الثاني', E2), ('الاختبار الثالث', E3), ('الاختبار الرابع', E4)])]
build(meta, exams, 'u5')
