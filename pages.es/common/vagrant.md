# vagrant

> Gestiona entornos de desarrollo ligeros, reproducibles y portátiles.
> Algunos subcomandos como `box`, `snapshot`, `halt`, etc. tienen su propia documentación de uso.
> Más información: <https://developer.hashicorp.com/vagrant/docs/cli>.

- Crea un `Vagrantfile` en el directorio actual con la caja base de Vagrant:

`vagrant init`

- Crea un `Vagrantfile` con una caja del Registro Público de Vagrant:

`vagrant init {{ubuntu/focal64}}`

- Inicia y aprovisiona el entorno Vagrant:

`vagrant up`

- Suspende la máquina:

`vagrant suspend`

- Detiene la máquina:

`vagrant halt`

- Se conecta a la máquina a través de SSH:

`vagrant ssh`

- Muestra el archivo de configuración SSH de la máquina Vagrant en ejecución:

`vagrant ssh-config`

- Muestra todas las cajas locales:

`vagrant box list`
