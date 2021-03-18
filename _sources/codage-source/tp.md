# Travaux pratiques


## Application de la théorie de l'information à la transmission d'un texte

<!-- bien faire comprendre la différence entre Shannon, bits, codes, symboles, ... -->

Un SMS en français est transmis sur un canal binaire.
Le texte contient $K=140$ caractères parmi les vingt-six lettres de l'alphabet (majuscules non accentuées)
et quatre signes de ponctuation (point, virgule, espace, apostrophe).

1. Quelle est la taille de l'alphabet de la source ?

1. Quelle est la taille de l'alphabet du canal ?

1. Les symboles de la source peuvent-ils être considérés comme équiprobables ?

1. Calculez l'entropie de la source.
   Le fichier probas.csv contient les probabilités d'occurrence des caractères en français (deuxième colonne) et en anglais (troisième colonne).
   Le logarithme à base 2 se calcule avec la fonction `numpy.log2`.

1. La transmission du texte se fait à une vitesse maximale de 10 bits/s avec un taux d'erreur nul.
   À quel débit canal cela correspond-il ? En déduire la capacité du canal.

1. D'après le second théorème de Shannon (théorème du codage canal),
   quel est le taux d'émission maximal pour pouvoir transmettre les données sans erreur ?

1. En déduire le débit de la source puis le temps minimal théorique nécessaire pour transmettre le texte sans erreur
   (aucun codage source sans perte ne permet donc de diminuer cette durée).

1. Que devient ce temps dans le cas d'un canal 8-aire (transmission 8-QAM par exemple),
   dans le cas d'un canal émettant 10 symboles par seconde ?

Pour réaliser la transmission sur le canal binaire, on propose de tester trois codes :
* le code ASCII classique qui code chaque symbole sur 8 bits ;
* un code de Huffman binaire de première extension ;
* un code de Huffman binaire de deuxième extension.
  Un code de deuxième extension est défini à partir d'un nouvel alphabet contenant les symboles originaux regroupés deux par deux.
  Dans le cas considéré ici, le nouvel alphabet correspond aux symboles $\{AA, AB, AC, \dots\}$.

1. Calculez la longueur moyenne de chaque code.
   La fonction `komm.HuffmanCode` créer un objet dont on peut récupérer les codes avec la syntaxe `code.enc_mapping.values()`.
   Pour calculer le dictionnaire associé au codage de Huffman de deuxième extention,
   il faut calculer les probabilités des nouveaux symboles avec `numpy.kron`.

1. Déterminez alors la durée de transmission nécessaire pour chaque code.


## Compression d'une image numérique

Nous allons étudier deux codages source sur une image à niveaux de gris (256 niveaux possibles), non compressée et de taille $128\times128$.
Pour cela, vous utiliserez l'une des images suivantes : smiley.png, schtroumpf.png, boat.png.

* Quelle est l'entropie de la source ?

* En déduire la longueur moyenne minimale d'un code dans le cas d'une compression sans perte, puis la taille d'une image en bits.

* Chargez (`imread`) l'une des images précédentes puis convertissez-la en double (`double`) avant de l'afficher
  (`imshow`, n'oubliez pas le deuxième argument qui permet de régler l'échelle des intensités !).

### Codage sans perte

Le codage par plage (RLE : _run length encoding_, utilisé par exemple pour le format BMP) est une technique de compression sans perte.
Le principe est de remplacer toute séquence consécutive d'un même symbole par la taille de cette séquence suivi du symbole.
Par exemple, le message
> $\{ 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255, 0 \}$
sera codé :
> $\{ 6, 255, 4, 0, 3, 255, 1, 0 \}$.


* Appliquez la compression RLE à l'image (\vcmd{rleenc}).

* On définit le taux de compression par :
  $$
    \text{Taux de compression} = 1 - \frac{\text{taille de l'image compressée}}{\text{taille de l'image non compressée}}.
  $$
  Quel taux de compression obtenez-vous ?

<!-- Codez la méthode de décompression et vérifiez qu'elle fonctionne correctement en affichant l'image décompressée. -->


### Codage avec perte

On peut autoriser la compression d'une image avec perte tout en conservant une qualité visuelle correcte.
Ainsi, le principe fondamental de la compression JPEG est de calculer la transformée en cosinus discrète (DCT : _discrete cosine transform_)
de l'image pour obtenir des coefficients qui seront quantifiés afin de réduire la taille de l'image.
Ce sont ces coefficients qui sont stockés ou transmis.
La transformation en cosinus discrète inverse permet de décoder l'image compressée.

1. Appliquez la transformée en cosinus discrète (`dct2`) sur l'image.
   La transformée obtenue est une image de même taille que l'originale,
   les basses fréquences se situent dans le coin en haut à gauche.

1. Dans les images naturelles, l'énergie est surtout concentrée dans les basses fréquences :
   les hautes fréquences peuvent donc être grossièrement quantifiées voire carrément annulées.
   Pour annuler ces hautes fréquences, on peut procéder de la sorte :
   ```
   C = length(D);              # Taille de l'image DCT D
   T = 0.5;                    # Taux de compression (entre 0 et 1)
   [X,Y] = meshgrid(1:C,1:C);  # Matrices des coordonnées
   M = ( (X+Y) <= 2*C*T );     # Définit un masque triangulaire
   imshow(M,[]);               # Affichage du masque
   E = D.*M;                   # Masquage de l'image
   ```
   Ces valeurs nulles n'étant pas transmises, quel taux de compression obtenez-vous ?

1. Appliquez la transformée inverse (_idct2_) sur l'image masquée des coefficient puis affichez l'image compressée.

1. Discutez la qualité de l'image compressée.
   On distingue la qualité visuelle de l'image (critère qualitatif et subjectif)
   et la qualité quantitative qui est souvent mesurée à l'aide du rapport signal-à-bruit (RSB).
   Le RSB quantifie l'erreur pixel par pixel entre l'image originale $I$ et l'image compressée $J$ (de taille $M \times N$) :
   $$
    \mathrm{RSB} = 10 \log_{10} \left( \frac{P_I}{P_{I-J}} \right)
   $$
   où $P_X$ représente la puissance de l'image $X$ :
   $$
     P_X = \frac{1}{MN} \sum_{m=1}^{M} \sum_{n=1}^{N} X(m,n)^2.
   $$

1. Concluez sur les deux méthodes de compression d'image étudiées.