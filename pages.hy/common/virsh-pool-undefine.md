# virsh pool-չսահմանել

> Ջնջեք կազմաձևման ֆայլը `/etc/libvirt/storage`-ում դադարեցված վիրտուալ մեքենայի պահեստավորման լողավազանի համար:.
> Տես նաև՝ `virsh`, `virsh-pool-destroy`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/virsh>:.

- Ջնջել պահեստային լողավազանի նշված անվանման կամ UUID-ի կոնֆիգուրացիան (որոշել՝ օգտագործելով `virsh pool-list`):

`virsh pool-undefine --pool {{name|uuid}}`
