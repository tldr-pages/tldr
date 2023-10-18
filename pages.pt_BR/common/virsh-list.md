# virsh-list

> Liste o ID, nome e estado das máquinas virtuais.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Listar informações sobre máquinas virtuais em execução:

`virsh list`

- Listar informações sobre máquinas virtuais independentemente do estado:

`virsh list --all`

- Listar informações sobre máquinas virtuais com autostart ativado ou desativado:

`virsh list --all --{{autostart|no-autostart}}`

- Listar informações sobre máquinas virtuais com ou sem snapshots:

`virsh list --all --{{with-snapshot|without-snapshot}}`
