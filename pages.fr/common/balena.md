# balena

> Interagis avec balenaCloud, openBAlena et l'API balena depuis la ligne de commande.
> Plus d'informations : <https://www.balena.io/docs/reference/cli/>.

- Connexion à balenaCloud :

`balena login`

- Crée une application balenaCloud ou openBalena :

`balena app create {{nom_d_application}}`

- Affiche toutes les applications balenaCloud ou openBalena du compte :

`balena apps`

- Affiche tous les appareils associés au compte balenaCloud ou openBalena :

`balena devices`

- Flash une image balenaOS sur l'appareil local :

`balena local flash {{chemin/vers/balenaos.img}} --drive {{localisation_de_l_appareil}}`
