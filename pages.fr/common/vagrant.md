# vagrant

> Gère des environnements de développement légers, reproductibles et portables.
> Plus d'informations : <https://developer.hashicorp.com/vagrant/docs/cli>.

- Crée un fichier Vagrantfile dans le répertoire actuel avec l'image Vagrant de base :

`vagrant init`

- Crée un fichier Vagrantfile avec l'image Ubuntu 20.04 (Focal Fossa) depuis HashiCorp Atlas :

`vagrant init ubuntu/focal64`

- Démarre et configure l’environnement Vagrant :

`vagrant up`

- Suspend la machine :

`vagrant suspend`

- Arrête la machine :

`vagrant halt`

- Se connecte à la machine via SSH :

`vagrant ssh`

- Affiche la configuration SSH de la machine Vagrant en cours d’exécution :

`vagrant ssh-config`

- Liste toutes les images locales :

`vagrant box list`
