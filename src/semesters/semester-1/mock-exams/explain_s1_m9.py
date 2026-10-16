"""Explanations: semester-1 mock paper 9 (m9q1..m9q30). wrong keys = option index as written in s1_papers_6_10.py (0 = correct)."""
from explain_common import E, synth, SYNTH_HOW, REM, FAC, MULT, QUADS, SIGNS
from explain_u3 import DER, PROD, QUOT, CHAIN, IMPL, PARAM, RATES
from explain_u4 import CONJ, DIVC, MOD, ARG, POLAR, CIRCLE, RAY, EQ, PERP

EXPLAIN = {
'm9q1': E(
    idea=r"نجعل الطرف الأيمن صفرًا، ونقسم على $(x+2)$ (العامل المقابل للحلّ $-2$).",
    steps=[
        r"$x^3=2x^2+13x+10 \Rightarrow x^3-2x^2-13x-10=0$",
        SYNTH_HOW + synth(-2, [1, -2, -13, -10]),
        r"$x^2-4x-5=(x-5)(x+1)=0 \Rightarrow x=5,\ x=-1$",
    ],
    quick=r"عوّضي $x=5$: $125$ و $50+65+10=125$ ✔.",
    wrong={
        1: r"إشارتا الحلّين معكوستان.",
        2: r"إشارة الحلّ $5$ خاطئة.",
        3: r"إشارة الحلّ $-1$ خاطئة.",
    },
),
'm9q2': E(
    idea=r"عامل خطي $x$ وعامل مكرّر $(x-1)^2$ ← ثلاثة كسور.",
    steps=[
        MULT + r" $2x^2-x+1=A(x-1)^2+Bx(x-1)+Cx$",
        r"$x=0$: $1=A$",
        r"$x=1$: $2=C$",
        r"معامل $x^2$: $2=A+B \Rightarrow B=1$",
    ],
    wrong={
        1: r"$B$ و $C$ مُبدَّلان: $C$ (فوق المربع) يُحسب عند $x=1$ وهو $2$.",
        2: r"عند $x=0$: $A(0-1)^2=A=1$ ، فـ $A$ موجب.",
        3: r"$A$ بإشارة خاطئة و $B,\ C$ مُبدَّلان.",
    },
),
'm9q3': E(
    idea=r"الباقي يساوي قيمة الاقتران عند صفر المقسوم عليه: $2x+1=0 \Rightarrow x=-\frac12$.",
    steps=[
        REM,
        r"$f\left(-\frac12\right)=4\left(-\frac18\right)+k\cdot\frac14-2\left(-\frac12\right)+1=-\frac12+\frac k4+2$",
        r"$\frac32+\frac k4=3 \Rightarrow \frac k4=\frac32 \Rightarrow k=6$",
    ],
    wrong={
        1: r"عُوّض بـ $x=\frac12$ (إشارة الصفر خاطئة): $\frac12+\frac k4=3$.",
        2: r"عُوّض بـ $x=-2$ بدل $x=-\frac12$.",
        3: r"خطأ إشارة عند نقل الحدود.",
    },
),
'm9q4': E(
    idea=r"نجرّب قواسم الحدّ الثابت $\pm1,\pm2,\pm3,\pm6$ لإيجاد صفر، ثم نقسم ونحلّل.",
    steps=[
        r"$f(-1)=-1+7-6=0$ ، فـ $(x+1)$ عامل",
        SYNTH_HOW + synth(-1, [1, 0, -7, -6]),
        r"$x^2-x-6=(x-3)(x+2)$ ، إذن $f(x)=(x+1)(x+2)(x-3)$",
    ],
    wrong={
        1: r"$f(1)=1-7-6=-12\ne0$ ، فـ $(x-1)$ ليس عاملًا.",
        2: r"$f(2)=8-14-6=-12\ne0$ ، فـ $(x-2)$ ليس عاملًا.",
        3: r"$f(1)\ne0$ ، فـ $(x-1)$ ليس عاملًا.",
    },
    tip=r"تحقّقي من بديل التحليل بنشره ذهنيًّا: الحدّ الثابت $(1)(2)(-3)=-6$ ✔ ومعامل $x^2$ صفر: $1+2-3=0$ ✔.",
),
'm9q5': E(
    idea=r"$\tan\frac{\theta}{2}=\dfrac{\sin\theta}{1+\cos\theta}$ ، فتأتي الإشارة تلقائيًّا من $\sin\theta$.",
    steps=[
        r"في الربع الرابع: $\cos\theta=\frac{12}{13}$",
        r"$\tan\frac{\theta}{2}=\dfrac{-\frac{5}{13}}{1+\frac{12}{13}}=\dfrac{-5}{25}=-\frac15$",
        r"تحقّق: $\frac{3\pi}{4}<\frac{\theta}{2}<\pi$ في الربع الثاني، والظل سالب ✔",
    ],
    wrong={
        1: r"الإشارة خاطئة: $\frac{\theta}{2}$ في الربع الثاني.",
        2: r"استُعملت $\dfrac{1+\cos\theta}{\sin\theta}$ وهي مقلوب الصيغة.",
        3: r"المقلوب والإشارة خاطئان.",
    },
),
'm9q6': E(
    idea=r"نفكّ الحدّين ونطرح، فيُحذف $\cos x$ ويتضاعف $\sin x$.",
    steps=[
        r"$\sin\left(x+\frac{\pi}{4}\right)=\frac{\sqrt2}{2}\sin x+\frac{\sqrt2}{2}\cos x$",
        r"$\cos\left(x+\frac{\pi}{4}\right)=\frac{\sqrt2}{2}\cos x-\frac{\sqrt2}{2}\sin x$",
        r"الفرق: $\frac{\sqrt2}{2}\sin x+\frac{\sqrt2}{2}\sin x=\sqrt2\sin x$",
    ],
    wrong={
        1: r"الحدّان اللذان يُحذفان هما حدّا $\cos x$.",
        2: r"لم يُجمع نصفا $\sin x$: الطرح يقلب إشارة $-\frac{\sqrt2}{2}\sin x$ فيصبح موجبًا.",
        3: r"النسبة والمعامل خطأ.",
    },
),
'm9q7': E(
    idea=r"نكتب $\tan x=\dfrac{\sin x}{\cos x}$ ونوحّد المقامات، ثم $\sin^2x+\cos^2x=1$.",
    steps=[
        r"المقام المشترك $(1-\sin x)\cos x$",
        r"البسط: $\cos^2x-\sin x(1-\sin x)=\cos^2x-\sin x+\sin^2x=1-\sin x$",
        r"$\dfrac{1-\sin x}{(1-\sin x)\cos x}=\dfrac{1}{\cos x}=\sec x$",
    ],
    quick=r"عند $x=0$: $\frac11-0=1=\sec0$ ، بينما $\csc0$ غير معرّف و $2\sec0=2$.",
    wrong={
        1: r"المقام المتبقي $\cos x$ لا $\sin x$.",
        2: r"عند $x=0$ المقدار $1$ لا $2$.",
        3: r"$\csc0$ غير معرّف بينما المقدار معرّف عند $x=0$.",
    },
),
'm9q8': E(
    idea=r"مجموع جيبي تمام ← ضرب: $\cos A+\cos B=2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$.",
    steps=[
        r"$\dfrac{A+B}{2}=\dfrac{6\pi/12}{2}=\frac{\pi}{4}$ ، $\dfrac{A-B}{2}=\dfrac{4\pi/12}{2}=\frac{\pi}{6}$",
        r"$2\cdot\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}=\frac{\sqrt6}{2}$",
    ],
    wrong={
        1: r"أُخذ $\cos\frac{\pi}{6}=\frac12$ (هذه $\cos\frac{\pi}{3}$).",
        2: r"نُسي العامل $2$ في المتطابقة.",
        3: r"أُخذ $\cos\frac{\pi}{4}=\frac12$ بدل $\frac{\sqrt2}{2}$.",
    },
),
'm9q9': E(
    idea=r"$\sec^2x=1+\tan^2x$ يحوّل المعادلة إلى مربع كامل في $\tan x$.",
    steps=[
        r"$1+\tan^2x-2\tan x=0 \Rightarrow (\tan x-1)^2=0 \Rightarrow \tan x=1$",
        SIGNS,
        r"$x=\frac{\pi}{4}$ (الربع الأول) و $x=\pi+\frac{\pi}{4}=\frac{5\pi}{4}$ (الربع الثالث)",
    ],
    wrong={
        1: r"الظل سالب في الربع الثاني؛ الحلّ الثاني في الربع الثالث.",
        2: r"نُسي الحلّ في الربع الثالث.",
        3: r"هذه حلول $\tan x=-1$.",
    },
),
'm9q10': E(
    idea=r"نحلّ لـ $2x$ في الفترة المضاعفة $(2\pi,4\pi)$ ثم نقسم على $2$.",
    steps=[
        r"$\cos2x=-\frac12$ ، وزاوية الإسناد $\frac{\pi}{3}$ ، وجيب التمام سالب في الربعين الثاني والثالث",
        r"$2x=2\pi+\frac{2\pi}{3}=\frac{8\pi}{3}$ ، $2x=2\pi+\frac{4\pi}{3}=\frac{10\pi}{3}$",
        r"$x=\frac{4\pi}{3},\ \frac{5\pi}{3}$",
    ],
    wrong={
        1: r"حُلّت $2x$ في $(0,2\pi)$ بدل $(2\pi,4\pi)$.",
        2: r"هذه قيم $2x$ ولم تُقسم على $2$.",
        3: r"قيم $2x$ في الدورة الأولى دون قسمة.",
    },
),
'm9q11': E(
    idea=r"نبسّط باستعمال قوانين اللوغاريتمات قبل الاشتقاق.",
    steps=[
        r"$\ln\dfrac{\sqrt x}{e^3}=\ln x^{\frac12}-\ln e^3=\frac12\ln x-3$",
        r"$f'(x)=\frac12\cdot\frac1x=\dfrac{1}{2x}$",
    ],
    wrong={
        1: r"مشتقة الثابت $-3$ صفر.",
        2: r"$\left(\ln\sqrt x\right)'=\dfrac{1}{\sqrt x}\cdot\dfrac{1}{2\sqrt x}=\dfrac{1}{2x}$ لا $\dfrac{1}{\sqrt x}$.",
        3: r"الخطآن معًا.",
    },
),
'm9q12': E(
    idea=r"$\left(\tan u\right)'=\sec^2u\cdot u'$ ، و $u'=\pi$.",
    steps=[
        r"$f'(x)=2\pi\sec^2(\pi x)$",
        r"$\sec\frac{\pi}{3}=2 \Rightarrow \sec^2\frac{\pi}{3}=4$ ، إذن $f'\left(\frac13\right)=8\pi$",
    ],
    wrong={
        1: r"نُسي العامل $\pi$ (مشتقة $\pi x$).",
        2: r"لم يُربَّع $\sec$.",
        3: r"نُسي $\pi$ ولم يُربَّع $\sec$.",
    },
),
'm9q13': E(
    idea=r"السكون اللحظي عندما $v(t)=0$ ، و «أوّل مرة بعد الانطلاق» تستثني $t=0$.",
    steps=[
        r"$v(t)=s'(t)=-2\pi\sin(\pi t)$",
        r"$\sin(\pi t)=0 \Rightarrow t=0,\ 1,\ 2,\dots$ ، وأوّل لحظة بعد الانطلاق $t=1$",
        r"$s(1)=4+2\cos\pi=4-2=2\ \text{m}$",
    ],
    wrong={
        1: r"هذا موقع الانطلاق $s(0)$ ، والمطلوب أوّل سكون بعده.",
        2: r"هذا الموقع عند $t=\frac12$ حيث السرعة أكبر ما يمكن لا صفر.",
        3: r"الموقع لا يقلّ عن $4-2=2$.",
    },
),
'm9q14': E(
    idea=r"نشتق مرتين ونجمع؛ حدّا $\cos2x$ يُحذفان.",
    steps=[
        r"$f'(x)=2\cos2x-2\sin2x$",
        r"$f''(x)=-4\sin2x-4\cos2x$",
        r"$f''+2f'=-4\sin2x-4\cos2x+4\cos2x-4\sin2x=-8\sin2x$",
    ],
    wrong={
        1: r"إشارة خاطئة (مشتقة $\cos2x$ هي $-2\sin2x$).",
        2: r"الحدّان اللذان يُحذفان هما حدّا $\cos2x$.",
        3: r"الحدّ الخطأ وبإشارة خاطئة.",
    },
),
'm9q15': E(
    idea=r"$\left(a^u\right)'=a^u\ln a\cdot u'$ ، و $u=\dfrac{1}{t+1}$ فمشتقته $-\dfrac{1}{(t+1)^2}$.",
    steps=[
        r"$N'(t)=600\left(\frac14\right)^{\frac{1}{t+1}}\ln\frac14\cdot\left(-\dfrac{1}{(t+1)^2}\right)$",
        r"عند $t=1$: $\left(\frac14\right)^{\frac12}=\frac12$ ، $\ln\frac14=-\ln4$ ، $-\frac{1}{4}$",
        r"$N'(1)=600\cdot\frac12\cdot(-\ln4)\cdot\left(-\frac14\right)=75\ln4$",
    ],
    wrong={
        1: r"إشارتان سالبتان حاصل ضربهما موجب: $\ln\frac14<0$ و $u'<0$.",
        2: r"مشتقة $\dfrac{1}{t+1}$ هي $-\dfrac{1}{(t+1)^2}$ (نُسي التربيع).",
        3: r"نُسي التربيع والإشارة خاطئة.",
    },
),
'm9q16': E(
    idea=r"$h'(x)=f'(g(x))\cdot g'(x)$ ، فنقرأ $g(1)$ أولًا ثم ميل $f$ عند $g(1)$.",
    steps=[
        r"$g$ من $(0,5)$ إلى $(4,1)$: $g(1)=4$ ، $g'(1)=-1$",
        r"$f$ من $(2,5)$ إلى $(6,3)$: الميل $-\frac12$ ، إذن $f'(4)=-\frac12$",
        r"$h'(1)=\left(-\frac12\right)(-1)=\frac12$",
    ],
    wrong={
        1: r"أُخذ $g'(1)$ موجبًا.",
        2: r"حُسب $f'(1)=2$ بدل $f'(g(1))=f'(4)$.",
        3: r"$f'(1)$ بدل $f'(4)$ وخطأ إشارة.",
    },
),
'm9q17': E(
    idea=r"$\left(\log u\right)'=\dfrac{u'}{u\ln10}$ مع $u=4-x^2$.",
    steps=[
        r"$(2-x)(2+x)=4-x^2$ ، $u'=-2x$",
        r"$f'(x)=\dfrac{-2x}{(4-x^2)\ln10}$ ، وبضرب البسط والمقام في $-1$: $\dfrac{2x}{(x^2-4)\ln10}$",
    ],
    wrong={
        1: r"عند قلب المقام إلى $x^2-4$ يجب قلب إشارة البسط أيضًا.",
        2: r"$\ln10$ في المقام لا في البسط.",
        3: r"$\ln10$ في البسط وإشارة خاطئة.",
    },
),
'm9q18': E(
    idea=r"$\ln(\csc^2x)=2\ln(\csc x)$ ، ثم $\left(\ln u\right)'=\dfrac{u'}{u}$.",
    steps=[
        r"$f'(x)=2\cdot\dfrac{-\csc x\cot x}{\csc x}=-2\cot x$",
        r"$\cot\frac{\pi}{6}=\sqrt3$ ، إذن $f'\left(\frac{\pi}{6}\right)=-2\sqrt3$",
    ],
    wrong={
        1: r"مشتقة $\csc x$ هي $-\csc x\cot x$ (سالبة).",
        2: r"استُعمل $\tan\frac{\pi}{6}=\frac{1}{\sqrt3}$ بدل $\cot\frac{\pi}{6}$.",
        3: r"$\tan$ بدل $\cot$ وخطأ إشارة.",
    },
),
'm9q19': E(
    idea=PARAM,
    steps=[
        r"$\dfrac{dy}{dt}=\sec^2t$ ، $\dfrac{dx}{dt}=\sec t\tan t$",
        r"$\dfrac{dy}{dx}=\dfrac{\sec t}{\tan t}=\dfrac{1}{\cos t}\cdot\dfrac{\cos t}{\sin t}=\csc t$",
    ],
    wrong={
        1: r"القسمة مقلوبة: $\dfrac{dx/dt}{dy/dt}$.",
        2: r"مشتقة $\sec t$ هي $+\sec t\tan t$.",
        3: r"القسمة مقلوبة والإشارة خاطئة.",
    },
),
'm9q20': E(
    idea=r"$\left(3^{u}\right)'=3^u\ln3\cdot u'$ مع $u=xy$ (قاعدة الضرب)، والنقطة من $x=0$.",
    steps=[
        r"عندما $x=0$: $3^0=1=0+y \Rightarrow y=1$",
        IMPL,
        r"$3^{xy}\ln3\left(y+x\dfrac{dy}{dx}\right)=1+\dfrac{dy}{dx}$",
        r"عند $(0,1)$: $\ln3\cdot1=1+y' \Rightarrow y'=\ln3-1$",
    ],
    wrong={
        1: r"خطأ إشارة عند نقل $1$.",
        2: r"نُقل $y'$ بإشارة خاطئة.",
        3: r"الخطآن معًا.",
    },
),
'm9q21': E(
    idea=r"الميل بالاشتقاق الضمني (قاعدة الضرب)، ثم المقطع $y$ بتعويض $x=0$.",
    steps=[
        r"$y^2+x\cdot2y\dfrac{dy}{dx}=0$ ، وعند $(3,2)$: $4+12y'=0 \Rightarrow y'=-\frac13$",
        r"$y-2=-\frac13(x-3)$ ، وعند $x=0$: $y=2+1=3$",
    ],
    wrong={
        1: r"هذا المقطع $x$.",
        2: r"أُخذ الميل $+\frac13$.",
        3: r"الميل مقلوب: $-3$.",
    },
),
'm9q22': E(
    idea=r"المسافة وتر مثلث قائم ضلعاه $x$ (متغيّر) و $8$ (ثابت).",
    steps=[
        RATES,
        r"$d^2=x^2+64 \Rightarrow d\dfrac{dd}{dt}=x\dfrac{dx}{dt}$",
        r"عند $x=6$: $d=10$ ، و $\dfrac{dd}{dt}=\dfrac{6\cdot60}{10}=36\ \text{km/h}$",
    ],
    wrong={
        1: r"السيارة تبتعد، فالمسافة تزداد والمعدّل موجب.",
        2: r"قُسم على $8$ (الضلع الثابت) بدل الوتر $10$.",
        3: r"القسمة على $8$ وخطأ الإشارة.",
    },
),
'm9q23': E(
    idea=r"نكتب $z$ بالصورة المثلثية الصحيحة أولًا (زاوية سالبة)، ثم نظرية ديموافر.",
    steps=[
        r"$\cos\frac{\pi}{8}-i\sin\frac{\pi}{8}=\cos\left(-\frac{\pi}{8}\right)+i\sin\left(-\frac{\pi}{8}\right)$",
        POLAR,
        r"$z^4=2^4\left(\cos\left(-\frac{\pi}{2}\right)+i\sin\left(-\frac{\pi}{2}\right)\right)=16\left(\cos\left(-\frac{\pi}{2}\right)+i\sin\left(-\frac{\pi}{2}\right)\right)$",
    ],
    wrong={
        1: r"سعة $z$ هي $-\frac{\pi}{8}$ بسبب إشارة الطرح.",
        2: r"المقياس يُرفع للقوة: $2^4=16$ لا $2\times4$.",
        3: r"المقياس والسعة كلاهما خطأ.",
    },
),
'm9q24': E(
    idea=r"نربّع كلًّا من $z$ و $w$ مع $i^2=-1$ ثم نطرح.",
    steps=[
        r"$z^2=(1-2i)^2=1-4i+4i^2=-3-4i$",
        r"$w^2=(2+i)^2=4+4i+i^2=3+4i$",
        r"$z^2-w^2=-6-8i$",
    ],
    wrong={
        1: r"أُخذ $4i^2=+4$ في $z^2$.",
        2: r"هذا $w^2-z^2$.",
        3: r"$w^2-z^2$ مع خطأ $i^2$.",
    },
),
'm9q25': E(
    idea=DIVC,
    steps=[
        r"$\dfrac{1}{1-2i}\cdot\dfrac{1+2i}{1+2i}=\dfrac{1+2i}{5}$",
        r"$\dfrac{1+2i}{5}+\dfrac{2+i}{5}=\dfrac{3+3i}{5}$",
    ],
    wrong={
        1: r"أُخذ $\frac1z=\frac{1-2i}{5}$ (لم يُضرب في المرافق).",
        2: r"استُعمل $\bar w$ بدل $w$.",
        3: r"الخطآن معًا.",
    },
),
'm9q26': E(
    idea=r"المقياس يعطي قيمتين لـ $k$ ، وشرط السعة يختار إحداهما.",
    steps=[
        MOD,
        r"$\sqrt{12+k^2}=4 \Rightarrow k^2=4 \Rightarrow k=\pm2$",
        r"$-\frac{\pi}{2}<\text{Arg}(z)<0$: الربع الرابع، فالجزء التخيلي سالب: $k=-2$",
    ],
    wrong={
        1: r"$k=2$ يضع $z$ في الربع الأول.",
        2: r"$4$ هو المقياس لا $k$.",
        3: r"$4$ هو المقياس، والإشارة خاطئة.",
    },
),
'm9q27': E(
    idea=EQ,
    steps=[
        r"الجزء التخيلي: $x^2-4=5 \Rightarrow x^2=9 \Rightarrow x=3$ (لأنّ $x>0$)",
        r"الجزء الحقيقي: $2(3)+y=5 \Rightarrow y=-1$",
    ],
    wrong={
        1: r"خطأ إشارة: $y=5-6=-1$.",
        2: r"استُعمل $x=-3$ المرفوض بالشرط $x>0$.",
        3: r"$x=-3$ وخطأ إشارة.",
    },
),
'm9q28': E(
    idea=POLAR,
    steps=[
        r"المقياس: $\frac82=4$",
        r"السعة: $\frac{5\pi}{6}-\frac{\pi}{4}=\frac{10\pi}{12}-\frac{3\pi}{12}=\frac{7\pi}{12}$",
    ],
    wrong={
        1: r"جُمعت السعتان (هذا للضرب).",
        2: r"ضُرب المقياسان (هذا للضرب).",
        3: r"هذا ناتج $z_1z_2$.",
    },
),
'm9q29': E(
    idea=r"الضلعان المتجاوران في المربع متساويان ومتعامدان، فالضرب في $\pm i$ يدوّر الضلع $\frac{\pi}{2}$.",
    steps=[
        r"$z_2-z_3=-3+3i$ (من $z_3$ إلى $z_2$)",
        r"من الشكل $z_4$ يمين $z_3$ ، فالضلع $z_3z_4$ هو الضلع $z_3z_2$ مدوَّرًا مع عقارب الساعة: نضرب في $-i$",
        r"$(-3+3i)(-i)=3i-3i^2=3+3i$ ، إذن $z_4=1+3+3i=4+3i$",
    ],
    wrong={
        1: r"التدوير عكس عقارب الساعة (الضرب في $i$) يعطي نقطة في الجهة الأخرى من $z_3$.",
        2: r"هذا $z_1=z_2+(3+3i)$.",
        3: r"هذا متجه الضلع، ولم يُضف إليه $z_3$.",
    },
),
'm9q30': E(
    idea=r"دائرة متقطّعة (لا تشمل محيطها) ومستقيم متصل هو عمود منصّف.",
    steps=[
        CIRCLE,
        r"المركز $(0,2)$ أي $2i$ ونصف القطر $2$ ، والخط متقطّع: $|z-2i|<2$",
        PERP,
        r"المستقيم $x=1$ عمود منصّف للقطعة بين $0$ و $2$ ، والمنطقة في جهة الأصل ومتصلة: $|z|\le|z-2|$",
    ],
    wrong={
        1: r"المتصل والمتقطّع مُبدَّلان.",
        2: r"المركز $2i$ يُكتب $|z-2i|$.",
        3: r"المركز خاطئ والمتصل/المتقطّع مُبدَّلان.",
    },
),
}
