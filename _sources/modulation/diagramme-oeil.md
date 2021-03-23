# Diagramme de l'œil

Le diagramme de l'œil est un graphe sur $\left[-\frac{T}{2}, \frac{T}{2}\right]$
qui représente la superposition de plusieurs traces du signal reçu $y(t)$.

```{figure} ../figs/diagoeil.svg
---
name: F:diagoeil
width: 400px
---
Exemple de diagramme de l'œil, ici dans le cas d'un canal non idéal et bruité.
```

Le diagramme de l'œil permet de voir plusieurs choses.

* L'ouverture de l'œil représente l'intervalle de temps où
  peut se faire l'échantillonnage du signal lors de la démodulation.
  Il vaut mieux que l'œil soit le plus ouvert.
  
* La hauteur de l'œil indique la quantité de bruit qui est tolérée pour que la distinction entre les niveaux soit possible.
  Si le rapport signal-à-bruit diminue (ce qui signifie que le bruit augmente), alors l'œil aura tendance à se fermer
  et alors on ne pourra plus distinguer les niveaux représentant les symboles.
  
* Les distortions sont dues au bruit mais aussi au filtrage du signal par le canal.

* L'instant où l'œil est le plus ouvert est le meilleur choix pour effectuer l'échantillonnage,
  puisque c'est à cet instant que les deux niveaux sont le plus éloignés.

<script src="_static/js/eyediag.js"></script>
<div id="eyediag" class="spetsi"></div>

<a class="btn btn-light" href="td.html#exercice-7" role="button">Exercice 7</a>