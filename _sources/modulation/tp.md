# Travaux pratiques


Remarque préliminaire :
dans la réalité, les signaux qui circulent sur le canal sont analogiques car le canal de communication est physique.
Comme la chaîne de communications est ici simulée, l'ordinateur traitera toujours des signaux numériques !
Il sera donc parfois nécessaire de fixer une fréquence d'échantillonnage qui n'a aucune interprétation physique...

Importation du module [comnum](www.unistra.fr)
Utilisez la syntaxe

```
help(fonction)
```

pour obtenir l'aide de la fonction `fonction`.

https://github.com/vincmazet/comnum/blob/main/_static/comnum/README.md

[ComNum](_static/comnum/README.md)


## Étude de quelques modulations numériques

L'objectif de cet exercice est d'implémenter et de comparer quelques modulations numériques :
* NRZ (_non-return-to-zero_) binaire ;
* Manchester ;
* AMI (_bipolar alternate mark inversion_) ;
* BPSK (_binary phase-shift keying_) ;
* 16-QAM (_quadrature amplitude modulation_).

1. Créez une séquence binaire aléatoire $x_2$ de $N$ bits (`randmary`)
   et convertissez-la en séquence hexadécimale $x_{16}$ (`bin2mary`) :
   vous disposez donc du même message disponible sous deux représentations différentes.
   Affichez-les avec `print`.

1. Appliquez les modulations `mod_a`, `mod_b`, `mod_c`, `mod_d` sur la séquence binaire,
   et `mod_e` sur la séquence hexadécimale.
   Identifiez chacune de ces modulations.

1. L'analyse spectrale des modulations peut être effectuée à l'aide de la densité spectrale de puissance,
   qui est le carré du module de la transformée de Fourier.
   En choisissant un message suffisamment long ($N$ grand),
   représentez la densité spectrale de puissance de chaque modulation en échelle décimale
   en utilisant la méthode du périodogramme (`periodogram`, les deuxième et troisième arguments de la fonction
   peuvent être laissé libres, le quatrième sera égal à $100/T$ où $T$ est la durée d'un bit).

1. Identifiez les modulations en bande de base et les modulations sur porteuse.

1. Comparez les codes en termes de simplicité de mise en œuvre, de largeur de bande,
   de téléalimentation possible, de robustesse au bruit,
   d'inversion de polarité
   et de détection d'interruption de la transmission.
  <!-- de possibilité de synchronisation -->

1. D'après vos conclusions, quel type de modulation est le plus adapté aux communications suivantes~?
   * bus informatique (I2C, SATA...) ou de terrain (ASI, Modbus...) ;
   <!--
   I2C : NRZ; PCI : ?; SATA : 8b/10b encoding, ASI : Manchester, Modbus : NRZ ?, KNX : sorte de Manchester,
   HART : FSK binaire superposé au 4-20 mA)
   -->
   * liaison Wi-Fi~; <!-- Porteuse (QAM, PSK, ou autre suivant la version de la norme) -->
   * périphérique USB et ordinateur ; <!-- Bande de base (NRZI) -->
   * téléphone mobile et antenne relais. <!-- Porteuse (GSM = 900 MHz et 1800 MHz, avec variantes) -->
<!-- sonde spatiale et Terre~;                                             % Porteuse -->
<!-- communication par laser à l'air libre entre deux bâtiments~;          % OOK ? -->
<!-- manette de jeu sans fil (fréquences radio) et console de jeu~; % Porteuse -->
<!-- téléphone fixe d'un abonné et commutateur (liaison classique France Telecom)~; % Bande de base (BHD3 est utilisé pour les liaisons MIC à 2Mbps) -->
<!-- téléphone fixe d'un abonné et serveur central (liaison par \og{}box\fg{} ADSL)~; % Porteuse (VoIP) -->
<!-- télécommande infrarouge et téléviseur~; % Bande de base (Manchester, 950 nm) -->

<!--
 - largeur de sa plage de fréquences : la plus étroite possible
  - téléalimentation : peu de puissance aux faibles fréquences, aucune à la fréquence nulle
  - codage de l'horloge : fréquence suffisante des transitions + synchronisation de l'horloge du récepteur sur le signal reçu
  - résistance au bruit : espacement des niveaux
  - complexité du codage : coût et vitesse de codage
  - dépendance à la polarité : facilité d'installation (Manchester?, AMI, NRZI)
  - équilibrage :
      mesure approximative de l'influence du codage sur des symboles successifs
      Running Digital Sequence : RDS({ak}) = \sum_k ak .
      DRDS({ak}) = max(abs{RDS({aj}) tel que {aj} sous-suite valide de {ak}}).
  - les transmissions en bande de base ont le grand intérêt d'être simples à mettre en place
    et sont donc utilisées dans de nombreux domaines où les communications se font sur de courtes distances.
 -->


% \exo{Intérêt du code de Gray}
%
% \begin{questions}
%
%   \item Tracez la constellation (\vcmd{constellation}) du signal modulé en QAM16 (donc en sortie de l'émetteur).
%
%   \item Que devient cette constellation lorsque le signal modulé est transmis via un canal idéal (de bande passante infinie) mais bruité (\vcmd{channel})~?
%   %utilisez la fonction \vcmd{awgnoise} pour ajouter du bruit)
%   %Pour la simulation du canal, vous pourrez prendre par exemple une bande passante du filtre de \question{0~Hz} et un rapport signal-à-bruit de \question{0~dB}.
%
%   \item En déduire les conséquences possibles pour la détection du message, et l'intérêt du code de Gray%
%   \footnote{On rappelle que le code de Gray est un code binaire où un seul bit change d'état entre deux nombres consécutifs.
%   Pour deux bits, on compte donc~: 00, 01, 11 et 10.}
%   pour les modulations QAM.
%
% \end{questions}


## Transmission en bande de base sur un canal idéal

Le principe d'une transmission en bande de base est représenté ci-dessous :

```
\includegraphics{transmission}
```

Un canal est dit idéal si sa largeur de bande est infinie :
sa réponse impulsionnelle est alors $g(t)=A\,\delta(t-\tau)$
où $A$ et $\tau$ sont l'atténuation et le retard du signal reçu
(sans perdre en généralité, on pourra prendre $A=1$ et $\tau=0$).

Un filtre adapté permet de détecter les formes d'onde $h(t)$ dans le signal bruité $y(t)$.
<!-- La détection des formes d'onde $h(t)$ dans le signal bruité $y(t)$, -->
<!-- est effectuée à l'aide d'un filtre adapté de réponse impulsionnelle $r(t) = h(-t)$. -->

* Donnez l'expression du signal reçu $y(t)$ en fonction du signal émis $x(t)$ et des caractéristiques du canal.
  <!-- y(t) = A\,x(t-\tau) + b(t) -->

* Simulez la transmission d'un message codé en NRZ binaire (`randmary`, `mod_d`, `channel`).
  On rappelle qu'on considère le canal est idéal, donc que sa largeur de bande est infinie (`Inf`).
  Observez le signal en entrée du détecteur pour différents niveaux de bruit.
  <!--
   Dans la fonction channel.m, je préfère définir l'écart-type du bruit plutôt que le RSB, car lors de l'émission
   d'un signal nul, je ne conserve pas la même puissance du bruit. De plus, on peut toujours calculer le RSB à partir
   de l'écart-type défini.
  -->

* Dans un premier temps, on ne tient pas compte du filtre de réception : $r(t) = \delta(t)$.
  Échantillonnez (`sampling`) le signal $z(t)=y(t)$ et appliquez un seuil pour retrouver, tous les $T$,
  les symboles $\alpha_k$ émis.
  <!--
    En prenant un seuil égal à la moyenne des niveaux hauts et bas du signal émis,
    cela revient à faire une décision au sens du maximum de vraisemblance.
  -->

* Dans un deuxième temps, appliquez le filtre de réception.
  Le filtre adapté peut s'implémenter à l'aide d'une corrélation,
  mais on peut montrer qu'il peut également s'écrire comme une convolution
  en utilisant `conv` (précisez le troisième argument `'same'` pour conserver des signaux de même taille).
  La réponse impulsionnelle du filtre adapté peut être obtenue à l'aide de `mod\_d`.
  Effectuez le seuillage et l'échantillonnage comme dans la question précédente.

* Calculez les taux d'erreurs obtenus avec et sans filtre de détection.
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