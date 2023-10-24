# virsh pool-undefine

> Exclui o arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento de máquina virtual parado.
> Veja também: `virsh`, `virsh-pool-destroy`.
> Mais informações: <https://manned.org/virsh>.

- Excluir a configuração do pool de armazenamento pelo nome ou UUID especificado (determinado usando `virsh pool-list`):

`virsh pool-undefine --pool {{nome|uuid}}`
