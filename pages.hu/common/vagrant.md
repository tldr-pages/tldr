# vagrant

> Könnyű, reprodukálható és hordozható fejlesztési környezetek kezelése. További információ: <https://www.vagrantup.com>.

- Vagrantfile létrehozása az aktuális könyvtárban az alap Vagrant dobozban:

`vagrant init`

- Vagrantfile létrehozása a HashiCorp Atlas Ubuntu 20.04 (Focal Fossa) dobozával:

`vagrant init ubuntu/focal64`

- Indítsa el és helyezze üzembe a vagrant környezetet:

`vagrant up`

- A gép felfüggesztése:

`vagrant suspend`

- Állítsa le a gépet:

`vagrant halt`

- Csatlakozás a géphez SSH-n keresztül:

`vagrant ssh`

- A futó Vagrant gép SSH konfigurációs fájljának kiadása:

`vagrant ssh-config`

- Az összes helyi doboz listázása:

`vagrant box list`
