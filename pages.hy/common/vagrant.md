#բոմժ

> Կառավարեք թեթև, վերարտադրվող և շարժական զարգացման միջավայրերը:.
> Որոշ ենթահրամաններ, ինչպիսիք են `box`, `snapshot`, `halt` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli>:.

- Ստեղծեք `Vagrantfile` ընթացիկ գրացուցակում Vagrant բազային տուփով.:

`vagrant init`

- Ստեղծեք `Vagrantfile` տուփով Vagrant Public Registry-ից.:

`vagrant init {{ubuntu/focal64}}`

- Սկսել և ապահովել Vagrant միջավայրը.:

`vagrant up`

- Կասեցնել մեքենան.:

`vagrant suspend`

- Կասեցնել մեքենան.:

`vagrant halt`

- Միացեք մեքենային SSH-ի միջոցով.:

`vagrant ssh`

- Արտադրեք գործող Vagrant մեքենայի SSH կազմաձևման ֆայլը.:

`vagrant ssh-config`

- Թվարկեք բոլոր տեղական տուփերը.:

`vagrant box list`
