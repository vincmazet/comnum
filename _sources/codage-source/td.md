# Exercices


## Exercice 1

Calculez le logarithme à base 2 des nombres 1, 2, 8 et 256.

## Exercice 2

<!-- Collet -->

Une source émet 100 symboles par seconde parmi un alphabet de trois symboles $\{A,B,C\}$
dont les probabilités respectives sont égales à $0,8$, $0,15$ et $0,05$.
On souhaite savoir si les messages de cette source peuvent être transmis sur un canal binaire
pouvant transmettre sans erreur 95 bits par seconde.

1. Calculez l'auto-information des symboles, puis l'entropie de la source. <!-- 0.884 Sh/symb -->
1. Quel est le débit de la source ? <!-- 100 symb/s -->
1. Calculez le taux d'émission de la source. <!-- 88.4 Sh/s -->
1. Quel est le débit du canal ? <!-- 100 bits/s (canal binaire) -->
1. Quelle est la capacité du canal ? <!-- 100 Sh/s -->
1. La transmission est-elle possible sans erreur ? <!-- Transmission (théoriquement) possible -->


## Exercice 3

<!-- MacKay, exercices 5.19 et 5.20 -->

1. Le code binaire
   {<code>00</code>, <code>11</code>, <code>0101</code>, <code>111</code>, <code>1010</code>, <code>100100</code>, <code>0110</code>}
   est-il à décodage unique ?
1. Le code ternaire
   {<code>00</code>, <code>012</code>, <code>0110</code>, <code>0112</code>, <code>100</code>, <code>201</code>, <code>212</code>, <code>22</code>}
   est-il à décodage unique ?


## Exercice 4

On considère une source qui émet quatre symboles, par exemple 😀, ☹️, 😛, 😎 avec les probabilités

$$
p(😀) = 0,4 \quad
p(☹️) = 0,3 \quad
p(😛) = 0,2 \quad
p(😎) = 0,1
$$

1. Calculez l'entropie de le source.
2. Pour chacun des codes ci-dessous, indiquez quelles propriétés ils vérifient et calculez leur longueur moyenne.

|        |   😀 |    ☹️ |   😛 |   😎 |
| ------ | ---- | ---- | ---- | ---- |
| Code 1 |   00 |   01 |   10 |   11 |
| Code 2 |    0 |    1 |   10 |   11 |
| Code 3 |    0 |   01 |  011 | 0111 |
| Code 4 |    1 |   01 |  001 |  000 |


## Exercice 5

<!-- Attention : l'exercice distribuée en cours cette année était erroné. Je propose cette nouvelle version -->
<!-- En effet, dans l'ancienne version, je faisais le lien entre longueur d'un code de longueur fixe et entropie, alors qu'il n'y en a pas. -->

Une source $X$ utilise un alphabet de cinq symboles.

1. Combien de bits sont nécessaires pour réaliser un code de longueur fixe à décodage unique ?

On décide de transmettre ces symboles en les regroupant deux par deux : cela revient à considérer une nouvelle source $Y$.

1. Combien y a-t-il de symboles dans l'alphabet de la source $Y$ ?
1. Combien de bits sont nécessaires pour réaliser un code de longueur fixe à décodage unique ?
1. Cette manière de procéder est-elle plus intéressante que pour la transmission de la source $X$ ?

<!-- % Une source $X$ utilise un alphabet de trois symboles $\{A,B,C\}$
% dont les probabilités respectives sont égales à $0,5$, $0,3$ et $0,2$.
% \begin{questions}
% 1. Calculez l'entropie de la source.
% 1. Combien de bits sont nécessaires pour réaliser un code de longueur fixe à décodage unique ?
% \end{questions}
% On décide alors de transmettre ces symboles en les regroupant par groupe de deux :
% cela revient à considérer une nouvelle source $Y$.
% \begin{questions}
% 1. Combien y a-t-il de symboles dans l'alphabet de la source $Y$ ?
% 1. Calculez l'entropie de la source $Y$.
% 1. Combien de bits sont nécessaires pour réaliser un code de longueur fixe à décodage unique ?
% 1. Cette manière de procéder est-elle plus intéressante que pour la transmission de la source $X$ ?
% \end{questions} -->

## Exercice 6

<!-- Proakis p. 96 -->

On considère l'alphabet défini ci-dessous :

| Symbole     | A    | B    | C    | D    | E    | F     | G     |
| ----------- | ---- | ---- | ---- | ---- | ---- | ----- | ----- |
| Probabilité | 0,35 | 0,30 | 0,20 | 0,10 | 0,04 | 0,005 | 0,005 |

1. Calculez l'auto-information des symboles, puis l'entropie de la source <!-- 2.11 -->
1. Déterminez le code de Huffman associé à la source.
1. Calculez la longueur moyenne du code obtenu. <!-- L = 2.21 -->

## Exercice 7

<!-- Proakis p. 96 -->

Mêmes questions que l'exercice précédent avec l'alphabet défini ci-dessous :

| Symbole     | A    | B    | C    | D    | E    | F     | G     | H     |
| ----------- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- |
| Probabilité | 0,36 | 0,14 | 0,13 | 0,12 | 0,10 | 0,009 | 0,004 | 0,002 |

<!-- H = 2.63, L = 2.70 -->
