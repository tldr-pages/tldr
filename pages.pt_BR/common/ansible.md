# ansible

> Gerencia grupos de computadores remotamente utilizando SSH. (use o arquivo `/etc/ansible/hosts` para adicionar novos grupos/hosts).
> Alguns subcomando como `ansible galaxy` possuis a própria documentação de uso.
> Mais informações: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Lista os hosts pertencentes a um grupo:

`ansible {{grupo}} --list-hosts`

- Realiza o ping de um grupo de hosts invocando o módulo ping:

`ansible {{grupo}} {{[-m|--module-name]}} ping`

- Exibe fatos sobre um grupo de hosts invocando o módulo setup:

`ansible {{grupo}} {{[-m|--module-name]}} setup`

- Executa um comando em um grupo de hosts invocando o módulo command com argumentos:

`ansible {{grupo}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{meu_comando}}'`

- Executa um comando com privilégios administrativos:

`ansible {{grupo}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{meu_comando}}'`

- Executa um comando usando um arquivos de inventário customizado:

`ansible {{grupo}} {{[-i|--inventory]}} {{arquivo_inventario}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{meu_comando}}'`

- Lista os grupos presentes em um inventário:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
