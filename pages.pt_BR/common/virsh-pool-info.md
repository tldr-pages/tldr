# virsh pool-info

> Lista informações sobre um pool de armazenamento de máquina virtual.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Lista o nome, UUID, estado, tipo de persistência, status de inicialização automática, capacidade, espaço alocado e espaço disponível para o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-info --pool {{nome|uuid}}`
