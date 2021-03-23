(S:codage-canal:intro)=
# Introduction


Pour réduire les erreurs de transmission, on peut :
* augmenter la puissance du signal émis,
* réduire le bruit et les interférences du canal,
* introduire de la rendondance dans le signal : c'est ce qu'on appelle le codage canal.

La codage canal est parfois appelé codage correcteur d'erreur.
Cette terminologie est incorrecte car le codage canal ne peut parfois que détecter des erreurs sans les corriger.

Pourquoi ajouter de la redondance alors que le codage source réduit la redondance ?
Parce que la redondance du codage canal est contrôlée.

Conséquence de l'introduction de redondance :
accroissement du débit et de la bande de fréquence occupée.

Il existe deux types de codages canal :
* codes en bloc : le message est déocpé en groupes de symboles, pour lesquels est associé un code (par exemple, le code à parité),
* codes convolutifs : tout le message est codé, sans découpage de blcos.
  Le message passe dans un système dont la sortie est le message codé.
  
Certaines techniques de codage canal combinent les deux types.

Dans ce cours, on considère exclusivement des codes binaires, mais il existe des codes canal M-aire.

Il existe, pour ces deux types, des codes linéaires et non linéaires.
Nous étudierons unquement les codes linéaires.
