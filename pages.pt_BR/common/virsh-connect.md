# virsh-connect

> Conectar-se a um hipervisor de máquina virtual.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Conectar-se ao hipervisor padrão:

`virsh connect`

- Conectar-se como root ao hipervisor local QEMU/KVM:

`virsh connect qemu:///system`

- Iniciar uma nova instância do hipervisor e conectar-se a ela como usuário local:

`virsh connect qemu:///session`

- Conectar-se como root a um hipervisor remoto usando ssh:

`virsh connect qemu+ssh://{{nome_do_usuário@nome_do_host}}/system`
