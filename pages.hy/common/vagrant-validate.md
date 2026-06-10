# թափառաշրջիկ վավերացում

> Ստուգեք Vagrantfile-ի վավերականությունը:.
> Տես նաև՝ `vagrant`, `vagrant box`, `vagrant plugin`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/validate>:.

- Վավերացրեք Vagrantfile-ի շարահյուսությունը՝ համոզվելու համար, որ այն ճիշտ է կառուցված և զերծ է սխալներից.:

`vagrant validate`

- Համոզվեք, որ Vagrantfile-ը ճիշտ է կառուցված՝ անտեսելով մատակարարի հատուկ կազմաձևման տարբերակները.:

`vagrant validate {{[-p|--ignore-provider]}} {{docker|hypervlibvirt|parallels|qemu|virtualbox|vmware_desktop}}`
