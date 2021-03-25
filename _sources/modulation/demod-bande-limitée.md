# Démodulation dans le cas d'un canal à bande limitée

Dans cette section, on n'étudie que la réception des modulations en bande de base
lorsque le canal est à bande passante limitée mais sans bruit.

Le signal reçu $y(t)$ s'écrit alors :

$$
y(t) = (x*g)(t) = \sum_{k=-\infty}^{+\infty} \alpha_k (h*g)(t-kT)
$$

et ce signal est généralement filtré par le filtre de réception de réponse impulsionnelle $r(t)$ puis échantillonné,
comme pour un {ref}`canal idéal <F:demodulation-bruit-bb>`.
Le signal reçu et filtré est noté $z(t)$ :

$$
z(t) = (x*g*r)(t) = \sum_{k=-\infty}^{+\infty} \alpha_k (\underbrace{h*g*r}_{u})(t-kT).
$$


## Interférences entre symboles

Le filtre du canal $g$ est plutôt passe-bas et aura donc tendance à « étaler » les formes d'onde du signal émis $x$.
C'est pourquoi, même si la forme d'onde $h$ est limitée à un intervalle de durée $T$,
la forme d'onde filtrée $u = h*g*r$ ne l'est pas forcément et peut donc être de durée supérieure à $T$ :
ce phénomène est illustré {numref}`F:ies`.
Aux instants d'échantillonnage, le signal $z(t+kT)$ ne dépend plus seulement du symbole sous-jacent,
mais également des symboles voisins : on parle d'**interférences entre symboles** ou IES (_intersymbol interference_).
Si les IES sont trop importantes, elles peuvent conduire à des erreurs de décodage.
Ceci est d'autant plus vrai si le canal est bruité.

```{figure} ../figs/ies.svg
---
name: F:ies
width: 700px
---
Interférences entre symboles.
Le signal bleu (première ligne) ne contient qu'un symbole autour de $t=0$.
Le signal orange (seconde ligne) contient trois symboles différents en $-T$, $0$ et $T$.
À cause des interférences entre symboles, les amplitudes aux instants d'échantillonnage (représentés par les points)
dépendent des symboles voisins.
```


## Critère de Nyquist

Pour éviter les IES, il faut que la forme d'onde filtrée $u(t)$ soit nulle à tous les instants d'échantillonnage $kT$
(sauf évidemment pour $k=0$ ou on peut supposer qu'elle est égale à 1) :

$$
u(kt) =
\begin{cases}
  1 &\text{si } k = 0, \\
  0 &\text{si } k \neq 0
\end{cases}
$$

<!-- Illustration ? -->

On montre que cette condition est équivalente à {ref}`[Madhow 2008, p.50]<S:refs>` :

$$
\sum_{k=-\infty}^{+\infty} U\left(f+\frac{k}{T}\right) = T
$$

où $U$ est la transformée de Fourier de $u$.
Cette condition est le **critère de Nyquist** (_Nyquist ISI criterion_).
Elle signifie que si la périodisation du spectre de la forme d'onde filtrée $u$ à une période $1/T$ (membre de gauche de l'équation)
est constant (membre de droite), alors on est assuré qu'il n'y a pas d'IES.


## Choix des filtres pour éviter les IES

Un signal simple qui répond au critère de Nyquist est le sinus cardinal ({numref}`F:sinc`) $u(t) = \mathrm{sinc}(t/T)$ dont le spectre est :

$$
U(f) =
\begin{cases}
  T &\text{si} |f| \leq \frac{1}{2T}, \\
  0 &\text{sinon}
\end{cases}
$$

```{figure} ../figs/sinc.svg
---
name: F:sinc
width: 100%
---
Sinus cardinal ($T=1$ ici).
```

Mais le sinus cardinal n'est pas utilisé en pratique parce d'une part il décroît trop lentement (il y a de nombreuses oscillations)
et d'autre part cela impose que les instants d'échantillonnage soient très précis.

La solution généralement retenue est d'utiliser un **cosinus surélevé** (_raised cosine_, {numref}`F:rcos`) d'expression :

$$
u(t) = \frac{1}{T} \mathrm{sinc}\left(\frac{t}{T}\right) \frac{ \cos\left(\pi a \frac{t}{T}\right) }{ 1-\left(2 a \frac{t}{T}\right)^2 }.
$$

où $a$ est un paramètre choisi en général dans $[0,1[$.
Sa transformée de Fourier est :

$$
U(f) =
\begin{cases}
T                                                              &\text{si } |f| \leq \frac{1-a}{2T}, \\
\frac{T}{2} \left[ 1 - \sin((|f|-1/2T)\frac{\pi T}{a}) \right] &\text{si } \frac{1-a}{2T} \leq |f| \leq \frac{1+a}{2T}, \\
0                                                              &\text{si } |f| > \frac{1+a}{2T}.
\end{cases}
$$

```{figure} ../figs/rcos.svg
---
name: F:rcos
width: 100%
---
Cosinus surélevé ($T=1$ et $a=0,5$ ici).
```

La décroissance plus rapide du cosinus surélevé par rapport au sinus cardinal est évidente en comparant les figures
{numref}`F:sinc` et {numref}`F:rcos`.

Le critère de Nyquist s'applique sur le filtre global $u=h*g*r$.
Mais comment vérifier le critère de Nyquist lorsque le filtre du canal $g$ n'est pas contrôlable ?
Typiquement, c'est le filtre constitué de la forme d'onde (ou filtre d'émission) et du filtre de réception
qui vérifient le critère de Nyquist, et les IES introduites par le canal sont traitées séparément le cas échéant.
Cela signifie que, dans le domaine fréquentiel, $HR$ est la transformée de Fourier d'un cosinus surélevé.
On dit alors que $h$ et $t$ sont des **filtres en racine de cosinus surélevé** (_root-raised-cosine filter_).

<!-- Todo : modulations sur porteuse ? -->

<a class="btn btn-light" href="td.html#exercice-6" role="button">Exercice 6</a>