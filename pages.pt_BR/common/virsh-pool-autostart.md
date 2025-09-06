# virsh pool-autostart

> Habilita ou desabilita a inicialização automática para um pool de armazenamento de máquina virtual.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Habilita a inicialização automática para o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-autostart --pool {{nome|uuid}}`

- Desabilita a inicialização automática para o pool de armazenamento especificado pelo nome ou UUID:

`virsh pool-autostart --pool {{nome|uuid}} --disable`
