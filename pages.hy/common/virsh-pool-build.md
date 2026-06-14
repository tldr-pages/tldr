# virsh pool-build

> Ստեղծեք վիրտուալ մեքենայի պահեստավորման հիմքում ընկած համակարգը, ինչպես սահմանված է դրա կազմաձևման ֆայլում՝ `/etc/libvirt/storage`-ում:.
> Տես նաև՝ `virsh`, `virsh-pool-define-as`, `virsh-pool-start`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/virsh>:.

- Ստեղծեք պահեստային լողավազան, որը նշված է անունով կամ UUID-ով (որոշեք՝ օգտագործելով `virsh pool-list`):

`virsh pool-build --pool {{name|uuid}}`
