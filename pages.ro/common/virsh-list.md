# virsh-list

> Listați ID-ul, numele și starea mașinilor virtuale.
> A se vedea, de asemenea: `virsh`.
> Mai multe informaţii: <https://manned.org/virsh>

- Lista de informații despre rularea mașinilor virtuale:

`virsh list`

- Lista de informații despre mașinile virtuale, indiferent de stat:

`virsh list --all`

- Lista de informații despre mașinile virtuale cu autostart fie activat sau dezactivat:

`virsh list --all --{{autostart|no-autostart}}`

- Lista de informații despre mașinile virtuale, fie cu sau fără instantanee:

`virsh list --all --{{with-snapshot|without-snapshot}}`
