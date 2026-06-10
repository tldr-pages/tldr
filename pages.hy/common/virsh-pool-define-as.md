# virsh pool-define-as

> Տրամադրված արգումենտներից ստեղծեք կազմաձևման ֆայլ `/etc/libvirt/storage`-ում մշտական վիրտուալ մեքենայի պահեստավորման համար:.
> Տես նաև՝ `virsh`, `virsh-pool-build`, `virsh-pool-start`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/virsh>:.

- Ստեղծեք կազմաձևման ֆայլը պահեստային լողավազանի համար, որը կոչվում է pool_name՝ օգտագործելով `/var/vms` որպես հիմքում ընկած պահեստային համակարգ.:

`virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}`
