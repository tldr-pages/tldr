# virsh-domblklist

> Listar informações sobre dispositivos de bloco associados a uma máquina virtual.
> Veja também: `virsh`.
> Mais informações: <https://manned.org/virsh>.

- Listar o nome do destino e o caminho da origem dos dispositivos de bloco:

`virsh domblklist --domain {{nome_da_vm}}`

- Listar o tipo de disco e o valor do dispositivo, bem como o nome do destino e o caminho da origem:

`virsh domblklist --domain {{nome_da_vm}} --details`
