# vagrant plugin

> Gérer les plugins Vagrant.
> Voir aussi : `vagrant`.
> Plus d’informations : <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- Liste tous les plugins actuellement installés:

`vagrant plugin list`

- Installer un plugin depuis des dépôts distants, généralement RubyGems:

`vagrant plugin install {{vagrant_vbguest}}`

- Installer un plugin à partir d’un fichier local:

`vagrant plugin install {{path/to/my_plugin.gem}}`

- Mettre à jour tous les plugins installés vers leur dernière version:

`vagrant plugin update`

- Mettre à jour un plugin à la dernière version:

`vagrant plugin update {{vagrant_vbguest}}`

- Désinstaller un plugin spécifique:

`vagrant uninstall {{vagrant_vbguest}}`
