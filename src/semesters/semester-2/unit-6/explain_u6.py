"""Teaching explanations for unit 6 (attached by build() in qb.py).
wrong: {original option index: reason}; option 0 is the correct one as written in u6.py."""
from explain_common import E

VEC = r"المتجه من النقطة $A$ إلى النقطة $B$: $\overrightarrow{AB}=B-A$ (إحداثيات النهاية ناقص إحداثيات البداية)"
MAG = r"مقدار المتجه $\langle a,b,c\rangle$ هو $\sqrt{a^2+b^2+c^2}$"
PAR = r"المتجهان متوازيان إذا كان أحدهما مضاعفًا للآخر: $\vec{\mathbf{u}}=k\vec{\mathbf{v}}$ لعدد حقيقي $k$"
LINE = r"المعادلة المتجهة للمستقيم: $\vec{\mathbf{r}}=\vec{\mathbf{r}}_0+t\vec{\mathbf{v}}$ ، حيث $\vec{\mathbf{r}}_0$ متجه موقع نقطة على المستقيم، و $\vec{\mathbf{v}}$ متجه اتجاهه"
REL = r"العلاقة بين مستقيمين: إذا توازى متجها الاتجاه فهما متوازيان أو منطبقان (نختبر نقطة من أحدهما على الآخر)، وإلّا فهما متقاطعان أو متخالفان (نحلّ معادلات تساوي الإحداثيات)"
DOT = r"الضرب القياسي: $\langle a_1,a_2,a_3\rangle\cdot\langle b_1,b_2,b_3\rangle=a_1b_1+a_2b_2+a_3b_3$ ، وأيضًا $\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=|\vec{\mathbf{u}}||\vec{\mathbf{v}}|\cos\theta$ ، والمتجهان متعامدان إذا كان ضربهما القياسي صفرًا"
UNIT = r"متجه الوحدة في اتجاه $\vec{\mathbf{v}}$ هو $\dfrac{\vec{\mathbf{v}}}{|\vec{\mathbf{v}}|}$ (نقسم كل مركبة على المقدار)، ومقداره دائمًا $1$"
MID = r"منتصف القطعة بين نقطتين = متوسط إحداثياتهما: $\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2},\frac{z_1+z_2}{2}\right)$"
ANGLE = r"الزاوية بين متجهين: $\cos\theta=\dfrac{\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}}{|\vec{\mathbf{u}}||\vec{\mathbf{v}}|}$ ، و $0\le\theta\le\pi$ (إشارة الضرب القياسي السالبة تعني زاوية منفرجة)"
PT = r"نقطة على المستقيم ← نكتب إحداثياتها العامة بدلالة $t$ ، ونستعمل المعلومة المعطاة لإيجاد $t$ ، ثم نعوّض في باقي الإحداثيات"
FOOT = r"مسقط العمود من $P$ على مستقيم هو النقطة $Q$ عليه التي تجعل $\overrightarrow{PQ}$ عموديًّا على متجه اتجاه المستقيم (ضربهما القياسي صفر)"
COLL = r"تقع ثلاث نقاط على استقامة واحدة إذا كان المتجهان المنطلقان من إحداها إلى الأخريين متوازيين (أحدهما مضاعف للآخر)"
REL4 = r"الحالات الأربع: متوازيان (اتجاهان متوازيان ولا نقطة مشتركة)، منطبقان (اتجاهان متوازيان ونقطة مشتركة)، متقاطعان (اتجاهان غير متوازيين ونقطة مشتركة)، متخالفان (اتجاهان غير متوازيين ولا نقطة مشتركة)"

EXPLAIN = {
# ============================================================ الاختبار الأول
'u6e1q1': E(
    idea=r"مقدار متجه بين نقطتين ← نجد المتجه أولًا (النهاية − البداية)، ثم نحسب مقداره بالجذر.",
    steps=[
        "## أولًا: المتجه",
        VEC,
        r"$\overrightarrow{AB}=\langle -3-3,\ 1-(-2),\ 4-2\rangle=\langle -6,\ 3,\ 2\rangle$",
        "## ثانيًا: المقدار",
        MAG,
        r"$|\overrightarrow{AB}|=\sqrt{(-6)^2+3^2+2^2}=\sqrt{36+9+4}=\sqrt{49}=7$",
    ],
    wrong={
        1: r"$49$ هو مربّع المقدار؛ يجب أخذ الجذر.",
        2: r"تحقّقي من الحساب: $36+9+4=49$ وجذره $7$ لا $5$.",
        3: r"نُسيت المركبة الأولى $-6$: $\sqrt{9+4}=\sqrt{13}$.",
    },
),
'u6e1q2': E(
    idea=r"$\overrightarrow{AB}=\overrightarrow{BD}$ يعني أن $B$ منتصف $\overline{AD}$ ← نكتب المعادلة بمتجهات الموقع ونعزل $D$.",
    steps=[
        "## أولًا: ترجمة الشرط",
        VEC,
        r"$\overrightarrow{AB}=B-A$ و $\overrightarrow{BD}=D-B$ ، والشرط: $B-A=D-B$",
        r"نعزل $D$: $D=2B-A$",
        "## ثانيًا: الحساب",
        r"$2B=\langle 8,\ -2,\ 4\rangle$",
        r"$D=\langle 8-1,\ -2-2,\ 4-(-3)\rangle=\langle 7,\ -4,\ 7\rangle$",
        "## تحقّق",
        r"منتصف $A(1,2,-3)$ و $D(7,-4,7)$ هو $(4,-1,2)$ ، وهو $B$ ✔",
    ],
    wrong={
        1: r"الإشارات معكوسة؛ هذا $A-2B$ لا $2B-A$.",
        2: r"هذا $\overrightarrow{AB}=\langle 3,-3,5\rangle$ نفسه، لا متجه موقع $D$.",
        3: r"هذا منتصف $\overline{AB}$ ، بينما المطلوب نقطة تجعل $B$ هي المنتصف.",
    },
),
'u6e1q3': E(
    idea=r"المقدار معطى ← نكتب $\overrightarrow{AC}$ بدلالة $\alpha$ ، نساوي مقداره بـ $\sqrt{30}$ ، ونحلّ.",
    steps=[
        "## أولًا: المتجه",
        r"$\overrightarrow{AC}=C-A=\langle \alpha-1,\ 3-2,\ 2-(-3)\rangle=\langle \alpha-1,\ 1,\ 5\rangle$",
        "## ثانيًا: المعادلة",
        MAG,
        r"$\sqrt{(\alpha-1)^2+1+25}=\sqrt{30}$ ، نربّع الطرفين: $(\alpha-1)^2+26=30$",
        r"$(\alpha-1)^2=4 \Rightarrow \alpha-1=\pm2$",
        r"$\alpha=3$ أو $\alpha=-1$",
        "## ثالثًا: الشرط",
        r"المعطى $\alpha>0$ ، إذن $\alpha=3$",
    ],
    wrong={
        1: r"$-1$ حلّ للمعادلة لكنه مرفوض لأن $\alpha>0$.",
        2: r"تحقّقي: $\alpha=5$ يعطي $16+1+25=42\neq30$.",
        3: r"تحقّقي: $\alpha=1$ يعطي $0+1+25=26\neq30$.",
    },
),
'u6e1q4': E(
    idea=UNIT + r".",
    steps=[
        "## أولًا: المقدار",
        r"$|\vec{\mathbf{v}}|=\sqrt{6^2+(-2)^2+3^2}=\sqrt{36+4+9}=\sqrt{49}=7$",
        "## ثانيًا: القسمة",
        r"$\dfrac{\vec{\mathbf{v}}}{7}=\left\langle \frac67,\ -\frac27,\ \frac37\right\rangle$",
        "## تحقّق",
        r"$\sqrt{\frac{36}{49}+\frac{4}{49}+\frac{9}{49}}=\sqrt{\frac{49}{49}}=1$ ✔",
    ],
    wrong={
        1: r"نقسم على المقدار $7$ لا على مربّعه $49$.",
        2: r"هذا في عكس اتجاه $\vec{\mathbf{v}}$ (كل الإشارات معكوسة).",
        3: r"المقدار ليس مجموع القيم المطلقة للمركبات ($6+2+3=11$) ؛ $|\vec{\mathbf{v}}|=7$.",
    },
),
'u6e1q5': E(
    idea=r"نصل إلى $M$ من $O$ عبر $A$: $\overrightarrow{OM}=\overrightarrow{OA}+\overrightarrow{AM}$ ، و $\overrightarrow{AM}$ جزء من $\overrightarrow{AB}$ حسب النسبة.",
    steps=[
        "## أولًا: المتجه AB",
        r"$\overrightarrow{AB}=\overrightarrow{AO}+\overrightarrow{OB}=-\overrightarrow{OA}+\overrightarrow{OB}=3\vec{\mathbf{b}}-2\vec{\mathbf{a}}$",
        "## ثانيًا: الجزء AM",
        r"$AM:MB=1:2$ يعني أن $\overline{AB}$ مقسوم إلى $1+2=3$ أجزاء، و $AM$ جزء واحد منها",
        r"$\overrightarrow{AM}=\frac13\overrightarrow{AB}=\frac13(3\vec{\mathbf{b}}-2\vec{\mathbf{a}})=\vec{\mathbf{b}}-\frac23\vec{\mathbf{a}}$",
        "## ثالثًا: الجمع",
        r"$\overrightarrow{OM}=\overrightarrow{OA}+\overrightarrow{AM}=2\vec{\mathbf{a}}+\vec{\mathbf{b}}-\frac23\vec{\mathbf{a}}$",
        r"$2-\frac23=\frac43$ ، إذن $\overrightarrow{OM}=\frac43\vec{\mathbf{a}}+\vec{\mathbf{b}}$",
    ],
    wrong={
        1: r"هذا ناتج أخذ $\frac23\overrightarrow{AB}$؛ لكن $AM$ ثلث $AB$ لا ثلثاه ($M$ أقرب إلى $A$).",
        2: r"نُسي أن $\frac13\overrightarrow{AB}$ فيه $-\frac23\vec{\mathbf{a}}$ أيضًا.",
        3: r"هذا متجه موقع منتصف $\overline{AB}$ ، والنسبة هنا $1:2$ لا $1:1$.",
    },
),
'u6e1q6': E(
    idea=LINE + r".",
    steps=[
        "## أولًا: النقطة",
        r"متجه موقع $A$: $4\hat{i}+\hat{j}-2\hat{k}=\langle 4,\ 1,\ -2\rangle$ (معامل $\hat i$ هو $x$ ، و $\hat j$ هو $y$ ، و $\hat k$ هو $z$)",
        "## ثانيًا: الاتجاه",
        r"$\vec{\mathbf{v}}=2\hat{i}-3\hat{j}+\hat{k}=\langle 2,\ -3,\ 1\rangle$",
        "## ثالثًا: المعادلة",
        r"$\vec{\mathbf{r}}=\langle 4,1,-2\rangle+t\langle 2,-3,1\rangle$",
    ],
    wrong={
        1: r"النقطة ومتجه الاتجاه مبدّلان: الثابت هو النقطة، والمضروب في $t$ هو الاتجاه.",
        2: r"ترتيب مركبات الاتجاه تغيّر: $2\hat i-3\hat j+\hat k$ هو $\langle 2,-3,1\rangle$.",
        3: r"ترتيب مركبات النقطة تغيّر: $4\hat i+\hat j$ يعني $x=4$ و $y=1$.",
    },
),
'u6e1q7': E(
    idea=PT + r".",
    steps=[
        "## أولًا: الإحداثيات العامة",
        r"$x=1+2t$ ، $y=-2+t$ ، $z=3-t$",
        "## ثانيًا: إيجاد t",
        r"$z=-1$: $3-t=-1 \Rightarrow t=4$",
        "## ثالثًا: باقي الإحداثيات",
        r"$x=1+2(4)=9$ ، $y=-2+4=2$",
        r"النقطة $(9,\ 2,\ -1)$",
    ],
    wrong={
        1: r"تنتج من $t=-4$؛ لكن من $3-t=-1$ تكون $t=4$ ، وعندها $z=7\neq-1$ في هذا البديل.",
        2: r"هذه النقطة عند $t=3$ ، وإحداثيها $z=0$ لا $-1$.",
        3: r"$y=-2+4=+2$.",
    },
),
'u6e1q8': E(
    idea=REL + r".",
    steps=[
        "## أولًا: متجها الاتجاه",
        r"$\langle -4,2,-6\rangle=-2\langle 2,-1,3\rangle$ ، فهما متوازيان",
        r"إذن المستقيمان إمّا متوازيان أو منطبقان",
        "## ثانيًا: هل توجد نقطة مشتركة؟",
        r"نختبر النقطة $(3,0,4)$ من $\vec{\mathbf{r}}_2$ على $\vec{\mathbf{r}}_1$: $1+2t=3 \Rightarrow t=1$",
        r"عند $t=1$: $y=1-1=0$ ✔ لكن $z=0+3=3\neq4$ ✗",
        r"النقطة ليست على $\vec{\mathbf{r}}_1$ ، فلا انطباق",
        "## النتيجة",
        r"المستقيمان متوازيان",
    ],
    wrong={
        1: r"المتقاطعان اتجاهاهما غير متوازيين، وهنا الاتجاهان متوازيان.",
        2: r"المتخالفان اتجاهاهما غير متوازيين.",
        3: r"المنطبقان يشتركان في كل النقاط، لكن $(3,0,4)$ ليست على $\vec{\mathbf{r}}_1$.",
    },
    tip=REL4,
),
'u6e1q9': E(
    idea=r"نقطة التقاطع تحقّق المعادلتين ← نساوي الإحداثيات الثلاثة، نحلّ معادلتين، ونتحقّق في الثالثة.",
    steps=[
        "## أولًا: المعادلات",
        r"$x$: $2+t=7+3s$ ، $y$: $1+2t=4-s$ ، $z$: $-t=2s$",
        "## ثانيًا: الحلّ",
        r"من معادلة $z$: $t=-2s$",
        r"نعوّض في معادلة $x$: $2-2s=7+3s \Rightarrow -5s=5 \Rightarrow s=-1$ ، و $t=2$",
        "## ثالثًا: التحقّق في المعادلة الباقية",
        r"معادلة $y$: $1+2(2)=5$ و $4-(-1)=5$ ✔",
        "## رابعًا: النقطة",
        r"$\langle 2,1,0\rangle+2\langle 1,2,-1\rangle=\langle 4,\ 5,\ -2\rangle$ ، أي $(4,\,5,\,-2)$",
    ],
    wrong={
        1: r"هذه نقطة على $\vec{\mathbf{r}}_2$ ($s=0$) لكنها ليست على $\vec{\mathbf{r}}_1$.",
        2: r"هذه نقطة على $\vec{\mathbf{r}}_1$ ($t=1$) لكنها ليست على $\vec{\mathbf{r}}_2$.",
        3: r"هذه نقطة على $\vec{\mathbf{r}}_2$ ($s=-2$) لكنها ليست على $\vec{\mathbf{r}}_1$.",
    },
),
'u6e1q10': E(
    idea=r"التعامد ⟺ الضرب القياسي صفر.",
    steps=[
        DOT,
        r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=3(1)+(-1)(4)+2(k)=3-4+2k=-1+2k$",
        r"$-1+2k=0 \Rightarrow 2k=1 \Rightarrow k=\frac12$",
    ],
    wrong={
        1: r"خطأ إشارة: $2k=1$.",
        2: r"من $2k=1$ تكون $k=\frac12$ لا $2$.",
        3: r"$(-1)(4)=-4$ لا $+4$: تحقّقي $3+4+2\left(\frac72\right)\neq0$.",
    },
),
'u6e1q11': E(
    idea=r"نحسب المتجهين، ثم ضربهما القياسي؛ فإن كان صفرًا فالزاوية قائمة.",
    steps=[
        "## أولًا: المتجهان",
        r"$\vec{\mathbf{a}}-\vec{\mathbf{b}}=\langle 2-1,\ 1+1,\ -1-2\rangle=\langle 1,\ 2,\ -3\rangle$",
        r"$\vec{\mathbf{a}}+\vec{\mathbf{b}}=\langle 3,\ 0,\ 1\rangle$",
        "## ثانيًا: الضرب القياسي",
        r"$1(3)+2(0)+(-3)(1)=3+0-3=0$",
        "## ثالثًا: الزاوية",
        r"$\cos\theta=0 \Rightarrow \theta=\frac{\pi}{2}$",
    ],
    quick=r"$(\vec{\mathbf{a}}-\vec{\mathbf{b}})\cdot(\vec{\mathbf{a}}+\vec{\mathbf{b}})=|\vec{\mathbf{a}}|^2-|\vec{\mathbf{b}}|^2=6-6=0$ مباشرة.",
    wrong={
        1: r"$\cos\frac{\pi}{3}=\frac12$ ، لكن الضرب القياسي صفر فجيب التمام صفر.",
        2: r"$\cos\frac{\pi}{4}\neq0$؛ الضرب القياسي صفر.",
        3: r"$\cos\frac{\pi}{6}\neq0$؛ الضرب القياسي صفر.",
    },
),
'u6e1q12': E(
    idea=r"المتجهان يبدآن من الرأس $B$ ← نحسب الزاوية بينهما بالضرب القياسي، فإن كانت قائمة فالمساحة نصف حاصل ضرب الضلعين.",
    steps=[
        "## أولًا: الزاوية B",
        r"$\overrightarrow{BA}\cdot\overrightarrow{BC}=2(4)+(-1)(4)+2(-2)=8-4-4=0$",
        r"الضرب القياسي صفر، فالزاوية $B$ قائمة",
        "## ثانيًا: طولا الضلعين",
        r"$|\overrightarrow{BA}|=\sqrt{4+1+4}=3$",
        r"$|\overrightarrow{BC}|=\sqrt{16+16+4}=\sqrt{36}=6$",
        "## ثالثًا: المساحة",
        r"مساحة المثلث القائم يساوي $\frac12\times$ الضلعين القائمين يساوي $\frac12(3)(6)=9$",
    ],
    wrong={
        1: r"نُسي العامل $\frac12$؛ $18$ مساحة المستطيل.",
        2: r"$6$ طول أحد الضلعين، لا المساحة.",
        3: r"تحقّقي: $\frac12\times3\times6=9$.",
    },
),
# ============================================================ الاختبار الثاني
'u6e2q1': E(
    idea=r"الضرب في عدد ثم الطرح يتمّان مركبة مركبة.",
    steps=[
        "## الضرب في عدد",
        r"$3\vec{\mathbf{v}}=\langle 3,\ -6,\ 12\rangle$",
        r"$2\vec{\mathbf{w}}=\langle 6,\ 0,\ -2\rangle$",
        "## الطرح مركبة مركبة",
        r"الأولى: $3-6=-3$ ، الثانية: $-6-0=-6$ ، الثالثة: $12-(-2)=14$",
        r"$3\vec{\mathbf{v}}-2\vec{\mathbf{w}}=\langle -3,\ -6,\ 14\rangle$",
    ],
    wrong={
        1: r"المركبة الثالثة: $12-(-2)=12+2=14$ لا $10$.",
        2: r"المركبة الأولى: $3-6=-3$ ، والثالثة $14$.",
        3: r"المركبة الثانية: $-6-0=-6$.",
    },
),
'u6e2q2': E(
    idea=PAR + r". نجد $k$ من المركبة المعلومة في المتجهين، ثم نستعمله في المركبتين الأخريين.",
    steps=[
        "## أولًا: إيجاد k",
        r"$\vec{\mathbf{u}}=k\vec{\mathbf{v}}$: $\langle a,\ 6,\ -3\rangle=\langle 2k,\ -4k,\ bk\rangle$",
        r"المركبة الثانية معلومة في الطرفين: $6=-4k \Rightarrow k=-\frac32$",
        "## ثانيًا: a و b",
        r"الأولى: $a=2k=2\left(-\frac32\right)=-3$",
        r"الثالثة: $-3=bk=-\frac32b \Rightarrow b=2$",
        "## ثالثًا: المجموع",
        r"$a+b=-3+2=-1$",
    ],
    wrong={
        1: r"تنتج من أخذ $k=+\frac32$ (فتصبح $a=3$ و $b=-2$)؛ لكن $6=k(-4)$ يعطي $k$ سالبًا.",
        2: r"$b=+2$: من $-3=-\frac32b$.",
        3: r"$a=-\frac32\times2=-3$ سالب، فـ $a+b=-1$.",
    },
),
'u6e2q3': E(
    idea=COLL + r".",
    steps=[
        "## أولًا: النسبة من المركبتين المعلومتين",
        r"$\overrightarrow{AB}=k\overrightarrow{AC}$: الأولى $2=3k \Rightarrow k=\frac23$ ، والثالثة $4=6k \Rightarrow k=\frac23$ ✔",
        "## ثانيًا: المركبة الثانية",
        r"$a-1=k\times6=\frac23\times6=4$",
        r"$a=5$",
    ],
    wrong={
        1: r"$4$ هي $a-1$ ، و $a=5$.",
        2: r"تحقّقي: $a=3$ يعطي $\langle 2,2,4\rangle$ ، وليس مضاعفًا لـ $\langle 3,6,6\rangle$.",
        3: r"تحقّقي: $a=9$ يعطي $\langle 2,8,4\rangle$ ، وليس مضاعفًا لـ $\langle 3,6,6\rangle$.",
    },
),
'u6e2q4': E(
    idea=r"نقرأ إحداثيات الرأسين من متوازي المستطيلات (أبعاده من $U$)، ثم نحسب المنتصف.",
    steps=[
        "## أولًا: الأبعاد",
        r"$U(4,6,3)$ هو الرأس المقابل للأصل، فالأبعاد: الطول على $x$ يساوي $4$ ، وعلى $y$ يساوي $6$ ، والارتفاع $3$",
        "## ثانيًا: الرأسان",
        r"$P$ على المحور $x$: $P(4,\,0,\,0)$",
        r"$V$ فوق $R(0,6,0)$ بارتفاع $3$: $V(0,\,6,\,3)$",
        "## ثالثًا: المنتصف",
        MID,
        r"$\left(\dfrac{4+0}{2},\ \dfrac{0+6}{2},\ \dfrac{0+3}{2}\right)=\left(2,\ 3,\ \dfrac32\right)$",
    ],
    wrong={
        1: r"المركبة الثالثة: $\frac{0+3}{2}=\frac32$؛ نُسيت القسمة على $2$.",
        2: r"هذه إحداثيات $U$ نفسه.",
        3: r"المركبة الثانية: $V$ لها $y=6$ ، فالمنتصف $y=3$.",
    },
),
'u6e2q5': E(
    idea=r"نكتب المقدار بدلالة $c$ ونساويه بـ $6$ ، ثم نحلّ (توجد قيمتان).",
    steps=[
        MAG,
        r"$\sqrt{c^2+(-2)^2+4^2}=6 \Rightarrow \sqrt{c^2+20}=6$",
        r"نربّع: $c^2+20=36 \Rightarrow c^2=16$",
        r"$c=\pm4$",
        r"تحقّق: $16+4+16=36$ وجذرها $6$ ✔",
    ],
    wrong={
        1: r"$c=-4$ أيضًا يحقّق: $16+4+16=36$.",
        2: r"تنتج من $c^2=36+20$؛ الصحيح $c^2=36-20$.",
        3: r"$16$ هي قيمة $c^2$ لا $c$.",
    },
),
'u6e2q6': E(
    idea=LINE + r". متجه الاتجاه هو المتجه بين النقطتين.",
    steps=[
        "## أولًا: الاتجاه",
        VEC,
        r"$\overrightarrow{AB}=\langle 5-3,\ 2-(-1),\ -2-2\rangle=\langle 2,\ 3,\ -4\rangle$",
        "## ثانيًا: النقطة",
        r"نأخذ $A(3,-1,2)$",
        "## ثالثًا: المعادلة",
        r"$\vec{\mathbf{r}}=\langle 3,-1,2\rangle+t\langle 2,3,-4\rangle$",
        r"تحقّق: عند $t=1$ نحصل على $(5,2,-2)$ وهي $B$ ✔",
    ],
    wrong={
        1: r"متجه الاتجاه هنا متجه موقع $B$ ، وليس متجهًا بين النقطتين.",
        2: r"النقطة ومتجه الاتجاه مبدّلان.",
        3: r"متجه الاتجاه هنا $A+B$ لا $B-A$.",
    },
),
'u6e2q7': E(
    idea=r"المستوى $yz$ هو المستوى الذي فيه $x=0$ ← نساوي الإحداثي $x$ للمستقيم بالصفر.",
    steps=[
        r"الإحداثي $x$ لأيّ نقطة على المستقيم: $6+3t$",
        r"على المستوى $yz$: $6+3t=0 \Rightarrow 3t=-6 \Rightarrow t=-2$",
        r"النقطة: $\langle 6-6,\ -2-2,\ 5+4\rangle=(0,\,-4,\,9)$ وإحداثيها $x$ صفر ✔",
    ],
    wrong={
        1: r"خطأ إشارة: $3t=-6$.",
        2: r"هذه قيمة $t$ عند $z=0$ ، أي التقاطع مع المستوى $xy$.",
        3: r"تحقّقي: $t=-3$ يعطي $x=-3\neq0$.",
    },
),
'u6e2q8': E(
    idea=REL + r".",
    steps=[
        "## أولًا: الاتجاهان",
        r"$\langle 1,1,1\rangle$ و $\langle 2,-1,1\rangle$: النسب $\frac21\neq\frac{-1}{1}$ ، فهما غير متوازيين",
        r"إذن المستقيمان متقاطعان أو متخالفان",
        "## ثانيًا: نساوي الإحداثيات",
        r"$x$: $1+t=2+2s$ ، $y$: $t=3-s$ ، $z$: $2+t=1+s$",
        r"من $y$ و $z$: نعوّض $t=3-s$ في $z$: $2+3-s=1+s \Rightarrow 4=2s \Rightarrow s=2$ ، و $t=1$",
        "## ثالثًا: التحقّق في المعادلة الباقية",
        r"معادلة $x$: $1+1=2$ ، و $2+2(2)=6$ ، و $2\neq6$ ✗",
        "## النتيجة",
        r"لا توجد نقطة مشتركة والاتجاهان غير متوازيين، فالمستقيمان متخالفان",
    ],
    wrong={
        1: r"متجها الاتجاه غير متوازيين.",
        2: r"قيم $t$ و $s$ لا تحقّق المعادلة الثالثة، فلا نقطة مشتركة.",
        3: r"المنطبقان متوازيان، وهذان غير متوازيين.",
    },
    tip=REL4,
),
'u6e2q9': E(
    idea=FOOT + r".",
    steps=[
        "## أولًا: نقطة عامة على المستقيم",
        r"$Q=(1+t,\ 2t,\ 2-t)$",
        "## ثانيًا: المتجه PQ",
        r"$\overrightarrow{PQ}=Q-P=\langle t-3,\ 2t-5,\ -t-1\rangle$",
        "## ثالثًا: شرط التعامد",
        r"$\overrightarrow{PQ}\cdot\langle 1,2,-1\rangle=(t-3)+2(2t-5)-(-t-1)=0$",
        r"$t-3+4t-10+t+1=0 \Rightarrow 6t-12=0 \Rightarrow t=2$",
        "## رابعًا: المسقط",
        r"$Q=(1+2,\ 4,\ 2-2)=(3,\ 4,\ 0)$",
    ],
    wrong={
        1: r"نقطة على المستقيم ($t=0$) لكن $\overrightarrow{PQ}\cdot\langle 1,2,-1\rangle=-12\neq0$.",
        2: r"نقطة على المستقيم ($t=1$) لكن الضرب القياسي $-6\neq0$.",
        3: r"نقطة على المستقيم ($t=4$) لكن الضرب القياسي $12\neq0$.",
    },
),
'u6e2q10': E(
    idea=r"المعطى المقداران والزاوية ← نستعمل الصيغة الهندسية للضرب القياسي.",
    steps=[
        DOT,
        r"$\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=|\vec{\mathbf{a}}||\vec{\mathbf{b}}|\cos\theta=4\times5\times\cos120^\circ$",
        r"$120^\circ$ في الربع الثاني، وزاوية الإسناد $60^\circ$ ، فـ $\cos120^\circ=-\cos60^\circ=-\frac12$",
        r"$20\times\left(-\frac12\right)=-10$",
    ],
    wrong={
        1: r"$\cos120^\circ$ سالب (الربع الثاني).",
        2: r"هذا باستعمال $\cos150^\circ=-\frac{\sqrt3}{2}$؛ الزاوية $120^\circ$.",
        3: r"نُسي الضرب في $\cos\theta$.",
    },
),
'u6e2q11': E(
    idea=r"الصيغة الهندسية للضرب القياسي فيها مجهول واحد $|\vec{\mathbf{b}}|$.",
    steps=[
        r"$\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=|\vec{\mathbf{a}}||\vec{\mathbf{b}}|\cos\theta$",
        r"$12=6\times|\vec{\mathbf{b}}|\times\cos60^\circ=6\times|\vec{\mathbf{b}}|\times\frac12=3|\vec{\mathbf{b}}|$",
        r"$|\vec{\mathbf{b}}|=\dfrac{12}{3}=4$",
    ],
    wrong={
        1: r"نُسي العامل $\cos60^\circ=\frac12$: $\frac{12}{6}=2$.",
        2: r"تحقّقي: $6\times8\times\frac12=24\neq12$.",
        3: r"هذا باستعمال $\cos30^\circ=\frac{\sqrt3}{2}$؛ الزاوية $60^\circ$.",
    },
),
'u6e2q12': E(
    idea=r"التعامد يعطي معادلة واحدة فيها $c$ و $d$ ، ونرتّبها على صورة $c-2d$ دون حاجة لإيجاد كلٍّ منهما.",
    steps=[
        DOT,
        r"$\vec{\mathbf{v}}=\langle 3,c,2\rangle$ ، $\vec{\mathbf{w}}=\langle 2,-1,d\rangle$",
        r"$\vec{\mathbf{v}}\cdot\vec{\mathbf{w}}=3(2)+c(-1)+2(d)=6-c+2d$",
        r"التعامد: $6-c+2d=0$",
        r"ننقل: $6=c-2d$ ، إذن $c-2d=6$",
    ],
    wrong={
        1: r"عند نقل $-c+2d$ يصبح $c-2d=6$ (موجب).",
        2: r"تحقّقي: الحدّ الثابت $3\times2=6$.",
        3: r"تحقّقي: الحدّ الثابت $6$ ، والعلاقة $c-2d=6$.",
    },
),
# ============================================================ الاختبار الثالث
'u6e3q1': E(
    idea=MID + r".",
    steps=[
        r"$x$: $\dfrac{-2+4}{2}=\dfrac22=1$",
        r"$y$: $\dfrac{5+(-1)}{2}=\dfrac42=2$",
        r"$z$: $\dfrac{1+7}{2}=\dfrac82=4$",
        r"المنتصف $(1,\ 2,\ 4)$",
    ],
    wrong={
        1: r"نُسيت القسمة على $2$ (هذا مجموع الإحداثيات).",
        2: r"هذا $\frac{B-A}{2}$ (نصف المتجه) لا المنتصف.",
        3: r"هذا $\frac{A-B}{2}$.",
    },
),
'u6e3q2': E(
    idea=VEC + r". انتبهي للترتيب: $\overrightarrow{BA}$ يبدأ من $B$.",
    steps=[
        r"البداية $B(-1,4,2)$ والنهاية $A(3,-2,5)$",
        r"$\overrightarrow{BA}=A-B=\langle 3-(-1),\ -2-4,\ 5-2\rangle$",
        r"$\overrightarrow{BA}=\langle 4,\ -6,\ 3\rangle$",
    ],
    wrong={
        1: r"هذا $\overrightarrow{AB}=B-A$؛ الترتيب معكوس.",
        2: r"هذا $A+B$؛ المتجه بين نقطتين فرق لا مجموع.",
        3: r"هذا $-(A+B)$.",
    },
),
'u6e3q3': E(
    idea=r"في متوازي الأضلاع $ABCD$ الضلعان المتقابلان متساويان ومتوازيان: $\overrightarrow{AD}=\overrightarrow{BC}$.",
    steps=[
        "## أولًا: المتجه BC",
        r"$\overrightarrow{BC}=C-B=\langle 4-5,\ 4-1,\ 2-0\rangle=\langle -1,\ 3,\ 2\rangle$",
        "## ثانيًا: الرأس D",
        r"$\overrightarrow{AD}=\overrightarrow{BC} \Rightarrow D=A+\overrightarrow{BC}$",
        r"$D=(2-1,\ -1+3,\ 3+2)=(1,\ 2,\ 5)$",
        "## تحقّق",
        r"منتصف $\overline{AC}$: $(3,\frac32,\frac52)$ ، ومنتصف $\overline{BD}$: $(3,\frac32,\frac52)$ ✔ (القطران ينصّف كلٌّ منهما الآخر)",
    ],
    wrong={
        1: r"هذا $B+C-A$ ، أي الرأس المقابل لـ $A$؛ لكن في $ABCD$ الرأس المقابل لـ $A$ هو $C$.",
        2: r"هذا $A+B-C$ ، ترتيب آخر للرؤوس.",
        3: r"المركبة الثالثة: $3+2=5$ لا $-5$.",
    },
),
'u6e3q4': E(
    idea=r"نكتب متجهَي موقع $M$ و $P$ من $O$ ، ثم $\overrightarrow{PM}=\overrightarrow{OM}-\overrightarrow{OP}$.",
    steps=[
        "## أولًا: متجه موقع M",
        r"في متوازي الأضلاع $\overrightarrow{CB}=\overrightarrow{OA}=2\vec{\mathbf{a}}$",
        r"$\overrightarrow{OM}=\overrightarrow{OC}+\frac12\overrightarrow{CB}=3\vec{\mathbf{c}}+\vec{\mathbf{a}}$",
        "## ثانيًا: متجه موقع P",
        r"$\overrightarrow{OB}=\overrightarrow{OA}+\overrightarrow{AB}=2\vec{\mathbf{a}}+3\vec{\mathbf{c}}$",
        r"$OP:PB=2:1$ ، فـ $\overrightarrow{OP}=\frac23\overrightarrow{OB}=\frac43\vec{\mathbf{a}}+2\vec{\mathbf{c}}$",
        "## ثالثًا: الطرح",
        r"$\overrightarrow{PM}=(\vec{\mathbf{a}}+3\vec{\mathbf{c}})-\left(\frac43\vec{\mathbf{a}}+2\vec{\mathbf{c}}\right)$",
        r"معامل $\vec{\mathbf{a}}$: $1-\frac43=-\frac13$ ، ومعامل $\vec{\mathbf{c}}$: $3-2=1$",
        r"$\overrightarrow{PM}=-\frac13\vec{\mathbf{a}}+\vec{\mathbf{c}}$",
    ],
    wrong={
        1: r"هذا $\overrightarrow{MP}$ (الاتجاه معكوس).",
        2: r"هذا $\overrightarrow{OM}+\overrightarrow{OP}$؛ المتجه بين نقطتين فرق لا مجموع.",
        3: r"معامل $\vec{\mathbf{c}}$: $3-2=1$ لا $3+2$.",
    },
),
'u6e3q5': E(
    idea=COLL + r".",
    steps=[
        "## أولًا: المتجهان",
        r"$\overrightarrow{PQ}=\langle 3-1,\ h-2,\ 7-3\rangle=\langle 2,\ h-2,\ 4\rangle$",
        r"$\overrightarrow{PR}=\langle 4-1,\ 8-2,\ k-3\rangle=\langle 3,\ 6,\ k-3\rangle$",
        "## ثانيًا: النسبة",
        r"من المركبتين الأوليين المعلومتين: $2=\frac23\times3$ ، فـ $\overrightarrow{PQ}=\frac23\overrightarrow{PR}$",
        "## ثالثًا: المجهولان",
        r"الثانية: $h-2=\frac23\times6=4 \Rightarrow h=6$",
        r"الثالثة: $4=\frac23(k-3) \Rightarrow k-3=6 \Rightarrow k=9$",
        r"$h+k=6+9=15$",
    ],
    wrong={
        1: r"تحقّقي: $h=6$ و $k=9$.",
        2: r"$9$ هي $k$ وحدها.",
        3: r"تحقّقي: من $4=\frac23(k-3)$ تكون $k=9$ لا $12$.",
    },
),
'u6e3q6': E(
    idea=PT + r".",
    steps=[
        r"الإحداثيات العامة: $x=-1+2t$ ، $y=4-t$ ، $z=2+3t$",
        r"$y=1$: $4-t=1 \Rightarrow t=3$",
        r"$x=-1+2(3)=5$ ، $z=2+3(3)=11$",
        r"النقطة $(5,\ 1,\ 11)$",
    ],
    wrong={
        1: r"تنتج من $t=-3$؛ لكن من $4-t=1$ تكون $t=3$.",
        2: r"$z=2+3(3)=11$ لا $-7$.",
        3: r"هذه $x$ و $z$ عند $t=1$ ، وعندها $y=3\neq1$.",
    },
),
'u6e3q7': E(
    idea=r"المستقيمان المتوازيان لهما متجه الاتجاه نفسه ← نأخذ اتجاه المستقيم المعطى والنقطة الجديدة.",
    steps=[
        LINE,
        r"الاتجاه من المستقيم المعطى: $\langle 4,-2,1\rangle$ (المضروب في $t$)",
        r"النقطة المعطاة: $(1,-1,2)$",
        r"$\vec{\mathbf{r}}=\langle 1,-1,2\rangle+t\langle 4,-2,1\rangle$",
    ],
    wrong={
        1: r"هذا يمرّ بنقطة المستقيم المعطى، واتجاهه هو النقطة الجديدة؛ خطآن.",
        2: r"$\langle 0,3,1\rangle$ نقطة على المستقيم المعطى، لا اتجاهه.",
        3: r"النقطة والاتجاه مبدّلان.",
    },
),
'u6e3q8': E(
    idea=REL + r".",
    steps=[
        "## أولًا: الاتجاهان",
        r"$\langle -2,-6,4\rangle=-2\langle 1,3,-2\rangle$ ، فهما متوازيان: متوازيان أو منطبقان",
        "## ثانيًا: نختبر نقطة",
        r"النقطة $(4,5,-4)$ من $\vec{\mathbf{r}}_2$: هل تقع على $\vec{\mathbf{r}}_1$؟",
        r"$2+t=4 \Rightarrow t=2$ ، وعندها $y=-1+6=5$ ✔ و $z=0-4=-4$ ✔",
        "## النتيجة",
        r"النقطة مشتركة والاتجاهان متوازيان، فالمستقيمان منطبقان",
    ],
    wrong={
        1: r"المتوازيان لا يشتركان في أيّ نقطة، وهنا $(4,5,-4)$ مشتركة.",
        2: r"المتقاطعان اتجاهاهما غير متوازيين.",
        3: r"المتخالفان اتجاهاهما غير متوازيين.",
    },
    tip=REL4,
),
'u6e3q9': E(
    idea=r"نساوي الإحداثيات الثلاثة، نحلّ معادلتين، ونتحقّق في الثالثة، ثم نعوّض لإيجاد النقطة.",
    steps=[
        "## أولًا: المعادلات",
        r"$x$: $1+2t=-3+s$ ، $y$: $-t=-3+2s$ ، $z$: $-2+3t=-7+s$",
        "## ثانيًا: الحلّ",
        r"نطرح معادلة $x$ من معادلة $z$ (لحذف $s$): $(-2+3t)-(1+2t)=(-7+s)-(-3+s)$",
        r"$-3+t=-4 \Rightarrow t=-1$ ، ومن معادلة $x$: $1-2=-3+s \Rightarrow s=2$",
        "## ثالثًا: التحقّق",
        r"معادلة $y$: $-(-1)=1$ و $-3+2(2)=1$ ✔",
        "## رابعًا: النقطة",
        r"$\langle 1,0,-2\rangle+(-1)\langle 2,-1,3\rangle=(-1,\ 1,\ -5)$",
    ],
    wrong={
        1: r"نقطة على $\vec{\mathbf{r}}_1$ عند $t=1$ ، لكنها ليست على $\vec{\mathbf{r}}_2$.",
        2: r"نقطة البداية على $\vec{\mathbf{r}}_2$ ($s=0$) ، لكنها ليست على $\vec{\mathbf{r}}_1$.",
        3: r"نقطة البداية على $\vec{\mathbf{r}}_1$ ($t=0$) ، لكنها ليست على $\vec{\mathbf{r}}_2$.",
    },
),
'u6e3q10': E(
    idea=DOT,
    steps=[
        r"نضرب المركبات المتناظرة ونجمع:",
        r"$2(4)=8$ ، $(-3)(1)=-3$ ، $1(-2)=-2$",
        r"$8-3-2=3$",
    ],
    wrong={
        1: r"خطأ إشارة؛ $8-3-2=+3$.",
        2: r"$(-3)(1)=-3$ لا $+3$.",
        3: r"$1\times(-2)=-2$ لا $+2$.",
    },
),
'u6e3q11': E(
    idea=ANGLE + r".",
    steps=[
        "## الضرب القياسي",
        r"$1(0)+(-1)(1)+0(-1)=-1$",
        "## المقداران",
        r"$\sqrt{1+1+0}=\sqrt2$ و $\sqrt{0+1+1}=\sqrt2$",
        "## الزاوية",
        r"$\cos\theta=\dfrac{-1}{\sqrt2\times\sqrt2}=-\dfrac12$",
        r"الزاوية منفرجة (جيب التمام سالب)، و $\cos\frac{2\pi}{3}=-\frac12$ ، إذن $\theta=\frac{2\pi}{3}$",
    ],
    wrong={
        1: r"$\cos\frac{\pi}{3}=+\frac12$؛ أُهملت الإشارة السالبة.",
        2: r"$\cos\frac{\pi}{6}=\frac{\sqrt3}{2}\neq-\frac12$.",
        3: r"$\cos\frac{5\pi}{6}=-\frac{\sqrt3}{2}\neq-\frac12$.",
    },
),
'u6e3q12': E(
    idea=r"نكتب $\overrightarrow{MP}$ بطريق يمرّ بـ $N$ ، مع الانتباه لاتجاه $\overrightarrow{PN}$.",
    steps=[
        "## أولًا: المتجه MP",
        r"$\overrightarrow{MP}=\overrightarrow{MN}+\overrightarrow{NP}$ ، و $\overrightarrow{NP}=-\overrightarrow{PN}=\langle -3,\ 1,\ -2\rangle$",
        r"$\overrightarrow{MP}=\langle 1-3,\ 4+1,\ -2-2\rangle=\langle -2,\ 5,\ -4\rangle$",
        "## ثانيًا: الضرب القياسي",
        r"$\overrightarrow{MN}\cdot\overrightarrow{MP}=1(-2)+4(5)+(-2)(-4)=-2+20+8=26$",
    ],
    wrong={
        1: r"تنتج من $\overrightarrow{MP}=\overrightarrow{MN}+\overrightarrow{PN}$؛ لكن $\overrightarrow{PN}$ في الاتجاه المعاكس لـ $\overrightarrow{NP}$.",
        2: r"هذا $\overrightarrow{MN}\cdot\overrightarrow{PN}$ ، لا مع $\overrightarrow{MP}$.",
        3: r"تحقّقي: $-2+20+8=26$.",
    },
),
}
