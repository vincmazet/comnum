(S:chaine)=
# Chaîne de communication

Une chaîne de communication numérique représente les différentes étapes de traitement de l'information.
Il relie l'émetteur au récepteur par l'intermédiaire d'un **canal de transmission** (_channel_).
Le canal est le milieu dans lequel est transmis ou stocké l'information du message (comme un câble électrique ou une fibre optique).

Ainsi, comme indiqué dans la {numref}`F:chaine`, le message $m$, qu'il soit analogique ($m(t)$) ou déjà sous forme numérique ($m[n]$),
est transformé via les différents blocs de l'émetteur pour finalement devenir un signal analogique $x(t)$ qui est émis.
Le récepteur reçoit quant à lui un signal analogique $y(t)$ qui diffère de $x(t)$ à cause des perturbations sur le canal de transmission.
Les opérations inverses de l'émetteur permettent d'obtenir un message reçu $\hat{m}$,
qu'on espère être exactement le message émis.

<br />

```{figure} ../figs/chaine.svg
---
name: F:chaine
---
Chaîne de communications numériques. Les deux lignes de la chaîne correspondent respectivement à l'émetteur et au récepteur.
```

<br />

* Le **convertisseur numérique--analogique** (CAN) transforme le message analogique en message numérique.
  Il effectue donc un échantillonnage et une quantification du signal portant le message analogique.
  Le CAN n'est bien sûr pas utile si le message est déjà sous forme numérique (comme c'est le cas d'un texte par exemple).

* Le [**codage source**](S:codage-source:information) effectue une mise en correspondance entre l'alphabet du message et celui du canal.
  Par exemple, un texte dont les symboles sont les lettres et les signes de ponctuation
  est transformé en message binaire dont les symboles sont 0 et 1.
  Le codage source peut également effectuer une compression des données,
  c'est-à-dire réduire le plus possible la taille du message qui sera effectivement transmis.

* Le [**chiffrement**](S:chiffrement) (parfois appelé, à tort, « cryptage ») consiste à modifier le message selon une certaine règle
  pour garantir son authentification ou pour le rendre incompréhensible si on ne possède pas la règle.

* Le [**codage canal**](S:codage-canal:intro) ajoute de la redondance dans le message ; le message est donc rallongé.
  L'objectif est de protéger le message des erreurs de transmission.
  Les codes utilisés permettent de détecter la présence d'erreurs dans le message reçu,
  et parfois même de les corriger.

* Le [**multiplexage**](S:multiplexage) regroupe plusieurs messages différents pour qu'il puissent être transmis sur le même canal.
  Ce bloc peut être situé à d'autres endroits sur la chaîne.

* Enfin, la [**modulation**](S:modulation:intro) convertit le message numérique en message analogique
  pour qu'il puisse être transmis via le canal, qui est un support physique et donc forcément analogique.

