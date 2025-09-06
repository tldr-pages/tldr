# virsh-list

> Liste o ID, nome e estado das máquinas virtuais.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Lista informações sobre máquinas virtuais em execução:

`virsh list`

- Lista informações sobre máquinas virtuais independentemente do estado:

`virsh list --all`

- Lista informações sobre máquinas virtuais com autostart ativado ou desativado:

`virsh list --all --{{autostart|no-autostart}}`

- Lista informações sobre máquinas virtuais com ou sem snapshots:

`virsh list --all --{{with-snapshot|without-snapshot}}`
