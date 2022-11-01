# ansible

> Gerencia grupos de computadores remotamente utilizando SSH. (use o arquivo `/etc/ansible/hosts` para adicionar novos grupos/hosts).
> Alguns subcomando como `ansible galaxy` possuis a própria documentação de uso.
> Mais informações: <https://www.ansible.com/>.

- Lista os hosts pertencentes a um grupo:

`ansible {{group}} --list-hosts`

- Realiza o ping de um grupo de hosts invocando o módulo ping:

`ansible {{group}} -m ping`

- Exibe fatos sobre um grupo de hosts invocando o módulo setup:

`ansible {{group}} -m setup`

- Executa um comando em um grupo de hosts invocando o módulo comando com argumentos:

`ansible {{group}} -m command -a '{{my_command}}'`

- Executa um comando com privilégios administrativos:

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- Executa um comando usando um arquivos de inventário customizado:

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`

- Lista os grupos presentes em um inventário:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
