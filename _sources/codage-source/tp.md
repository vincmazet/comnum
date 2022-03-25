# Travaux pratiques


```{admonition} Modules Python
Dans ce TP, nous aurons besoin des modules :
* [numpy](https://numpy.org/doc/stable/reference/index.html),
* [scipy](https://docs.scipy.org/doc/scipy/reference/index.html#api-reference),
* [matplotlib](https://matplotlib.org/stable/api/index.html),
* [skimage](https://scikit-image.org/docs/stable/api/api.html),
* [komm](http://komm.readthedocs.io/) (s'il n'est pas installé, tapez dans un terminal : `pip install komm`).
* [comnumfip](https://github.com/vincmazet/comnumfip) (à télécharger en zip et installer dans le répertoire de travail).
```

## Compression d'un texte

Un texte en français est transmis sur un canal binaire.
Le texte contient 16 000 caractères parmi les vingt-six lettres de l'alphabet (majuscules non accentuées)
et quatre signes de ponctuation (point `.`, virgule `,`, espace `⎵`, apostrophe `'`).

* Quelle est la taille de l'alphabet de la source ?

* Quelle est la taille de l'alphabet du canal ?

* Les symboles de la source peuvent-ils être considérés comme équiprobables ?

* Calculez l'entropie de la source.
  Le fichier probas.csv contient les probabilités d'occurrence des caractères en français (deuxième colonne) et en anglais (troisième colonne).
  Un fichier csv peut se charger avec `numpy.loadtxt` et le logarithme à base 2 se calcule avec la fonction `numpy.log2`.

* La transmission du texte se fait à une vitesse de 100 Mbits/s avec un taux d'erreur nul.
  À quel débit canal cela correspond-il ? En déduire la capacité du canal.

* D'après le théorème du codage canal,
  quel est le taux d'émission maximal pour pouvoir transmettre les données sans erreur ?

* En déduire le débit de la source puis le temps minimal théorique nécessaire pour transmettre le texte sans erreur.
  Aucun codage source sans perte ne pourra donc diminuer cette durée.

Dans la suite, trois codes sources sont évalués.


### Code ASCII

* Donnez la longueur moyenne du code ASCII.

* Déterminez la durée de transmission nécessaire du texte codé en ASCII.


### Code de Huffman binaire de première extension

Le code de Huffman binaire classique est dit « de première extension ».

* Calculez la longueur moyenne du code de Huffman de première extension.
  La fonction `komm.HuffmanCode` créer un objet dont on peut récupérer les codes avec la syntaxe `code.enc_mapping.values()`.

* Déterminez la durée de transmission nécessaire du texte codé avec ce code.


### Code de Huffman binaire de deuxième extension

Un code de deuxième extension est défini à partir d'un nouvel alphabet contenant les symboles originaux regroupés deux par deux.
Dans le cas considéré ici, le nouvel alphabet correspond aux symboles
{`AA`, `AB`, `AC`, ..., `',`, `'⎵`, `''`}.

* Calculez la longueur moyenne du code de Huffman de deuxième extension.
  Les probabilités des nouveaux symboles peuvent être calculées avec l'aide de `numpy.kron`.

* Déterminez la durée de transmission nécessaire du texte codé avec ce code.


## Compression d'une image

Nous allons étudier deux codages source sur une image à niveaux de gris (256 niveaux possibles) de taille 128 × 128.
Pour cela, vous disposez des images non compressées suivantes : smiley.png, schtroumpf.png, boat.png
(disponibles dans [comnumfip](https://github.com/vincmazet/comnumfip)).

* Quelle est la taille de l'alphabet de la source ?

* Les symboles de la source peuvent-ils être considérés comme équiprobables ?

* Calculez l'entropie de la source.

* En déduire la longueur moyenne Nminimale d'un code dans le cas d'une compression sans perte, puis la taille d'une image en bits.

* Chargez (`skimage.io.imread`) l'une des images précédentes puis affichez-la (`matplotlib.pyplot.imshow`).


### Compression sans perte

Le codage par plage (RLE : _run length encoding_, utilisé par exemple pour le format BMP) est une technique de compression sans perte.
Le principe est de remplacer toute séquence consécutive d'un même symbole par la taille de cette séquence suivi du symbole.
Par exemple, le message
> 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 133, 133, 133, 0

sera codé :

> 6, 255, 4, 0, 3, 133, 1, 0.

* Appliquez la compression RLE à l'image (`comnumfip.rleenc`).

* Vous pouvez ensuite appliquez la décompression RLE (`comnumfip.rledec`) et vérifier que vous retrouvez l'image initiale, sans défaut.

* On définit le taux de compression par :

  $$
    \text{Taux de compression} = \frac{\text{taille de l'image compressée}}{\text{taille de l'image non compressée}}.
  $$
  
  Quel taux de compression obtenez-vous ?

<!-- Codez la méthode de décompression et vérifiez qu'elle fonctionne correctement en affichant l'image décompressée. -->


### Compression avec perte

On peut autoriser la compression d'une image avec perte tout en conservant une qualité visuelle correcte.
Ainsi, le principe fondamental de la compression JPEG est de calculer la transformée en cosinus discrète (DCT : _discrete cosine transform_)
de l'image pour obtenir des coefficients qui seront quantifiés afin de réduire la taille de l'image.
Ce sont ces coefficients qui sont stockés ou transmis.
La transformation en cosinus discrète inverse permet de décoder l'image compressée.

* Appliquez la transformée en cosinus discrète (`scipy.fftpack.dctn`) sur l'image.
   Précisez l'argument `norm='ortho'`.
   La transformée obtenue est une image de même taille que l'originale,
   les basses fréquences se situent dans le coin en haut à gauche.

* Dans les images naturelles, l'énergie est surtout concentrée dans les basses fréquences :
   les hautes fréquences peuvent donc être grossièrement quantifiées voire carrément annulées.
   Pour annuler ces hautes fréquences, on peut procéder de la sorte :
   ```
   M, N = I.shape              # Taille de la DCT I
   m = np.arange(M)            # Liste des indices des lignes
   n = np.arange(N)            # Liste des indices des colonnes
   X, Y = np.meshgrid(m,n)     # Matrices des coordonnées
   F = 0.5                     # Facteur de compression (entre 0 et 1)
   mask = ((X+Y) < 2*M*F)      # Définit un masque triangulaire
   J = I*mask                  # Masquage de l'image
   ```
   Ces valeurs nulles n'étant pas transmises, quel taux de compression obtenez-vous ?

* Appliquez la transformée inverse (`scipy.fftpack.idctn`) sur l'image masquée puis affichez l'image compressée.

* Discutez la qualité de l'image compressée.
   On distingue la qualité visuelle de l'image (critère qualitatif et subjectif)
   et la qualité quantitative qui est souvent mesurée à l'aide du rapport signal-à-bruit (RSB).
   Le RSB quantifie l'erreur pixel par pixel entre l'image originale $f$ et l'image compressée $g$ (de taille $M \times N$) :
   
   $$
    \mathrm{RSB} = 10 \log_{10} \left( \frac{P_f}{P_{f-g}} \right)
   $$
   
   où $P_x$ représente la puissance de l'image $x$ :
   
   $$
     P_x = \frac{1}{MN} \sum_{m=1}^{M} \sum_{n=1}^{N} x(m,n)^2
   $$
   
   (vous pouvez utiliser `numpy.linalg.norm`).