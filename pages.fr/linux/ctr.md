# ctr

> Gère les conteneurs et images de `containerd`.
> Plus d'informations : <https://containerd.io>.

- Liste tous les conteneurs (en marche et arrêtés) :

`ctr containers list`

- Liste toutes les images :

`ctr images list`

- Télécharge une image :

`ctr images pull {{image}}`

- Étiquette une image :

`ctr images tag {{image_source}}:{{étiquette_source}} {{image_destination}}:{{étiquette_destination}}`
