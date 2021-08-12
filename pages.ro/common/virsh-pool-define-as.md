# virsh pool-define-as

> Creați un fișier de configurare în `/etc/libvirt/stocare pentru un rezervor de stocare persistent al mașinilor virtuale din argumentele furnizate.
> A se vedea, de asemenea: `virsh`, `virsh-bazin-build`, `virsh-piscina-start`.
> Mai multe informaţii: <https://manned.org/virsh>

- Creați fișierul de configurare pentru un rezervor de stocare numit pool_name utilizând `/var/vms` ca sistem de stocare subiacent:

`virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}`
