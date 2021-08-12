# virsh-domblklist

> Listați informații despre dispozitivele bloc asociate cu o mașină virtuală.
> A se vedea, de asemenea: `virsh`.
> Mai multe informaţii: <https://manned.org/virsh>

- Listați numele țintă și calea sursă a dispozitivelor bloc:

`virsh domblklist --domain {{vm_name}}`

- Listați tipul de disc și valoarea dispozitivului, precum și numele țintă și calea sursă:

`virsh domblklist --domain {{vm_name}} --details`
