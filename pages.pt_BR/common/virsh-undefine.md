# virsh-undefine

> Excluir uma máquina virtual.
> Mais informações: <https://manned.org/virsh>.

- Exclui apenas o arquivo de configuração da máquina virtual:

`virsh undefine --domain {{nome_da_vm}}`

- Exclui o arquivo de configuração e todos os volumes de armazenamento associados:

`virsh undefine --domain {{nome_da_vm}} --remove-all-storage`

- Exclui o arquivo de configuração e os volumes de armazenamento especificados usando o nome de destino ou o nome de origem (obtido a partir do comando `virsh domblklist`):

`virsh undefine --domain {{nome_da_vm}} --storage {{sda,caminho/para/origem}}`
