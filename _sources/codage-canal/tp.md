# Travaux pratiques


```{admonition} Modules Python
Dans ce TP, nous utiliserons les modules
[numpy](https://numpy.org/doc/stable/reference/index.html),
[scipy](https://docs.scipy.org/doc/scipy/reference/index.html#api-reference),
[matplotlib](https://matplotlib.org/stable/api/index.html),
[comnumfip](https://github.com/vincmazet/comnumfip) et
[komm](http://komm.readthedocs.io/).
```

```{admonition} Modules Python
Durant le TP, vous pouvez échanger des astuces, fonctions utiles ou morceaux de code sur
[Moodle](https://moodle.unistra.fr/mod/glossary/view.php?id=585756).
```

Trois codes canal sont comparés sur des simulations numériques :
le code à parité (5,4), le code de Hamming (7,4) et le code convolutif de polynômes générateurs $7_8$ et $5_8$.
Ces trois codes ont été étudiés en TD et en cours à l'exception du code à parité (5,4),
mais ce dernier consiste, comme le code à parité (3,2), à ajouter un bit de parité à chaque bloc du message.

Le codage et le décodage seront, pour ces trois codes, effectués avec le module komm.

1. Cherchez dans l'aide de komm quelles instructions permettent de coder et décoder une séquence binaire.

1. Testez le fonctionnement de chaque code sur une séquence binaire aléatoire (`comnumfip.randmary`).

1. Vérifiez que le décodage fonctionne également en l'appliquant directement sur la séquence codée.

1. Introduisez quelques erreurs dans la séquence pour vérifier que le décodage fonctionne bien.
   Expliquez en particulier le cas du code à parité (5,4).

On applique maintenant ces trois codes sur des séquences binaires très longues,
en considérant un canal binaire symétrique de probabilité d'erreur $\alpha$,
c'est-à-dire que chaque bit a une probabilité $\alpha$ d'être erroné.
La transmission est dite « simplex » c'est-à-dire qu'elle s'effectue dans un seul sens :
il n'est pas possible pour le récepteur de demander à l'émetteur de transmettre une nouvelle fois le message
si une erreur a été détectée sans avoir pu être corrigée.

1. Simulez la transmission via ce canal (`komm.BinarySymmetricChannel`) d'une séquence binaire aléatoire
   sans code canal et avec les trois codes précédents.

1. Tracez la probabilité d'erreur par élément du message en fonction de la probabilité d'erreur sur le canal de transmission
   (faites plusieurs simulations avec des messages suffisamment longs).
