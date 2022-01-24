# Excercices


## Exercice 1

L'[article Wikipédia](https://en.wikipedia.org/w/index.php?title=List_of_ITU-T_V-series_recommendations&oldid=658869531)
sur les recommandations de transfert de données sur le réseau téléphonique présente la norme V.32
(utilisée par les modems dans les années 1980 et 1990) ainsi :
>  V.32 is an ITU-T recommendation for a modem operating as full-duplex on a 4-wire circuit,
   or half-duplex on a two-wire circuit, allowing bidirectional data transfer at either 9.6 kbit/s or 4.8 kbit/s
   at a symbol rate of 2,400 baud.

1. Quelle est la rapidité de modulation ?
1. Quel est le débit binaire ?
1. Quelle est la taille en bits des symboles émis ?


## Exercice 2

Représentez la séquence binaire <code>01011</code> modulée en NRZ bipolaire, Manchester et AMI.


## Exercice 3

Représentez les constellations des modulations suivantes :

* OOK (_on-off keying_) définie dans [Wikipédia](https://en.wikipedia.org/w/index.php?title=On-off_keying&oldid=669950443) par :
  > On-off keying (OOK) denotes the simplest form of amplitude-shift keying (ASK) modulation
    that represents digital data as the presence or absence of a carrier wave.
    In its simplest form, the presence of a carrier for a specific duration represents a binary one,
    while its absence for the same duration represents a binary zero.

* 4-ASK ;

* 2-PSK (appelée aussi BPSK pour _binary PSK_) ;

* 8-QAM.


<!-- ## Exercice 
%
% \begin{questions}
%   \item Quelle est le type de modulation dont la constellation est représentée ci-dessous~?
%   \item En utilisant dans la mesure du possible un code de Gray,
%   donnez les symboles associés à chaque point de la constellation.
% \end{questions}
% \begin{center}
%   \psset{unit=5mm}
%   \begin{pspicture}(-4,-4)(4,4)
%     \psaxes[labels=none,linewidth=.5pt]{->}(0,0)(-3.999,-3.999)(3.999,3.999)
%     \qdisk(-3,+1){1.5pt}
%     \qdisk(-1,+3){1.5pt}
%     \qdisk(-3,-3){1.5pt}
%     \qdisk(-1,-1){1.5pt}
%     \qdisk(+1,+1){1.5pt}
%     \qdisk(+3,+3){1.5pt}
%     \qdisk(+1,-3){1.5pt}
%     \qdisk(+3,-1){1.5pt}
%   \end{pspicture}
% \end{center}
 -->


## Exercice 4

Les quatre modulations linéaires ci-dessous représentent la séquence binaire <code>011001011100</code>.

1. Identifiez les modulations en bande de base et les modulations sur porteuse.
1. Déterminez les valeurs des symboles et les formes d'onde de ces modulations.

```{image} ../figs/exo-modulation.svg
:width: 100%
:align: center
```


## Exercice 5

<!-- Joindot, p. 3.9 -->

La transmission d'un message binaire à un débit $D=600$ Mbits/s est effectuée en utilisant huit signaux
$\{\pm s(t), \pm 3s(t), \pm 5s(t), \pm 7s(t)\}$ où $s(t)$ est un signal de durée $T$.

1. Quelle est la rapidité de la modulation ?
1. Est-ce une modulation en bande de base ou sur porteuse ?


<!-- ## Exercice 
%
% \begin{questions}
%   \item Représentez la forme d'onde $h_1(t)$~:
%   \begin{equation*}
%     h_1(t) =
%     \begin{cases}
%       1       &\text{si $t\in[0,\,T[$}, \\
%       0       &\text{sinon}.
%     \end{cases}
%   \end{equation*}
%   \item Quelle est la réponse impulsionnelle du filtre de réception associé à $h_1(t)$~?
%   \item Calculez le signal en sortie du filtre lorsque l'entrée est $h_1(t)$.
%   \item Mêmes questions pour la forme d'onde
%   \begin{equation*}
%     h_2(t) =
%     \begin{cases}
%       1       &\text{si $t\in[0,\,T/2[$}, \\
%       0       &\text{sinon}.
%     \end{cases}
%   \end{equation*}
% \end{questions} -->


<!-- ## Exercice 6

!-- Joindot, ex 3.9 --

Un message binaire est transmis avec une rapidité de modulation $R = 300$ Bd.

1. Y a-t-il des interférences entre symboles si le canal a une fréquence de coupure de $100$ Hz ? !-- (oui) --
1. Y a-t-il des interférences entre symboles si le canal a une fréquence de coupure de $200$ Hz ? !-- (on ne sait pas) --
-->


## Exercice 6

Déterminez, à partir des diagrammes de l'œil ci-dessous :

1. le nombre de symboles du message ;
1. le meilleur instant d'échantillonnage ;
1. la meilleure valeur de seuil ;
1. s'il y a des IES ;
1. s'il y a du bruit.

```{image} ../figs/eyediag1.svg
:width: 40%
```

```{image} ../figs/eyediag2.svg
:width: 40%
```

```{image} ../figs/eyediag3.svg
:width: 40%
```

```{image} ../figs/eyediag4.svg
:width: 40%
```