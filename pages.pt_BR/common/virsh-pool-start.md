# virsh pool-start

> Inicia um pool de armazenamento de máquina virtual previamente configurado, mas inativo.
> Veja também: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
> Mais informações: <https://manned.org/virsh>.

- Inicia o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`) e cria o sistema de armazenamento subjacente se ele não existir:

`virsh pool-start --pool {{nome|uuid}} --build`
