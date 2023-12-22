# virsh

> Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado).
> Alguns subcomandos, como `virsh list`, têm sua própria documentação de uso.
> Mais informações: <https://libvirt.org/virshcmdref.html>.

- Conecta a uma sessão do hipervisor:

`virsh connect {{qemu:///system}}`

- Lista todos os domínios:

`virsh list --all`

- Despeja arquivo de configuração do convidado:

`virsh dumpxml {{guest_id}} > {{caminho/para/convidado.xml}}`

- Cria um convidado a partir de um arquivo de configuração:

`virsh create {{caminho/para/arquivo_de_configuracao.xml}}`

- Edita o arquivo de configuração de um convidado (o editor pode ser alterado com $EDITOR):

`virsh edit {{guest_id}}`

- Inicia/reinicia/desliga/suspende/resume um convidado:

`virsh {{comando}} {{guest_id}}`

- Salva o estado atual de um convidado em um arquivo:

`virsh save {{guest_id}} {{nome_do_arquivo}}`

- Exclui um convidado em execução:

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`
