(S:codage-canal:conv)=
# Codes convolutifs


## Principe

La sortie d'un codeur convolutif est calculée en appliquant une fenêtre glissante sur la totalité du message.

```{margin}
La taille de la fenêtre n'est pas très élégante, mais je n'y peux rien : c'est les notations de la littérature. 💩
```

Cette fenêtre glissante est constituée de $K$ groupes de $k$ bits chacun : elle est donc de taille $Kk$.
$K$ est appelée **longeur de contrainte** (_constraint length_).
À chaque cycle d'horloge, la fenêtre avance d'un groupe de bits,
et donc $k$ nouveaux bits rentrent dans la fenêtre alors que les $k$ plus anciens bits en ressortent.
Une ou plusieurs additions de quelques bits de la fenêtre sont calculées (toujours en respectant les règle du corps de Galois)
pour obtenir autant de bits de sortie.
On note $n$ le nombre de bits de sortie, ils sont ajoutés au code déjà produit.

Les bits utilisés par les additions sont représentés par des polynômes générateurs ;
il y a donc autant de polynômes que de bits de sortie.
Par exemple, le polynôme générateur $g = 15_8$ a pour représentation binaire $001101_2$ :
l'addition qu'il représente s'effectue donc entre les bits 1, 3 et 4.

```{figure} ../figs/code-conv-5.png
---
width: 568px
---
Exemple de code convolutif de polynômes générateurs $7_8$ et $5_8$ appliqué sur le message `10110011`
à un instant donné.
La sortie $u$ du codeur est représentée par la séquence rouge.
```

```{figure} ../figs/code-conv.gif
---
width: 568px
---
Exemple de code convolutif de polynômes générateurs $7_8$ et $5_8$ appliqué sur le message `10110011`.
La sortie $u$ du codeur est représentée par la séquence rouge.
```

```{note}

* Le rendement d'un code convolutif est, comme pour les codes en bloc, $k/n$.

* Traditionnellement, le registre est initialisé à zéro.

* Contrairement aux codes en bloc, les $n$ bits de sortie ne dépendent pas seulement des $k$ bits d'entrée
  mais également des $K-1$ blocs précédents : il y a donc un effet de mémoire.
  
* Les codes convolutifs sont appelés ainsi car chacune des $n$ sortie du codeur correspond
  au produit de convolution de l'entrée avec le polynôme générateur correspondant (toujours dans le corps de Galois !).
  
```

## Représentation en treillis

Lorsqu'un code convolutif est suffisamment simple, il peut être représenté sous forme d'un **treillis**.
Il s'agit d'une représentation graphique en deux dimension, où chaque état du codeur est représenté par un point.
L'état d'un codeur correspond aux valeurs des bits de la fenêtre, à l'exception des bits qui viennent de rentrer à l'instant correspondant.
L'axe horizontal représente le temps, et l'axe vertical les différents états possibles.
Enfin, des flèches indiquent les valeurs du ou des bits d'entrée du codeur.

```{figure} ../figs/treillis.png
---
width: 70%
---
Représentation en treillis du code convolutif de polynômes générateurs $7_8$ et $5_8$.
Les quatre états du codeur sont en bleu, les flèches pleines et en pointillés représentent respectivement l'entrée d'un bit à 0 ou à 1.
```


## Décodage

Le décodage d'un code convolutif s'effectue avec l'algorithme de Viterbi, qui est illustré dans [ce document](https://vincmazet.github.io/comnum/_static/viterbi.pdf).