# virsh pool-list

> Lista informações sobre pools de armazenamento de máquinas virtuais.
> Veja também: `virsh`, `virsh-pool-autostart`, `virsh-pool-define-as`.
> Mais informações: <https://manned.org/virsh>.

- Lista o nome, estado e se a inicialização automática está habilitada ou desabilitada para pools de armazenamento ativos:

`virsh pool-list`

- Lista informações para pools de armazenamento ativos e inativos ou apenas inativos:

`virsh pool-list --{{all|inactive}}`

- Lista informações estendidas sobre persistência, capacidade, alocação e espaço disponível para pools de armazenamento ativos:

`virsh pool-list --details`

- Lista informações para pools de armazenamento ativos com inicialização automática habilitada ou desabilitada:

`virsh pool-list --{{autostart|no-autostart}}`

- Lista informações para pools de armazenamento ativos que são persistentes ou transitórios:

`virsh pool-list --{{persistent|transient}}`

- Lista o nome e UUID dos pools de armazenamento ativos:

`virsh pool-list --name --uuid`
