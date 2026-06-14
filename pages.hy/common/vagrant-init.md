# թափառաշրջիկ նախաձեռնություն

> Նախաձեռնեք Vagrant միջավայրը ընթացիկ գրացուցակում՝ ստեղծելով `Vagrantfile`:.
> Տես նաև՝ `vagrant`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/init>:.

- Ստեղծեք `Vagrantfile`:

`vagrant init`

- Ստեղծեք `Vagrantfile` առանց հրահանգչական մեկնաբանությունների.:

`vagrant init {{[-m|--minimal]}}`

- Նշեք տուփի անունը և URL-ը.:

`vagrant init {{box_name}} {{box_url}}`

- Ստեղծեք `Vagrantfile` կոնկրետ տուփի տարբերակով.:

`vagrant init --box-version {{version}} {{box_name}}`

- Ուղարկեք `Vagrantfile`-ը `stdout` հասցեին՝:

`vagrant init {{[-o|--output]}} -`

- Վերագրեք գոյություն ունեցող `Vagrantfile`:

`vagrant init {{[-f|--force]}}`

- Տրամադրեք հատուկ ERB ձևանմուշ՝ `Vagrantfile`-ը ստեղծելու համար:

`vagrant init --template {{path/to/file.erb}}`
