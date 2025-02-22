# vagrant plugin

> Gestiona los complementos de Vagrant.
> Vea también: `vagrant`.
> Más información: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- Lista todos los complementos actualmente instalados:

`vagrant plugin list`

- Instala un complemento desde repositorios remotos, normalmente RubyGems:

`vagrant plugin install {{vagrant_vbguest}}`

- Instala un complemento desde un archivo local:

`vagrant plugin install {{ruta/a/mi_complemento.gem}}`

- Actualiza todos los complementos instalados a su última versión:

`vagrant plugin update`

- Actualiza un complemento a la última versión:

`vagrant plugin update {{vagrant_vbguest}}`

- Desinstala un complemento específico:

`vagrant plugin uninstall {{vagrant_vbguest}}`
