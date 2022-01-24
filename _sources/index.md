# Avant-propos

<br />

```{figure} shannon1948.png
---
name: F:shannon1948
width: 500px
---
Représentation schématique de la chaîne de communication<br />proposée par C.E. Shannon en 1948.
```

<br />

Ce manuel est le support du cours de Communications numériques de la formation EII
de [Télécom Physique Strasbourg](http://www.telecom-physique.fr/).
Il s'accompagne d'exercices théoriques (sur feuille) et pratiques (programmation en Python).
Pour compléter le cours, je vous conseille de lire les documents listés dans les [références](P:references).

Ce manuel est accessible depuis n'importe quel terminal connecté.
Il peut être téléchargé et imprimé en cliquant sur l'icône &nbsp;<i class="fas fa-download"></i>&nbsp;
en haut de la page, qui permet de générer un PDF.

<p style="text-align: center; margin: 2em 0;">⁂</p>

Les communications numériques regroupent les techniques permettant à deux machines, ou plus,
d'échanger des informations sous forme de symboles issus d'un dictionnaire défini au préalable.
La communication entre un téléphone et un serveur web, ou entre une souris et un ordinateur,
ou entre deux robots sont des exemples parmi tant d'autres de communication numérique.

Pour transmettre un message sous forme numérique, il faut passer par un ensemble d'étapes qui représentent la [chaîne de communication](P:chaine).
Pour chaque étape au niveau de l'émetteur, on retrouve son pendant au niveau du récepteur : les étapes vont toujours par paire.
Dans ce cours, nous nous concentrons sur les trois blocs fondamentaux,
sans qui il ne serait presque pas possible de réaliser une communication numérique:
* le [codage source](P:codage-source:information), qui permet de transformer le message, quelle que soit sa nature, en séquence numérique ;
* le [codage canal](P:codage-canal:intro), qui ajoute de la redondance d'information
  pour rendre la transmission plus robuste face aux perturbations de la transmission ;
* la [modulation](P:modulation:intro), qui transforme la séquence numérique en un signal adapté à la transmission.


<!-- Notations :

  \alpha  : amplitude des formes d'onde
  b       : signal
  \beta   : amplitude des formes d'onde
  c       : message codé
  C       : capacité                           ***
  C       : code correcteur                    ***
  d       : durée d'un symbole                          NEW
  D       : débits
  e       : erreur
  f_p     : fréquence de la porteuse
  G       : matrice génératrice
  h       : forme d'onde
  H       : entropie                           ***
  H       : matrice de contrôle de parité      ***
  I       : auto-information
  g       : réponse impulsionnelle du canal d'onde
  k       : indice des symboles
  k       : code convolutif
  K       : code convolutif
  L       : longueur d'un mot
  m       : message
  \hat{m} : message
  M       : taille de l'alphabet
  n       : code convolutif
  N       : nombre de symboles dans le message
  p       : probabilité
  P       : matrice P
  r       : filtre de réception                ***
  r       : message reçu                       ***
  s       : syndrome
  R       : rapidité de modulation
  T       : durée d'un symbole => remplacer par D ou d ?
  u       : h*g*r
  u       : F[u]
  V       : amplitude de la forme d'onde
  x       : signal
  X       : source                            ***
  X       : variable du polynôme              ***
  y       : signal
  z       : signal
-->