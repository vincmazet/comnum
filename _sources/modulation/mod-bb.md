# Modulation en bande de base

Le signal analogique $x(t)$ modulé en bande de base à partir d'un message $m$ s'obtient grâce à l'équation :

$$
x(t) = \sum_{k=-\infty}^{+\infty} \alpha_k h(t-kd)
$$

où $h$ est un signal prédéfini appelé **forme d'onde** et les $\alpha_k$ sont les amplitudes de la forme d'onde et elles dépendent du message.
Notez que la somme est écrite avec une infinité de termes car le message peut être considéré, en toute généralité, de taille infinie.

Le choix de la forme d'onde $h$ et du lien entre le message $m$ et les amplitudes $\alpha$ défini un **code en ligne**.
Il existe beaucoup de codes en ligne, quelques exemples sont donnés ci-après, et nous étudierons leurs avantages respectifs en TP.
En général, le lien entre le message et les amplitudes se fait par l'intermédiaire d'une table de correspondance,
c'est-à-dire que pour chaque symbole de l'alphabet correspond une amplitude particulière.


## Code NRZ bipolaire

Le code NRZ (non retour à zéro) bipolaire est défini par la table de correspondance et la forme d'onde ci-dessous :

````{panels}

Forme d'onde
^^^
$$
h(t) =
\begin{cases}
  V &\text{si } t \in [0,d], \\
  0 &\text{sinon}
\end{cases}
$$

```{image} figs/code-nrz.svg
:width: 70%
:align: center
```

---

Amplitudes
^^^
| $m_k$ | $\alpha_k$ |
| ----- | ---------- |
| $0$   | $-1$       |
| $1$   | $+1$       |

````


## Code Manchester

Le code Manchester est utilisé pour le protocole Ethernet.

````{panels}

Forme d'onde
^^^
$$
h(t) =
\begin{cases}
  V  &\text{si } t \in [0,d/2], \\
  -V &\text{si } t \in [d/2,d], \\
  0  &\text{sinon}
\end{cases}
$$

```{image} figs/code-manchester.svg
:width: 70%
:align: center
```

---

Amplitudes
^^^
| $m_k$ | $\alpha_k$ |
| ----- | ---------- |
| $0$   | $-1$       |
| $1$   | $+1$       |

````


## Code AMI

Le code AMI (_alternate mark inversion_) a été utilisé dans certaines communications téléphoniques.

````{panels}

Forme d'onde
^^^
$$
h(t) =
\begin{cases}
  V &\text{si } t \in [0,d], \\
  0 &\text{sinon}
\end{cases}
$$

```{image} figs/code-ami.svg
:width: 70%
:align: center
```

---

Amplitudes
^^^
| $m_k$ | $\alpha_k$ |
| ----- | ---------- |
| $0$   | $0$        |
| $1$   | $\pm1$ alternativement |

````

<a class="exercise btn btn-light" href="td.html#exercice-2" role="button">2</a>
