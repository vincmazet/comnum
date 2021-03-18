# Introduction

## Quelques définitions

Les **communications numériques** (_digital communication_) concernent la transmission
d'un **message** d'un émetteur vers un ou plusieurs récepteurs.
L'émetteur et le récepteur peuvent être des machines, des supports de stockage ou des humains.
Le message correspond à une suite de **symboles**, l'ensemble de tous les symboles possibles est appelé un **alphabet**.
Une communication est numérique lorsque le nombre de symboles dans l'alphabet est fini,
à la différence d'une communication analogique pour laquelle il existe un nombre infini de symboles possibles.

Si $M$ est la taille de l'alphabet, c'est-à-dire le nombre de symboles le constituant,
alors on dit que la communication est **M-aire** (ou **binaire** si $M=2$).

```{div} exemple

* La transmission entre un ordinateur personnel et un serveur web est numérique :
  seulement deux types de symboles peuvent être transmis (0 et 1).
  La communication est donc binaire ($M=2$).

* En Morse, qui est aussi un type de communications numériques, on peut considérer que $M=3$ :
  les symboles de l'alphabet sont le point, le trait et le silence.
  
* Entre un automobiliste et un feu de signalisation, la communication est également numérique !
  Il y a dans ce cas trois types de symboles : vert, orange et rouge ($M=3$).
  En Allemagne, il y a un quatrième symbole avec le orange-rouge et donc $M=4$.

* Entre deux humains, la communication est traditionnellement analogique ;
  la voix, même si elle utilise un nombre possible de mots qui est fini, est modulée par l'intonation, l'expression faciale.
  Cependant, il existe des cas où la communications entre deux humains est numérique,
  comme sur les pistes d'aéroport entre le pilote d'un avion et le [marshaller](https://fr.wikipedia.org/wiki/Marshaller).

```

## L'intérêt du numérique

La popularité croissante du numérique dans les communications est due à plusieurs facteurs.

```{toggle}
* Le numérique permet le routage (décision du chemin que prennent les messages)
  et l'adressage (procédé de définition et la destination) dans un système multi-utilisateur
  (comme pour le courrier électronique).
```

```{toggle}
* Des messages de natures différentes peuvent être transmis via le même canal
  (la fameuse offre _triple-play_ des box internet qui permettent d'acheminer du contenu web,
  des signaux de télévision ou de la voix pour le téléphone).
```

```{toggle}
* Le chiffrement de données est plus simple et plus performant qu'en analogique.
```

```{toggle}
* Le stockage et la lecture d'information sur un support physique (disque dur SSD par exemple)
  sont à la fois rapides et parfaits en comparaison à leur équivalent analogique (cassette par exemple).
```

```{toggle}
* La reconstitution du message pendant le transfert pour limiter sa dégradation est possible
  (par exemple, le premier câble à fibre optique transatlantique [TAT-8](https://en.wikipedia.org/wiki/TAT-8)
  utilisait une centaine de répéteurs sous l'océan).
```

```{toggle}
* Les circuits d'électronique numérique sont généralement plus fiables et moins coûteux que les circuits analogiques équivalents.
```

```{toggle}
* Les caractéristiques des sytèmes de communication numérique peuvent facilement être mis à jour
  puisqu'il suffit de modifier le logiciel plutôt que le matériel.
```