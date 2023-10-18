# virsh pool-build

> Constrói o sistema de armazenamento subjacente para um pool de armazenamento de máquina virtual, conforme definido em seu arquivo de configuração em `/etc/libvirt/storage`.
> Veja também: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
> Mais informações: <https://manned.org/virsh>.

- Constrói o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-build --pool {{nome|uuid}}`
