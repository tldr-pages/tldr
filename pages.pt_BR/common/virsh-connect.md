# virsh-connect

> Conectar-se a um hipervisor de máquina virtual.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Conecta ao hipervisor padrão:

`virsh connect`

- Conecta como root ao hipervisor local QEMU/KVM:

`virsh connect qemu:///system`

- Inicia uma nova instância do hipervisor e conectar-se a ela como usuário local:

`virsh connect qemu:///session`

- Conecta como root a um hipervisor remoto usando SSH:

`virsh connect qemu+ssh://{{nome_do_usuário@nome_do_host}}/system`
