"""Unit-6 exams 4-8 (imported by u6.py). Every item is a sibling of the official item named in the comment above
it (2026 = the 2008-generation paper, items 38-45; 2026r = 2026 repeaters paper 2; 2023-2025 = paper 2,
items 13-20). Each exam has 6 items on vectors in space, 3 on lines in space and 3 on the dot product, in that
order, and the figures follow the ministry's drawings (cuboid with O at the back, parallelogram/triangle ratios)."""
from qb import *
from u6_helpers import *

L1, L2, L3 = 'u6-l1', 'u6-l2', 'u6-l3'
qq = Symbol('q')

# ============================================================== Exam 4 (the 2026 blueprint, items 38-45)
# parallelogram ABCD, E on DC with DE = 2EC, F on BC produced with A, E, F collinear (k = 2)
pg4 = plane_pts((0.5, 2.5), (-0.25, -1.0), (5/6, 0.1),
                {'A': 0, 'B': 6*vb, 'C': 2*va + 6*vb, 'D': 2*va, 'E': 2*va + 4*vb, 'F': 3*va + 6*vb})
E4 = [
# 2026r #17: displacement from A to B in context; options = order (B - A or A - B) x sign slip with a negative coordinate
Q('u6e4q1', L1, 'easy',
  r"تحرّكت طائرة مسيّرة في خطّ مستقيم من النقطة $A(-5,\,2,\,8)$ إلى النقطة $B(3,\,-7,\,-4)$ ، فإنّ متجه إزاحتها هو:",
  [vec_opt(8, -9, -12), vec_opt(-8, 9, 12), vec_opt(-2, -9, -12), vec_opt(2, 9, 12)],
  r"متجه الإزاحة من $A$ إلى $B$ هو $\overrightarrow{AB}=B-A=\langle 3+5,\,-7-2,\,-4-8\rangle=\langle 8,\,-9,\,-12\rangle$",
  truth=T3(V(3, -7, -4) - V(-5, 2, 8))),
# 2026 #39: AB = BD -> position vector of D; options = 2B - A, 2A - B, B - A (the vector AB itself), -(2B - A)
Q('u6e4q2', L1, 'medium',
  r"إذا كانت: $A(4,\,-1,\,3)$ ، $B(1,\,2,\,-2)$ ، وكانت $D$ نقطة في الفضاء بحيث $\overrightarrow{AB}=\overrightarrow{BD}$ ، فإنّ متجه الموقع للنقطة $D$ هو:",
  [vec_opt(-2, 5, -7), vec_opt(7, -4, 8), vec_opt(-3, 3, -5), vec_opt(2, -5, 7)],
  r"$\overrightarrow{AB}=\overrightarrow{BD} \Rightarrow B-A=D-B \Rightarrow D=2B-A$" "\n"
  r"$D=\langle 2-4,\,4+1,\,-4-3\rangle=\langle -2,\,5,\,-7\rangle$ (أي أن $B$ منتصف $\overline{AD}$)",
  truth=T3(2*V(1, 2, -2) - V(4, -1, 3))),
# 2026 #40: |AC| = sqrt(n) with alpha < 0; options = +-3, +-7 (the other root, and the (alpha + 2) sign slip)
Q('u6e4q3', L1, 'medium',
  r"إذا كانت: $A(2,\,-1,\,4)$ ، $C(\alpha,\,1,\,2)$ نقطتين في الفضاء، وكان: $|\overrightarrow{AC}|=\sqrt{33}$ ، فإنّ قيمة الثابت $\alpha$ ، حيث $\alpha<0$ ، هي:",
  [O('-3', -3), O('-7', -7), O('7', 7), O('3', 3)],
  r"$\overrightarrow{AC}=\langle \alpha-2,\,2,\,-2\rangle$ ، و $(\alpha-2)^2+4+4=33 \Rightarrow (\alpha-2)^2=25$" "\n"
  r"$\alpha-2=\pm5 \Rightarrow \alpha=7$ أو $\alpha=-3$ ، وبما أن $\alpha<0$ فإن $\alpha=-3$",
  truth=lambda: [r_ for r_ in solve((x - 2)**2 + 8 - 33, x) if r_ < 0][0]),
# 2026 #41: cuboid in the ministry's drawing, vertex B given, midpoint of a segment joining two vertices;
# options = one vertex misread each time (A read as E, A read as D, G read as O)
Q('u6e4q4', L1, 'medium',
  r"في متوازي المستطيلات الآتي، إذا كانت إحداثيات الرأس $B$ هي: $(4,\,2,\,6)$ ، فإنّ إحداثيات نقطة منتصف $\overline{GA}$ هي:",
  [pt_opt(2, 1, 3), pt_opt(2, 1, 0), pt_opt(0, 1, 3), pt_opt(2, 0, 3)],
  r"من الشكل: $G(0,\,2,\,0)$ على المحور $y$ ، و $A(4,\,0,\,6)$ (فوق $E(4,0,0)$ بارتفاع $6$)" "\n"
  r"منتصف $\overline{GA}$: $\left(\dfrac{0+4}{2},\ \dfrac{2+0}{2},\ \dfrac{0+6}{2}\right)=(2,\,1,\,3)$",
  truth=T3((V(0, 2, 0) + V(4, 0, 6))/2), figure=figure('u6e4q4', iso_box(4, 2, 6), 3.2, 3.6)),
# 2026 #42: collinear points, AB and AC given, the unknown inside AC; options = sign of the ratio x moving the constant
Q('u6e4q5', L1, 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle 4,\,-2,\,6\rangle$ ، $\overrightarrow{AC}=\langle a+3,\,3,\,-9\rangle$ ، فإنّ قيمة $a$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('-9', -9), O('3', 3), O('-3', -3), O('9', 9)],
  r"تقع النقاط على استقامة واحدة إذا كان $\overrightarrow{AC}=k\overrightarrow{AB}$: من المركبة الثانية $3=-2k \Rightarrow k=-\frac32$ (وتتحقّق في الثالثة: $-9=6k$)" "\n"
  r"$a+3=4k=-6 \Rightarrow a=-9$",
  truth=lambda: solve(V(4, -2, 6).cross(V(a + 3, 3, -9))[1], a)[0]),
# 2026r #18: parallelogram, a point on a side in a given ratio, Z on a produced side, k from the given vector;
# options = k, 1/k (the ratio read the other way) and small values of the same kind
Q('u6e4q6', L1, 'hard',
  r"في الشكل الآتي $ABCD$ متوازي أضلاع. إذا كان: $\overrightarrow{AB}=6\vec{\mathbf{b}}$ ، $\overrightarrow{AD}=2\vec{\mathbf{a}}$ ، وكانت النقطة $E$ تقع على $\overline{DC}$ حيث $DE=2EC$ ، وكان: $\overrightarrow{BC}=k\,\overrightarrow{CF}$ ، $\overrightarrow{EF}=2\vec{\mathbf{b}}+\vec{\mathbf{a}}$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('2', 2), O(r'\frac{1}{2}', R(1, 2)), O('3', 3), O('4', 4)],
  r"$\overrightarrow{DE}=\frac23\overrightarrow{DC}=\frac23(6\vec{\mathbf{b}})=4\vec{\mathbf{b}}$ ، فيكون $\overrightarrow{EC}=2\vec{\mathbf{b}}$" "\n"
  r"$\overrightarrow{CF}=\frac1k\overrightarrow{BC}=\frac{2}{k}\vec{\mathbf{a}}$ ، و $\overrightarrow{EF}=\overrightarrow{EC}+\overrightarrow{CF}=2\vec{\mathbf{b}}+\frac{2}{k}\vec{\mathbf{a}}$" "\n"
  r"بالمقارنة مع $2\vec{\mathbf{b}}+\vec{\mathbf{a}}$: $\frac{2}{k}=1 \Rightarrow k=2$",
  truth=lambda: solve_k((2*va + 6*vb + 2*va/k) - (2*va + R(2, 3)*6*vb), 2*vb + va),
  figure=figure('u6e4q6', poly_fig(pg4, [('B', 'C'), ('D', 'C'), ('C', 'F')],
                                    [('A', 'B', r'$6\vec{\mathbf{b}}$', (-0.2, 0.2)), ('A', 'D', r'$2\vec{\mathbf{a}}$', (-0.75, 0.0))],
                                    {'A': (-0.15, 0.15), 'B': (0.1, 0.1), 'C': (0.12, 0.05), 'D': (-0.3, -0.3), 'E': (-0.1, -0.42), 'F': (0.12, -0.3)},
                                    thick=[('A', 'F')]), 4.0, 2.6)),
# 2023 #18: a point with one unknown coordinate lies on a line; options = t right or sign-slipped, x the line's point
# added or forgotten
Q('u6e4q7', L2, 'easy',
  r"إذا كانت النقطة $(3,\,b,\,-5)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle 1,\,4,\,-1\rangle+t\langle 1,\,-3,\,-2\rangle$ ، فإنّ قيمة الثابت $b$ هي:",
  [O('-2', -2), O('10', 10), O('-6', -6), O('6', 6)],
  r"من الإحداثي $x$: $1+t=3 \Rightarrow t=2$ ، وتحقّق في $z$: $-1-2(2)=-5$ ✔" "\n"
  r"الإحداثي $y$: $b=4-3(2)=-2$",
  truth=lambda: solve(list(V(3, b, -5) - V(1, 4, -1) - t*V(1, -3, -2)), [b, t], dict=True)[0][b]),
# 2024s #18 (2026 #38 family): line parallel to v through a position vector with a missing component;
# options = point and direction swapped x the missing component put in the wrong place
IndexQ('u6e4q8', L2, 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=5\hat{i}+2\hat{j}-\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $4\hat{j}-3\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((0, 4, -3), (5, 2, -1)), line_opt((5, 2, -1), (0, 4, -3)), line_opt((4, -3, 0), (5, 2, -1)), line_opt((5, 2, -1), (4, -3, 0))],
  r"متجه موقع النقطة $A$ هو $0\hat{i}+4\hat{j}-3\hat{k}=\langle 0,\,4,\,-3\rangle$ ، ومتجه الاتجاه $\langle 5,\,2,\,-1\rangle$:" "\n"
  r"$\vec{\mathbf{r}}=\langle 0,4,-3\rangle+t\langle 5,2,-1\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((0, 4, -3), ln) and par(ln[1], (5, 2, -1)))),
# 2024 #19: point where a line meets the xz plane; options = the right plane, the yz plane, the xy plane, t sign slip
Q('u6e4q9', L2, 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle -6,\,4,\,2\rangle+t\langle 3,\,-1,\,2\rangle$ معادلة متجهة للمستقيم $l$ ، فإنّ إحداثيات نقطة تقاطع المستقيم $l$ مع المستوى $xz$ هي:",
  [pt_opt(6, 0, 10), pt_opt(0, 2, 6), pt_opt(-9, 5, 0), pt_opt(-18, 8, -6)],
  r"على المستوى $xz$ يكون $y=0$: $4-t=0 \Rightarrow t=4$" "\n"
  r"النقطة: $(-6+12,\ 0,\ 2+8)=(6,\,0,\,10)$",
  truth=lambda: T3(V(-6, 4, 2) + solve(4 - t, t)[0]*V(3, -1, 2))),
# 2026 #43 family: AB and CB given -> AB . AC; options = right AC, AC = AB + CB (sign slip), CB used as AC, sign
Q('u6e4q10', L3, 'hard',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle 3,\,-1,\,2\rangle$ ، $\overrightarrow{CB}=\langle 1,\,2,\,-2\rangle$ ، فإنّ $\overrightarrow{AB}\cdot\overrightarrow{AC}$ يساوي:",
  [O('17', 17), O('11', 11), O('-3', -3), O('-17', -17)],
  r"$\overrightarrow{AC}=\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AB}-\overrightarrow{CB}=\langle 2,\,-3,\,4\rangle$" "\n"
  r"$\overrightarrow{AB}\cdot\overrightarrow{AC}=6+3+8=17$",
  truth=V(3, -1, 2).dot(V(3, -1, 2) - V(1, 2, -2))),
# 2025 #20: angle from the magnitudes and the dot product; options = cos = -sqrt3/2 or -1/2, x obtuse or acute
Q('u6e4q11', L3, 'easy',
  r"إذا كان: $|\vec{\mathbf{u}}|=2$ ، $|\vec{\mathbf{v}}|=3$ ، $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=-3\sqrt{3}$ ، فإنّ قياس الزاوية بين المتجهين $\vec{\mathbf{u}}$ و $\vec{\mathbf{v}}$ هو:",
  [O(r'\frac{5\pi}{6}', 5*P/6), O(r'\frac{\pi}{6}', P/6), O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{3}', P/3)],
  r"$\cos\theta=\dfrac{\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}}{|\vec{\mathbf{u}}||\vec{\mathbf{v}}|}=\dfrac{-3\sqrt3}{6}=-\dfrac{\sqrt3}{2} \Rightarrow \theta=\dfrac{5\pi}{6}$",
  truth=acos(-3*sqrt(3)/(2*3))),
# 2026 #45: triangle from BA and BC (right angle not stated); options = 1/2|BA||BC|, without 1/2, and the
# hypotenuse AC taken as a side (with and without 1/2)
Q('u6e4q12', L3, 'hard',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{BA}=\langle -6,\,3,\,6\rangle$ ، $\overrightarrow{BC}=\langle 8,\,8,\,4\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O('54', 54), O('108', 108), O('90', 90), O('180', 180)],
  r"$\overrightarrow{BA}\cdot\overrightarrow{BC}=-48+24+24=0$ ، إذن الزاوية $B$ قائمة" "\n"
  r"$|\overrightarrow{BA}|=\sqrt{36+9+36}=9$ ، $|\overrightarrow{BC}|=\sqrt{64+64+16}=12$ ، والمساحة تساوي $\frac12(9)(12)=54$",
  truth=R(1, 2)*V(-6, 3, 6).norm()*V(8, 8, 4).norm()*sin(ang(V(-6, 3, 6), V(8, 8, 4)))),
]

# ============================================================== Exam 5
# parallelogram EFGH, N on the diagonal HF with HN:NF = 1:3
pg5 = plane_pts((0.6, 2.6), (-0.2, -0.8), (2.2, 0.2),
                {'E': 0, 'F': 2*vb, 'G': 3*va + 2*vb, 'H': 3*va, 'N': 3*va + (2*vb - 3*va)/4})
E5 = [
# 2025s #14: 2f - g with i, j, k; options = 2f - g, 2f + g, sign slip in the k component, f - 2g
Q('u6e5q1', L1, 'easy',
  r"إذا كان: $\vec{\mathbf{f}}=3\hat{i}-\hat{j}+2\hat{k}$ ، $\vec{\mathbf{g}}=\hat{i}+4\hat{j}-5\hat{k}$ ، فإنّ $2\vec{\mathbf{f}}-\vec{\mathbf{g}}$ يساوي:",
  [ijk_opt(5, -6, 9), ijk_opt(7, 2, -1), ijk_opt(5, -6, -1), ijk_opt(1, -9, 12)],
  r"$2\vec{\mathbf{f}}=6\hat{i}-2\hat{j}+4\hat{k}$ ، ثم نطرح $\vec{\mathbf{g}}$ مركبةً مركبة:" "\n"
  r"$(6-1)\hat{i}+(-2-4)\hat{j}+(4+5)\hat{k}=5\hat{i}-6\hat{j}+9\hat{k}$",
  truth=T3(2*V(3, -1, 2) - V(1, 4, -5))),
# 2026r #13: midpoint and one end -> the other end; options = 2N - A, 2A - N, and their negatives
Q('u6e5q2', L1, 'medium',
  r"إذا كانت النقطة $N(-1,\,3,\,2)$ منتصف القطعة المستقيمة $\overline{AB}$ ، وكانت $A(4,\,-2,\,-3)$ ، فإنّ إحداثيات النقطة $B$ هي:",
  [pt_opt(-6, 8, 7), pt_opt(6, -8, -7), pt_opt(9, -7, -8), pt_opt(-9, 7, 8)],
  r"$N=\dfrac{A+B}{2} \Rightarrow B=2N-A$" "\n"
  r"$B=(-2-4,\ 6+2,\ 4+3)=(-6,\,8,\,7)$",
  truth=T3(2*V(-1, 3, 2) - V(4, -2, -3))),
# 2025 #14: unit vector in the direction of GH; options = GH or HG, x divided by |GH| or by |GH|^2
Q('u6e5q3', L1, 'easy',
  r"إذا كانت: $G(-3,\,2,\,1)$ ، $H(1,\,-2,\,8)$ ، فإنّ متجه الوحدة في اتجاه $\overrightarrow{GH}$ هو:",
  [vec_opt(R(4, 9), R(-4, 9), R(7, 9)), vec_opt(R(-4, 9), R(4, 9), R(-7, 9)), vec_opt(R(4, 81), R(-4, 81), R(7, 81)), vec_opt(R(-4, 81), R(4, 81), R(-7, 81))],
  r"$\overrightarrow{GH}=\langle 1+3,\,-2-2,\,8-1\rangle=\langle 4,\,-4,\,7\rangle$ ، $|\overrightarrow{GH}|=\sqrt{16+16+49}=9$" "\n"
  r"متجه الوحدة: $\dfrac{\overrightarrow{GH}}{|\overrightarrow{GH}|}=\left\langle \frac49,\,-\frac49,\,\frac79\right\rangle$",
  truth=(lambda w_: T3(w_/w_.norm()))(V(1, -2, 8) - V(-3, 2, 1))),
# 2025 #18: parallel vectors with one unknown; options = the ratio or its reciprocal, x sign
Q('u6e5q4', L1, 'easy',
  r"إذا كان المتجه $\vec{\mathbf{u}}=\langle 6,\,a,\,-4\rangle$ يوازي المتجه $\vec{\mathbf{v}}=\langle -9,\,12,\,6\rangle$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('-8', -8), O('8', 8), O('-18', -18), O('18', 18)],
  r"$\vec{\mathbf{u}}=k\vec{\mathbf{v}}$: من المركبة الأولى $6=-9k \Rightarrow k=-\frac23$ (وتتحقّق في الثالثة: $-4=6k$)" "\n"
  r"$a=12k=12\left(-\frac23\right)=-8$",
  truth=lambda: solve(V(6, a, -4).cross(V(-9, 12, 6))[2], a)[0]),
# 2025 #15: point dividing a segment, TN = 1/3 NM; options = 1/4 or 1/3 of TM, x measured from T or from M
Q('u6e5q5', L1, 'medium',
  r"إذا كانت: $T(-3,\,7,\,1)$ ، $M(9,\,-5,\,13)$ ، وكانت النقطة $N$ تقع على $\overline{TM}$ بحيث $TN=\frac{1}{3}NM$ ، فإنّ إحداثيات النقطة $N$ هي:",
  [pt_opt(0, 4, 4), pt_opt(1, 3, 5), pt_opt(6, -2, 10), pt_opt(5, -1, 9)],
  r"$TN=\frac13NM$ يعني أن $TN:NM=1:3$ ، فيكون $\overrightarrow{TN}=\frac14\overrightarrow{TM}$" "\n"
  r"$\overrightarrow{TM}=\langle 12,\,-12,\,12\rangle$ ، و $N=T+\frac14\overrightarrow{TM}=(-3+3,\ 7-3,\ 1+3)=(0,\,4,\,4)$",
  truth=T3(V(-3, 7, 1) + R(1, 4)*(V(9, -5, 13) - V(-3, 7, 1)))),
# 2025s #19: parallelogram, N on a diagonal in a given ratio, GN = k(...); options = k, -k, 1/k, -1/k
Q('u6e5q6', L1, 'hard',
  r"في الشكل الآتي $EFGH$ متوازي أضلاع، فيه: $\overrightarrow{EF}=2\vec{\mathbf{b}}$ ، $\overrightarrow{EH}=3\vec{\mathbf{a}}$. إذا كانت النقطة $N$ تقع على القطر $\overline{HF}$ بحيث $HN:NF=1:3$ ، وكان: $\overrightarrow{GN}=k(\vec{\mathbf{a}}+2\vec{\mathbf{b}})$ ، فإنّ قيمة الثابت $k$ هي:",
  [O(r'-\frac{3}{4}', R(-3, 4)), O(r'\frac{3}{4}', R(3, 4)), O(r'-\frac{4}{3}', R(-4, 3)), O(r'\frac{4}{3}', R(4, 3))],
  r"$\overrightarrow{HF}=\overrightarrow{HE}+\overrightarrow{EF}=-3\vec{\mathbf{a}}+2\vec{\mathbf{b}}$ ، و $\overrightarrow{HN}=\frac14\overrightarrow{HF}=-\frac34\vec{\mathbf{a}}+\frac12\vec{\mathbf{b}}$" "\n"
  r"$\overrightarrow{GN}=\overrightarrow{GH}+\overrightarrow{HN}=-2\vec{\mathbf{b}}-\frac34\vec{\mathbf{a}}+\frac12\vec{\mathbf{b}}=-\frac34\vec{\mathbf{a}}-\frac32\vec{\mathbf{b}}=-\frac34(\vec{\mathbf{a}}+2\vec{\mathbf{b}})$",
  truth=lambda: solve_k((3*va + (2*vb - 3*va)/4) - (3*va + 2*vb), k*(va + 2*vb)),
  figure=figure('u6e5q6', poly_fig(pg5, [('F', 'G'), ('H', 'G'), ('H', 'F')],
                                    [('E', 'F', r'$2\vec{\mathbf{b}}$', (-0.2, 0.18)), ('E', 'H', r'$3\vec{\mathbf{a}}$', (-0.75, 0.0))],
                                    {'E': (-0.2, 0.15), 'F': (0.1, 0.1), 'G': (0.12, -0.25), 'H': (-0.3, -0.3), 'N': (-0.08, 0.2)},
                                    dashed=[('G', 'N')]), 3.8, 2.4)),
# 2024 #19 / 2025s #17: point where a line meets the xy plane; options = the right plane, the xz plane, the yz plane,
# t sign slip
Q('u6e5q7', L2, 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 3,\,-2,\,4\rangle+t\langle 1,\,2,\,-2\rangle$ معادلة متجهة للمستقيم $l$ ، فإنّ إحداثيات نقطة تقاطع المستقيم $l$ مع المستوى $xy$ هي:",
  [pt_opt(5, 2, 0), pt_opt(4, 0, 2), pt_opt(0, -8, 10), pt_opt(1, -6, 8)],
  r"على المستوى $xy$ يكون $z=0$: $4-2t=0 \Rightarrow t=2$" "\n"
  r"النقطة: $(3+2,\ -2+4,\ 0)=(5,\,2,\,0)$",
  truth=lambda: T3(V(3, -2, 4) + solve(4 - 2*t, t)[0]*V(1, 2, -2))),
# 2025 #19: cube in the ministry's drawing, line through a vertex and the centre; options = direction M - A or the
# position vector of M, x through A or through the misread vertex C
IndexQ('u6e5q8', L2, 'hard',
  r"في الشكل الآتي مكعّب طول حرفه $8$ وحدات، أحد رؤوسه نقطة الأصل $O$ ، وأحرفه $\overline{OE}$ و $\overline{OG}$ و $\overline{OD}$ تقع على المحاور $x$ و $y$ و $z$ الموجبة على الترتيب. إذا كانت $M$ مركز المكعّب، فإنّ معادلة متجهة للمستقيم المارّ بالرأس $A$ والنقطة $M$ هي:",
  [line_opt((8, 0, 8), (-1, 1, -1)), line_opt((8, 0, 8), (1, 1, 1)), line_opt((0, 8, 8), (1, -1, -1)), line_opt((0, 8, 8), (1, 1, 1))],
  r"من الشكل: $A(8,\,0,\,8)$ ، ومركز المكعّب منتصف القطر $\overline{OB}$: $M(4,\,4,\,4)$" "\n"
  r"$\overrightarrow{AM}=\langle -4,\,4,\,-4\rangle=4\langle -1,\,1,\,-1\rangle$ ، فمعادلة المستقيم: $\vec{\mathbf{r}}=\langle 8,0,8\rangle+t\langle -1,1,-1\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((8, 0, 8), ln) and on_line((4, 4, 4), ln)),
  figure=figure('u6e5q8', iso_box(8, 8, 8, marks=[('M', (4, 4, 4), (0.06, -0.06))]), 3.4, 3.4)),
# 2024s #19: a point whose coordinates contain the unknown lies on a line; options = a, the parameter t,
# t = a - 3 sign slip, t taken equal to a
Q('u6e5q9', L2, 'medium',
  r"إذا كانت النقطة $(2a,\,a+1,\,-a)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle 1,\,4,\,-4\rangle+t\langle 3,\,-1,\,2\rangle$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('2', 2), O('1', 1), O('8', 8), O('-1', -1)],
  r"نساوي الإحداثيات: $2a=1+3t$ ، $a+1=4-t$ ، $-a=-4+2t$" "\n"
  r"من الثانية: $t=3-a$ ، وبالتعويض في الأولى: $2a=1+9-3a \Rightarrow a=2$ ، $t=1$" "\n"
  r"تحقّق في الثالثة: $-2=-4+2$ ✔",
  truth=lambda: solve(list(V(2*a, a + 1, -a) - V(1, 4, -4) - t*V(3, -1, 2)), [a, t], dict=True)[0][a]),
# 2026r #19: perpendicular vectors, quadratic in alpha; options = right factor pair or the other pair of 18, x sign
Q('u6e5q10', L3, 'hard',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 3,\,2,\,\alpha\rangle$ ، $\vec{\mathbf{w}}=\langle \alpha,\,9,\,-\alpha\rangle$ ، وكان المتجهان $\vec{\mathbf{v}}$ و $\vec{\mathbf{w}}$ متعامدين، فإنّ القيمتين المُمكنتين للثابت $\alpha$ هما:",
  [pair_opt(r'-3,\ 6', -3, 6), pair_opt(r'3,\ -6', 3, -6), pair_opt(r'-2,\ 9', -2, 9), pair_opt(r'2,\ -9', 2, -9)],
  r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=3\alpha+18-\alpha^2=0 \Rightarrow \alpha^2-3\alpha-18=0$" "\n"
  r"$(\alpha-6)(\alpha+3)=0 \Rightarrow \alpha=6$ أو $\alpha=-3$",
  truth=lambda: FiniteSet(*solve(V(3, 2, x).dot(V(x, 9, -x)), x))),
# 2026r #20: distance from a point to a line, foot given; options = |PF| or |PF|^2, x sign slip with a negative coordinate
Q('u6e5q11', L3, 'easy',
  r"إذا كانت $P(-1,\,2,\,4)$ نقطة غير واقعة على المستقيم $l$ ، وكانت $F(3,\,-2,\,6)$ مسقط العمود من النقطة $P$ على المستقيم $l$ ، فإنّ البُعد بين النقطة $P$ والمستقيم $l$ (بوحدات الطول) هو:",
  [O('6', 6), O('36', 36), O(r'2\sqrt{6}', 2*sqrt(6)), O('24', 24)],
  r"البُعد بين النقطة والمستقيم هو طول العمود $\overline{PF}$:" "\n"
  r"$\overrightarrow{PF}=\langle 3+1,\,-2-2,\,6-4\rangle=\langle 4,\,-4,\,2\rangle$ ، $|\overrightarrow{PF}|=\sqrt{16+16+4}=\sqrt{36}=6$",
  truth=(V(3, -2, 6) - V(-1, 2, 4)).norm()),
# 2023s #19: u . c with u = AB; options = AB or BA, x A + B used instead of B - A
Q('u6e5q12', L3, 'medium',
  r"إذا كانت: $A(4,\,-1,\,2)$ ، $B(6,\,2,\,-3)$ ، وكان: $\vec{\mathbf{u}}=\overrightarrow{AB}$ ، $\vec{\mathbf{c}}=\langle 3,\,-1,\,2\rangle$ ، فإنّ $\vec{\mathbf{u}}\cdot\vec{\mathbf{c}}$ يساوي:",
  [O('-7', -7), O('7', 7), O('27', 27), O('-27', -27)],
  r"$\vec{\mathbf{u}}=\overrightarrow{AB}=\langle 6-4,\,2+1,\,-3-2\rangle=\langle 2,\,3,\,-5\rangle$" "\n"
  r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{c}}=2(3)+3(-1)+(-5)(2)=6-3-10=-7$",
  truth=(V(6, 2, -3) - V(4, -1, 2)).dot(V(3, -1, 2))),
]

# ============================================================== Exam 6
# triangle OAB, P on AB with AP:PB = 1:2
tr6 = plane_pts((0, 0), (1.6/3, 3.4/3), (1, 0), {'O': 0, 'A': 3*va, 'B': 6*vb, 'P': 3*va + R(1, 3)*(6*vb - 3*va)})
E6 = [
# 2023s #14: a point in a coordinate plane; options = points with the same numbers in the three planes
IndexQ('u6e6q1', L1, 'easy',
  r"أيُّ النقاط الآتية تقع في المستوى $xz$؟",
  [pt_opt(3, 0, -5), pt_opt(0, 3, -5), pt_opt(3, -5, 0), pt_opt(0, -5, 3)],
  r"النقاط الواقعة في المستوى $xz$ يكون الإحداثي $y$ لها صفرًا، وهذا متحقّق في النقطة $(3,\,0,\,-5)$ فقط.",
  truth=lambda vals: only(vals, lambda p_: p_[1] == 0)),
# 2025 #16: p a - q b equals a given vector -> p + q; a has a zero component (as in the model), so one equation gives
# q at once; options = +-(p + q), +-(p - q): the q sign slip gives p - q, a and b swapped gives -(p + q)
Q('u6e6q2', L1, 'medium',
  r"إذا كان: $\vec{\mathbf{a}}=\langle 0,\,-1,\,3\rangle$ ، $\vec{\mathbf{b}}=\langle -1,\,1,\,2\rangle$ ، وكان: $p\vec{\mathbf{a}}-q\vec{\mathbf{b}}=\langle 2,\,-6,\,8\rangle$ ، حيث $p,\ q$ ثابتان، فإنّ قيمة $p+q$ هي:",
  [O('6', 6), O('2', 2), O('-6', -6), O('-2', -2)],
  r"نساوي المركبات: $q=2$ ، $-p-q=-6$ ، $3p-2q=8$" "\n"
  r"من الأولى: $q=2$ ، وبالتعويض في الثانية: $-p-2=-6 \Rightarrow p=4$" "\n"
  r"تحقّق في الثالثة: $12-4=8$ ✔ ، إذن $p+q=6$",
  truth=lambda: (lambda s_: s_[p] + s_[qq])(solve(list(p*V(0, -1, 3) - qq*V(-1, 1, 2) - V(2, -6, 8)), [p, qq], dict=True)[0])),
# 2024s #15: |PQ| = |QR| -> values of k; options = right roots, (k + 3) sign slip, the other components of QR forgotten (x sign)
Q('u6e6q3', L1, 'medium',
  r"إذا كانت: $P(1,\,2,\,-1)$ ، $Q(3,\,0,\,1)$ ، $R(k,\,2,\,3)$ ، وكان: $|\overrightarrow{PQ}|=|\overrightarrow{QR}|$ ، فإنّ قيم الثابت $k$ هي:",
  [pair_opt(r'1,\ 5', 1, 5), pair_opt(r'-5,\ -1', -5, -1), pair_opt(r'3-2\sqrt{3},\ 3+2\sqrt{3}', 3 - 2*sqrt(3), 3 + 2*sqrt(3)),
   pair_opt(r'-3-2\sqrt{3},\ -3+2\sqrt{3}', -3 - 2*sqrt(3), -3 + 2*sqrt(3))],
  r"$|\overrightarrow{PQ}|^2=2^2+(-2)^2+2^2=12$ ، و $\overrightarrow{QR}=\langle k-3,\,2,\,2\rangle$ ، فيكون $|\overrightarrow{QR}|^2=(k-3)^2+8$" "\n"
  r"$(k-3)^2+8=12 \Rightarrow (k-3)^2=4 \Rightarrow k-3=\pm2 \Rightarrow k=1$ أو $k=5$",
  truth=lambda: FiniteSet(*solve((x - 3)**2 + 8 - 12, x))),
# 2026 #41: cuboid in the ministry's drawing, vertex B given, vector between two vertices; options = order x C misread as B
Q('u6e6q4', L1, 'easy',
  r"في متوازي المستطيلات الآتي، إذا كانت إحداثيات الرأس $B$ هي: $(5,\,3,\,4)$ ، فإنّ الصورة الإحداثية للمتجه $\overrightarrow{EC}$ هي:",
  [vec_opt(-5, 3, 4), vec_opt(5, -3, -4), vec_opt(0, 3, 4), vec_opt(0, -3, -4)],
  r"من الشكل: $E(5,\,0,\,0)$ على المحور $x$ ، و $C(0,\,3,\,4)$ (فوق $G(0,3,0)$ بارتفاع $4$)" "\n"
  r"$\overrightarrow{EC}=C-E=\langle 0-5,\,3-0,\,4-0\rangle=\langle -5,\,3,\,4\rangle$",
  truth=T3(V(0, 3, 4) - V(5, 0, 0)), figure=figure('u6e6q4', iso_box(5, 3, 4), 3.6, 3.2)),
# 2026 #42: collinear points, AB and AC given, the unknown inside AB; options = sign of the ratio x moving the constant
Q('u6e6q5', L1, 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle -2,\,a-3,\,5\rangle$ ، $\overrightarrow{AC}=\langle 6,\,-3,\,-15\rangle$ ، فإنّ قيمة $a$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('4', 4), O('2', 2), O('-2', -2), O('-4', -4)],
  r"$\overrightarrow{AB}=k\overrightarrow{AC}$: من المركبة الأولى $-2=6k \Rightarrow k=-\frac13$ (وتتحقّق في الثالثة: $5=-15k$)" "\n"
  r"$a-3=-3k=1 \Rightarrow a=4$",
  truth=lambda: solve(V(-2, a - 3, 5).cross(V(6, -3, -15))[0], a)[0]),
# 2024s #16: triangle, P on AB in a given ratio, PO = k(...); options = k, -k, 1/k, -1/k (P's ratio 1:2 here, 2:1 there)
Q('u6e6q6', L1, 'hard',
  r"في الشكل الآتي $OAB$ مثلث، فيه: $\overrightarrow{OA}=3\vec{\mathbf{a}}$ ، $\overrightarrow{OB}=6\vec{\mathbf{b}}$ ، والنقطة $P$ تقع على $\overline{AB}$ بحيث $AP:PB=1:2$. إذا كان: $\overrightarrow{PO}=k(\vec{\mathbf{a}}+\vec{\mathbf{b}})$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('-2', -2), O('2', 2), O(r'-\frac{1}{2}', R(-1, 2)), O(r'\frac{1}{2}', R(1, 2))],
  r"$\overrightarrow{AB}=6\vec{\mathbf{b}}-3\vec{\mathbf{a}}$ ، و $\overrightarrow{AP}=\frac13\overrightarrow{AB}=2\vec{\mathbf{b}}-\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{OP}=\overrightarrow{OA}+\overrightarrow{AP}=2\vec{\mathbf{a}}+2\vec{\mathbf{b}}$ ، إذن $\overrightarrow{PO}=-2\vec{\mathbf{a}}-2\vec{\mathbf{b}}=-2(\vec{\mathbf{a}}+\vec{\mathbf{b}})$",
  truth=lambda: solve_k(-(3*va + R(1, 3)*(6*vb - 3*va)), k*(va + vb)),
  figure=figure('u6e6q6', poly_fig(tr6, [('A', 'B')], [('O', 'A', r'$3\vec{\mathbf{a}}$', (-0.85, 0.05)), ('O', 'B', r'$6\vec{\mathbf{b}}$', (-0.1, -0.5))],
                                    {'O': (-0.35, -0.3), 'A': (-0.1, 0.18), 'B': (0.12, -0.3), 'P': (0.15, 0.08)}, dashed=[('P', 'O')]), 3.8, 2.6)),
# 2024s #19: a point whose coordinates all contain the unknown lies on a line; options = a, the parameter t,
# t = 3a - 5 sign slip, t taken equal to a
Q('u6e6q7', L2, 'medium',
  r"إذا كانت النقطة $(a+2,\,3a,\,1-a)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle -3,\,-5,\,8\rangle+t\langle 2,\,1,\,-3\rangle$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('-1', -1), O('2', 2), O('3', 3), O('5', 5)],
  r"نساوي الإحداثيات: $a+2=-3+2t$ ، $3a=-5+t$ ، $1-a=8-3t$" "\n"
  r"من الثانية: $t=3a+5$ ، وبالتعويض في الأولى: $a+2=6a+7 \Rightarrow -5a=5 \Rightarrow a=-1$ ، $t=2$" "\n"
  r"تحقّق في الثالثة: $1-(-1)=2$ و $8-3(2)=2$ ✔",
  truth=lambda: solve(list(V(a + 2, 3*a, 1 - a) - V(-3, -5, 8) - t*V(2, 1, -3)), [a, t], dict=True)[0][a]),
# 2026 #38: line parallel to v through a position vector with a missing component (k); options as in 2026 #38
IndexQ('u6e6q8', L2, 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=-2\hat{i}+3\hat{j}+4\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $6\hat{i}-\hat{j}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((6, -1, 0), (-2, 3, 4)), line_opt((-2, 3, 4), (6, -1, 0)), line_opt((0, 6, -1), (-2, 3, 4)), line_opt((-2, 3, 4), (0, 6, -1))],
  r"متجه موقع النقطة $A$ هو $6\hat{i}-\hat{j}+0\hat{k}=\langle 6,\,-1,\,0\rangle$ ، ومتجه الاتجاه $\langle -2,\,3,\,4\rangle$:" "\n"
  r"$\vec{\mathbf{r}}=\langle 6,-1,0\rangle+t\langle -2,3,4\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((6, -1, 0), ln) and par(ln[1], (-2, 3, 4)))),
# 2025s #17: point where a line meets the yz plane; options = right point, x merely set to 0, t sign slip (with and without x = 0)
Q('u6e6q9', L2, 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 2,\,-5,\,1\rangle+t\langle -1,\,4,\,2\rangle$ معادلة متجهة للمستقيم $l$ ، فإنّ إحداثيات نقطة تقاطع المستقيم $l$ مع المستوى $yz$ هي:",
  [pt_opt(0, 3, 5), pt_opt(0, -5, 1), pt_opt(4, -13, -3), pt_opt(0, -13, -3)],
  r"على المستوى $yz$ يكون $x=0$: $2-t=0 \Rightarrow t=2$" "\n"
  r"النقطة: $(0,\ -5+8,\ 1+4)=(0,\,3,\,5)$",
  truth=lambda: T3(V(2, -5, 1) + solve(2 - t, t)[0]*V(-1, 4, 2))),
# 2023 #19: perpendicular vectors, linear in c; options = +-3, +-1 (sign slip in one product)
Q('u6e6q10', L3, 'easy',
  r"إذا كان المتجهان: $\vec{\mathbf{u}}=\langle 2c,\,5,\,-4\rangle$ ، $\vec{\mathbf{v}}=\langle 5,\,-2,\,5\rangle$ متعامدين، فإنّ قيمة الثابت $c$ هي:",
  [O('3', 3), O('-3', -3), O('1', 1), O('-1', -1)],
  r"المتجهان متعامدان إذا كان $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=0$: $10c-10-20=0 \Rightarrow 10c=30 \Rightarrow c=3$",
  truth=lambda: solve(V(2*c, 5, -4).dot(V(5, -2, 5)), c)[0]),
# 2024s #20: |b| from the angle, the dot product and |a|; options = divide or multiply by cos, x cos 30 or 1/2
Q('u6e6q11', L3, 'medium',
  r"إذا كان قياس الزاوية بين المتجهين $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو $30^\circ$ ، وكان: $|\vec{\mathbf{a}}|=3$ ، $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=9$ ، فإنّ مقدار المتجه $\vec{\mathbf{b}}$ هو:",
  [O(r'2\sqrt{3}', 2*sqrt(3)), O(r'\frac{3\sqrt{3}}{2}', 3*sqrt(3)/2), O('6', 6), O(r'\frac{3}{2}', R(3, 2))],
  r"$\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=|\vec{\mathbf{a}}||\vec{\mathbf{b}}|\cos30^\circ \Rightarrow 9=3|\vec{\mathbf{b}}|\cdot\dfrac{\sqrt3}{2}=\dfrac{3\sqrt3}{2}|\vec{\mathbf{b}}|$" "\n"
  r"$|\vec{\mathbf{b}}|=\dfrac{9\times2}{3\sqrt3}=\dfrac{6}{\sqrt3}=2\sqrt3$",
  truth=9/(3*cos(pi/6))),
# 2023s #18: F the foot of the perpendicular from P to the line -> PF in terms of t (the first step of finding F);
# options = F - P, F + P, the constant part reversed (P - A + t v), P used as the line's point (P + t v)
Q('u6e6q12', L3, 'medium',
  r"إذا كانت: $\vec{\mathbf{r}}=\langle 2,\,0,\,-1\rangle+t\langle 2,\,1,\,-1\rangle$ معادلة متجهة للمستقيم $l$ ، و $P(-4,\,-2,\,-3)$ نقطة غير واقعة عليه، وكانت النقطة $F$ مسقط العمود من النقطة $P$ على المستقيم $l$ ، فإنّ $\overrightarrow{PF}$ هو:",
  [O(r'\langle 6+2t,\,2+t,\,2-t\rangle', Tuple(6 + 2*t, 2 + t, 2 - t), 'vec'),
   O(r'\langle -2+2t,\,-2+t,\,-4-t\rangle', Tuple(-2 + 2*t, -2 + t, -4 - t), 'vec'),
   O(r'\langle -6+2t,\,-2+t,\,-2-t\rangle', Tuple(-6 + 2*t, -2 + t, -2 - t), 'vec'),
   O(r'\langle -4+2t,\,-2+t,\,-3-t\rangle', Tuple(-4 + 2*t, -2 + t, -3 - t), 'vec')],
  r"$F$ نقطة على المستقيم، فإحداثياتها $F=(2+2t,\ t,\ -1-t)$" "\n"
  r"$\overrightarrow{PF}=F-P=\langle 2+2t+4,\ t+2,\ -1-t+3\rangle=\langle 6+2t,\ 2+t,\ 2-t\rangle$",
  truth=T3(V(2, 0, -1) + t*V(2, 1, -1) - V(-4, -2, -3))),
]

# ============================================================== Exam 7
# parallelogram KLMN, Y the midpoint of KM, Z on LM produced with LM:MZ = 2:1
pg7 = plane_pts((0.5, 2.5), (-0.25, -1.1), (4.5/4, 0.5/4),
                {'K': 0, 'L': 4*vb, 'M': 2*va + 4*vb, 'N': 2*va, 'Y': va + 2*vb, 'Z': 3*va + 4*vb})
E7 = [
# 2024s #14: magnitude of the position vector of a midpoint; options = |OM|, |OA + OB| (not halved), half of |AB|, |AB|
Q('u6e7q1', L1, 'easy',
  r"إذا كانت: $A(3,\,-2,\,7)$ ، $B(-1,\,6,\,-3)$ ، وكانت $M$ نقطة منتصف $\overline{AB}$ ، فإنّ مقدار متجه الموقع للنقطة $M$ هو:",
  [O('3', 3), O('6', 6), O(r'3\sqrt{5}', 3*sqrt(5)), O(r'6\sqrt{5}', 6*sqrt(5))],
  r"$M=\left(\dfrac{3-1}{2},\ \dfrac{-2+6}{2},\ \dfrac{7-3}{2}\right)=(1,\,2,\,2)$" "\n"
  r"$|\overrightarrow{OM}|=\sqrt{1+4+4}=\sqrt9=3$",
  truth=((V(3, -2, 7) + V(-1, 6, -3))/2).norm()),
# 2025s #13: midpoint with unknowns in both points; options = n right or not doubled, x sign slip when moving -3
Q('u6e7q2', L1, 'medium',
  r"إذا كانت النقطة $M(2,\,-1,\,k)$ منتصف القطعة المستقيمة $\overline{AB}$ ، حيث: $A(-3,\,4,\,5)$ ، $B(n,\,-6,\,-3n)$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('-8', -8), O('-5', -5), O('1', 1), O('4', 4)],
  r"من الإحداثي $x$: $\dfrac{-3+n}{2}=2 \Rightarrow -3+n=4 \Rightarrow n=7$ ، فتكون $B(7,\,-6,\,-21)$" "\n"
  r"$k=\dfrac{5+(-21)}{2}=\dfrac{-16}{2}=-8$",
  truth=lambda: (lambda nn: (5 - 3*nn)/2)(solve((-3 + n)/2 - 2, n)[0])),
# 2024 #20: parallel vectors with two unknowns -> a + b; options = sign of the ratio x moving the constants
Q('u6e7q3', L1, 'medium',
  r"إذا كان المتجه $\vec{\mathbf{u}}=\langle 2,\,a+1,\,-3\rangle$ يوازي المتجه $\vec{\mathbf{v}}=\langle -6,\,9,\,b-2\rangle$ ، فإنّ قيمة $a+b$ هي:",
  [O('7', 7), O('5', 5), O('-5', -5), O('-7', -7)],
  r"$\vec{\mathbf{u}}=k\vec{\mathbf{v}}$: من المركبة الأولى $2=-6k \Rightarrow k=-\frac13$" "\n"
  r"$a+1=-\frac13(9)=-3 \Rightarrow a=-4$ ، و $-3=-\frac13(b-2) \Rightarrow b-2=9 \Rightarrow b=11$ ، إذن $a+b=7$",
  truth=lambda: (lambda s_: s_[a] + s_[b])(solve(list(V(2, a + 1, -3).cross(V(-6, 9, b - 2))), [a, b], dict=True)[0])),
# 2026 #44 (asked the other way): parallelogram, Y the midpoint of a diagonal, Z on a produced side in a given
# ratio -> YZ; options = MZ right or the ratio read the other way, x YZ or ZY
Q('u6e7q4', L1, 'hard',
  r"في الشكل الآتي $KLMN$ متوازي أضلاع، فيه: $\overrightarrow{KL}=4\vec{\mathbf{b}}$ ، $\overrightarrow{KN}=2\vec{\mathbf{a}}$ ، والنقطة $Y$ منتصف القطر $\overline{KM}$. إذا كانت النقطة $Z$ تقع على امتداد $\overline{LM}$ بحيث $LM:MZ=2:1$ ، فإنّ $\overrightarrow{YZ}$ بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ هو:",
  [vopt(2*va + 2*vb), vopt(5*va + 2*vb), vopt(-2*va - 2*vb), vopt(-5*va - 2*vb)],
  r"$\overrightarrow{KM}=2\vec{\mathbf{a}}+4\vec{\mathbf{b}}$ ، فيكون $\overrightarrow{YM}=\frac12\overrightarrow{KM}=\vec{\mathbf{a}}+2\vec{\mathbf{b}}$" "\n"
  r"$\overrightarrow{LM}=\overrightarrow{KN}=2\vec{\mathbf{a}}$ ، و $\overrightarrow{MZ}=\frac12\overrightarrow{LM}=\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{YZ}=\overrightarrow{YM}+\overrightarrow{MZ}=2\vec{\mathbf{a}}+2\vec{\mathbf{b}}$",
  truth=(2*va + 4*vb + (2*va)/2) - (va + 2*vb),
  figure=figure('u6e7q4', poly_fig(pg7, [('L', 'M'), ('N', 'M'), ('M', 'Z'), ('K', 'M')],
                                    [('K', 'L', r'$4\vec{\mathbf{b}}$', (-0.2, 0.18)), ('K', 'N', r'$2\vec{\mathbf{a}}$', (-0.75, 0.0))],
                                    {'K': (-0.2, 0.15), 'L': (0.1, 0.1), 'M': (0.15, 0.0), 'N': (-0.3, -0.3), 'Y': (-0.08, 0.2), 'Z': (0.12, -0.25)},
                                    dashed=[('Y', 'Z')]), 3.8, 2.6)),
# 2024 #18: vector of a given magnitude opposite to a vector in i, j, k; options = opposite or same direction, x normalised or not
Q('u6e7q5', L1, 'easy',
  r"المتجه الذي مقداره $14$ وحدة، وفي عكس اتجاه المتجه $\vec{\mathbf{v}}=3\hat{i}-6\hat{j}+2\hat{k}$ ، هو:",
  [ijk_opt(-6, 12, -4), ijk_opt(6, -12, 4), ijk_opt(-42, 84, -28), ijk_opt(42, -84, 28)],
  r"$|\vec{\mathbf{v}}|=\sqrt{9+36+4}=\sqrt{49}=7$ ، ومتجه الوحدة في عكس اتجاهه $-\dfrac{\vec{\mathbf{v}}}{7}$" "\n"
  r"المتجه المطلوب: $14\left(-\dfrac{\vec{\mathbf{v}}}{7}\right)=-2\vec{\mathbf{v}}=-6\hat{i}+12\hat{j}-4\hat{k}$",
  truth=T3(-14*V(3, -6, 2)/V(3, -6, 2).norm())),
# 2023 #17: PF = 2/3 PQ -> F; options = 2/3 or 1/3 of PQ, x added to P or not
Q('u6e7q6', L1, 'medium',
  r"إذا كانت: $P(-1,\,5,\,2)$ ، $Q(5,\,-4,\,8)$ ، وكانت $F$ نقطة على $\overline{PQ}$ بحيث $\overrightarrow{PF}=\frac{2}{3}\overrightarrow{PQ}$ ، فإنّ إحداثيات النقطة $F$ هي:",
  [pt_opt(3, -1, 6), pt_opt(1, 2, 4), pt_opt(4, -6, 4), pt_opt(2, -3, 2)],
  r"$\overrightarrow{PQ}=\langle 6,\,-9,\,6\rangle$ ، و $\overrightarrow{PF}=\frac23\overrightarrow{PQ}=\langle 4,\,-6,\,4\rangle$" "\n"
  r"$F=P+\overrightarrow{PF}=(-1+4,\ 5-6,\ 2+4)=(3,\,-1,\,6)$",
  truth=T3(V(-1, 5, 2) + R(2, 3)*(V(5, -4, 8) - V(-1, 5, 2)))),
# 2026 #38: line parallel to v (v has a missing component, j) through a position vector; options = point and
# direction swapped x the zero of v put in the wrong place
IndexQ('u6e7q7', L2, 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=5\hat{i}-3\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $-\hat{i}+2\hat{j}+4\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((-1, 2, 4), (5, 0, -3)), line_opt((5, 0, -3), (-1, 2, 4)), line_opt((-1, 2, 4), (5, -3, 0)), line_opt((5, -3, 0), (-1, 2, 4))],
  r"متجه الاتجاه: $5\hat{i}+0\hat{j}-3\hat{k}=\langle 5,\,0,\,-3\rangle$ ، ومتجه موقع النقطة $\langle -1,\,2,\,4\rangle$:" "\n"
  r"$\vec{\mathbf{r}}=\langle -1,2,4\rangle+t\langle 5,0,-3\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((-1, 2, 4), ln) and par(ln[1], (5, 0, -3)))),
# 2023 #18: a point with an unknown coordinate lies on a line; options = t right or slipped, x 2a divided by 2 or not
Q('u6e7q8', L2, 'medium',
  r"إذا كانت النقطة $(5,\,2a,\,-4)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle -1,\,7,\,5\rangle+t\langle 2,\,-1,\,-3\rangle$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('2', 2), O('4', 4), O(r'\frac{5}{2}', R(5, 2)), O('5', 5)],
  r"من الإحداثي $x$: $-1+2t=5 \Rightarrow t=3$ ، وتحقّق في $z$: $5-9=-4$ ✔" "\n"
  r"الإحداثي $y$: $2a=7-3=4 \Rightarrow a=2$",
  truth=lambda: solve(list(V(5, 2*a, -4) - V(-1, 7, 5) - t*V(2, -1, -3)), [a, t], dict=True)[0][a]),
# 2023s #18: general point of a segment, PF = t PQ; options = start at P or at Q, x direction PQ or QP
Q('u6e7q9', L2, 'medium',
  r"إذا كانت: $P(1,\,4,\,-2)$ ، $Q(4,\,2,\,3)$ ، وكانت $F$ نقطة على $\overline{PQ}$ بحيث $\overrightarrow{PF}=t\,\overrightarrow{PQ}$ ، حيث $0\le t\le1$ ، فإنّ إحداثيات النقطة $F$ بدلالة $t$ هي:",
  [O(r'(1+3t,\,4-2t,\,-2+5t)', Tuple(1 + 3*t, 4 - 2*t, -2 + 5*t), 'tuple'), O(r'(4+3t,\,2-2t,\,3+5t)', Tuple(4 + 3*t, 2 - 2*t, 3 + 5*t), 'tuple'),
   O(r'(1-3t,\,4+2t,\,-2-5t)', Tuple(1 - 3*t, 4 + 2*t, -2 - 5*t), 'tuple'), O(r'(4-3t,\,2+2t,\,3-5t)', Tuple(4 - 3*t, 2 + 2*t, 3 - 5*t), 'tuple')],
  r"$\overrightarrow{PQ}=\langle 3,\,-2,\,5\rangle$ ، و $F=P+t\overrightarrow{PQ}=(1+3t,\ 4-2t,\ -2+5t)$" "\n"
  r"(وهي المعادلة المتجهة للمستقيم $PQ$ ، والشرط $0\le t\le1$ يحصر النقطة على القطعة)",
  truth=T3(V(1, 4, -2) + t*(V(4, 2, 3) - V(1, 4, -2)))),
# 2023 #20: which figure shows u . v > 0 (sign of the dot product from the angle); options = the four panels
IndexQ('u6e7q10', L3, 'easy',
  r"أيُّ الأشكال الآتية يكون فيه $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}>0$؟",
  [T('الشكل (2)', pi/4), T('الشكل (1)', 2*pi/3), T('الشكل (3)', pi/2), T('الشكل (4)', pi)],
  r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=|\vec{\mathbf{u}}||\vec{\mathbf{v}}|\cos\theta$ ، فإشارته إشارة $\cos\theta$: موجبة للزاوية الحادّة فقط." "\n"
  r"في الشكل (2) الزاوية $45^\circ$ حادّة، أمّا $120^\circ$ و $180^\circ$ فجيب تمامهما سالب، و $90^\circ$ تعطي صفرًا.",
  truth=lambda vals: only(vals, lambda th: cos(th) > 0),
  figure=figure('u6e7q10', sign_panels([120, 45, 90, 180]), 4.4, 3.0)),
# 2026 #43: three points, two side vectors given -> dot product; options = +-(right value), +-(KL . ML used directly)
Q('u6e7q11', L3, 'hard',
  r"إذا كانت $K,\ L,\ M$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{KL}=\langle 2,\,-3,\,1\rangle$ ، $\overrightarrow{ML}=\langle 4,\,1,\,-2\rangle$ ، فإنّ $\overrightarrow{KL}\cdot\overrightarrow{KM}$ يساوي:",
  [O('11', 11), O('-11', -11), O('3', 3), O('-3', -3)],
  r"$\overrightarrow{KM}=\overrightarrow{KL}+\overrightarrow{LM}=\overrightarrow{KL}-\overrightarrow{ML}=\langle -2,\,-4,\,3\rangle$" "\n"
  r"$\overrightarrow{KL}\cdot\overrightarrow{KM}=-4+12+3=11$",
  truth=V(2, -3, 1).dot(V(2, -3, 1) - V(4, 1, -2))),
# 2026 #45: triangle from the two side vectors at the right-angle vertex (C here; the right angle is not stated);
# options = 1/2 x the legs, without 1/2, and the hypotenuse AB taken as a leg (with and without 1/2)
Q('u6e7q12', L3, 'hard',
  r"إذا كان $ABC$ مثلثًا فيه: $\overrightarrow{CA}=\langle 2,\,4,\,4\rangle$ ، $\overrightarrow{CB}=\langle 4,\,2,\,-4\rangle$ ، فإنّ مساحته بالوحدات المربعة تساوي:",
  [O('18', 18), O('36', 36), O(r'18\sqrt{2}', 18*sqrt(2)), O(r'36\sqrt{2}', 36*sqrt(2))],
  r"$\overrightarrow{CA}\cdot\overrightarrow{CB}=8+8-16=0$ ، إذن الزاوية $C$ قائمة" "\n"
  r"$|\overrightarrow{CA}|=6$ ، $|\overrightarrow{CB}|=6$ ، والمساحة تساوي $\frac12(6)(6)=18$",
  truth=R(1, 2)*V(2, 4, 4).norm()*V(4, 2, -4).norm()*sin(ang(V(2, 4, 4), V(4, 2, -4)))),
]

# ============================================================== Exam 8
# parallelogram PQRS, Y the midpoint of PR, Z on QR produced with QR:RZ = 3:1
pg8 = plane_pts((0.5, 2.6), (-0.1, -0.4), (1.0, 0.125),
                {'P': 0, 'Q': 4*vb, 'R': 6*va + 4*vb, 'S': 6*va, 'Y': 3*va + 2*vb, 'Z': 8*va + 4*vb})
E8 = [
# 2024 #17: position vector of a midpoint, given with i, j, k; options = sum or difference, x halved or not
Q('u6e8q1', L1, 'easy',
  r"إذا كان: $\overrightarrow{OA}=3\hat{i}-4\hat{j}+\hat{k}$ ، $\overrightarrow{OB}=-\hat{i}+2\hat{j}+5\hat{k}$ ، وكانت $K$ نقطة منتصف $\overline{AB}$ ، فإنّ متجه الموقع للنقطة $K$ هو:",
  [ijk_opt(1, -1, 3), ijk_opt(2, -2, 6), ijk_opt(-2, 3, 2), ijk_opt(-4, 6, 4)],
  r"$\overrightarrow{OK}=\dfrac{\overrightarrow{OA}+\overrightarrow{OB}}{2}=\dfrac{(3-1)\hat{i}+(-4+2)\hat{j}+(1+5)\hat{k}}{2}=\hat{i}-\hat{j}+3\hat{k}$",
  truth=T3((V(3, -4, 1) + V(-1, 2, 5))/2)),
# 2025s #16: GH = HD -> D; options = 2H - G, 2G - H and their negatives
Q('u6e8q2', L1, 'easy',
  r"إذا كانت: $G(-1,\,4,\,2)$ ، $H(2,\,1,\,-3)$ ، وكانت $D$ نقطة في الفضاء بحيث $\overrightarrow{GH}=\overrightarrow{HD}$ ، فإنّ متجه الموقع للنقطة $D$ هو:",
  [vec_opt(5, -2, -8), vec_opt(-5, 2, 8), vec_opt(-4, 7, 7), vec_opt(4, -7, -7)],
  r"$\overrightarrow{GH}=\overrightarrow{HD} \Rightarrow D=2H-G$ (أي أن $H$ منتصف $\overline{GD}$)" "\n"
  r"$D=\langle 4+1,\,2-4,\,-6-2\rangle=\langle 5,\,-2,\,-8\rangle$",
  truth=T3(2*V(2, 1, -3) - V(-1, 4, 2))),
# 2023s #15: |AB| = 13 with an unknown coordinate -> its values; options = right roots, (7 + k) slip,
# the other components forgotten (x sign)
Q('u6e8q3', L1, 'medium',
  r"إذا كانت: $A(2,\,-3,\,k)$ ، $B(5,\,1,\,7)$ ، وكان: $|\overrightarrow{AB}|=13$ ، فإنّ قيمتي الثابت $k$ هما:",
  [pair_opt(r'-5,\ 19', -5, 19), pair_opt(r'5,\ -19', 5, -19), pair_opt(r'-6,\ 20', -6, 20), pair_opt(r'6,\ -20', 6, -20)],
  r"$\overrightarrow{AB}=\langle 3,\,4,\,7-k\rangle$ ، و $9+16+(7-k)^2=169 \Rightarrow (7-k)^2=144$" "\n"
  r"$7-k=\pm12 \Rightarrow k=-5$ أو $k=19$",
  truth=lambda: FiniteSet(*solve(9 + 16 + (7 - x)**2 - 169, x))),
# 2026 #42: collinear with AB and BC (not AC) given; options = sign of the ratio x the ratio inverted
Q('u6e8q4', L1, 'medium',
  r"إذا كانت $A,\ B,\ C$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{AB}=\langle a,\,2,\,-1\rangle$ ، $\overrightarrow{BC}=\langle 6,\,-4,\,2\rangle$ ، فإنّ قيمة $a$ التي تجعل النقاط $A,\ B,\ C$ تقع على استقامة واحدة هي:",
  [O('-3', -3), O('3', 3), O('-12', -12), O('12', 12)],
  r"تقع النقاط على استقامة واحدة إذا توازى $\overrightarrow{AB}$ و $\overrightarrow{BC}$ (ولهما النقطة المشتركة $B$)" "\n"
  r"$\overrightarrow{AB}=k\overrightarrow{BC}$: من المركبة الثانية $2=-4k \Rightarrow k=-\frac12$ ، و $a=6k=-3$",
  truth=lambda: solve(V(a, 2, -1).cross(V(6, -4, 2))[1], a)[0]),
# 2025s #18: parallel vectors with the unknown in two components; options = right root, the root that fails the
# first component, and their negatives
Q('u6e8q5', L1, 'hard',
  r"إذا كان المتجه $\vec{\mathbf{a}}=\langle 2,\,\alpha,\,10\rangle$ يوازي المتجه $\vec{\mathbf{b}}=\langle -1,\,4,\,\alpha+3\rangle$ ، فإنّ قيمة الثابت $\alpha$ هي:",
  [O('-8', -8), O('5', 5), O('8', 8), O('-5', -5)],
  r"$\vec{\mathbf{a}}=k\vec{\mathbf{b}}$: من المركبة الأولى $2=-k \Rightarrow k=-2$" "\n"
  r"المركبة الثانية: $\alpha=4k=-8$ ، وتحقّق في الثالثة: $10=-2(\alpha+3)=-2(-5)$ ✔",
  truth=lambda: solve(list(V(2, x, 10).cross(V(-1, 4, x + 3))), [x], dict=True)[0][x]),
# 2026 #44: parallelogram, Y the midpoint of a diagonal, Z on a produced side, k from the given vector;
# options = k, 1/k (the ratio read the other way) and values of the same kind
Q('u6e8q6', L1, 'hard',
  r"في الشكل الآتي $PQRS$ متوازي أضلاع. إذا كان: $\overrightarrow{PQ}=4\vec{\mathbf{b}}$ ، $\overrightarrow{PS}=6\vec{\mathbf{a}}$ ، وكانت $Y$ نقطة منتصف $\overline{PR}$ ، وكان: $QR:RZ=k:1$ ، $\overrightarrow{YZ}=2\vec{\mathbf{b}}+5\vec{\mathbf{a}}$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('3', 3), O(r'\frac{1}{3}', R(1, 3)), O('2', 2), O(r'\frac{3}{2}', R(3, 2))],
  r"$\overrightarrow{YR}=\frac12\overrightarrow{PR}=\frac12(6\vec{\mathbf{a}}+4\vec{\mathbf{b}})=3\vec{\mathbf{a}}+2\vec{\mathbf{b}}$" "\n"
  r"$\overrightarrow{QR}=6\vec{\mathbf{a}}$ ، و $\overrightarrow{RZ}=\frac1k\overrightarrow{QR}=\frac6k\vec{\mathbf{a}}$" "\n"
  r"$\overrightarrow{YZ}=\overrightarrow{YR}+\overrightarrow{RZ}=\left(3+\frac6k\right)\vec{\mathbf{a}}+2\vec{\mathbf{b}}$ ، وبالمقارنة: $3+\frac6k=5 \Rightarrow k=3$",
  truth=lambda: solve_k((6*va + 4*vb + 6*va/k) - (3*va + 2*vb), 2*vb + 5*va),
  figure=figure('u6e8q6', poly_fig(pg8, [('Q', 'R'), ('S', 'R'), ('R', 'Z'), ('P', 'R')],
                                    [('P', 'Q', r'$4\vec{\mathbf{b}}$', (-0.2, 0.18)), ('P', 'S', r'$6\vec{\mathbf{a}}$', (-0.75, 0.0))],
                                    {'P': (-0.2, 0.15), 'Q': (0.1, 0.1), 'R': (0.15, 0.0), 'S': (-0.3, -0.3), 'Y': (-0.08, 0.2), 'Z': (0.12, -0.25)},
                                    dashed=[('Y', 'Z')]), 3.8, 2.6)),
# 2026 #38: line parallel to v through a position vector with a missing component (j); options as in 2026 #38
IndexQ('u6e8q7', L2, 'easy',
  r"إذا كان المستقيم $l$ يوازي المتجه: $\vec{\mathbf{v}}=4\hat{i}-\hat{j}+3\hat{k}$ ، ويمرّ بالنقطة $A$ التي متجه موقعها: $-2\hat{i}+5\hat{k}$ ، فإنّ للمستقيم $l$ معادلة متجهة هي:",
  [line_opt((-2, 0, 5), (4, -1, 3)), line_opt((4, -1, 3), (-2, 0, 5)), line_opt((-2, 5, 0), (4, -1, 3)), line_opt((4, -1, 3), (-2, 5, 0))],
  r"متجه موقع النقطة $A$ هو $-2\hat{i}+0\hat{j}+5\hat{k}=\langle -2,\,0,\,5\rangle$ ، ومتجه الاتجاه $\langle 4,\,-1,\,3\rangle$:" "\n"
  r"$\vec{\mathbf{r}}=\langle -2,0,5\rangle+t\langle 4,-1,3\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((-2, 0, 5), ln) and par(ln[1], (4, -1, 3)))),
# 2023 #18: a point with two unknown coordinates lies on a line -> a + b; options = t = -3 (right), 3, -2, 2
Q('u6e8q8', L2, 'medium',
  r"إذا كانت النقطة $(a,\,-1,\,b)$ تقع على المستقيم: $\vec{\mathbf{r}}=\langle 3,\,5,\,-2\rangle+t\langle -1,\,2,\,4\rangle$ ، فإنّ قيمة $a+b$ هي:",
  [O('-8', -8), O('10', 10), O('-5', -5), O('7', 7)],
  r"من الإحداثي $y$: $5+2t=-1 \Rightarrow t=-3$" "\n"
  r"$a=3-(-3)=6$ ، و $b=-2+4(-3)=-14$ ، إذن $a+b=-8$",
  truth=lambda: (lambda tt: (3 - tt) + (-2 + 4*tt))(solve(5 + 2*t + 1, t)[0])),
# 2025 #19: cuboid in the ministry's drawing, line through two vertices; options = direction GA or GB (misread
# vertex), x point and direction in the right order or swapped
IndexQ('u6e8q9', L2, 'medium',
  r"في متوازي المستطيلات الآتي، إذا كانت إحداثيات الرأس $B$ هي: $(6,\,4,\,2)$ ، فإنّ معادلة متجهة للمستقيم المارّ بالرأسين $G$ و $A$ هي:",
  [line_opt((0, 4, 0), (3, -2, 1)), line_opt((0, 4, 0), (3, 0, 1)), line_opt((3, -2, 1), (0, 4, 0)), line_opt((3, 0, 1), (0, 4, 0))],
  r"من الشكل: $G(0,\,4,\,0)$ ، $A(6,\,0,\,2)$ ، و $\overrightarrow{GA}=\langle 6,\,-4,\,2\rangle=2\langle 3,\,-2,\,1\rangle$" "\n"
  r"$\vec{\mathbf{r}}=\langle 0,4,0\rangle+t\langle 3,-2,1\rangle$",
  truth=lambda vals: only(vals, lambda ln: on_line((0, 4, 0), ln) and on_line((6, 0, 2), ln)),
  figure=figure('u6e8q9', iso_box(6, 4, 2), 3.8, 2.8)),
# 2026r #19: perpendicular vectors, quadratic in alpha; options = right factor pair or the other pair of 15, x sign
Q('u6e8q10', L3, 'medium',
  r"إذا كان: $\vec{\mathbf{v}}=\langle 2,\,\alpha,\,3\rangle$ ، $\vec{\mathbf{w}}=\langle \alpha,\,\alpha,\,-5\rangle$ ، وكان المتجهان $\vec{\mathbf{v}}$ و $\vec{\mathbf{w}}$ متعامدين، فإنّ القيمتين المُمكنتين للثابت $\alpha$ هما:",
  [pair_opt(r'-5,\ 3', -5, 3), pair_opt(r'5,\ -3', 5, -3), pair_opt(r'-15,\ 1', -15, 1), pair_opt(r'15,\ -1', 15, -1)],
  r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=2\alpha+\alpha^2-15=0 \Rightarrow (\alpha+5)(\alpha-3)=0$" "\n"
  r"$\alpha=-5$ أو $\alpha=3$",
  truth=lambda: FiniteSet(*solve(V(2, x, 3).dot(V(x, x, -5)), x))),
# 2025s #20: distance from a point to a line, foot given with fractions; options = |PF| or |PF|^2, x sign slip in y
Q('u6e8q11', L3, 'easy',
  r"إذا كانت $P(3,\,-1,\,2)$ نقطة غير واقعة على المستقيم $l$ ، وكانت $F\left(\frac{5}{2},\,1,\,\frac{3}{2}\right)$ مسقط العمود من النقطة $P$ على المستقيم $l$ ، فإنّ البُعد بين النقطة $P$ والمستقيم $l$ (بوحدات الطول) هو:",
  [O(r'\frac{3\sqrt{2}}{2}', 3*sqrt(2)/2), O(r'\frac{9}{2}', R(9, 2)), O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'\frac{1}{2}', R(1, 2))],
  r"$\overrightarrow{PF}=\left\langle \frac52-3,\ 1+1,\ \frac32-2\right\rangle=\left\langle -\frac12,\ 2,\ -\frac12\right\rangle$" "\n"
  r"$|\overrightarrow{PF}|=\sqrt{\frac14+4+\frac14}=\sqrt{\frac92}=\dfrac{3}{\sqrt2}=\dfrac{3\sqrt2}{2}$",
  truth=(V(R(5, 2), 1, R(3, 2)) - V(3, -1, 2)).norm()),
# 2026 #43: three points, two side vectors given -> dot product; options = +-(right value), +-(RS . TS used directly)
Q('u6e8q12', L3, 'hard',
  r"إذا كانت $R,\ S,\ T$ ثلاث نقاط في الفضاء، وكان: $\overrightarrow{RS}=\langle -1,\,2,\,4\rangle$ ، $\overrightarrow{TS}=\langle 3,\,-2,\,1\rangle$ ، فإنّ $\overrightarrow{RS}\cdot\overrightarrow{RT}$ يساوي:",
  [O('24', 24), O('-24', -24), O('-3', -3), O('3', 3)],
  r"$\overrightarrow{RT}=\overrightarrow{RS}+\overrightarrow{ST}=\overrightarrow{RS}-\overrightarrow{TS}=\langle -4,\,4,\,3\rangle$" "\n"
  r"$\overrightarrow{RS}\cdot\overrightarrow{RT}=4+8+12=24$",
  truth=V(-1, 2, 4).dot(V(-1, 2, 4) - V(3, -2, 1))),
]

EXAMS_4_8 = [('الاختبار الرابع', E4), ('الاختبار الخامس', E5), ('الاختبار السادس', E6),
             ('الاختبار السابع', E7), ('الاختبار الثامن', E8)]
