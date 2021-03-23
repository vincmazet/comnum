# Codes en bloc

<!--
## Principe

Le codage en bloc consiste à associer, à chaque bloc de $k$ bits du message, un bloc de $n$ bits (avec $n>k$).
On utilise la notation $C(n,k)$.
On définit le rendement du code comme étant $k/n$.

---

Les opérations de codage et décodage se font, mathématiquement, à l'aide d'additions et de multiplications sur des symboles binaires

| $a$ | $b$ | $a+b$ | $a \cdot b$ |
| --- | --- | ----- | ----------- |
|  0  |  0  |   0   |      0      |
|  0  |  1  |   1   |      0      |
|  1  |  0  |   1   |      0      |
|  1  |  1  |   0   |      1      |

L'opération $+$ est équivalente à un ou exclusif, et l'opération $\cdot$ est équivalente à un et.

L'ensemble $\{0,1\}$ muni de cette addition et de cette multiplication est noté $\mathbb{F}_2$
et s'appelle le corps de Galois de cardinal 2.


## Codage

Plutôt que d'établir une table pour définir les correspondances entre les blocs de $k$ symboles du message et les mots du code,
on utilise la **matrice génératrice** (_???_) $G\in\mathbb{F}_{k \times n}$.

Chaque mot $c$ du code est calculé à partir d'un bloc $m$ du message par :

$$
c = mG.
$$

(Attention, la multiplication matricielle est également à effectuer dans $\mathbb{F}_2$ !).

```{exemple}
Le code à répétition $C(3,1)$ est tel que $n=3$ et $k=1$.
Le rendement est donc de $1/3$. 

| $m$ | $c$ |
| --- | --- |
|  0  | 000 |
|  1  | 111 |

Donc

$$
G = \begin{pmatrix}1 & 1 & 1\end{pmatrix}
$$

```

Si le mot du code contient le message $m$, on dit que le code est systémtique.
Donc :

$$
G = \begin{pmatrix} I_k & P \end{pmatrix}
  = \begin{pmatrix}
      1 &       & 0 &   \\
        & \dots &   & P \\
      0 &       & 1 &   \\
    \end{pmatrix}
$$

```{exemple}
Le code à répétition $C(3,1)$ est systématique.

$$
G = \begin{pmatrix}1 & | & 1 & 1\end{pmatrix}
\qquad\Leftrightarrow\qquad
P = \begin{pmatrix}1 & 1\end{pmatrix}
$$

```


### Décodage

À chaque matrice génératrice on peut associer une **matrice de contrôle de parité** (_???_) $H\in\mathbb{F}_2^{n-k \times n}$ telle que

$$
H = \begin{pmatrix} P^T & I_{n-k} \end{pmatrix}.
$$

```{exemple}
Le code à répétition $C(3,1)$ a pour matrice de contrôle de parité

$$
P = \begin{pmatrix}1 & 1\end{pmatrix}
\qquad\Leftrightarrow\qquad
H = \begin{pmatrix}
      1 & | & 1 & 0 \\
      1 & | & 0 & 1 \\
    \end{pmatrix}
$$

```

Le vecteur reçu par le récepteur peut s'écrire :

$$
r = c + e
$$

où $e$ est un vecteur binaire dont les <code>1</code> indiquent la présence d'une erreur.
Par exemple, si on émet $c = 0101$ et qu'on reçoit $r=0110$, on a bien $e=0011$.
On parle de **canal binaire symétrique** (_???_).

On définit le **syndrome** (_??_) $s$ par :

$$
s = rH^T \\
  = (c+e)H^T \\
  = cH^T + eH^T \\
  = mGH^T + eH^T
$$

Or,

$$
GH = \begin{pmatrix} I_k & P \end{pmatrix} \begin{pmatrix} P^T & I_{n-k} \end{pmatrix}^T \\
   = \begin{pmatrix} I_k & P \end{pmatrix} \begin{pmatrix} P \\ I_{n-k} \end{pmatrix}^T \\
   = P + P \\
   = 0
$$

(puisque $0+0=0$, et $1+1=0$).

Donc :

$$
s = eH^T.
$$

Donc, le syndrome est nul si $r$ est un mot du code.
Un syndrome non nul indique la présence d'une erreur, maus un syndrome nul n'indique pas qu'il y a une erreur,
par exemple, si on reçoit un autre mot du code !
**PAS CLAIR ET PEUT ETRE FAUX !!!*

```{exemple}
Code à répétition $C(3,1)$.
Si on reçoit $r=011$, il y a manifestation une erreur puisque ce mot n'est pas un triplet du même bit,
ce n'est pas un mot du code.
En effet :

$$
s = rH^T
  = \begin{pamtrix} 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}
  = \begin{pamtrix} 1 & 1 \end{pmatrix}
  \neq 0
$$

Une erreur est donc détectée !
```

Interprétation géométrique du code à répétition $C(3,1)$.

**SCHEMA**

La **distance de Hamming** (_???_) $d_H(u,v)$ entre deux séquences binaires $u$ et $v$ est le nombre de bits différents entre $u$ et $v$.

```{exemple}
d_H(001,000)=1
d_H(000,111)=3
```

**exercice 1**

La distance minimale $d_\text{min}$ d'un code est la plus petite distance qu'il existe entre deux mots du code.
On peut montrer que $d_\text{min}$ est égale au nombre minimal d'éléments non nuls dans les mots du code
(en excluant l mot nul) (pour les codes linéaires) [Proakis p.414].

```{exemple}
Code à répétition $C(3,1)$ : $d_\text{min}=3$.
```

si le syndrome $s$ est nul, la règle ...
-->