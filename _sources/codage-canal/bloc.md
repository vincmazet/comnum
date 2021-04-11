# Codes en bloc


## Principe

Le codage en bloc consiste à associer, à chaque bloc de $k$ bits du message, un bloc de $n$ bits (avec $n>k$).
On définit le **rendement du code** comme étant $k/n$.

Pour nommer un code en bloc, on utilise la notation $C(n,k)$.

```{div} exemple

Dans ce chapitre, nous utiliserons comme exemple le code à répétition $C(3,1)$.
Ce code est très simple puisqu'il consiste à répéter $n=3$ fois chaque bloc de $k=1$ bits du message.
Il a donc un rendement de $1/3$, ce qui signifie que dans le message codé, seul un tiers n'est pas redondant.

Les blocs possibles et leur code respectif est donc listés dans le tableau ci-dessous :

| $m$ | $c$ |
| --- | --- |
|  0  | 000 |
|  1  | 111 |

Pas de quoi casser des briques, mais cet exemple très simple illustrera les concepts des codes en bloc.
```


## Codage

Plutôt que d'établir une table pour définir les correspondances entre les blocs du message et les mots du code,
on utilise la **matrice génératrice** (_generator matrix_) $G\in\mathbb{F}^{k \times n}$.
Chaque mot $c$ du code est calculé à partir d'un bloc $m$ du message par l'équation :

$$
c = mG.
$$

(Attention, la multiplication matricielle est également à effectuer dans $\mathbb{F}_2$ !).

```{div} exemple

La matrice génératrice du code à répétition $C(3,1)$ est

$$
G = \begin{pmatrix}1 & 1 & 1\end{pmatrix}.
$$

En effet :

$$
\begin{pmatrix}0\end{pmatrix} \begin{pmatrix}1 & 1 & 1\end{pmatrix} = \begin{pmatrix}0 & 0 & 0\end{pmatrix}
\quad\text{et}\quad
\begin{pmatrix}1\end{pmatrix} \begin{pmatrix}1 & 1 & 1\end{pmatrix} = \begin{pmatrix}1 & 1 & 1\end{pmatrix}
$$
```

Si les mot du code contiennent le message qui les a généré, alors le code est dit **systématique**
et la matrice génératrice peut s'écrire sous la forme :

$$
G = \begin{pmatrix} I_k & | & P \end{pmatrix}
  = \left(
    \begin{array}{ccc|c}
      1 &        & 0 &   \\
        & \ddots &   & P \\
      0 &        & 1 &   \\
    \end{array}
    \right)
$$

où $P\in\mathbb{F}^{k \times n-k}$ est une matrice qui définit les bits à ajouter au message.

```{div} exemple

Le code à répétition $C(3,1)$ est systématique et puisque $G = \begin{pmatrix}1 & | & 1 & 1\end{pmatrix}$
alors $P = \begin{pmatrix}1 & 1\end{pmatrix}$.
```


## Interprétation géométrique

Les mots du code générés peuvent être considérés comme des points dans un espace à $n$ dimensions.
Dans le cas où $n \leq 3$, ces points peuvent être représentés.

```{div} exemple

Le code à répétition $C(3,1)$ produit deux mots.
Le premier, $000$, est représenté par le point aux coordonnées $(0,0,0)$ dans $\mathbb{F}_2^3$.
Le second, $111$, est représenté par le point aux coordonnées $(1,1,1)$ dans $\mathbb{F}_2^3$.
Tous les autres mots de trois bits sont également des points spécifiques, mais ils n'appartiennent pas au code.

<font color="red"><b>SCHEMA</b></font>
```

La **distance de Hamming** (_Hamming distance_) $d(u,v)$ entre deux mots de même longueur $u$ et $v$
est le nombre de symboles différents entre $u$ et $v$.
Géométriquement, la distance de Hamming correspond au nombre de segments qui relient les deux mots.

La **distance minimale** $d_\text{min}$ d'un code est la plus petite distance qu'il existe entre deux mots du code.

Dans le cas des codes linéaires, on peut montrer que $d_\text{min}$ est égale au nombre minimal de symboles non nuls
dans tous les mots du code, à l'exception du mot nul {ref}`[Proakis 2008, p.414]<S:refs>`.


## Décodage

À chaque matrice génératrice on peut associer une **matrice de contrôle de parité** (_parity-check matrix_) $H\in\mathbb{F}_2^{n-k \times n}$.
Cette matrice a la particularité que $cH^T=0$ pour tout mot $c$ du code.
Si le code est systématique, la matrice de contrôle de parité s'écrit

$$
H = \begin{pmatrix} P^T & | & I_{n-k} \end{pmatrix}.
$$

```{div} exemple

Le code à répétition $C(3,1)$ a pour matrice de contrôle de parité

$$
H = \left(
    \begin{array}{c|cc}
      1 & 1 & 0 \\
      1 & 0 & 1 \\
    \end{array}
    \right)
$$
```

À cause des erreurs de transmission, le code reçu par le récepteur n'est pas forcément $c$ et  peut présenter des différences.
On peut donc considérer que le code reçu $r$ est défini par :

$$
r = c + e
$$

où $e$ est un vecteur binaire dont les `1` indiquent la présence d'une erreur.
Par exemple, si on émet $c = 0101$ et qu'on reçoit $r=0110$, on a bien $e=0011$.
On parle de **canal binaire symétrique** (_binary symmetric channel_).

Le décodage du code reçu $r$ s'effectue en le multipliant par $H^T$.
Le résultat est appelé **syndrome** (_syndrome_) $s$ :

$$
\begin{align*}
  s &= rH^T \\
    &= (c+e)H^T \\
    &= cH^T + eH^T \\
    &= mGH^T + eH^T.
\end{align*}
$$

Or, du fait des règles de l'addition dans le corps de Galois,

$$
\begin{align*}
  GH^T &= \begin{pmatrix} I_k & P \end{pmatrix} \begin{pmatrix} P^T & I_{n-k} \end{pmatrix}^T \\
       &= \begin{pmatrix} I_k & P \end{pmatrix} \begin{pmatrix} P \\ I_{n-k} \end{pmatrix}^T \\
       &= P + P \\
       &= 0
\end{align*}
$$

Ainsi, $mGH^T = cH^T = 0$ : on retrouve la particularité de la matrice de contrôle de parité évoquée ci-avant.
Par ailleurs, cela implique que

$$
s = eH^T.
$$

```{margin}
Cependant, un syndrome nul n'implique pas que la transmission se soit faite sans erreur !
Par exemple, le code reçu peut être différent du code envoyé, tout en étant un autre mot du code !
Mais ça, on ne peut pas le détecter simplement...
```

S'il n'y a aucune erreur de transmission, alors $e=0$ et donc le syndrome $s$ est nul.
De manière équivalente, un syndrome non nul indique la présence d'une erreur de transmission.

```{div} exemple

Avec le cde à répétition $C(3,1)$, si on reçoit $r=011$, il y a manifestation une erreur puisque ce mot n'est pas un triplet du même bit :
ce n'est pas un mot du code.
Le syndrome est effectivement non nul :

$$
s = rH^T
  = \begin{pmatrix} 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}
  = \begin{pmatrix} 1 & 1 \end{pmatrix}
  \neq 0
$$

L'erreur de transmission est donc détectée !
```

Comment, alors, corriger le code reçu si une erreur de transmission a été détectée ?
Sans autre information a priori, il est logique de décider que le mot émis soit le mot le plus proche du mot reçu :
on fait dans ce cas l'hypothèse qu'il y a eu le moins d'erreurs possibles.

En termes géométriques, cela signifie que la règle est de rechercher le mot du code le plus proche
(en termes de distance de Hamming) du code reçu.


## Pouvoir de détection

Le **pouvoir de détection** d'un code est le nombre maximal d'erreurs qui peut affecter le mot transmis
sans que l'on confonde le mot reçu avec un autre mot du code.

On montre que le pouvoir de détection est égal à $d_\text{min}-1$.

```{div} exemple
Le code à répétition $C(3,1)$ est capable de détecter jusqu'à deux erreurs,
puisque si la transmission introduit une ou deux erreurs, alors le mot reçu n'est pas une triple répétition du bit émis.
Cela correspond bien à $d_\text{min}-1$.
```


## Pouvoir de correction

Le **pouvoir de correction** d'un code est le nombre maximal d'erreurs qui peut affecter le mot transmis
et qui peuvent être corrigées pour retrouver le mot effectivement émis.

```{margin}
La notation $\lfloor\cdot\rfloor$ désigne la partie entière.
```

On montre que le pouvoir de correction est égal à $\lfloor(d_\text{min}-1)/2\rfloor$.

```{div} exemple
Le code à répétition $C(3,1)$ est capable de corriger jusqu'à une erreur.
En effet :
* si une seule erreur de transmission est intervenue, alors les deux bits non erronés permettront de prendre la bonne décision quant au bit émis
  (par exemple, si on reçoit `100` alors on suppose que c'est `0` qui a été émis) ;
* si deux seule erreurs de transmission sont intervenues, alors la décision prise sera mauvaise
  (par exemple, si on reçoit `101` alors que `0` a été émis, le récepteur supposera tout de même que c'est `1` qui a été émis).
  
Cela correspond bien à $\lfloor(d_\text{min}-1)/2\rfloor$.
```


## Codes cycliques

<font color="red"><b>TODO</b></font>


<!-- http://pfister.ee.duke.edu/courses/ece590_gmi/coding_intro.pdf -->