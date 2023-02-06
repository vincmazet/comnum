(P:codage-source:information)=
# Mesure de l'information


Le codage source convertit un message numérique en une séquence de symboles.
Très souvent, on souhaite que cette séquence soit la plus petite possible : le code source peut alors effectuer une compression du message.


## Qu'est-ce que l'information ?

Pour être sûr que l'information que porte le message initial soit bien transcrite dans la séquence de symboles obtenue après le codage source,
il faut d'abord définir et savoir mesurer l'information contenue dans un message.
Claude Shannon a répondu à ces questions dans ces travaux à la fin des années 1940,
et notamment dans son célèbre article [_A Mathematical Theory of Communication_](http://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf).
Ces travaux font suite aux recherches effectuées durant cette même décennie par Nyquist, Hartley, Wiener, Kotelnikov ou Gabor.

Shannon considère qu'un message parfaitement connu n'a pas de raison d'être transmis :
on peut donc considérer qu'il ne contient aucune information.
En effet, vous dire ce que vous savez déjà ne vous apportera aucune valeur ajoutée.
De même, un émetteur binaire qui serait conçu pour n'envoyer que des bits à 1 n'aurait aucune utilité.

Ainsi, la quantité d'information portée par un message est liée à l'utilité de transmettre le message plutôt qu'à sa signification.
Dit autrement, l'information (au sens de Shannon) ne tient pas compte du contenu sémantique du message,
mais du caractère inattendu de celui-ci.


## Caractère aléatoire du message

<!-- attention notation : remplacer x qui est le signal émis ! Par m ou s ? -->

On appelle $S$ une source et $\{s_1, s_2,\dots,s_M\}$ son alphabet où chaque $s_m$ est un symbole.
Le modèle mathématique d'une source $S$ tel que proposé par Shannon considère que la source produit un message aléatoire.
Donc, chaque symbole $s_m$ a une probabilité $p_m$ d'être émis.
Cela signifie que pour un message contenant $N$ symboles, il y aura statistiquement $N \times p_m$ occurrences du symbole $s_m$.


## Auto-information

L'**auto-information** (_self information_), parfois appelée information propre,
correspond à l'information $I(s_m)$ associée au symbole $s_m$.
En suivant le principe évoqué ci-avant, l'auto-information devrait donc respecter les deux règles suivantes :

* l'auto-information $I(s_m)$ est nulle si $p_m=1$.
  En effet, on est dans ce cas en présence d'une source déterministe qui n'émet que le symbole $s_m$.
  Comme on l'a vu précédemment, ce message n'a pas besoin d'être envoyé : il ne contient pas d'information.
  
* À l'inverse, l'auto-information $I(s_m)$ tend vers l'infini si $p_m$ tend vers zéro,
  car plus un symbole est rare, plus il est inattendu et donc porte beaucoup d'information.
  
Par ailleurs, il serait logique que l'information portée par un message constitué des deux symboles $s_m$ et $s_n$
soit la somme des auto-informations des deux symboles : $I(s_ms_n) = I(s_m) + I(s_n)$.

Ainsi, la définition retenue pour l'auto-information $I(s_m)$ est :

$$
I(s_m) = - \log_2(p_m)
$$

```{margin}
On rappelle que :

$$
\log_2 x = \frac{\log x}{\log 2} = \frac{\ln x}{\ln 2}.
$$
```

où $\log_2$ est le logarithme à base 2 ; l'utilisation d'un logarithme fait que l'information portée deux symboles
est la somme des auto-informations des symboles (en supposant les symboles indépendants : $p(s_m,s_n)=p(s_m)p(s_n)$).
L'auto-information s'exprime en shannon (abbréviation : Sh),
et sa représentation graphique est donnée {numref}`F:auto-information` :
c'est bien une courbe qui décroit avec la probabilité d'apparition du symbole.

```{figure} figs/auto-information.svg
---
name: F:auto-information
---
Auto-information.
```

<a class="exercise btn btn-light" href="td.html#exercice-1" role="button">1</a>


## Entropie

L'**entropie** (_entropy_) d'une source $X$ est la moyenne des auto-informations de chaque symbole
pondérées par leur probabilité :

$$
H(X) = \sum_{m=1}^M p_m I(s_m) = - \sum_{m=1}^M p_m \log_2 p_m.
$$

L'entropie s'exprime en shannon par symbole (Sh/symb).

```{margin}
Il paraît que le terme « entropie » a été choisi par Shannon alors qu'il demandait à von Neumann comment l'appeler.
Celui-ci aurait répondu :
« tu devrais l'appeler entropie pour deux raisons.
D'abord parce que c'est la même formule qu'en mécanique statistique,
mais aussi parce que personne ne sait ce qu'est l'entropie,
donc dans une discussion tu auras toujours l'avantage ! »
(voir par exemple [ici](http://www.spatialcomplexity.info/what-von-neumann-said-to-shannon)).
```

<!-- Proakis, problème 3-5 -->
On peut montrer que l'entropie est bornée :

$$
0 \leq H(X) \leq \log_2 M.
$$

Il se trouve que la borne supérieure correspond à l'entropie de symboles équiprobables,
pour lesquels $p_m = 1/M$ quel que soit $m$.
Ainsi, l'entropie d'une source est maximale lorsque ces symboles sont équiprobables.

````{div} example

Une source binaire émet le symbole <code>0</code> avec une probabilité $\alpha$ et le symbole <code>1</code> avec une probabilité $1-\alpha$.
L'entropie de cette source a donc pour expression $H(X) = - \alpha \log_2 \alpha - (1-\alpha) \log_2 (1-\alpha)$
et elle est représentée {numref}`F:entropie`.

```{figure} figs/entropie.svg
---
name: F:entropie
---
Entropie d'une source binaire en fonction de la probabilité d'un des symboles.
```

````

<a class="exercise btn btn-light" href="td.html#exercice-2" role="button">2</a>


## Débit source

Le **débit source**, noté $D_S$, est le nombre de symboles émis par la source en une seconde ;
il s'exprime donc en symb/s.


## Taux d'émission

Considérons une source $X$, d'entropie $H(X)$ et de débit source $D_S$.
La quantité d'information produite par cette source est appelée le **taux d'émission** $T_S$ et s'exprime en Sh/s :

$$
T_S = D_S \times H(X).
$$


## Débit canal

Les symboles du message ne sont généralement pas identiques aux symboles qui transitent par le canal.
Par exemple, un message textuel, dont l'alphabet est constitué de plusieurs dizaines de symboles,
peut être transmis sur un câble électrique en Morse dont l'alphabet est constitué des trois symboles (trait, point et silence).
Le **débit canal**, noté $D_C$, est le nombre de symboles transmis par le canal en une seconde ;
il s'exprime donc en symb/s.
Le débit canal est équivalent à la rapidité de modulation exprimée en bauds.

Le débit canal est donc similaire au débit source mais peut avoir une valeur différente.
D'ailleurs, les unités des débit source et débit canal sont différentes car elles s'expriment respectivement
en symboles _de la source_ par seconde et en symboles _du canal_ par seconde.


## Capacité canal

En notant $N$ la taille de l'alphabet du canal et $D_C$ le débit canal,
on définit la **capacité canal** qui s'exprime en Sh/s par :

$$
C_C = D_C \times \log_2(N).
$$

La capacité canal correspond à la quantité d'information que peut transmettre le canal en une seconde.


## Théorème du codage canal

Le théorème du codage canal porte également les noms de second théorème de Shannon ou _noisy channel coding theorem_.
Il est lié à la transmission de l'information et dit que :

> Sur un canal bruité de capacité $C_C$, il est possible de transmettre sans erreur jusqu'à une valeur limite du taux d'émission $T_S$.

Autrement dit, si $T_S > C_C$, alors l'acheminement de la totalité de l'information émise par la source au travers du canal est impossible sans erreur.

<a class="exercise btn btn-light" href="td.html#exercice-2" role="button">2</a>
