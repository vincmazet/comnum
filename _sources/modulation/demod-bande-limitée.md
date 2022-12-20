# Démodulation sur un canal à bande limitée

Dans cette section, on n'étudie que la réception des modulations en bande de base
lorsque le canal est à bande passante limitée mais sans bruit.

Le signal reçu $y(t)$ s'écrit alors :

$$
y(t) = (x*g)(t) = \sum_{k=-\infty}^{+\infty} \alpha_k (h*g)(t-kd)
$$

où $g$ est le filtre du canal.

La technique de démodulation consiste généralement à filtrer le signal reçu $y$
par le filtre de réception de réponse impulsionnelle $r$ puis à l'échantillonner,
comme pour un {ref}`canal idéal <F:demodulation-bruit-bb>`.
Le signal reçu et filtré est noté $z(t)$ :

$$
z(t) = (x*g*r)(t) = \sum_{k=-\infty}^{+\infty} \alpha_k (\underbrace{h*g*r}_{u})(t-kd).
$$


## Interférences entre symboles

Le filtre du canal $g$ est plutôt passe-bas et aura donc tendance à « étaler » les formes d'onde du signal émis $x$.
C'est pourquoi, même si la forme d'onde $h$ est limitée à un intervalle de durée $d$,
la forme d'onde filtrée $u = h*g*r$ ne l'est pas forcément et peut donc être de durée supérieure à $d$ :
ce phénomène est illustré {numref}`F:ies`.
Aux instants d'échantillonnage, le signal $z(t+kd)$ ne dépend plus seulement du symbole sous-jacent,
mais également des symboles voisins : on parle d'**interférences entre symboles** ou IES (ISI : _intersymbol interference_).
Si les IES sont trop importantes, elles peuvent conduire à des erreurs de décodage.
Ceci est d'autant plus vrai si le canal est bruité.

```{figure} figs/ies.svg
---
name: F:ies
width: 700px
---
Interférences entre symboles.
Le signal bleu (première ligne) ne contient qu'un symbole autour de $t=0$.
Le signal orange (seconde ligne) contient cinq symboles différents sur $\{-2d,-d,0,+d,+2d\}$.
À cause des interférences entre symboles, les amplitudes aux instants d'échantillonnage (représentés par les points)
dépendent des symboles voisins.
```


## Critère de Nyquist

Pour éviter les IES, il faut que la forme d'onde filtrée $u(t)$ soit nulle à tous les instants d'échantillonnage $kd$
(sauf évidemment pour $k=0$ ou on peut supposer qu'elle est égale à 1) :

$$
u(kd) =
\begin{cases}
  1 &\text{si } k = 0, \\
  0 &\text{si } k \neq 0
\end{cases}
$$

On montre que cette condition est équivalente à {ref}`[Madhow 2008, p. 50]<P:references>` :

$$
\sum_{k=-\infty}^{+\infty} U\left(f+\frac{k}{d}\right) = d
$$

où $U$ est la transformée de Fourier de $u$.
Cette condition est le **critère de Nyquist** (_Nyquist ISI criterion_).
Elle signifie que si la périodisation du spectre de la forme d'onde filtrée $u$ à une période $1/d$ (membre de gauche de l'équation)
est constant (membre de droite), alors on est assuré qu'il n'y a pas d'IES.


## Choix des filtres pour éviter les IES

Un signal simple qui répond au critère de Nyquist est le sinus cardinal ({numref}`F:sinc`) $u(t) = \mathrm{sinc}(t/d)$ dont le spectre est :

$$
U(f) =
\begin{cases}
  d &\text{si} |f| \leq \frac{1}{2d}, \\
  0 &\text{sinon}
\end{cases}
$$

```{figure} figs/sinc.svg
---
name: F:sinc
width: 100%
---
Sinus cardinal (avec $d=1$).
```

Mais le sinus cardinal n'est pas utilisé en pratique pour deux raisons.
D'une part il décroît trop lentement (il y a de nombreuses oscillations),
et d'autre part cela impose que les instants d'échantillonnage soient très précis.

La solution généralement retenue est d'utiliser un **cosinus surélevé** (_raised cosine_, {numref}`F:rcos`) d'expression :

$$
u(t) = \frac{1}{d} \mathrm{sinc}\left(\frac{t}{d}\right) \frac{ \cos\left(\pi a \frac{t}{d}\right) }{ 1-\left(2 a \frac{t}{d}\right)^2 }.
$$

où $a$ est un paramètre choisi en général dans $[0,1[$.
Sa transformée de Fourier est :

$$
U(f) =
\begin{cases}
d                                                              &\text{si } |f| \leq \frac{1-a}{2d}, \\
\frac{d}{2} \left[ 1 - \sin((|f|-1/2d)\frac{\pi d}{a}) \right] &\text{si } \frac{1-a}{2d} \leq |f| \leq \frac{1+a}{2d}, \\
0                                                              &\text{si } |f| > \frac{1+a}{2d}.
\end{cases}
$$

```{figure} figs/rcos.svg
---
name: F:rcos
width: 100%
---
Cosinus surélevé (avec $d=1$ et $a=0,5$).
```

La décroissance plus rapide du cosinus surélevé par rapport au sinus cardinal est évidente en comparant les {numref}`F:sinc` et {numref}`F:rcos`.

Le critère de Nyquist s'applique sur le filtre global $u=h*g*r$.
Mais comment vérifier le critère de Nyquist lorsque le filtre du canal $g$ n'est pas contrôlable ?
Typiquement, c'est le filtre constitué de la forme d'onde $h$ (ou filtre d'émission) et du filtre de réception $r$
qui vérifie le critère de Nyquist, et les IES introduites par le canal sont traitées séparément le cas échéant.
Cela signifie que, dans le domaine fréquentiel, $HR$ est la transformée de Fourier d'un cosinus surélevé.
On dit alors que $h$ et $r$ sont des **filtres en racine de cosinus surélevé** (_root-raised-cosine filter_).
