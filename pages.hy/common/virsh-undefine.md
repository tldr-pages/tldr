# virsh undefine

> Ջնջել վիրտուալ մեքենա:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/virsh>:.

- Ջնջել միայն վիրտուալ մեքենայի կազմաձևման ֆայլը.:

`virsh undefine --domain {{vm_name}}`

- Ջնջել կազմաձևման ֆայլը և բոլոր հարակից պահեստային ծավալները.:

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- Ջնջեք կազմաձևման ֆայլը և պահեստավորման նշված ծավալները՝ օգտագործելով թիրախային անունը կամ աղբյուրի անունը (ինչպես ստացվել է `virsh domblklist` հրամանից):

`virsh undefine --domain {{vm_name}} --storage {{sda,sdb,path/to/source,...}}`
