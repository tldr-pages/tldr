# virsh

> Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado).
> Alguns subcomandos, como `virsh list`, têm sua própria documentação de uso.
> Mais informações: <https://libvirt.org/virshcmdref.html>.

- Conectar-se a uma sessão do hipervisor:

`virsh connect {{qemu:///system}}`

- Listar todos os domínios:

`virsh list --all`

- Despejar arquivo de configuração do convidado:

`virsh dumpxml {{guest_id}} > {{caminho/para/convidado.xml}}`

- Criar um convidado a partir de um arquivo de configuração:

`virsh create {{caminho/para/arquivo_de_configuracao.xml}}`

- Editar o arquivo de configuração de um convidado (o editor pode ser alterado com $EDITOR):

`virsh edit {{guest_id}}`

- Iniciar/reiniciar/desligar/suspender/resumir um convidado:

`virsh {{comando}} {{guest_id}}`

- Salvar o estado atual de um convidado em um arquivo:

`virsh save {{guest_id}} {{nome_do_arquivo}}`

- Excluir um convidado em execução:

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`
