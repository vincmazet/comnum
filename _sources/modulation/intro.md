(P:modulation:intro)=
# Introduction

la modulation d'un message numérique est destinée à adapter le message au support de transmission, à savoir le canal physique.

Dans ce chapitre, on considère que le message contient $N$ symboles $m_1,\dots,m_N$ et qu'il est $M$-aire :
l'alphabet contient donc $M$ symboles.
Par ailleurs, on utilisera les notations données dans la {numref}`F:modulation-demodulation`.

```{figure} figs/modulation-demodulation.svg
---
name: F:modulation-demodulation
---
Notations pour le chapitre.
```

Parmi les différentes façons de représenter un message numérique sous forme de signal analogique,
la **modulation d'impulsion en amplitude** (PAM : _pulse amplitude modulation_) est la technique la plus simple et la plus répandue.
Elle consiste à associer à chaque symbole du message un signal de durée $d$,
et plus précisément à modifier l'amplitude d'un signal type en fonction du symbole : c'est une modulation linéaire.
On distingue deux types de modulations PAM :

* la **modulation en bande de base** (_baseband PAM_) génère des signaux dont le spectre contient des basses fréquences.
  Elle est principalement utilisée dans les conducteurs métalliques ;
  
* la **modulation sur porteuse** (_bandpass PAM_) génère des signaux de bande passante réduite et centrée autour d'une fréquence spécifique
  appelée **fréquence porteuse** (_carrier_).
  Elle est utilisée principalement pour les communications sans fil.

Les sections suivantes détaillent ces deux types de modulation puis les techniques de démodulation pour transformer le signal reçu en une séquence $M$-aire.

Par ailleurs, la **rapidité de modulation** (_symbol rate_) $R$ est le nombre de symboles émis par seconde:

$$
R = \frac{1}{d}.
$$

La rapidité de modulation s'exprime en baud (Bd) qui est l'équivalent de symboles par seconde.
On utilise parfois le **débit binaire** (_bit rate_) qui représente la rapidité de modulation en bits (et non en symboles).
Le débit binaire est donc égal à la rapidité de modulation $R$ multipliée par le nombre de bits par symbole du canal.

<a class="exercise btn btn-light" href="td.html#exercice-1" role="button">1</a>