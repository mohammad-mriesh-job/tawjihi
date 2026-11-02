"""Unit-7 exams 4-8 (imported by u7.py). Every item is a sibling of the official item named in the comment above
it (2026 = the 2008-generation paper, items 46-50; 2026r = 2026 repeaters paper 2; 2023-2025 = paper 2,
items 21-25). Each exam has 6 items on the geometric and binomial distributions and 6 on the normal distribution, in
that order; normal-table values are the ministry's 4-decimal ones, given in the stem as the ministry does."""
from qb import *
from u7_helpers import *

L1, L2 = 'u7-l1', 'u7-l2'
EMPNOTE = "\n" r"ملحوظة: يمكنك الاستفادة من القاعدة التجريبية المبيّنة في الشكل الآتي."
SHADED = r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، فإنّ مساحة المنطقة المُظلَّلة أسفل منحنى التوزيع الطبيعي المعياري المُبيَّنة في الشكل الآتي هي:"


def root01(expr, var=p):
    """the root of expr strictly between 0 and 1 (a probability)"""
    rs = [r_ for r_ in solve(expr, var) if r_.is_real and 0 < r_ < 1]
    assert len(rs) == 1, rs
    return rs[0]


# ============================================================== Exam 4 (the 2026 blueprint, items 46-50)
E4 = [
# 2026 #46: ratio of two geometric probabilities -> E(X); options = 1/p, p, 1 - p, 1/(1 - p)
Q('u7e4q1', L1, 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $\dfrac{P(X=2)}{P(X=5)}=\dfrac{343}{27}$ ، فإنّ التوقّع للمتغيّر العشوائي $X$ هو:",
  [O(r'\frac{7}{4}', R(7, 4)), O(r'\frac{4}{7}', R(4, 7)), O(r'\frac{3}{7}', R(3, 7)), O(r'\frac{7}{3}', R(7, 3))],
  r"$\dfrac{P(X=2)}{P(X=5)}=\dfrac{(1-p)p}{(1-p)^4p}=\dfrac{1}{(1-p)^3}=\dfrac{343}{27} \Rightarrow (1-p)^3=\dfrac{27}{343} \Rightarrow 1-p=\dfrac37$" "\n"
  r"$p=\dfrac47$ ، و $E(X)=\dfrac1p=\dfrac74$",
  truth=lambda: 1/root01(1/(1 - p)**3 - R(343, 27))),
# 2026 #47: quality control, reject when 2 or more defective; options = P(X >= 2), P(X = 0), 1 - P(X = 0), P(X <= 1)
Q('u7e4q2', L1, 'hard',
  r"يختار قسم ضبط الجودة في مصنع للمصابيح عيّنة عشوائية مكوّنة من $8$ مصابيح من كل صندوق لفحصها، ويُرفَض الصندوق إذا وُجد في العيّنة مصباحان تالفان فأكثر. إذا كانت نسبة المصابيح التالفة في إنتاج المصنع $5\%$ ، فإنّ احتمال رفض الصندوق هو تقريبًا:",
  [D('0.0572'), D('0.6634'), D('0.3366'), D('0.9428')],
  r"$X\sim B(8,\,0.05)$ ، و $P(X\ge2)=1-P(X=0)-P(X=1)$" "\n"
  r"$P(X=0)=(0.95)^8\approx0.66342$ ، $P(X=1)=\binom81(0.05)(0.95)^7\approx0.27934$" "\n"
  r"$P(X\ge2)\approx1-0.66342-0.27934=0.05724\approx0.0572$",
  truth=r4(1 - binom(8, R(5, 100), 0) - binom(8, R(5, 100), 1))),
# 2026r #22: n from E(X) and Var(X); options = n, E/(1 - p) (p and 1 - p swapped), Var/p, E/(p(1 - p))
Q('u7e4q3', L1, 'medium',
  r"إذا كان: $X\sim B(n,\,p)$ ، وكان: $E(X)=3$ ، $\text{Var}(X)=2.25$ ، فإنّ قيمة $n$ هي:",
  [O('12', 12), O('4', 4), O('9', 9), O('16', 16)],
  r"$\dfrac{\text{Var}(X)}{E(X)}=\dfrac{np(1-p)}{np}=1-p=\dfrac{2.25}{3}=0.75 \Rightarrow p=0.25$" "\n"
  r"$np=3 \Rightarrow n=\dfrac{3}{0.25}=12$",
  truth=lambda: solve([n*p - 3, n*p*(1 - p) - R(225, 100)], [n, p], dict=True)[0][n]),
# 2024s #21: a die thrown until a given outcome; options = (1-p)^2 p, p^2 (1-p) (swapped), (1-p)^2 (p forgotten), (1-p)^3
Q('u7e4q4', L1, 'easy',
  r"أُلقي حجر نرد منتظم بشكل متكرّر حتى ظهور العدد $5$ أو العدد $6$ أوّل مرّة، فإنّ احتمال إلقائه $3$ مرّات بالضبط هو:",
  [O(r'\frac{4}{27}', R(4, 27)), O(r'\frac{2}{27}', R(2, 27)), O(r'\frac{4}{9}', R(4, 9)), O(r'\frac{8}{27}', R(8, 27))],
  r"النجاح ظهور $5$ أو $6$: $p=\dfrac26=\dfrac13$ ، فيكون $X\sim Geo\left(\frac13\right)$" "\n"
  r"$P(X=3)=\left(\dfrac23\right)^2\cdot\dfrac13=\dfrac{4}{27}$",
  truth=geo(R(1, 3), 3)),
# 2024 #22: P(X = 1) = P(X = 2) -> Var(X); options = Var, E, sigma, p(1 - p)
Q('u7e4q5', L1, 'hard',
  r"إذا كان: $X\sim B(9,\,p)$ ، وكان: $P(X=1)=P(X=2)$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [D('1.44'), D('1.8'), D('1.2'), D('0.16')],
  r"$\binom91p(1-p)^8=\binom92p^2(1-p)^7 \Rightarrow 9(1-p)=36p \Rightarrow p=0.2$" "\n"
  r"$\text{Var}(X)=np(1-p)=9(0.2)(0.8)=1.44$",
  truth=lambda: (lambda pp: 9*pp*(1 - pp))(root01(binom(9, p, 1) - binom(9, p, 2)))),
# 2025 #21: which experiment is geometric; options = geometric, binomial, drawing together, measuring
IndexQ('u7e4q6', L1, 'easy',
  r"إحدى التجارب الآتية تُمثّل تجربة احتمالية هندسية:",
  [T('إلقاء قطعة نقد منتظمة بشكل متكرّر، ثم التوقّف عند ظهور الكتابة أوّل مرّة', 'geo'),
   T('إلقاء قطعة نقد منتظمة $12$ مرّة، ثم تسجيل عدد مرّات ظهور الكتابة', 'bin'),
   T('سحب $3$ كرات معًا من صندوق فيه $5$ كرات حمراء و $4$ كرات زرقاء، ثم تسجيل عدد الكرات الحمراء', 'draw'),
   T('اختيار $6$ طلبة عشوائيًّا من صفّ، ثم تسجيل أطوالهم', 'measure')],
  r"التجربة الهندسية: محاولات مستقلّة متكرّرة باحتمال نجاح ثابت، **وتتوقّف عند أوّل نجاح** (عدد المحاولات غير محدّد مسبقًا)." "\n"
  r"إلقاء القطعة $12$ مرّة تجربة ذات حدّين، والسحب معًا ليس محاولات مستقلّة، وتسجيل الأطوال ليس نجاحًا وفشلًا.",
  truth=lambda vals: only(vals, lambda v_: v_ == 'geo')),
# 2026 #48: P(X < a) for N(mu, sigma^2); options = complement or not x sigma or the variance used in z
Q('u7e4q7', L2, 'easy',
  r"إذا كان: $X\sim N(70,\,25)$ ، فإنّ $P(X<68)$ هو:" + ztable(0.08, 0.4, 0.8),
  [D('0.3446'), D('0.6554'), D('0.4681'), D('0.5319')],
  r"$\sigma=\sqrt{25}=5$ ، $z=\dfrac{68-70}{5}=-0.4$" "\n"
  r"$P(X<68)=P(Z<-0.4)=1-P(Z<0.4)=1-0.6554=0.3446$",
  truth=1 - Ph(R(4, 10))),
# 2026 #49: P(-k/c < Z < k/c) given -> k; options = right table entry times c, neighbouring entries, z divided by c
Q('u7e4q8', L2, 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{12}<Z<\dfrac{k}{12}\right)=0.7698$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:" + ztable(1.1, 1.2, 1.25),
  [D('14.4'), D('13.2'), D('15'), D('0.1')],
  r"$2P\left(Z<\dfrac{k}{12}\right)-1=0.7698 \Rightarrow P\left(Z<\dfrac{k}{12}\right)=\dfrac{1.7698}{2}=0.8849$" "\n"
  r"من الجدول: $\dfrac{k}{12}=1.2 \Rightarrow k=14.4$",
  truth=lambda: 12*[z_ for z_ in (R(11, 10), R(12, 10), R(125, 100)) if 2*Ph(z_) - 1 == R('0.7698')][0]),
# 2026 #50: sigma from the percentage above a value (closest table entry); options = sigma, z, d.z, z/d
Q('u7e4q9', L2, 'hard',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(24,\,\sigma^2)$ على أطوال نباتات (بالسنتيمتر) بعد شهر من زراعتها في أحد المشاتل. إذا كانت أطوال $4\%$ منها تزيد على $31\ \text{cm}$ ، فإنّ قيمة الانحراف المعياري لأطوال النباتات (مُقرَّبًا إلى أقرب منزلتين عشريتين) هي:" + ztable(1.74, 1.75, 1.76),
  [D('4.00', 'cm'), D('1.75', 'cm'), D('12.25', 'cm'), D('0.25', 'cm')],
  r"$P(X>31)=0.04 \Rightarrow P(X<31)=0.96$ ، وأقرب قيمة في الجدول $P(Z<1.75)=0.9599$ ، إذن $z=1.75$" "\n"
  r"$\dfrac{31-24}{\sigma}=1.75 \Rightarrow \sigma=\dfrac{7}{1.75}=4.00\ \text{cm}$",
  truth=lambda: 7/zclosest(R(96, 100), (R(174, 100), R(175, 100), R(176, 100)))),
# 2026r #23: shaded area between a negative and a positive z (figure); options = right, sign ignored, and their complements
Q('u7e4q10', L2, 'medium',
  SHADED + ztable(0.5, 1.25),
  [D('0.5859'), D('0.2029'), D('0.4141'), D('0.7971')],
  r"المنطقة بين $z=-0.5$ و $z=1.25$:" "\n"
  r"$P(-0.5<Z<1.25)=P(Z<1.25)-P(Z<-0.5)=0.8944-(1-0.6915)=0.8944-0.3085=0.5859$",
  truth=Ph(R(125, 100)) - Ph(-R(1, 2)), figure=figure('u7e4q10', bell(-0.5, 1.25, [-0.5, 1.25]), 4.0, 2.4)),
# 2023 #24: probability between mu - 2 sigma and mu + sigma by the empirical rule (figure): three bands, as in 2023 #24
# and 2024s #23; options = the right sum, the interval taken as mu +- 2 sigma, mu +- sigma only, one side (mu - 2 sigma
# to mu) only
Q('u7e4q11', L2, 'medium',
  r"إذا كان: $X\sim N(50,\,16)$ ، فإنّ $P(42<X<54)$ هو:" + EMPNOTE,
  [D('0.815'), D('0.95'), D('0.68'), D('0.475')],
  r"$\sigma=\sqrt{16}=4$ ، و $42=50-8=\mu-2\sigma$ ، و $54=50+4=\mu+\sigma$" "\n"
  r"$P(42<X<54)=0.135+0.34+0.34=0.815$",
  truth=emp(-2, 1), figure=figure('u7e4q11', emp_fig, 4.4, 2.4)),
# 2025 #24: P(X < mu - k) given -> P(mu - k < X < mu + k); options = 1 - 2a, 1 - a, a, 2a
Q('u7e4q12', L2, 'easy',
  r"إذا كان: $X\sim N(\mu,\,\sigma^2)$ ، وكان: $P(X<\mu-k)=0.18$ ، حيث $k$ ثابت موجب، فإنّ قيمة $P(\mu-k<X<\mu+k)$ هي:",
  [D('0.64'), D('0.82'), D('0.18'), D('0.36')],
  r"المنحنى متماثل حول $\mu$ ، فيكون $P(X>\mu+k)=P(X<\mu-k)=0.18$" "\n"
  r"$P(\mu-k<X<\mu+k)=1-0.18-0.18=0.64$",
  truth=1 - 2*R(18, 100)),
]

# ============================================================== Exam 5
E5 = [
# 2025 #22: P(X > k) given -> E(X); options = 1/p, 1/(1 - p), p, 1 - p
Q('u7e5q1', L1, 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $P(X>2)=0.04$ ، فإنّ توقّع المتغيّر العشوائي $X$ هو:",
  [D('1.25'), D('5'), D('0.8'), D('0.2')],
  r"$X>2$ يعني أنّ المحاولتين الأوليين فشل: $P(X>2)=(1-p)^2=0.04 \Rightarrow 1-p=0.2 \Rightarrow p=0.8$" "\n"
  r"$E(X)=\dfrac{1}{0.8}=1.25$",
  truth=lambda: 1/root01((1 - p)**2 - R(4, 100))),
# 2025s #22: E(X) and p -> Var(X); options = E(1 - p), Ep, p(1 - p), n(1 - p)
Q('u7e5q2', L1, 'easy',
  r"إذا كان: $X\sim B(n,\,0.3)$ ، وكان: $E(X)=6$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [D('4.2'), D('1.8'), D('0.21'), O('14', 14)],
  r"$\text{Var}(X)=np(1-p)=E(X)\,(1-p)=6(0.7)=4.2$ (وهنا $n=\dfrac{6}{0.3}=20$)",
  truth=6*(1 - R(3, 10))),
# 2023 #22: at least n - 1 successes in n trials, written in powers (n(1 - p) = 1 collapses the binomial coefficient);
# options = the right sum, all successes only, one term without its coefficient, the failure power added
Q('u7e5q3', L1, 'medium',
  r"إذا كان احتمال أن تُصيب رامية الهدف في الرمية الواحدة يساوي $\dfrac34$ ، ورمت $4$ رميات متتالية، فإنّ احتمال إصابتها الهدف في $3$ رميات على الأقل هو:",
  [O(r'\left(\frac{3}{4}\right)^{3}+\left(\frac{3}{4}\right)^{4}', R(3, 4)**3 + R(3, 4)**4), O(r'\left(\frac{3}{4}\right)^{4}', R(3, 4)**4),
   O(r'\left(\frac{3}{4}\right)^{3}\cdot\frac{1}{4}', R(3, 4)**3*R(1, 4)), O(r'\left(\frac{3}{4}\right)^{3}+\left(\frac{1}{4}\right)^{4}', R(3, 4)**3 + R(1, 4)**4)],
  r"$X\sim B\left(4,\frac34\right)$ ، و $P(X\ge3)=P(X=3)+P(X=4)$" "\n"
  r"$P(X\ge3)=\binom43\left(\frac34\right)^3\left(\frac14\right)+\left(\frac34\right)^4=\left(\frac34\right)^3+\left(\frac34\right)^4$ (لأن $4\times\frac14=1$)",
  truth=binom(4, R(3, 4), 3) + binom(4, R(3, 4), 4)),
# 2026r #21: trials until the first success in context; options = (1-p)^3 p, (1-p)^4, p^3 (1-p), (1-p)^3
Q('u7e5q4', L1, 'easy',
  r"يُرسل جهاز إشارات متتالية إلى قمر صناعي حتى يستقبل القمر أوّل إشارة، واحتمال استقبال الإشارة الواحدة $0.2$. احتمال أن يستقبل القمر أوّل إشارة عند الإشارة الرابعة هو:",
  [D('0.1024'), D('0.4096'), D('0.0064'), D('0.512')],
  r"$X\sim Geo(0.2)$ ، و $P(X=4)=(0.8)^3(0.2)=0.512(0.2)=0.1024$",
  truth=geo(R(2, 10), 4)),
# 2024s #22: Var of a given binomial; options = Var, E, sigma, p(1 - p)
Q('u7e5q5', L1, 'easy',
  r"إذا كان: $X\sim B(25,\,0.2)$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [O('4', 4), O('5', 5), O('2', 2), D('0.16')],
  r"$\text{Var}(X)=np(1-p)=25(0.2)(0.8)=4$",
  truth=25*R(2, 10)*R(8, 10)),
# 2023 #23: Var given -> the two possible p; options = pairs p, 1 - p
Q('u7e5q6', L1, 'hard',
  r"إذا كان: $X\sim B(100,\,p)$ ، وكان التباين للمتغيّر العشوائي $X$ يساوي $16$ ، فإنّ قيم الثابت $p$ الممكنة هي:",
  [pair_opt(r'p=0.2,\ p=0.8', R(2, 10), R(8, 10)), pair_opt(r'p=0.4,\ p=0.6', R(4, 10), R(6, 10)),
   pair_opt(r'p=0.1,\ p=0.9', R(1, 10), R(9, 10)), pair_opt(r'p=0.3,\ p=0.7', R(3, 10), R(7, 10))],
  r"$100p(1-p)=16 \Rightarrow p^2-p+0.16=0 \Rightarrow (p-0.2)(p-0.8)=0$" "\n"
  r"$p=0.2$ أو $p=0.8$",
  truth=lambda: FiniteSet(*solve(100*x*(1 - x) - 16, x))),
# 2026r #24: P(Z > z) given -> P(-z < Z < z); options = 1 - 2a, 1 - a, a, 2a
Q('u7e5q7', L2, 'easy',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P(Z>z)=0.2119$ ، فإنّ $P(-z<Z<z)$ هو:",
  [D('0.5762'), D('0.7881'), D('0.2119'), D('0.4238')],
  r"بالتماثل: $P(Z<-z)=P(Z>z)=0.2119$" "\n"
  r"$P(-z<Z<z)=1-2(0.2119)=1-0.4238=0.5762$",
  truth=1 - 2*R('0.2119')),
# 2026 #49: P(-k/c < Z < k/c) given -> k (replaced an x-from-P item on 2026-11-02: the exam had two, and no 2026 #49);
# options = right z or the unhalved one (closest entry), x times c or divided by c
Q('u7e5q8', L2, 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{5}<Z<\dfrac{k}{5}\right)=0.2358$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:" + ztable(0.3, 0.63),
  [D('1.5'), D('3.15'), D('0.06'), D('0.126')],
  r"$2P\left(Z<\dfrac{k}{5}\right)-1=0.2358 \Rightarrow P\left(Z<\dfrac{k}{5}\right)=\dfrac{1.2358}{2}=0.6179$" "\n"
  r"من الجدول: $\dfrac{k}{5}=0.3 \Rightarrow k=1.5$",
  truth=lambda: 5*[z_ for z_ in (R(3, 10), R(63, 100)) if 2*Ph(z_) - 1 == R('0.2358')][0]),
# 2025s #25: sigma from the interval holding 95% (empirical rule, figure); options = sigma, sigma^2, 2 sigma, 4 sigma
Q('u7e5q9', L2, 'medium',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(7.6,\,\sigma^2)$ على أقطار ثمار البرتقال (بالسنتيمتر) في إحدى المزارع. إذا كانت أقطار $95\%$ منها تتراوح بين $6.8\ \text{cm}$ و $8.4\ \text{cm}$ ، فإنّ قيمة الانحراف المعياري $\sigma$ لأقطار الثمار هي:" + EMPNOTE,
  [D('0.4', 'cm'), D('0.16', 'cm'), D('0.8', 'cm'), D('1.6', 'cm')],
  r"حسب القاعدة التجريبية تقع $95\%$ من القيم بين $\mu-2\sigma$ و $\mu+2\sigma$:" "\n"
  r"$\mu+2\sigma=8.4 \Rightarrow 7.6+2\sigma=8.4 \Rightarrow 2\sigma=0.8 \Rightarrow \sigma=0.4\ \text{cm}$",
  truth=(R(84, 10) - R(76, 10))/2, figure=figure('u7e5q9', emp_fig, 4.4, 2.4)),
# 2024 #25: P(a < Z < b) with a < 0 < b; options = right, sign ignored, and their complements
Q('u7e5q10', L2, 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، فإنّ $P(-1<Z<0.5)$ يساوي:" + ztable(0.5, 1),
  [D('0.5328'), D('0.1498'), D('0.4672'), D('0.8502')],
  r"$P(-1<Z<0.5)=P(Z<0.5)-P(Z<-1)=0.6915-(1-0.8413)=0.6915-0.1587=0.5328$",
  truth=Ph(R(1, 2)) - Ph(-1)),
# 2025 #25: x from P(mu < X < x) (closest table entry); options = right, the other entry, P(Z < z) = 0.3 read, the
# probability used as z
Q('u7e5q11', L2, 'hard',
  r"إذا كان: $X\sim N(150,\,100)$ ، وكان: $P(150<X<x)=0.3$ ، فإنّ قيمة $x$ هي:" + ztable(0.52, 0.84, 0.85),
  [D('158.4'), D('158.5'), D('144.8'), D('153')],
  r"$P(150<X<x)=P(0<Z<z)=P(Z<z)-0.5=0.3 \Rightarrow P(Z<z)=0.8$" "\n"
  r"أقرب قيمة في الجدول $P(Z<0.84)=0.7995$ ، إذن $z=0.84$ ، و $x=150+10(0.84)=158.4$",
  truth=lambda: 150 + 10*zclosest(R(8, 10), (R(52, 100), R(84, 100), R(85, 100)))),
# 2023s #25: X ~ N(mu, mu^2/9) -> P(X > 1.5 mu); options = 1 - P(Z<1.5), P(Z<1.5), and both with sigma = mu
Q('u7e5q12', L2, 'hard',
  r"إذا كان: $X\sim N\left(\mu,\,\dfrac{\mu^2}{9}\right)$ ، حيث $\mu>0$ ، فإنّ قيمة $P(X>1.5\mu)$ تساوي:" + ztable(0.5, 1.5),
  [D('0.0668'), D('0.9332'), D('0.3085'), D('0.6915')],
  r"$\sigma=\sqrt{\dfrac{\mu^2}{9}}=\dfrac{\mu}{3}$ ، و $z=\dfrac{1.5\mu-\mu}{\mu/3}=\dfrac{0.5\mu}{\mu/3}=1.5$" "\n"
  r"$P(X>1.5\mu)=P(Z>1.5)=1-0.9332=0.0668$",
  truth=1 - Ph(R(3, 2))),
]

# ============================================================== Exam 6
E6 = [
# 2023 #21: P(X > k) of a given geometric variable (replaced a third E(X) = 1/p item on 2026-11-02); options = (1-p)^2
# or p^2 (p and 1 - p swapped), x P(X > 2) or its complement P(X <= 2)
Q('u7e6q1', L1, 'easy',
  r"إذا كان: $X\sim Geo(0.1)$ ، فإنّ $P(X>2)$ يساوي:",
  [D('0.81'), D('0.19'), D('0.01'), D('0.99')],
  r"$X>2$ يعني أنّ المحاولتين الأوليين فشل: $P(X>2)=(1-p)^2=(0.9)^2=0.81$",
  truth=(1 - R(1, 10))**2),
# 2026 #47: acceptance with at most one defective; options = P(X <= 1), P(X = 0), 1 - P(X <= 1), P(X = 1)
Q('u7e6q2', L1, 'hard',
  r"تختار شركة عيّنة عشوائية من $6$ عبوات من كل شحنة تصلها، وتقبل الشحنة إذا كانت في العيّنة عبوة تالفة واحدة على الأكثر. إذا كانت نسبة العبوات التالفة لدى المورّد $15\%$ ، فإنّ احتمال قبول الشحنة هو تقريبًا:",
  [D('0.7765'), D('0.3771'), D('0.2235'), D('0.3993')],
  r"$X\sim B(6,\,0.15)$ ، و $P(X\le1)=P(X=0)+P(X=1)$" "\n"
  r"$P(X=0)=(0.85)^6\approx0.37715$ ، $P(X=1)=\binom61(0.15)(0.85)^5\approx0.39934$" "\n"
  r"$P(X\le1)\approx0.37715+0.39934=0.77649\approx0.7765$",
  truth=r4(binom(6, R(15, 100), 0) + binom(6, R(15, 100), 1))),
# 2023s #22: binomial P(X = k) in context with a percentage, approximate value (replaced a 2026 #46 item on 2026-11-02:
# exam 6 shared four of its six binomial/geometric ideas with exam 4); options = right, the coefficient C(6, 2) forgotten,
# x the failure power n instead of n - k
Q('u7e6q3', L1, 'medium',
  r"نسبة الرحلات التي تتأخّر فيها حافلات إحدى الشركات عن موعدها $10\%$. إذا اختيرت $6$ رحلات عشوائيًّا، فإنّ احتمال أن يكون التأخّر في رحلتين منها بالضبط هو تقريبًا:",
  [D('0.0984'), D('0.0066'), D('0.0797'), D('0.0053')],
  r"$X\sim B(6,\,0.1)$ ، و $P(X=2)=\binom62(0.1)^2(0.9)^4=15(0.01)(0.6561)\approx0.0984$",
  truth=r4(binom(6, R(1, 10), 2))),
# 2023 #22: at least n - 1 successes, written in powers; options = the right sum, all successes, one term, the
# coefficient n kept
Q('u7e6q4', L1, 'medium',
  r"إذا كان احتمال أن يُجيب طالب إجابة صحيحة عن سؤال يساوي $\dfrac{9}{10}$ ، وأجاب عن $10$ أسئلة مستقلّة، فإنّ احتمال أن تكون إجاباته الصحيحة $9$ على الأقل هو:",
  [O(r'\left(\frac{9}{10}\right)^{9}+\left(\frac{9}{10}\right)^{10}', R(9, 10)**9 + R(9, 10)**10), O(r'\left(\frac{9}{10}\right)^{10}', R(9, 10)**10),
   O(r'\left(\frac{9}{10}\right)^{9}\cdot\frac{1}{10}', R(9, 10)**9*R(1, 10)), O(r'10\cdot\left(\frac{9}{10}\right)^{9}+\left(\frac{9}{10}\right)^{10}', 10*R(9, 10)**9 + R(9, 10)**10)],
  r"$X\sim B\left(10,\frac{9}{10}\right)$ ، و $P(X\ge9)=P(X=9)+P(X=10)$" "\n"
  r"$P(X\ge9)=\binom{10}{9}\left(\frac{9}{10}\right)^9\left(\frac{1}{10}\right)+\left(\frac{9}{10}\right)^{10}=\left(\frac{9}{10}\right)^9+\left(\frac{9}{10}\right)^{10}$ (لأن $10\times\frac{1}{10}=1$)",
  truth=binom(10, R(9, 10), 9) + binom(10, R(9, 10), 10)),
# 2026r #22: n from E(X) and Var(X); options = n, E/(1 - p), E/(p(1 - p)), Var/p
Q('u7e6q5', L1, 'medium',
  r"إذا كان: $X\sim B(n,\,p)$ ، وكان: $E(X)=6$ ، $\text{Var}(X)=3.6$ ، فإنّ قيمة $n$ هي:",
  [O('15', 15), O('10', 10), O('25', 25), O('9', 9)],
  r"$\dfrac{\text{Var}(X)}{E(X)}=1-p=\dfrac{3.6}{6}=0.6 \Rightarrow p=0.4$" "\n"
  r"$np=6 \Rightarrow n=\dfrac{6}{0.4}=15$",
  truth=lambda: solve([n*p - 6, n*p*(1 - p) - R(36, 10)], [n, p], dict=True)[0][n]),
# 2024 #22: P(X = 3) = P(X = 4) -> Var(X); options = Var, E, p(1 - p), p
Q('u7e6q6', L1, 'hard',
  r"إذا كان: $X\sim B(7,\,p)$ ، وكان: $P(X=3)=P(X=4)$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [D('1.75'), D('3.5'), D('0.25'), D('0.5')],
  r"$\binom73p^3(1-p)^4=\binom74p^4(1-p)^3$ ، و $\binom73=\binom74=35$ ، إذن $1-p=p \Rightarrow p=0.5$" "\n"
  r"$\text{Var}(X)=7(0.5)(0.5)=1.75$",
  truth=lambda: (lambda pp: 7*pp*(1 - pp))(root01(binom(7, p, 3) - binom(7, p, 4)))),
# 2025s #23: probability above a value in context; options = 1 - P(Z<z), P(Z<z), P(Z<z) - 0.5, 0.5 + (1 - P(Z<z))
Q('u7e6q7', L2, 'easy',
  r"تتوزّع أطوال طلبة الصف الثاني عشر في إحدى المدارس توزيعًا طبيعيًّا وسطه الحسابي $170\ \text{cm}$ وانحرافه المعياري $8\ \text{cm}$. إذا اختير طالب عشوائيًّا، فإنّ احتمال أن يزيد طوله على $178.8\ \text{cm}$ هو:" + ztable(0.5, 1, 1.1, 1.5),
  [D('0.1357'), D('0.8643'), D('0.3643'), D('0.6357')],
  r"$z=\dfrac{178.8-170}{8}=\dfrac{8.8}{8}=1.1$" "\n"
  r"$P(X>178.8)=P(Z>1.1)=1-0.8643=0.1357$",
  truth=1 - Ph(R(11, 10))),
# 2026 #50 asked for mu instead of sigma (the unified trial exam asks for mu and/or sigma; replaced a 2026 #49 item on
# 2026-11-02): the percentage above a value with sigma known (in words: mock n3q30 already writes N(mu, 25)) -> mu;
# options = x - z sigma or x + z sigma, x sigma multiplied or forgotten
Q('u7e6q8', L2, 'medium',
  r"تتوزّع سرعات السيارات على أحد الطرق توزيعًا طبيعيًّا وسطه الحسابي $\mu$ وانحرافه المعياري $5\ \text{km/h}$. إذا كانت سرعات $5.48\%$ من السيارات تزيد على $82\ \text{km/h}$ ، فإنّ قيمة $\mu$ هي:" + ztable(1.5, 1.6, 1.7),
  [D('74', 'km/h'), D('90', 'km/h'), D('80.4', 'km/h'), D('83.6', 'km/h')],
  r"$P(X>82)=0.0548 \Rightarrow P(X<82)=0.9452=P(Z<1.6)$ ، إذن $z=1.6$" "\n"
  r"$\dfrac{82-\mu}{5}=1.6 \Rightarrow \mu=82-5(1.6)=74\ \text{km/h}$",
  truth=lambda: 82 - 5*[z_ for z_ in (R(15, 10), R(16, 10), R(17, 10)) if Ph(z_) == 1 - R('0.0548')][0]),
# 2024s #24: shaded area between two negative z (figure); options = right, sign slip, sum of the tails, complement
Q('u7e6q9', L2, 'medium',
  SHADED + ztable(0.5, 2),
  [D('0.2857'), D('0.7143'), D('0.6687'), D('0.3313')],
  r"المنطقة بين $z=-2$ و $z=-0.5$:" "\n"
  r"$P(-2<Z<-0.5)=P(Z<-0.5)-P(Z<-2)=(1-0.6915)-(1-0.9772)=0.3085-0.0228=0.2857$",
  truth=Ph(-R(1, 2)) - Ph(-2), figure=figure('u7e6q9', bell(-2, -0.5, [-2, -0.5]), 4.0, 2.4)),
# 2025s #24: P(X > mu + k) given -> P(X < mu - k) by symmetry; options = a, 1 - a, 1 - 2a, 2a
Q('u7e6q10', L2, 'easy',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(\mu,\,\sigma^2)$ على كتل أكياس الطحين في أحد المطاحن. إذا كان: $P(X>\mu+12)=0.29$ ، فإنّ $P(X<\mu-12)$ هو:",
  [D('0.29'), D('0.71'), D('0.42'), D('0.58')],
  r"المنحنى متماثل حول $\mu$ ، والقيمتان $\mu-12$ و $\mu+12$ على البُعد نفسه منه:" "\n"
  r"$P(X<\mu-12)=P(X>\mu+12)=0.29$",
  truth=R(29, 100)),
# 2023s #24: percentage between two values by the empirical rule (figure), a sum of two bands as in the model (the mean
# to mu + 2 sigma here); options = mu..mu+2s, both sides mu +- 2s, mu..mu+s, 50%
Q('u7e6q11', L2, 'easy',
  r"تتوزّع كتل علب أحد المنتجات توزيعًا طبيعيًّا وسطه الحسابي $500\ \text{g}$ وانحرافه المعياري $20\ \text{g}$. النسبة المئوية للعلب التي تتراوح كتلها بين $500\ \text{g}$ و $540\ \text{g}$ هي:" + EMPNOTE,
  [O(r'47.5\%', R(475, 10)), O(r'95\%', 95), O(r'34\%', 34), O(r'50\%', 50)],
  r"$500=\mu$ ، و $540=500+2(20)=\mu+2\sigma$" "\n"
  r"النسبة: $34\%+13.5\%=47.5\%$",
  truth=100*emp(0, 2), figure=figure('u7e6q11', emp_fig, 4.4, 2.4)),
# 2024s #25: x from P(X < x) below the mean (closest table entry); options = mu - z sigma, mu + z sigma, mu - z, mu - z sigma^2
Q('u7e6q12', L2, 'hard',
  r"إذا كان: $X\sim N(20,\,16)$ ، فإنّ قيمة $x$ التي تُحقّق $P(X<x)=0.2$ هي:" + ztable(0.84, 0.85),
  [D('16.64'), D('23.36'), D('19.16'), D('6.56')],
  r"الاحتمال أقل من $0.5$ ، فـ $x$ أقلّ من الوسط: $P(Z<-z)=0.2 \Rightarrow P(Z<z)=0.8$ ، وأقرب قيمة في الجدول $z=0.84$" "\n"
  r"$\dfrac{x-20}{4}=-0.84 \Rightarrow x=20-4(0.84)=16.64$",
  truth=lambda: 20 - 4*zclosest(R(8, 10), (R(84, 100), R(85, 100)))),
]

# ============================================================== Exam 7
E7 = [
# 2025 #22: P(X > k) given -> P(X = k); options = (1-p)p, (1-p)^2 p, p^2, 1 - p
Q('u7e7q1', L1, 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $P(X>2)=0.09$ ، فإنّ $P(X=2)$ يساوي:",
  [D('0.21'), D('0.063'), D('0.49'), D('0.3')],
  r"$P(X>2)=(1-p)^2=0.09 \Rightarrow 1-p=0.3 \Rightarrow p=0.7$" "\n"
  r"$P(X=2)=(1-p)p=0.3(0.7)=0.21$",
  truth=lambda: geo(root01((1 - p)**2 - R(9, 100)), 2)),
# 2026 #47: reject when at least one is defective; options = P(X >= 1), P(X = 0), P(X = 1), P(X >= 2)
Q('u7e7q2', L1, 'medium',
  r"يفحص مختبر عيّنة عشوائية من $10$ قطع من كل دفعة إنتاج، وتُرفَض الدفعة إذا وُجدت في العيّنة قطعة معيبة واحدة على الأقل. إذا كانت نسبة القطع المعيبة $5\%$ ، فإنّ احتمال رفض الدفعة هو تقريبًا:",
  [D('0.4013'), D('0.5987'), D('0.3151'), D('0.0861')],
  r"$X\sim B(10,\,0.05)$ ، و $P(X\ge1)=1-P(X=0)=1-(0.95)^{10}\approx1-0.5987=0.4013$",
  truth=r4(1 - binom(10, R(5, 100), 0))),
# 2025 #21: which experiment is binomial; options = binomial, geometric, drawing together, measuring
IndexQ('u7e7q3', L1, 'easy',
  r"إحدى التجارب الآتية تُمثّل تجربة احتمالية ذات حدّين:",
  [T('إلقاء حجر نرد منتظم $12$ مرّة، ثم تسجيل عدد مرّات ظهور عدد زوجي', 'bin'),
   T('إلقاء حجر نرد منتظم بشكل متكرّر، ثم التوقّف عند ظهور العدد $1$ أوّل مرّة', 'geo'),
   T('سحب $4$ بطاقات معًا من مجموعة بطاقات، ثم تسجيل عدد البطاقات الحمراء', 'draw'),
   T('اختيار $5$ أشجار عشوائيًّا من حديقة، ثم قياس ارتفاعاتها', 'measure')],
  r"تجربة ذات الحدّين: عدد **ثابت** من المحاولات المستقلّة، لكلّ منها نتيجتان، واحتمال النجاح ثابت." "\n"
  r"الإلقاء حتى أوّل نجاح تجربة هندسية، والسحب معًا ليس محاولات مستقلّة، وقياس الارتفاعات ليس نجاحًا وفشلًا.",
  truth=lambda vals: only(vals, lambda v_: v_ == 'bin')),
# 2023 #23: Var given -> the two possible values of p (the model stops there; no E(X) asked); options = pairs p, 1 - p:
# the right pair, the zero-product rule misapplied to p(1 - p) = 0.21 (p = 0.21 or 1 - p = 0.21), two pairs of tenths
Q('u7e7q4', L1, 'hard',
  r"إذا كان: $X\sim B(50,\,p)$ ، وكان التباين للمتغيّر العشوائي $X$ يساوي $10.5$ ، فإنّ قيم الثابت $p$ الممكنة هي:",
  [pair_opt(r'p=0.3,\ p=0.7', R(3, 10), R(7, 10)), pair_opt(r'p=0.21,\ p=0.79', R(21, 100), R(79, 100)),
   pair_opt(r'p=0.2,\ p=0.8', R(2, 10), R(8, 10)), pair_opt(r'p=0.4,\ p=0.6', R(4, 10), R(6, 10))],
  r"$50p(1-p)=10.5 \Rightarrow p^2-p+0.21=0 \Rightarrow (p-0.3)(p-0.7)=0$" "\n"
  r"$p=0.3$ أو $p=0.7$",
  truth=lambda: FiniteSet(*solve(50*x*(1 - x) - R(105, 10), x))),
# 2024s #22: Var of a given binomial; options = Var, E, sigma, p(1 - p)
Q('u7e7q5', L1, 'easy',
  r"إذا كان: $X\sim B\left(18,\,\dfrac13\right)$ ، فإنّ التباين للمتغيّر العشوائي $X$ هو:",
  [O('4', 4), O('6', 6), O('2', 2), O(r'\frac{2}{9}', R(2, 9))],
  r"$\text{Var}(X)=np(1-p)=18\left(\dfrac13\right)\left(\dfrac23\right)=4$",
  truth=18*R(1, 3)*R(2, 3)),
# 2023s #23: E(X) of a geometric variable; options = 1/p, 1/(1 - p), p, 1 - p (decimals)
Q('u7e7q6', L1, 'easy',
  r"إذا كان: $X\sim Geo(0.125)$ ، فإنّ توقّع المتغيّر العشوائي $X$ هو:",
  [O('8', 8), D('1.143'), D('0.125'), D('0.875')],
  r"$E(X)=\dfrac1p=\dfrac{1}{0.125}=8$",
  truth=1/R(125, 1000)),
# 2026 #50: sigma from the percentage below a value (closest table entry); options = sigma, z, d.z, z/d
Q('u7e7q7', L2, 'hard',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(600,\,\sigma^2)$ على أعمار البطاريات (بالساعات) التي يُنتجها أحد المصانع. إذا كان عمر $10\%$ منها يقلّ عن $536$ ساعة، فإنّ قيمة الانحراف المعياري لأعمار البطاريات هي:" + ztable(1.28, 1.29),
  [O('50', 50), D('1.28'), D('81.92'), D('0.02')],
  r"$P(X<536)=0.1 \Rightarrow P(Z<-z)=0.1 \Rightarrow P(Z<z)=0.9$ ، وأقرب قيمة في الجدول $P(Z<1.28)=0.8997$" "\n"
  r"$\dfrac{536-600}{\sigma}=-1.28 \Rightarrow \sigma=\dfrac{64}{1.28}=50$ ساعة",
  truth=lambda: 64/zclosest(R(9, 10), (R(128, 100), R(129, 100)))),
# 2026r #24: P(Z > z) given -> P(-z < Z < z); options = 1 - 2a, 1 - a, a, 2a
Q('u7e7q8', L2, 'easy',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P(Z>z)=0.0228$ ، فإنّ $P(-z<Z<z)$ هو:",
  [D('0.9544'), D('0.9772'), D('0.0228'), D('0.0456')],
  r"بالتماثل: $P(Z<-z)=P(Z>z)=0.0228$" "\n"
  r"$P(-z<Z<z)=1-2(0.0228)=0.9544$",
  truth=1 - 2*R('0.0228')),
# 2025 #23: sigma from a curve whose 2.5% tails are marked, with the empirical-rule figure given as a note as in the
# model (one figure: the item's curve on top, the note's curve below); options = sigma, 2 sigma, 4 sigma, sigma/2
Q('u7e7q9', L2, 'medium',
  r"يُمثّل منحنى التوزيع الطبيعي العلوي في الشكل الآتي نمذجة لكتل حبّات التفاح (بالغرام) في إحدى المزارع، فإنّ الانحراف المعياري لكتل حبّات التفاح هو:"
  "\n" r"ملحوظة: يمكنك الاستفادة من القاعدة التجريبية المبيّنة في المنحنى السفلي من الشكل.",
  [O('8', 8, units='g'), O('16', 16, units='g'), O('32', 32, units='g'), O('4', 4, units='g')],
  r"من شكل القاعدة التجريبية: فوق $\mu+2\sigma$ النسبة $2.35\%+0.15\%=2.5\%$ ، وكذلك تحت $\mu-2\sigma$ ، فالقيمتان $124$ و $156$ هما $\mu-2\sigma$ و $\mu+2\sigma$" "\n"
  r"$4\sigma=156-124=32 \Rightarrow \sigma=8\ \text{g}$ (والوسط $\mu=140\ \text{g}$)",
  truth=R(156 - 124, 4), figure=figure('u7e7q9', tails_emp_fig('124', r'$\mu$', '156', '2.5%'), 4.4, 4.6)),
# 2024s #24: shaded area between two negative z (figure; replaced a 2024 #25 item on 2026-11-02, which exam 5 also
# has); options = right, complement, -2.5 read as 2.5, sum of the two areas
Q('u7e7q10', L2, 'medium',
  SHADED + ztable(0.5, 2.5),
  [D('0.3023'), D('0.6977'), D('0.6853'), D('0.3147')],
  r"المنطقة بين $z=-2.5$ و $z=-0.5$:" "\n"
  r"$P(-2.5<Z<-0.5)=P(Z<-0.5)-P(Z<-2.5)=(1-0.6915)-(1-0.9938)=0.3085-0.0062=0.3023$",
  truth=Ph(-R(1, 2)) - Ph(-R(5, 2)), figure=figure('u7e7q10', bell(-2.5, -0.5, [-2.5, -0.5]), 4.0, 2.4)),
# 2024 #24: X ~ N(mu, mu^2) (sigma = mu, as in the model) and the z-score of a given x -> sigma; options = sigma, the
# variance mu^2 used in z (2 mu^2 + mu - 15 = 0 gives 2.5), sigma^2, x
Q('u7e7q11', L2, 'medium',
  r"إذا كان: $X\sim N(\mu,\,\mu^2)$ ، حيث $\mu>0$ ، وكانت قيمة $z$ المعيارية المقابلة لقيمة $x=15$ هي $2$ ، فإنّ قيمة الانحراف المعياري لهذا التوزيع هي:",
  [O('5', 5), D('2.5'), O('25', 25), O('15', 15)],
  r"$\sigma=\sqrt{\mu^2}=\mu$ ، و $\dfrac{15-\mu}{\mu}=2 \Rightarrow 15-\mu=2\mu \Rightarrow \mu=5$" "\n"
  r"$\sigma=\mu=5$",
  truth=lambda: solve((15 - x)/x - 2, x)[0]),
# 2026 #50 asked for mu (as u7e6q8; replaced an x-from-P item on 2026-11-02), the percentage below a value: x is below
# the mean, so mu = x + z sigma; options = x + z sigma or x - z sigma, x sigma or the variance used
Q('u7e7q12', L2, 'medium',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(\mu,\,100)$ على كتل أرغفة الخبز (بالغرام) التي يُنتجها أحد المخابز. إذا كانت كتل $9.68\%$ من الأرغفة تقلّ عن $237\ \text{g}$ ، فإنّ قيمة $\mu$ هي:" + ztable(1.2, 1.3, 1.4),
  [D('250', 'g'), D('224', 'g'), D('367', 'g'), D('107', 'g')],
  r"$P(X<237)=0.0968<0.5$ ، فـ $237$ تحت الوسط: $P(Z<-z)=0.0968 \Rightarrow P(Z<z)=0.9032 \Rightarrow z=1.3$" "\n"
  r"$\dfrac{237-\mu}{10}=-1.3 \Rightarrow \mu=237+10(1.3)=250\ \text{g}$",
  truth=lambda: 237 + 10*[z_ for z_ in (R(12, 10), R(13, 10), R(14, 10)) if Ph(z_) == 1 - R('0.0968')][0]),
]

# ============================================================== Exam 8
E8 = [
# 2026 #46: ratio of geometric probabilities two apart -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) (decimals)
Q('u7e8q1', L1, 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $\dfrac{P(X=3)}{P(X=5)}=\dfrac{100}{81}$ ، فإنّ التوقّع للمتغيّر العشوائي $X$ هو:",
  [O('10', 10), D('0.1'), D('0.9'), D('1.11')],
  r"$\dfrac{P(X=3)}{P(X=5)}=\dfrac{(1-p)^2p}{(1-p)^4p}=\dfrac{1}{(1-p)^2}=\dfrac{100}{81} \Rightarrow 1-p=0.9 \Rightarrow p=0.1$" "\n"
  r"$E(X)=\dfrac{1}{0.1}=10$",
  truth=lambda: 1/root01(1/(1 - p)**2 - R(100, 81))),
# 2026r #21: testing chips until the first defective; options = (1-p)^3 p, (1-p)^4, p^3 (1-p), (1-p)^3
Q('u7e8q2', L1, 'easy',
  r"بدأ مهندس اختبار رقاقات إلكترونية واحدة تلو الأخرى على أن يتوقّف عند إيجاد أوّل رقاقة معيبة. إذا كان احتمال أن تكون الرقاقة معيبة $0.1$ ، فإنّ احتمال أن يتوقّف المهندس بعد فحصه $4$ رقاقات هو:",
  [D('0.0729'), D('0.6561'), D('0.0009'), D('0.729')],
  r"$X\sim Geo(0.1)$ ، و $P(X=4)=(0.9)^3(0.1)=0.729(0.1)=0.0729$",
  truth=geo(R(1, 10), 4)),
# 2025 #22: P(X > k) given -> P(X <= 3); options = 1 - (1-p)^3, (1-p)^3, (1-p)^2 p, 1 - (1-p)^2
Q('u7e8q3', L1, 'medium',
  r"إذا كان: $X\sim Geo(p)$ ، وكان: $P(X>2)=0.49$ ، فإنّ $P(X\le3)$ يساوي:",
  [D('0.657'), D('0.343'), D('0.147'), D('0.51')],
  r"$P(X>2)=(1-p)^2=0.49 \Rightarrow 1-p=0.7$" "\n"
  r"$P(X\le3)=1-P(X>3)=1-(0.7)^3=1-0.343=0.657$",
  truth=lambda: 1 - (1 - root01((1 - p)**2 - R(49, 100)))**3),
# 2024 #21: a fair die thrown n times, P(an outcome k times) (replaced a 2025s #22 item on 2026-11-02, which exam 5
# also has); options = right, the coefficient C(3, 2) forgotten, x the failure factor forgotten
Q('u7e8q4', L1, 'easy',
  r"في تجربة إلقاء حجر نرد منتظم $3$ مرّات، فإنّ احتمال ظهور العدد $6$ مرّتين هو:",
  [O(r'\frac{5}{72}', R(5, 72)), O(r'\frac{5}{216}', R(5, 216)), O(r'\frac{1}{12}', R(1, 12)), O(r'\frac{1}{36}', R(1, 36))],
  r"$p=\dfrac16$ ، و $X\sim B\left(3,\frac16\right)$" "\n"
  r"$P(X=2)=\binom32\left(\dfrac16\right)^2\left(\dfrac56\right)=3\cdot\dfrac{1}{36}\cdot\dfrac56=\dfrac{15}{216}=\dfrac{5}{72}$",
  truth=binom(3, R(1, 6), 2)),
# 2023 #22: at least n - 1 successes, written in powers; options = the right sum, all successes, one term, the failure
# power added
Q('u7e8q5', L1, 'hard',
  r"إذا كان احتمال أن يُسجّل لاعب هدفًا من ركلة جزاء يساوي $\dfrac56$ ، وسدّد $6$ ركلات جزاء، فإنّ احتمال أن يُسجّل $5$ أهداف على الأقل هو:",
  [O(r'\left(\frac{5}{6}\right)^{5}+\left(\frac{5}{6}\right)^{6}', R(5, 6)**5 + R(5, 6)**6), O(r'\left(\frac{5}{6}\right)^{6}', R(5, 6)**6),
   O(r'\left(\frac{5}{6}\right)^{5}\cdot\frac{1}{6}', R(5, 6)**5*R(1, 6)), O(r'\left(\frac{5}{6}\right)^{5}+\left(\frac{1}{6}\right)^{6}', R(5, 6)**5 + R(1, 6)**6)],
  r"$X\sim B\left(6,\frac56\right)$ ، و $P(X\ge5)=P(X=5)+P(X=6)$" "\n"
  r"$P(X\ge5)=\binom65\left(\frac56\right)^5\left(\frac16\right)+\left(\frac56\right)^6=\left(\frac56\right)^5+\left(\frac56\right)^6$ (لأن $6\times\frac16=1$)",
  truth=binom(6, R(5, 6), 5) + binom(6, R(5, 6), 6)),
# 2025s #21: a spinner of congruent sectors (figure), X = spins until a given outcome first -> E(X) (replaced a plain
# E(X) = 1/p item on 2026-11-02); options = 1/p, p, 1/(1 - p), 1 - p
Q('u7e8q6', L1, 'easy',
  r"يُمثّل الشكل الآتي قرصًا مُقسّمًا إلى $8$ قطاعات دائرية متطابقة. إذا دلّ المتغيّر العشوائي $X$ على عدد مرّات تدوير مؤشّر القرص حتى يقف عند قطاع يحمل عددًا أكبر من $5$ أوّل مرّة، فإنّ قيمة $E(X)$ هي:",
  [O(r'\frac{8}{3}', R(8, 3)), O(r'\frac{3}{8}', R(3, 8)), O(r'\frac{8}{5}', R(8, 5)), O(r'\frac{5}{8}', R(5, 8))],
  r"القطاعات $6$ و $7$ و $8$ من $8$ قطاعات متطابقة: $p=\dfrac38$ ، و $X\sim Geo\left(\frac38\right)$" "\n"
  r"$E(X)=\dfrac1p=\dfrac83$",
  truth=1/R(3, 8), figure=figure('u7e8q6', spinner_fig([str(i_) for i_ in range(1, 9)], pointer_deg=80), 2.6, 2.6)),
# 2026 #48: P(X > a) with a below the mean; options = P(Z<z), its complement, and both with the variance used in z
Q('u7e8q7', L2, 'easy',
  r"إذا كان: $X\sim N(36,\,25)$ ، فإنّ $P(X>33)$ هو:" + ztable(0.12, 0.6),
  [D('0.7257'), D('0.2743'), D('0.5478'), D('0.4522')],
  r"$\sigma=5$ ، $z=\dfrac{33-36}{5}=-0.6$" "\n"
  r"$P(X>33)=P(Z>-0.6)=P(Z<0.6)=0.7257$",
  truth=1 - Ph(-R(6, 10))),
# 2026 #49: P(-k/c < Z < k/c) given -> k; options = right z or the unhalved one, x times c or divided by c
Q('u7e8q8', L2, 'medium',
  r"إذا كان $Z$ متغيّرًا عشوائيًّا طبيعيًّا معياريًّا، وكان: $P\left(-\dfrac{k}{8}<Z<\dfrac{k}{8}\right)=0.383$ ، حيث $k>0$ ، فإنّ قيمة الثابت $k$ هي:" + ztable(0.5, 1.19),
  [O('4', 4), D('9.52'), D('0.0625'), D('0.149')],
  r"$2P\left(Z<\dfrac{k}{8}\right)-1=0.383 \Rightarrow P\left(Z<\dfrac{k}{8}\right)=\dfrac{1.383}{2}=0.6915$" "\n"
  r"من الجدول: $\dfrac{k}{8}=0.5 \Rightarrow k=4$",
  truth=lambda: 8*[z_ for z_ in (R(1, 2), R(119, 100)) if 2*Ph(z_) - 1 == R('0.383')][0]),
# 2026 #50: sigma from a small percentage above a value; options = sigma, z, d.z, z/d
Q('u7e8q9', L2, 'hard',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(40,\,\sigma^2)$ على الزمن (بالدقائق) الذي يستغرقه موظّفو إحدى الشركات للوصول إلى العمل. إذا كان $0.62\%$ منهم يستغرقون أكثر من $52$ دقيقة، فإنّ قيمة الانحراف المعياري للزمن هي:" + ztable(2.4, 2.5, 2.6),
  [D('4.8'), D('2.5'), O('30', 30), D('0.21')],
  r"$P(X>52)=0.0062 \Rightarrow P(X<52)=0.9938=P(Z<2.5)$ ، إذن $z=2.5$" "\n"
  r"$\dfrac{52-40}{\sigma}=2.5 \Rightarrow \sigma=\dfrac{12}{2.5}=4.8$ دقيقة",
  truth=lambda: 12/[z_ for z_ in (R(24, 10), R(25, 10), R(26, 10)) if Ph(z_) == 1 - R('0.0062')][0]),
# 2025s #25: sigma from the interval holding a percentage by the empirical rule (99.7% here, 95% in the model; figure;
# replaced a 2024 #23 item on 2026-11-02 so that exams 4, 6 and 8 stop sharing their normal-distribution ideas);
# options = sigma, the 95% rule used (width / 4), half the interval (3 sigma), sigma^2
Q('u7e8q10', L2, 'medium',
  r"يدلّ المتغيّر العشوائي الطبيعي: $X\sim N(50,\,\sigma^2)$ على أطوال الأسماك (بالسنتيمتر) في إحدى المزارع السمكية. إذا كانت أطوال $99.7\%$ منها تتراوح بين $38\ \text{cm}$ و $62\ \text{cm}$ ، فإنّ قيمة الانحراف المعياري $\sigma$ لأطوال الأسماك هي:" + EMPNOTE,
  [D('4', 'cm'), D('6', 'cm'), D('12', 'cm'), D('16', 'cm')],
  r"حسب القاعدة التجريبية تقع $99.7\%$ من القيم بين $\mu-3\sigma$ و $\mu+3\sigma$:" "\n"
  r"$\mu+3\sigma=62 \Rightarrow 50+3\sigma=62 \Rightarrow 3\sigma=12 \Rightarrow \sigma=4\ \text{cm}$",
  truth=R(62 - 50, 3), figure=figure('u7e8q10', emp_fig, 4.4, 2.4)),
# 2024s #24: shaded area between two negative z (figure); options = right, sum of the two areas, and complements
Q('u7e8q11', L2, 'medium',
  SHADED + ztable(0.25, 1.25),
  [D('0.2957'), D('0.7043'), D('0.5069'), D('0.4931')],
  r"المنطقة بين $z=-1.25$ و $z=-0.25$:" "\n"
  r"$P(-1.25<Z<-0.25)=P(Z<-0.25)-P(Z<-1.25)=(1-0.5987)-(1-0.8944)=0.4013-0.1056=0.2957$",
  truth=Ph(-R(1, 4)) - Ph(-R(5, 4)), figure=figure('u7e8q11', bell(-1.25, -0.25, [-1.25, -0.25]), 4.0, 2.4)),
# 2024s #25 / 2026r #25: x from P(X > x); options = mu + z sigma, mu - z sigma, mu + z, mu + z sigma^2
Q('u7e8q12', L2, 'hard',
  r"إذا كان: $X\sim N(60,\,100)$ ، فإنّ قيمة $x$ التي تُحقّق الاحتمال $P(X>x)=0.0401$ هي:" + ztable(1.65, 1.75, 1.85),
  [D('77.5'), D('42.5'), D('61.75'), O('235', 235)],
  r"$P(X<x)=1-0.0401=0.9599=P(Z<1.75)$ ، إذن $z=1.75$" "\n"
  r"$\dfrac{x-60}{10}=1.75 \Rightarrow x=60+10(1.75)=77.5$",
  truth=lambda: 60 + 10*[z_ for z_ in (R(165, 100), R(175, 100), R(185, 100)) if Ph(z_) == 1 - R('0.0401')][0]),
]

EXAMS_4_8 = [('الاختبار الرابع', E4), ('الاختبار الخامس', E5), ('الاختبار السادس', E6),
             ('الاختبار السابع', E7), ('الاختبار الثامن', E8)]
