(P:chiffrement)=
# Chiffrement

La **cryptographie** modifie le message pour le protéger et ainsi garantir :
* sa confidentialité (personne ne peut lire le message sans la clé) ;
* son authenticité (vérifier l'identité de l'émetteur) ;
* son intégrité (vérifier que le message n'a pas été modifié).

La modification est définie à l'aide d'une ou plusieurs **clé**, comme on le verra ci-après.

```{note}
En bon français, on dit « chiffrer un message » et pas « crypter un message » pour le protéger
(« crypter » est un anglicisme).
Pour retrouver le message initial, on le « déchiffre » si on posséde la clé,
et on le « décrypte » sinon.
```

On distingue trois familles de méthodes de chiffrement.

* Les algorithmes de chiffrement faible sont facilement décryptables.
  Ils consistent principalement à remplacer les symboles du message suivant une règle assez simple,
  comme par exemple un [décalage des lettres](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage) dans l'alphabet pour les messages texte.
  Citons par exemple le chiffre de César qui remplace chaque lettre d'un texte par la $n$<sup>e</sup> lettre suivante dans l'alphabet.
  Ainsi, si $n=2$, alors le mot « ECOLE » devient « GEQNG ».
  Pour déterminer $n$, on peut tester toutes les possibilités (force brute)
  ou observer les statistiques d'apparition de chaque lettre, sachant qu'en français la lettre « E » est la plus courante.
  
* Les [algorithmes de chiffrement symétrique](https://fr.wikipedia.org/wiki/Cryptographie_sym%C3%A9trique)
  nécessitent une clé qui sert au chiffrement et au déchiffrement.
  La clé doit donc rester secrète.
  On peut citer l'algorithme AES qui est notamment utilisé dans certaines communications WiFi.
  
* Enfin, les [algorithmes de chiffrement asymétrique](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique)
  nécessitent deux clés :
  - une clé publique, connue de tous, pour effectuer le chiffrement du message,
  - une clé privée, gardée secrète, pour déchiffrer le message.
  
  L'algorithme RSA est un algorithme de chiffrement asymétrique utilisé pour le commerce électronique, les signatures électroniques, etc.