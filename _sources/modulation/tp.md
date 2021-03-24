# Travaux pratiques


```{note}
Dans la réalité, les signaux qui circulent sur le canal sont analogiques car le canal de communication est physique.
Comme la chaîne de communications est ici simulée, l'ordinateur traite en fait des signaux numériques !
Il sera donc parfois nécessaire de fixer une fréquence d'échantillonnage qui n'a aucune interprétation physique...
```


## Modules Python

Les TP nécessitent d'utiliser les modules classiques
[numpy](https://numpy.org/doc/stable/reference/index.html),
[scipy](https://docs.scipy.org/doc/scipy/reference/index.html#api-reference),
[matplotlib](https://matplotlib.org/stable/api/index.html),
mais également
[komm](https://komm.readthedocs.io/en/latest/) et
[comnum](https://github.com/vincmazet/comnum/tree/main/_static/comnum).


## Étude de quelques modulations numériques

L'objectif de cet exercice est d'implémenter et de comparer quelques modulations numériques :
* NRZ (_non-return-to-zero_) binaire ;
* Manchester ;
* AMI (_bipolar alternate mark inversion_) ;
* BPSK (_binary phase-shift keying_) ;
* 16-QAM (_quadrature amplitude modulation_).

Ces modulations sont étudiées et comparées à la fois dans le domaine temporel et dans le domaine fréquentiel.

1. Créez une séquence binaire aléatoire $x_2$ de $N$ bits (`randmary`)
   et convertissez-la en séquence hexadécimale $x_{16}$ (`bin2mary`) :
   vous disposez donc du même message disponible sous deux représentations différentes.
   Affichez-les avec `print`.

1. Appliquez les modulations `mod_a`, `mod_b`, `mod_c`, `mod_d` sur la séquence binaire, et `mod_e` sur la séquence hexadécimale.
   Identifiez chacune de ces modulations.

1. L'analyse spectrale des modulations peut être effectuée à l'aide de la densité spectrale de puissance,
   qui est le carré du module de la transformée de Fourier.
   En choisissant un message suffisamment long ($N$ grand),
   représentez la densité spectrale de puissance de chaque modulation en échelle décimale en utilisant la méthode du périodogramme
   (`scipy.signal.periodogram`, en fixant la fréquence d'échantillonnage égale à $100/T$ où $T$ est la durée d'un bit).

1. Identifiez les modulations en bande de base et les modulations sur porteuse.

1. Comparez les codes en termes de simplicité de mise en œuvre, de largeur de bande, de téléalimentation possible,
   de robustesse au bruit, d'inversion de polarité et de détection d'interruption de la transmission.

1. D'après vos conclusions, quel type de modulation est le plus adapté aux communications suivantes ?
   * bus informatique (I2C, SATA...) ou de terrain (ASI, Modbus...) ;
   * liaison Wi-Fi ;
   * périphérique USB et ordinateur ;
   * téléphone mobile et antenne relais.

<!--
Intérêt du code de Gray
* Tracez la constellation (\vcmd{constellation}) du signal modulé en QAM16 (donc en sortie de l'émetteur).
* Que devient cette constellation lorsque le signal modulé est transmis via un canal idéal (de bande passante infinie)
  mais bruité (\vcmd{channel})~?
  %utilisez la fonction \vcmd{awgnoise} pour ajouter du bruit)
  %Pour la simulation du canal, vous pourrez prendre par exemple une bande passante du filtre de \question{0~Hz}
  %et un rapport signal-à-bruit de \question{0~dB}.
* En déduire les conséquences possibles pour la détection du message, et l'intérêt du code de Gray%
  \footnote{On rappelle que le code de Gray est un code binaire où un seul bit change d'état entre deux nombres consécutifs.
  Pour deux bits, on compte donc~: 00, 01, 11 et 10.}
  pour les modulations QAM.
-->


## Transmission en bande de base sur un canal idéal

Le principe d'une transmission en bande de base est représenté ci-dessous :

```{image} ../figs/transmission.png
:width: 100%
```

Un canal est dit idéal si sa largeur de bande est infinie :
sa réponse impulsionnelle est alors $g(t)=K\,\delta(t-\tau)$ où $K$ et $\tau$ sont l'atténuation et le retard du signal reçu
(sans perdre en généralité, on pourra prendre $K=1$ et $\tau=0$).

Un filtre adapté permet de détecter les formes d'onde $h(t)$ dans le signal bruité $y(t)$.

1. Donnez l'expression du signal reçu $y(t)$ en fonction du signal émis $x(t)$ et des caractéristiques du canal.
   <!-- y(t) = K\,x(t-\tau) + b(t) -->

1. Simulez la transmission d'un message codé en NRZ binaire (`randmary`, `mod_d`, `channel`).
   On rappelle qu'on considère le canal est idéal, donc que sa largeur de bande est infinie (`Inf`).
   Observez le signal en entrée du détecteur pour différents niveaux de bruit.
   <!--
   Dans la fonction channel.m, je préfère définir l'écart-type du bruit plutôt que le RSB, car lors de l'émission
   d'un signal nul, je ne conserve pas la même puissance du bruit. De plus, on peut toujours calculer le RSB à partir
   de l'écart-type défini.
   -->

1. Dans un premier temps, on ne tient pas compte du filtre de réception : $r(t) = \delta(t)$.
   Échantillonnez (`sampling`) le signal $z(t)=y(t)$ et appliquez un seuil pour retrouver, tous les $T$,
   les symboles $\alpha_k$ émis.
   <!--
    En prenant un seuil égal à la moyenne des niveaux hauts et bas du signal émis,
    cela revient à faire une décision au sens du maximum de vraisemblance.
   -->

1. Dans un deuxième temps, appliquez le filtre de réception.
   Le filtre adapté peut s'implémenter à l'aide d'une corrélation,
   mais on peut montrer qu'il peut également s'écrire comme une convolution
   en utilisant `conv` (précisez le troisième argument `'same'` pour conserver des signaux de même taille).
   La réponse impulsionnelle du filtre adapté peut être obtenue à l'aide de `mod\_d`.
   Effectuez le seuillage et l'échantillonnage comme dans la question précédente.

1. Calculez les taux d'erreurs obtenus avec et sans filtre de détection.
   Comment varie la qualité de la détection en fonction du niveau de bruit ?
   <!--
    En Matlab, il existe pdist, mais son utilisation est moins évidente (il faut définir une matrice dont les deux
    colonnes correspondent aux signaux), et cela n'oblige pas les étudiants à comprendre cette distance en la recodant.
   -->


## Transmission en bande de base sur un canal à bande limitée

Cette fois, on suppose le canal sans bruit mais à bande limitée.
On peut alors être en présence d'IES lorsque les valeurs du signal $z(t)$ aux instants $T$
dépendent de plusieurs symboles $\alpha_k$.
La détection est alors perturbée même s'il n'y a pas de bruit.

* Simulez l'émission d'un message codé en NRZ binaire.
  Observez le signal en entrée du récepteur pour différentes fréquences de coupure du canal.

* Le diagramme de l'œil correspond aux différentes traces d'un signal affichées sur une période.
  Tracez le diagramme de l'œil (`eyediag`) de $y(t)$ : que se passe-t-il lorsque la bande passante du canal varie ?

<!--
  Quelle est la condition sur le signal temporel $y(t)$ pour éviter les IES~?
  Comment se traduit-elle sur la transformée de Fourier de $y(t)$~? % critère de Nyquist
  En déduire pourquoi une forme d'onde rectangulaire n'est pas adaptée
  lorsque la bande passante du canal est trop faible.
-->

* Lorsque la bande passante du canal est trop faible, la forme d'onde rectangulaire n'est pas adaptée.
  Il est préférable d'utiliser une forme d'onde en racine de cosinus surélevé (\vcmd{modnrzrrc}).
  Simulez la transmission du message avec cette nouvelle forme d'onde,
  notamment en observant le diagramme de l'\oe{}il pour plusieurs valeurs de~$\alpha$.

* Simulez l'opération de détection en comparant les deux formes d'onde.

<!-- Répartition optimale du filtrage entre l'émission et la réception ? -->

<!-- Probabilité d'erreur minimale sur un canal à bande limitée ? -->