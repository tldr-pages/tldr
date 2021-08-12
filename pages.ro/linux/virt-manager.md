# virt-manager

> Lansator CLI pentru virt-manager, o interfață utilizator desktop pentru gestionarea mașinilor virtuale KVM și Xen și containere LXC.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/man1/virt-manager.1.html>

- Lansare virt-manager:

`virt-manager`

- Conectaţi-vă la un hipervizor:

`virt-manager --connect {{hypervisor_uri}}`

- Nu forțați procesul virt-manager în fundal la pornire:

`virt-manager --no-fork`

- Imprimare de ieșire de depanare:

`virt-manager --debug`

- Deschideți expertul „New VM”:

`virt-manager --show-domain-creator`

- Arată fereastra cu detalii domeniu:

`virt-manager --show-domain-editor {{name|id|uuid}}`

- Arată fereastra de performanță a domeniului:

`virt-manager --show-domain-performance {{name|id|uuid}}`

- Afișează fereastra detaliilor conexiunii:

`virt-manager --show-host-summary`
