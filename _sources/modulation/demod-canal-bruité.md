# Démodulation en présence de bruit

On s'intéresse dans cette section à la réception d'un signal analogique lorsque le canal est bruité mais de bande passante infinie :
la filtre passe-bas modélisant le canal (cf. {numref}`F:modulation-demodulation`)
s'écrit $g(t) = K \delta(t-\tau)$ où $K$ est une constante et $\tau$ un retard.
On parle de **canal idéal**.
Sans perdre en généralité, on peut considérer $K=1$ et $\tau=0$.
Dans ce cas, le signal reçu $y(t)$ s'écrit :

$$
y(t) = x(t) + b(t)
$$

où $b(t)$ et le bruit.


## Cas des modulations en bande de base

Le signal reçu $y(t)$ est égal à

$$
y(t) = \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd) + b(t).
$$

Pour retrouver la séquence binaire que représente ce signal, il faut déterminer les amplitudes $\alpha_k$ des formes d'onde $h(t-kd)$.
Cela revient à chercher en chaque instant $kd$ la ressemblance du signal reçu $y$ avec la forme d'onde $h$.
Aussi, un **filtre adapté** (_matched filter_) est effectué entre $y$ et $h$ afin de calculer leur intercorrélation.
Ensuite, le signal filtré est échantillonné tous les $d$ puis comparé à un seuil pour décider du symbole émis.

Schématiquement, la démodulation est représentée {numref}`F:demodulation-bruit-bb` :

```{figure} figs/demodulation-bruit-bb.svg
---
name: F:demodulation-bruit-bb
width: 60%
---
Démodulation d'un signal en bande de base avec un canal idéal.
```

Le filtre de réception est le filtre adapté $r(t)=h(-t)$ et $d$ est la durée d'un symbole.
Quant au seuil, sa valeur optimale dépend du nombre de symboles dans l'alphabet et de la probabilité d'émettre les bits $0$ et $1$.
Dans le cas d'une communication binaire et lorsque les probabilités sont égales, alors le seuil optimal est la moyenne des amplitudes associées à ces deux bits.
Dans le cas $M$-aire, il y a plusieurs seuils, chacun étant situé au milieu de l'intervalle défini par les amplitudes de deux symboles consécutifs.


## Cas des modulations linéaires sur porteuse

On rappelle que les modulations linéaires sur porteuse sont les modulations ASK, PSK et QAM,
et qu'elles correspondent à deux modulations en bande de base multipliées par des sinusoïdes en quadrature de phase.
La première étape de la démodulation consiste à supprimer les sinusoïdes, pour se retrouver ensuite dans le cas de deux démodulations en bande de base.
Pour supprimer les sinusoïdes, on peut effectuer une **démodulation cohérente** en multipliant le signal reçu $y$ par la porteuse.

```{div} full-width
$$
w(t) &= y(t) \cos(2\pi f_p t) \\
     &= \left[
          \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd) \cos(2\pi f_p t)
        + \sum_{k=-\infty}^{+\infty} \beta_k  h(t-kd) \sin(2\pi f_p t)
        + b(t)
       \right] \cos(2\pi f_p t) \\
     &=    \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd) \frac{1}{2} \left(1+\cos(4\pi f_p t)\right)
        + \sum_{k=-\infty}^{+\infty} \beta_k  h(t-kd) \frac{1}{2} \sin(4\pi f_p t)
        + b(t) \cos(2\pi f_p t) \\
     &=   \underbrace{ \frac{1}{2} \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd) }_{\text{basse fréquence}}
        + \underbrace{ \frac{1}{2} \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd) \cos(4\pi f_p t) }_{\text{haute fréquence}}
        + \underbrace{ \frac{1}{2} \sum_{k=-\infty}^{+\infty} \beta_k  h(t-kd) \sin(4\pi f_p t) }_{\text{haute fréquence}}
        + \underbrace{ b(t) \cos(2\pi f_p t) }_{\text{bruit}}
$$
```

Le signal $w(t)$ contient une composante basse fréquence, une composante haute fréquence et du bruit.
Un filtre passe-bas de fréquence de coupure égale à $f_p$ permet d'éliminer les composantes hautes fréquences.
En effet, ces composantes haute fréquence sont centrées autour de $2f_p$.
Le signal basse fréquence résultant est un signal en bande de base sur lequel on effectue une démodulation en bande de base
(filtre adapté, échantillonnage, seuillage) pour obtenir les symboles associés aux amplitudes $\alpha_k$.

Pour obtenir les symboles associés aux amplitudes $\beta_k$, on procède de la même manière en multipliant le signal reçu par $\sin(2\pi f_p t)$.

<!-- Schéma d'un démodulateur -->

Pour terminer, notons que la démodulation cohérente nécessite de connaître parfaitement la fréquence et la phase de la porteuse,
ce qui peut se faire avec une [boucle à verrouillage de phase](https://fr.wikipedia.org/wiki/Boucle_%C3%A0_phase_asservie)
ou une [détection d'enveloppe](https://fr.wikipedia.org/wiki/Circuit_d%C3%A9tecteur_d%27enveloppe).