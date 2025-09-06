# vagrant plugin

> Gère les plugiciels Vagrant.
> Voir aussi : `vagrant`.
> Plus d'informations : <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- Liste tous les plugiciels actuellement installés :

`vagrant plugin list`

- Installe un plugiciel depuis des dépôts distants, généralement RubyGems :

`vagrant plugin install {{vagrant_vbguest}}`

- Installe un plugiciel à partir d’un fichier local :

`vagrant plugin install {{chemin/vers/plugiciel.gem}}`

- Met à jour tous les plugiciels installés vers leur dernière version :

`vagrant plugin update`

- Met à jour un plugiciel à la dernière version :

`vagrant plugin update {{vagrant_vbguest}}`

- Désinstalle un plugiciel spécifique :

`vagrant plugin uninstall {{vagrant_vbguest}}`
