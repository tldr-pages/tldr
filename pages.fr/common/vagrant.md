# vagrant

> Gérer des environnements de développement légers, reproductibles et portables.
> Plus d’informations : <https://www.vagrantup.com>.

- Créer un fichier Vagrantfile dans le répertoire actuel avec la box Vagrant de base:

`vagrant init`

- Créer un fichier Vagrantfile avec la box Ubuntu 20.04 (Focal Fossa) depuis HashiCorp Atlas:

`vagrant init ubuntu/focal64`

- Démarrer et provisionner l’environnement Vagrant:

`vagrant up`

- Suspendre la machine:

`vagrant suspend`

- Arrêter la machine:

`vagrant halt`

- Se connecter à la machine via SSH:

`vagrant ssh`

- Afficher la configuration SSH de la machine Vagrant en cours d’exécution:

`vagrant ssh-config`

- Lister toutes les boxes locaux:

`vagrant box list`
