"""Explanations: semester-1 mock paper 10 (m10q1..m10q30). wrong keys = option index as written in s1_papers_6_10.py (0 = correct)."""
from explain_common import E, synth, SYNTH_HOW, REM, FAC, MULT, QUADS, SIGNS
from explain_u3 import DER, PROD, QUOT, CHAIN, IMPL, PARAM, RATES
from explain_u4 import IPOW, CONJ, DIVC, MOD, ARG, POLAR, CIRCLE, RAY, EQ, FORM

EXPLAIN = {
'm10q1': E(
    idea=r"نجعل الطرف الأيمن صفرًا ونقسم على $(x-3)$ ، والتربيعي الناتج معامله الرئيس $2$.",
    steps=[
        r"$2x^3-3=3x^2+8x \Rightarrow 2x^3-3x^2-8x-3=0$",
        SYNTH_HOW + synth(3, [2, -3, -8, -3]),
        r"$2x^2+3x+1=(2x+1)(x+1)=0 \Rightarrow x=-\frac12,\ x=-1$",
    ],
    quick=r"عوّضي $x=-1$: $-2-3=-5$ و $3-8=-5$ ✔.",
    wrong={
        1: r"إشارتا الحلّين معكوستان.",
        2: r"$2x+1=0$ يعطي $x=-\frac12$ لا $\frac12$.",
        3: r"$x+1=0$ يعطي $x=-1$ لا $1$.",
    },
),
'm10q2': E(
    idea=r"$\dfrac{A}{x+2}+\dfrac{B}{(x+2)^2}$ ، و $A$ معامل $x$ ، و $B$ قيمة البسط عند $x=-2$.",
    steps=[
        MULT + r" $5x+2=A(x+2)+B$",
        r"معامل $x$: $A=5$",
        r"عند $x=-2$: $-10+2=B \Rightarrow B=-8$",
    ],
    wrong={
        1: r"إشارة $B$ خاطئة: $5(-2)+2=-8$.",
        2: r"الثابتان مُبدَّلان.",
        3: r"الثابتان مُبدَّلان وإشارة $-8$ خاطئة.",
    },
),
'm10q3': E(
    idea=r"تساوي الباقيين: $f(-1)=f(3)$.",
    steps=[
        REM,
        r"$f(-1)=(-1)^3-2(-1)^2-p+4=-1-2-p+4=1-p$",
        r"$f(3)=27-18+3p+4=13+3p$",
        r"$1-p=13+3p \Rightarrow -4p=12 \Rightarrow p=-3$",
    ],
    wrong={
        1: r"خطأ إشارة عند القسمة على $-4$.",
        2: r"أُخذ $-2(-1)^2=+2$: $f(-1)=5-p$ ، فـ $p=-2$.",
        3: r"خطأ $(-1)^2$ وخطأ إشارة.",
    },
),
'm10q4': E(
    idea=r"$(2x-1)$ عامل يعني أنّ $f\left(\frac12\right)=0$.",
    steps=[
        FAC,
        r"$f\left(\frac12\right)=2\cdot\frac18+k\cdot\frac14-\frac52+2=\frac14+\frac k4-\frac12$",
        r"$\frac k4-\frac14=0 \Rightarrow k=1$",
    ],
    wrong={
        1: r"عُوّض بـ $x=2$ (صفر $x-2$ لا $2x-1$): $4k+8=0$.",
        2: r"عُوّض بـ $x=-\frac12$: إشارة الصفر خاطئة.",
        3: r"خطأ إشارة عند حلّ المعادلة.",
    },
),
'm10q5': E(
    idea=r"نجد $\cos\theta$ من $\tan\theta$ ($\sec^2\theta=1+\tan^2\theta$) ، ثم صيغة $\cos\frac{\theta}{2}$ بإشارة ربعها.",
    steps=[
        r"$\sec^2\theta=1+8=9$ ، وفي الربع الثاني $\sec\theta=-3$ ، أي $\cos\theta=-\frac13$",
        r"$\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ (الربع الأول) فجيب التمام موجب",
        r"$\cos\frac{\theta}{2}=\sqrt{\dfrac{1+\cos\theta}{2}}=\sqrt{\dfrac{2/3}{2}}=\dfrac{1}{\sqrt3}$",
    ],
    wrong={
        1: r"الإشارة خاطئة: $\frac{\theta}{2}$ في الربع الأول.",
        2: r"هذه صيغة $\sin\frac{\theta}{2}$: $\sqrt{\dfrac{1-\cos\theta}{2}}$.",
        3: r"صيغة $\sin\frac{\theta}{2}$ والإشارة خاطئة.",
    },
),
'm10q6': E(
    idea=r"نفكّ الحدّين ونطرح، فيُحذف $\cos x$.",
    steps=[
        r"$\cos\left(x-\frac{\pi}{6}\right)=\frac{\sqrt3}{2}\cos x+\frac12\sin x$",
        r"$\cos\left(x+\frac{\pi}{6}\right)=\frac{\sqrt3}{2}\cos x-\frac12\sin x$",
        r"الفرق: $\sin x$",
    ],
    wrong={
        1: r"حدّا $\cos x$ هما اللذان يُحذفان.",
        2: r"معامل $\sin x$ هو $\sin\frac{\pi}{6}=\frac12$ في كلّ حدّ.",
        3: r"المعامل والنسبة كلاهما خطأ.",
    },
),
'm10q7': E(
    idea=r"نوحّد المقامات ونستعمل $\sin^2x+\cos^2x=1$.",
    steps=[
        r"$\dfrac{\sin x}{\cos x}+\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x+\cos^2x}{\sin x\cos x}=\dfrac{1}{\sin x\cos x}$",
        r"وبما أنّ $\frac{1}{\cos x}=\sec x$ و $\frac{1}{\sin x}=\csc x$ فالناتج $\sec x\csc x$",
    ],
    wrong={
        1: r"الكسر مقلوب.",
        2: r"$\sec^2x=1+\tan^2x$ ، لا $\tan x+\cot x$.",
        3: r"$\csc^2x=1+\cot^2x$ ، لا $\tan x+\cot x$.",
    },
),
'm10q8': E(
    idea=r"$2\sin A\cos B=\sin(A+B)+\sin(A-B)$.",
    steps=[
        r"$A+B=\frac{6\pi}{12}=\frac{\pi}{2}$ ، $A-B=\frac{4\pi}{12}=\frac{\pi}{3}$",
        r"$\sin\frac{\pi}{2}+\sin\frac{\pi}{3}=1+\frac{\sqrt3}{2}=\frac{2+\sqrt3}{2}$",
    ],
    wrong={
        1: r"الحدّان يُجمعان: $\sin(A+B)+\sin(A-B)$.",
        2: r"المقدار $2\sin A\cos B$ يساوي المجموع مباشرة، فلا نقسم على $2$.",
        3: r"طرح وقسمة على $2$.",
    },
),
'm10q9': E(
    idea=r"معادلة تربيعية في $\cos x$ ، نرفض $\cos x=-2$ ، ثم نحدّد أرباع $\cos x$ الموجب.",
    steps=[
        r"$(2\cos x-1)(\cos x+2)=0$",
        r"$\cos x=-2$ مرفوض لأنّ $-1\le\cos x\le1$ ، و $\cos x=\frac12$: زاوية الإسناد $\frac{\pi}{3}$",
        SIGNS,
        r"الربع الأول: $\frac{\pi}{3}$ ، الرابع: $2\pi-\frac{\pi}{3}=\frac{5\pi}{3}$",
    ],
    wrong={
        1: r"هذه حلول $\cos x=-\frac12$ (خطأ إشارة في التحليل).",
        2: r"زاوية الإسناد $\frac{\pi}{6}$ خاطئة ($\cos\frac{\pi}{6}=\frac{\sqrt3}{2}$).",
        3: r"إشارة خاطئة وزاوية إسناد خاطئة.",
    },
),
'm10q10': E(
    idea=r"$\sin2x=\cos2x \Rightarrow \tan2x=1$ ، ونحلّ لـ $2x$ في $[0,2\pi)$ ثم نقسم.",
    steps=[
        r"$\tan2x=1$: $2x=\frac{\pi}{4}$ أو $2x=\pi+\frac{\pi}{4}=\frac{5\pi}{4}$",
        r"$x=\frac{\pi}{8},\ \frac{5\pi}{8}$",
    ],
    wrong={
        1: r"هذه قيم $2x$ ولم تُقسم على $2$.",
        2: r"نُسي الحلّ الثاني لـ $2x$ في الربع الثالث.",
        3: r"لم تُقسم على $2$ ونُسي الحلّ الثاني.",
    },
),
'm10q11': E(
    idea=DER,
    steps=[
        r"$f'(x)=-3\sin(x-\pi)+\dfrac{2x}{2\pi}=-3\sin(x-\pi)+\dfrac{x}{\pi}$",
        r"$\sin\left(\frac{\pi}{2}-\pi\right)=\sin\left(-\frac{\pi}{2}\right)=-1$",
        r"$f'\left(\frac{\pi}{2}\right)=3+\frac12=\frac72$",
    ],
    wrong={
        1: r"مشتقة $\cos$ هي $-\sin$ ؛ أُخذت موجبة: $-3+\frac12$.",
        2: r"مشتقة $\dfrac{x^2}{2\pi}$ هي $+\dfrac{x}{\pi}$ لا سالبة.",
        3: r"الإشارتان خاطئتان.",
    },
),
'm10q12': E(
    idea=r"$\left(3^{u}\right)'=3^u\ln3\cdot u'$ ، ونساوي بالمعطى.",
    steps=[
        r"$f'(a)=3^{2a-1}\ln3\cdot2=6\ln3$",
        r"$3^{2a-1}=3=3^1 \Rightarrow 2a-1=1 \Rightarrow a=1$",
    ],
    wrong={
        1: r"بالتعويض: $f'(0)=2\ln3\cdot3^{-1}=\frac23\ln3\ne6\ln3$.",
        2: r"بالتعويض: $f'(2)=2\ln3\cdot27=54\ln3$.",
        3: r"بالتعويض: $f'(-1)=2\ln3\cdot3^{-3}$.",
    },
),
'm10q13': E(
    idea=r"نجد اللحظة التي يعود فيها الموقع إلى $s(0)$ ، ثم نعوّضها في $v(t)$.",
    steps=[
        r"$s(0)=5$ ، و $t^3-6t^2+5=5 \Rightarrow t^2(t-6)=0 \Rightarrow t=6$",
        r"$v(t)=3t^2-12t$ ، $v(6)=108-72=36\ \text{m/s}$",
    ],
    wrong={
        1: r"هذه سرعة الانطلاق $v(0)$ ، لا لحظة العودة.",
        2: r"$v(2)=-12$ ، لكنّ الجسم لا يكون في موقعه الابتدائي عند $t=2$.",
        3: r"خطأ إشارة؛ $v(6)>0$.",
    },
),
'm10q14': E(
    idea=r"مشتقة $\sec x\tan x$ بقاعدة الضرب، و $\pi^2$ ثابت.",
    steps=[
        r"$f'(x)=\sec x\tan x$",
        PROD,
        r"$f''(x)=\sec x\tan x\cdot\tan x+\sec x\cdot\sec^2x=\sec x\tan^2x+\sec^3x$",
        r"$\sec\frac{\pi}{3}=2$ ، $\tan^2\frac{\pi}{3}=3$: $f''=2(3)+8=14$",
    ],
    wrong={
        1: r"هذا الحدّ الأول وحده ($\sec x\tan^2x=6$).",
        2: r"هذا الحدّ الثاني وحده ($\sec^3x=8$).",
        3: r"$\pi^2$ ثابت، فمشتقته صفر لا $2\pi$.",
    },
),
'm10q15': E(
    idea=r"$\dfrac{dy}{dt}=\dfrac{dy}{dx}\cdot\dfrac{dx}{dt}$ (قاعدة السلسلة).",
    steps=[
        r"$y=12(1+\sqrt x)^{-1} \Rightarrow \dfrac{dy}{dx}=-12(1+\sqrt x)^{-2}\cdot\dfrac{1}{2\sqrt x}$",
        r"عند $x=4$: $-\dfrac{12}{9}\cdot\dfrac14=-\dfrac13$",
        r"$\dfrac{dy}{dt}=-\dfrac13\cdot3=-1\ \text{cm/s}$",
    ],
    wrong={
        1: r"إشارة خاطئة؛ $y$ يتناقص كلّما زاد $x$.",
        2: r"نُسيت مشتقة $\sqrt x$ (العامل $\frac{1}{2\sqrt x}$).",
        3: r"نُسي العامل وخطأ الإشارة.",
    },
),
'm10q16': E(
    idea=r"$\left(\dfrac{4}{g}\right)'=-\dfrac{4g'}{g^2}$ ، والقيم من الشكل.",
    steps=[
        r"$f$ من $(0,2)$ إلى $(4,4)$: $f'(2)=\frac12$",
        r"$g$ من $(0,1)$ إلى $(3,4)$: $g'(2)=1$ ، $g(2)=3$",
        r"$u'(2)=\frac12-\frac{4(1)}{9}=\frac{1}{18}$",
    ],
    wrong={
        1: r"مشتقة $\frac4g$ سالبة: $-\dfrac{4g'}{g^2}$.",
        2: r"نُسي تربيع $g$ في المقام: $\frac12-\frac43$.",
        3: r"إشارة موجبة وبلا تربيع.",
    },
),
'm10q17': E(
    idea=r"$\left(e^u\right)'=e^u\cdot u'$ مع $u=x^{\frac23}$.",
    steps=[
        r"$u'=\frac23x^{-\frac13}=\dfrac{2}{3\sqrt[3]{x}}$",
        r"$f'(x)=\dfrac{2}{3\sqrt[3]{x}}e^{\sqrt[3]{x^2}}$",
    ],
    wrong={
        1: r"المعامل $\frac23$ (الأس) لا $\frac32$.",
        2: r"الأس $-\frac13$ سالب، فالجذر في المقام.",
        3: r"المعامل مقلوب والجذر في البسط.",
    },
),
'm10q18': E(
    idea=CHAIN,
    steps=[
        r"$\left(\sin(\pi x^2)\right)'=\cos(\pi x^2)\cdot2\pi x$",
        r"$f'(x)=3+2\pi x\cos(\pi x^2)$",
    ],
    wrong={
        1: r"مشتقة $\sin$ هي $+\cos$.",
        2: r"نُسي العامل $x$ من مشتقة الداخل $\pi x^2$ (مشتقته $2\pi x$).",
        3: r"خطأ إشارة ونقص في مشتقة الداخل.",
    },
),
'm10q19': E(
    idea=PARAM,
    steps=[
        r"$\dfrac{dy}{dt}=e^t-1$ ، $\dfrac{dx}{dt}=2e^{2t}$",
        r"عند $t=\ln2$: $e^t=2$ ، $e^{2t}=4$: $\dfrac{dy}{dt}=1$ ، $\dfrac{dx}{dt}=8$",
        r"$\dfrac{dy}{dx}=\dfrac18$",
    ],
    wrong={
        1: r"القسمة مقلوبة.",
        2: r"نُسي العامل $2$ في مشتقة $e^{2t}$.",
        3: r"القسمة مقلوبة ونُسي العامل $2$.",
    },
),
'm10q20': E(
    idea=r"نجد $x$ من $y=0$ ، ثم نشتق ضمنيًّا (قاعدة الضرب في $xe^y$).",
    steps=[
        r"$y=0$: $x\cdot1+0=2x-1 \Rightarrow x=1$",
        IMPL,
        r"$e^y+xe^y\dfrac{dy}{dx}+\dfrac{dy}{dx}=2$ ، وعند $(1,0)$: $1+y'+y'=2 \Rightarrow y'=\frac12$",
    ],
    wrong={
        1: r"نُسي الحدّ $xe^y\dfrac{dy}{dx}$: $1+y'=2$.",
        2: r"بالتعويض: $1+2\cdot\frac13\ne2$.",
        3: r"بالتعويض: $1+2\cdot2\ne2$.",
    },
),
'm10q21': E(
    idea=r"$\ln y=x\ln(\sin x)$ ، ثم قاعدة الضرب.",
    steps=[
        r"$\dfrac{d}{dx}(\ln y)=1\cdot\ln(\sin x)+x\cdot\dfrac{\cos x}{\sin x}$",
        r"أي $\ln(\sin x)+x\cot x$",
    ],
    wrong={
        1: r"مشتقة $\sin x$ هي $+\cos x$.",
        2: r"$\left(\ln\sin x\right)'=\dfrac{\cos x}{\sin x}=\cot x$ لا $\tan x$.",
        3: r"$\tan$ بدل $\cot$ وخطأ إشارة.",
    },
),
'm10q22': E(
    idea=r"مساحة المثلث $\frac12ab\sin\theta$ ، ثم نشتق بالنسبة إلى $t$.",
    steps=[
        RATES,
        r"$A=\frac12(8)(8)\sin\theta=32\sin\theta$",
        r"$\dfrac{dA}{dt}=32\cos\theta\dfrac{d\theta}{dt}=32\cdot\dfrac{\sqrt3}{2}\cdot\dfrac{\pi}{90}=\dfrac{8\sqrt3\pi}{45}$",
    ],
    wrong={
        1: r"استُعمل $\sin\theta$ بدل مشتقته $\cos\theta$.",
        2: r"نُسي العامل $\frac12$ في قانون المساحة.",
        3: r"$\sin$ بدل $\cos$ ونُسي $\frac12$.",
    },
),
'm10q23': E(
    idea=r"$\text{Arg}(\bar z)=-\text{Arg}(z)$ ، ثم $z=r(\cos\theta+i\sin\theta)$.",
    steps=[
        r"$\text{Arg}(z)=\frac{\pi}{6}$",
        r"$z=6\cos\frac{\pi}{6}+6i\sin\frac{\pi}{6}=3\sqrt3+3i$",
    ],
    wrong={
        1: r"هذا $\bar z$ (استُعملت سعة $\bar z$ مباشرة).",
        2: r"$\cos$ و $\sin$ مُبدَّلان.",
        3: r"مُبدَّلان ومرافق.",
    },
),
'm10q24': E(
    idea=r"المقام تخيّلي بحت، فنضرب البسط والمقام في $i$.",
    steps=[
        r"$\dfrac{(2+6i)i}{-2i\cdot i}=\dfrac{2i+6i^2}{-2i^2}=\dfrac{-6+2i}{2}=-3+i$",
    ],
    wrong={
        1: r"إشارة المقام: $-2i^2=+2$.",
        2: r"إشارة الجزء التخيلي خاطئة.",
        3: r"إشارة الجزء الحقيقي خاطئة.",
    },
),
'm10q25': E(
    idea=r"$|z^2|=|z|^2$.",
    steps=[
        MOD,
        r"$|z|^2=4+36=40$",
    ],
    wrong={
        1: r"هذا $|z|$ نفسه.",
        2: r"هذا الجزء الحقيقي لـ $z^2=-32+24i$ دون إشارة.",
        3: r"هذا $|z|^4$.",
    },
),
'm10q26': E(
    idea=IPOW,
    steps=[
        r"$35=4(8)+3 \Rightarrow i^{35}=i^3=-i$",
        r"$\sqrt{-18}=\sqrt{18}\,i=3\sqrt2\,i$",
        r"$(-i)(3\sqrt2\,i)=-3\sqrt2\,i^2=3\sqrt2$",
    ],
    wrong={
        1: r"أُخذ $i^{35}=i$.",
        2: r"أُخذ $i^{35}=i$ و $\sqrt{-18}=3\sqrt2$ دون $i$.",
        3: r"نُسي $i$ في $\sqrt{-18}$.",
    },
),
'm10q27': E(
    idea=r"نربّع ثم نضرب، مع $i^2=-1$.",
    steps=[
        r"$(1+2i)^2=1+4i+4i^2=-3+4i$",
        r"$(-3+4i)(1+2i)=-3-6i+4i+8i^2=-11-2i$",
    ],
    wrong={
        1: r"أُخذ $i^2=1$ و $i^3=i$.",
        2: r"أُخذ $i^3=i$ بدل $-i$.",
        3: r"أُخذ $i^2=1$.",
    },
),
'm10q28': E(
    idea=MOD,
    steps=[
        r"$\left(\dfrac4k\right)^2+(\sqrt5)^2=9 \Rightarrow \dfrac{16}{k^2}=4 \Rightarrow k^2=4$",
        r"$k>0 \Rightarrow k=2$",
    ],
    wrong={
        1: r"بالتعويض: $1+5=6\ne9$.",
        2: r"بالتعويض: $16+5=21\ne9$.",
        3: r"بالتعويض: $64+5\ne9$.",
    },
),
'm10q29': E(
    idea=CONJ,
    steps=[
        r"من الشكل: $z=-2-i$",
        r"$\bar z=-2+i$",
    ],
    wrong={
        1: r"هذا $-\bar z$: غُيّرت إشارة الجزء الحقيقي أيضًا.",
        2: r"هذا $-z$.",
        3: r"هذا $z$ نفسه.",
    },
),
'm10q30': E(
    idea=r"نقرأ المركز ونصف القطر، ونكتب $|z-z_0|\le r$ لأنّ الدائرة متصلة والداخل مظلّل.",
    steps=[
        CIRCLE,
        r"المركز $(-2,1)$ ، نصف القطر $2$",
        FORM,
        r"$|z+2-i|\le2$",
    ],
    wrong={
        1: r"إشارتا المركز معكوستان.",
        2: r"الجزء الحقيقي والتخيلي للمركز مُبدَّلان.",
        3: r"مُبدَّلان وإشارتان معكوستان.",
    },
),
}
