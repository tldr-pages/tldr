# թափառաշրջիկ նկար

> Կառավարեք Vagrant մեքենաների լուսանկարները:.
> Տես նաև՝ `vagrant`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/snapshot>:.

- Վերցրեք մեքենայի լուսանկարը (աշխատող կամ դադարեցված).:

`vagrant snapshot save {{snapshot_name}}`

- Վերականգնել լուսանկարը և գործարկել մեքենան.:

`vagrant snapshot restore {{snapshot_name}}`

- Վերականգնել նկարը առանց մեքենան գործարկելու.:

`vagrant snapshot restore --no-start {{snapshot_name}}`

- Ջնջել նկարը.:

`vagrant snapshot delete {{snapshot_name}}`

- Թվարկեք մեքենայի հասանելի նկարները.:

`vagrant snapshot list`
