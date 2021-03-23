# Canal de transmission

Les canaux étant des dispositifs physiques, le signal qui y circule est toujours analogique,
même si l'information reste codée par un message numérique. 
La transmission est souvent perturbée par deux phénomènes qui limitent la quantité de données pouvant être transmises :
* du bruit, qui peut être électronique (produits par les composants),
  électromagnétique (dû aux rayons cosmiques) ou des interférences avec d'autres signaux (phénomène de diaphonie) ;
* des distorsions dues aux limitations physiques du canal ou aux imperfections des équipements :
  - atténuation du signal,
  - distortion d'amplitude et de phase,
  - échos (trajets multiples),
  - largeur de bande du canal limité.

Pour ces raisons, un canal et souvent modélisé, en première approche, par un filtre passe-bas et un bruit additif :

```{figure} ../figs/modele-canal.svg
---
width: 50%
name: F:modele-canal
---
Modèle simple d'un canal.
```


Il existe plusieurs familles de canaux, avec leurs caractéristiques propres, qui sont listés ci-dessous.


## Câble électrique

Un câble électrique simple est constitué de deux fils conducteurs d'électricité.
On distingue notamment :
* le câble simple où les deux fils sont côte à côte,
* la paire torsadée ({numref}`F:paire-torsadee`) où les deux fils sont enroulés l'un sur l'autre : on limite ainsi les interférences et la diaphonie,
  et on utilise ce type de canal pour des communications sur de courtes distances.
  <!-- BP : plusieurs centaines de kilohertz / distortion amplitude phase diaphonie -->
* le câble coaxial ({numref}`F:cable-coaxial`) où l'un des deux fils est en fait un treillis qui entoure l'autre fil.
  Ainsi, les interférences avec d'autres dispositifs sont extrêmement réduites.
  Le câble coaxial est utilisé dans certains réseaux Ethernet ou pour transmettre un signal vidéo sur quelques dizaines de mètres.
  Les premiers câbles sous-marin étaient co-axiaux, mais ils sont maintenant largement dépassés par les câbles à fibre optique.
  <!-- bande passante plusieurs mégahertz distortion amplitude phase application connexion entre centraux téléphoniques  -->

```{figure} https://upload.wikimedia.org/wikipedia/commons/f/f3/Futp_cable.jpg
---
width: 50%
name: F:paire-torsadee
---
Paires torsadées.
```

```{figure} https://upload.wikimedia.org/wikipedia/commons/7/73/RG-59.jpg
---
width: 50%
name: F:cable-coaxial
---
Câble coaxial.
```


## Fibre optique

Une fibre optique est un fil en verre ou en plastique qui conduit la lumière entre ses deux extrémités avec très peu de pertes.
De ce fait, elle présente très peu de distorsion et n'introduit quasiment pas de bruit.
La fibre optique est utilisée à tous les niveaux de l'architecture de communication : des câbles sous-marins aux logements.
<!-- BP : > 10 GHz, débit : 10 Gbits/s -->

```{figure} https://upload.wikimedia.org/wikipedia/commons/e/e6/Optical_breakout_cable.jpg
---
width: 50%
name: F:fibre-optique
---
Illustration d'un câble contenant plusieurs fibres optiques.
```


## Canal électromagnétique

Le canal électromagnétique regroupe tous les milieux où les ondes électromagnétiques
(comme les ondes radio ou la lumière) peuvent se déplacer.
Typiquement, il s'agit de l'air libre.
On distingue trois types de propagation :
* la propagation en ligne de mire qui permet des communications très haute fréquence ;
  elle est utilisé en téléphonie mobile ou pour la communication par laser entre bâtiments
* la propagation par onde de sol : l'atmosphère joue le rôle d'un guide d'onde ;
  elle permet des communications à très basses fréquence et autorise la diffusion du message dans le monde entier
  (par exemple en navigation)
* la propagation ionosphérique où les ondes rebondissent sur la ionosphère et la surface de la Terre.

<!-- SCHEMAS -->


## Canaux acoustiques sous-marins

La communication dans l'eau est très difficile car les ondes électromagnétiques ne se propage pas bien sur de longues distances.
À l'inverse, les signaux acoustiques peuvent s'étendre sur des centaines de kilomètres
(les grands cétacés peuvent communiquer de cette façon).
Cependant, la communication acoustique sous-marine est sujette à des atténuations fortes et des trajets multiples
en raison des réflexions à la surface et au fond de l'océan.
Néanmoins, elle est utilisée pour certains robots sous-marin ou des télémètres (comme des tsunamètres).


## Stockage

Stocker une information numérique est d'un certain point de vue équivalent à transmettre cette information :
on y retrouve notamment les notions de codage source et codage canal.
Le stockage d'une information numérique peut se faire dans une mémoire électronique (disque SSD par exemple),
une bande magnétique, disque optique, et même du papier (code barre et QR code) !
