# ansible

> Gerencia grupos de computadores remotamente utilizando SSH. (use o arquivo `/etc/ansible/hosts` para adicionar novos grupos/hosts).
> Alguns subcomando como `ansible galaxy` possuis a própria documentação de uso.
> Mais informações: <https://www.ansible.com/>.

- Lista os hosts pertencentes a um grupo:

`ansible {{grupo}} --list-hosts`

- Realiza o ping de um grupo de hosts invocando o módulo ping:

`ansible {{grupo}} -m ping`

- Exibe fatos sobre um grupo de hosts invocando o módulo setup:

`ansible {{grupo}} -m setup`

- Executa um comando em um grupo de hosts invocando o módulo command com argumentos:

`ansible {{grupo}} -m command -a '{{meu_comando}}'`

- Executa um comando com privilégios administrativos:

`ansible {{grupo}} --become --ask-become-pass -m command -a '{{meu_comando}}'`

- Executa um comando usando um arquivos de inventário customizado:

`ansible {{grupo}} -i {{arquivo_inventario}} -m command -a '{{meu_comando}}'`

- Lista os grupos presentes em um inventário:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
