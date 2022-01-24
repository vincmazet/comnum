(S:codage-canal:cycliques)=
# Codes cycliques


## Principe

```{margin}
Les codes BCH et Reed-Solomon sont des codes circulaires.
Ce sont des codes très répandus et que l'on retrouve notamment dans les communications spatiales et l'ADSL
ou certains supports de stockage comme les CD ou les QR codes.
```

Les codes cycliques sont des codes en blocs linéaires particuliers.
Ils ont le grand intérêt d'offrir un décodage simple.
Un code est cyclique si, lorsque $c=c_{n-1}c_{n-2}\dots c_1c_0$ est un mot du code,
alors $c=c_{n-2}c_{n-3}\dots c_0c_{n-1}$ (ou tout autre décalage circulaire des symboles)
est également un mot du code.

```{div} exemple
Le code à parité $C(3,2)$ consiste à ajouter à chaque mot de 2 bits un troisième bit,
de telle sorte que le nombre total de bit à 1 soit pair.
Les codes associés aux quatre messages possibles sont listés dans le tableau ci-dessous.

| $m$ | $c$ |
| --- | --- |
|  00 | 000 |
|  01 | 011 |
|  10 | 101 |
|  11 | 110 |

Ce code est cyclique car on peut effectuer on peut effectuer les décalages circulaires suivants :

$$
011 \rightarrow 110 \rightarrow 101 \rightarrow 011 \rightarrow \text{etc.}
$$

et un décalage circulaire sur $000$ revient à ce même mot.
```


## Polynôme générateur

Plutôt que de définir un code cyclique par des phrases ou un tableau de correspondance,
on le représente par un polynôme : c'est beaucoup plus court.
C'est ce qu'on appelle un **polynôme générateur** (_generator polynomial_).

Un bloc du message $m=m_{k-1}m_{k-2}\dots m_1m_0$ peut être représenté par le polynôme en $X$ dont les coefficients sont les symboles $m_k$.
Ainsi, on pourra écrire le message $m$ comme le polynôme

$$
m(X) = m_{k-1}X^{k-1} + m_{k-2}X^{k-2} + \dots + m_1X + m_0.
$$

De même, le code associé à ce message sera représenté par le polynôme

$$
c(X) = c_{n-1}X^{n-1} + c_{n-2}X^{n-2} + \dots + c_1X + c_0.
$$

Le calcul du code $c$ à partir du message $m$ s'effectue en multipliant $m(X)$ par le polynôme générateur $g(X)$.
Ce polynôme générateur est de degré $n-k$ :

$$
g(X) = X^{n-k} + g_{n-k-1}X^{n-k-1} + \dots + g_1X + g_0.
$$

```{div} exemple
Le polynôme générateur du code à parité $C(3,2)$, dont on a vu ci-avant qu'il était cyclique, est

$$
g(X) = X+1.
$$

Il est bien de degré $n-k=1$.

En effet :

| $m$ | $m(X)$ |   $c(X)=m(X)g(X)$ | $c$ |
| --- | ------ | ----------------- | --- |
|  00 |      0 |      $0(X+1) = 0$ | 000 |
|  01 |      1 |             $X+1$ | 011 |
|  10 |    $X$ |  $X(X+1) = X^2+X$ | 110 |
|  11 |  $X+1$ | $(X+1)^2 = X^2+1$ | 101 |

Notez que $2X=X+X=0$ quelle que soit la valeur de $X$
(souvenez-vous que $1+1=0$ dans le corps de Galois $\mathbb{F}_2$).

À la différence du premier tableau définissant le code à parité, le bit de parité est ici situé en deuxième position.

```

Bref, un code cyclique est représenté par son polynôme générateur.
Plus précisément, puisque ce sont seulement les coefficients du polynôme qui déterminent le code cyclique,
on ne représente celui-ci que par ses coefficients.
Et pour raccourcir encore plus leur représentation, on utilise une représentation octale qui correspond à la valeur en base 8 de groupes de trois coefficients.

Par exemple :
* le polynôme $g(X) =       X+1$ a pour coefficients   $11_2$ soit  $3_8$ en base 8 ;
* le polynôme $g(X) = X^3+X^2+1$ a pour coefficients $1101_2$ soit $15_8$ en base 8.


## Quelques codes cycliques

Les codes CRC (_cyclic redundancy check_) sont une forme particulière de codes cycliques.
Ils ne permettent que de détecter des erreurs, mais pas de les corriger.

Les codes BCH (du nom de leurs inventeurs : Bose, Chaudhuri, Hocquenghem en 1959-1960)
sont des codes cycliques binaires ou M-aires.
Il en existe de plusieurs longueurs et rendements et leur décodage est simple.
C'est pourquoi ils sont très utilisés comme codes de taille faible ou modérée,
comme par exemple en communication satellitaire, pour les disques optiques,
les disques durs et SSD ou les codes barres bi-dimensionnels.

```{dropdown} Polynômes générateurs des codes BCH

Le tableau ci-dessous donne les coefficients (en octal) des polynômes générateurs de quelques codes BCH binaires {ref}`[Proakis 2008]<S:refs>`.
Ces codes fournissent des mots de longueur $n$ à partir de blocs du message de taille $k$.
Le code résultant, de rendement $k/n$, a un pouvoir de correction égal à $t$.

Pour préciser les idées, le code BCH $(7,4)$ de coefficient $13_8=1011_2$ est donc le polynôme

$$
g(X) = 1 \cdot X^3 + 0 \cdot X^2 + 1 \cdot X^1 + 1 \cdot X^0 = g(X) = X^3 + X + 1.
$$

Il est capable de corriger $t=1$ erreur.

| $n$ | $k$ | $k/n$ | $t$ | coefficients de $g(X)$                   |
| --- | --- | ----- | --- | ---------------------------------------- |
| 7   | 4   | 0,57  | 1   | 13                                       |
| 15  | 11  | 0,73  | 1   | 23                                       |
|     | 7   | 0,47  | 2   | 721                                      |
|     | 5   | 0,33  | 3   | 2467                                     |
| 31  | 26  | 0,84  | 1   | 45                                       |
|     | 21  | 0,68  | 2   | 3551                                     |
|     | 16  | 0,52  | 3   | 107657                                   |
|     | 11  | 0,35  | 5   | 5423325                                  |
|     | 6   | 0,19  | 7   | 313365047                                |
| 63  | 57  | 0,90  | 1   | 103                                      |
|     | 51  | 0,81  | 2   | 12471                                    |
|     | 45  | 0,71  | 3   | 1701317                                  |
|     | 39  | 0,62  | 4   | 166623567                                |
|     | 36  | 0,57  | 5   | 1033500423                               |
|     | 30  | 0,48  | 6   | 157464165547                             |
|     | 24  | 0,38  | 7   | 17323260404441                           |
|     | 18  | 0,29  | 10  | 1363026512351725                         |
|     | 16  | 0,25  | 11  | 6331141367235453                         |
|     | 10  | 0,16  | 13  | 472622305527250155                       |
|     | 7   | 0,11  | 15  | 5231045543503271737                      |
| 127 | 120 | 0,94  | 1   | 211                                      |
|     | 113 | 0,89  | 2   | 41567                                    |
|     | 106 | 0,83  | 3   | 11554743                                 |
|     | 99  | 0,78  | 4   | 3447023271                               |
|     | 92  | 0,72  | 5   | 624730022327                             |
|     | 85  | 0,67  | 6   | 130704476322273                          |
|     | 78  | 0,61  | 7   | 26230002166130115                        |
|     | 71  | 0,56  | 9   | 6255010713253127753                      |
|     | 64  | 0,50  | 10  | 1206534025570773100045                   |
|     | 57  | 0,45  | 11  | 33526525205705053517721                  |
|     | 50  | 0,39  | 13  | 54446512523314012421501421               |
|     | 43  | 0,34  | 14  | 17721772213651227521220574343            |
|     | 36  | 0,28  | 15  | 3146074666522075044764574721735          |
|     | 29  | 0,23  | 21  | 403114461367670603667530141176155        |
|     | 22  | 0,17  | 23  | 123376070404722522435445626637647043     |
|     | 15  | 0,12  | 27  | 22057042445604554770523013762217604353   |
|     | 8   | 0,06  | 31  | 7047264052751030651476224271567733130217 |

```