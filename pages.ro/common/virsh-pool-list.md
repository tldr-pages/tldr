# virsh pool-list

> Listă informații despre piscine de stocare mașină virtuală.
> A se vedea de asemenea: `virsh`, `virsh-pool-autostart', `virsh-pool-define-ca`.
> Mai multe informaţii: <https://manned.org/virsh>

- Listați numele, starea și dacă autostart este activată sau dezactivată pentru piscine de stocare active:

`virsh pool-list`

- Lista de informații pentru piscine de stocare active și inactive sau doar inactive:

`virsh pool-list --{{all|inactive}}`

- Listați informații extinse despre persistență, capacitate, alocare și spațiu disponibil pentru piscine de stocare active:

`virsh pool-list --details`

- Lista de informații pentru piscine de stocare active cu autostart activat sau dezactivat:

`virsh pool-list --{{autostart|no-autostart}}`

- Lista de informații pentru bazine de stocare active care sunt fie persistente sau tranzitorii:

`virsh pool-list --{{persistent|transient}}`

- Listați numele și UUID ale bazinelor de stocare active:

`virsh pool-list --name --uuid`
