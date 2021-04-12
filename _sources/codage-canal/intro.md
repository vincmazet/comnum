(S:codage-canal:intro)=
# Introduction


Pour réduire les erreurs de transmission, l'idéal est de diminuer le bruit et les interférences dus au canal.
Mais dans la pratique, on ne peut pas les annuler complètement car souvent le canal n'est pas entièrement configurable.
Une autre solution pour réduire les erreurs de transmission est d'augmenter la puissance du signal émis pour augmenter le RSB du signal reçu.
Or, cela implique une augmentation de la consommation énergétique et, parfois, d'un rayonnement plus fort.
Une troisième possibilité est d'introduire de la rendondance dans le signal : c'est ce qu'on appelle le codage canal.
Cependant, l'ajout de redondance aura automatiquement pour effet d'allonger la durée d'émission ou d'accroître la bande de fréquence occupée.

On peut alors se demander pourquoi ajouter de la redondance alors que le bloc précédent dans la chaîne de communication
(le codage source) avait notamment pour objectif de la réduire ?
En fait, la redondance introduite par le codage canal est contrôlée et interprétable.
Ainsi, le récepteur sera en mesure d'utiliser à bon escient cette redondance pour décoder le message et le corriger si nécessaire,
alors que l'information supplémentaire présente dans le message avant sa compression par le codage source n'est pas utilisable.


## Deux familles de codage canal

Il existe deux grandes familles de codage canal.
* Les **{ref}`codes en bloc<S:codage-canal:bloc>`** (_block codes_) consistent à découper le message en petits blocs de symboles,
  pour chacun desquels est associé un code (on peut citer comme exemple le code à parité).
  Parmi eux, les **{ref}`codes cycliques<S:codage-canal:cycliques>`** (_cyclic codes_) sont une classe particulière de codes en blocs.
* Les **{ref}`codes convolutifs<S:codage-canal:conv>`** (_convolutional codes_) où tout le message est codé, sans découpage en blocs :
  le message passe dans un système dont la sortie est le message codé.
  On peut modéliser ce fonctionnement par une convolution.

Dans le cadre de ce cours, nous distinguerons ces deux types,
bien que beaucoup d'applications pratiques combinent ces deux familles de codes.
Par ailleurs, pour simplifier l'exposé, nous considèrons exclusivement des codes linéaires et binaires,
même s'il existe des codes non linéaires ou M-aire.

Enfin, notons que les codes correcteurs d'erreur sont un cas particulier des codes canal,
car il existe des codes qui ne sont capables que de détecter des erreurs, sans les corriger.


## Corps de Galois

Les opérations de codage et décodage se font, mathématiquement, à l'aide d'additions et de multiplications sur des symboles binaires
(ou, plus généralement, en $M$-aire).
L'addition et la multiplication sont définies de la façon suivante.

````{panels}

Addition
^^^

L'opération $+$ est équivalente à un « ou exclusif ».

$$
0 + 0 = 0 \\
0 + 1 = 1 \\
1 + 0 = 1 \\
1 + 1 = 0
$$

---

Multiplication
^^^
L'opération $\cdot$ est équivalente à un « et ».


$$
0 \cdot 0 = 0 \\
0 \cdot 1 = 0 \\
1 \cdot 0 = 0 \\
1 \cdot 1 = 1
$$

````

L'ensemble $\{0,1\}$ muni de cette addition et de cette multiplication est noté $\mathbb{F}_2$
et s'appelle le corps de [Galois](https://fr.wikipedia.org/wiki/%C3%89variste_Galois) de cardinal 2.