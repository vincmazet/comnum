# Avant-propos

<br />

```{figure} figs/shannon1948.png
---
name: F:shannon1948
width: 500px
---
Représentation schématique d'une chaîne de communication proposée par C.E. Shannon en 1948.
```

<br />

Ce manuel est le support du cours de Communications numériques du diplôme FIP EII
de [Télécom Physique Strasbourg](http://www.telecom-physique.fr/).
Ce cours est accompagné d’exercices théoriques (à faire sur feuille) et pratiques (programmation en Python).
Une page [Moodle](http://moodle.unistra.fr/) accompagne l'apprentissage (accessible uniquement pour mes étudiants).
Pour compléter le cours, je vous conseille de lire les documents listés dans les {ref}`S:refs`.

Pour transmettre un message sous forme numérique, il faut passer par un ensemble d'étapes qui représentent la {ref}`S:chaine`.
Pour chaque étape au niveau de l'émetteur, on retrouve son pendant au niveau du récepteur : les étapes vont toujours par paire.
Dans ce cours, nous nous concentrons sur les trois blocs fondamentaux,
sans qui il ne serait presque pas possible de réaliser une communication numérique:
* le {ref}`codage source<S:codage-source:information>`, qui permet de transformer le message, quelle que soit sa nature, en séquence numérique,
* le {ref}`codage canal <S:codage-canal:intro>`, qui ajoute de la redondance d'information
  pour rendre la transmission plus robuste face aux perturbations de la transmission,
* la {ref}`modulation <S:modulation:intro>`, qui transforme la séquence numérique en un signal adapté à la transmission.


<!--

TODO

* Graphes, schémas en svg (avec savefig)
* hamorniser le look des figures : grilles, LaTeX, une taille correcte, etc.
* commandes (ex $\mathcal{F}$ ou pour écrire "Exercice X" où X s'incrémente)
  [substitutions](https://jupyterbook.org/content/content-blocks.html?highlight=substitution#substitutions-and-variables-in-markdown)
* Le book me permet d'aller plus vite en CM et de privilégier les exercices, interactions, discussions, etc.
* termes nouveaux et traduction anglaise: "on parle de modulation en **bande de base** (_baseband modulation_)"

QUESTIONS

* la police du book ne passe pas sur tout les PC (l'intégrer au CSS ?)
  > j'ai mis un @import dans le CSS : vérifier que c'est ok
* Synthèse en fin de chapitre/séance (take-way message, one minute paper, ticket to leave...),
  pour les obliger à synthétiser et à bénéficier de la mémoire kinesthésique.
* Corrections de TP accessibles (pas les codes : uniquement les résultats avec commentaires et questions en plus,
  mais comme en OFTI, ils risquent de demander ensuite du code pour reproduire le résultat...) ?
* Introduire de l'interactivité : certaines parties au tableau pour construire avec les étus
  (ex : leur demander de lister les différences entre deux méthodes) ?
* Intégrer des tests d'auto-évaluation (socrative, Moodle). {{wooclap}}
* Contrôles : papier ou Moodle ? Corrections : feuille avec liste des questions sous la main, ou projeter le test au VP ?
* TD : comment accéder au cours et aux formules ? (solutions : écrire formules au tableau, utiliser deux navigateurs,
  synthèse par les étus, smartphone des étus...)
* Méthodes pédagos à réfléchir : 1-table-tous ? Découper les séances en grains (chunks) de 10/15 min (présentation, application, évaluation...) ?
* Taxonomie SOLO
* Apprendre à poser les bonnes questions est préférable à emmagasiner les réponses toutes faite [source : Taddei]

-->