# Codage d'une source sans mémoire

Un code source associe à chaque symbole $x_m$ de la source un « mot » formé de $l_m$ symboles issus de l'alphabet du canal.
Par exemple, le symbole `A` d'une source texte pourra être codé par le mot `01000001` formé de 8 symboles du canal (en l'occurrence, des bits).

On définit la **longueur moyenne d'un code** par la moyenne des longueurs de chaque symbole de la source, pondérés par leur probabilité :

$$
L = \sum_{m=1}^M p_m \cdot l_m.
$$

L'unité de la longueur moyenne est le symbole (du canal) par symbole (de la source).
La longueur moyenne d'un code a donc une influence directe sur le temps de transfert du message :
dans cet optique, on veillera à utiliser des codes de longueur moyenne la plus petite possible.


## Théorème du codage source

<!-- Shannon 1948, théorèmes 3 et 4 + Proakis, théorème p. 91 et équation 3.3-51 -->

Ce théorème est aussi appelé premier théorème de Shannon ou _noiseless coding theorem_ et dit que :

> La longueur moyenne $L$ d'un code associé à une source $X$ d'entropie $H(X)$
  doit être supérieur à $H(X)$ pour que la transmission se fasse à un taux d'erreur arbitrairement petit.

Cela signifie que la condition $L \geq H(X)$ doit être respectée si on veut avoir une chance de transmettre un message sans erreur.
La longueur minimale d'un code est donc égale à l'entropie.
Malheureusement, ce théorème ne dit pas comment construire un tel code...


## Propriété des codes sources

* Un code de **longueur fixe** est un code dont tous les mots ont le même nombre de symboles.
  Sinon, le code est de **longueur variable**.

* Un code à **décodage unique** n'admet aucune ambiguité lors de son décodage.
  Par exemple, le code qui à `A` associe `1` et à `B` associe `11` n'est pas à décodage unique
  (et oui ! Quel est le message si on reçoit `111` ?).

* Un code **instantané** permet de décoder chaque symbole sans avoir à attendre le symbole suivant.
  Par exemple, le code qui à `C` associe `01` et à `D` associe `011` n'est pas instantané
  car pour décoder `C` il faut attendre le bit suivant.
  
<a class="btn btn-light" href="td.html#exercice-3" role="button">Exercice 3</a>
<a class="btn btn-light" href="td.html#exercice-4" role="button">Exercice 4</a>
<a class="btn btn-light" href="td.html#exercice-5" role="button">Exercice 5</a>


## Codage de Huffman

Le codage de Huffman (1952) fournit un code instantané, à décodage unique, de longueur variable mais dont la longueur moyenne est la plus petite possible.
Il peut s'appliquer quel que soit la taille $M$ de l'alphabet de la source.

La procédure pour construire un code de Huffman dans le cas binaire est la suivante :

1. ordonner les symboles dans l'ordre des probabilités décroissantes :

   $$
   x_1,\dots,x_M
   \quad\text{tel que}\quad
   p(x_1) \geq \dots \geq p(x_M),
   $$

2. affecter au symbole de plus faible probabilité $x_M$ le bit `0`,

3. affecter au deuxième symbole de plus faible probabilité $x_{M-1}$ le bit `1`,

4. combiner $x_M$ et $x_{M-1}$ pour former un nouveau symbole de probabilité $p(x_M)+p(x_{M-1})$,

5. retourner à l'étape 2 tant qu'il reste plus de un seul symbole.

Un exemple de codage de Huffman est représenté dans l'animation ci-dessous, où les probabilités peuvent être définies.

<br />

<script src="_static/js/huffman.js"></script>
<div id='huffman' class='spetsi'></div>

<a class="btn btn-light" href="td.html#exercice-6" role="button">Exercice 6</a>
<a class="btn btn-light" href="td.html#exercice-7" role="button">Exercice 7</a>
