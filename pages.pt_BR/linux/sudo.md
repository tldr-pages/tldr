# sudo

> Executa um único comando como o Superuser, ou como outro usuário. Para mais informações, acesse [este site](https://manned.org/sudo).

- Executar um comando como Superuser:

`sudo {{less /var/log/syslog}}`

- Editar um arquivo, como Superuser, com seu editor padrão:

`sudo --edit {{/etc/fstab}}`

- Executar um comando como outro usuário e/ou grupo:

`sudo --user={{usuário}} --group={{grupo}} {{id -a}}}`

- Executar um comando anterior com o prefixo `sudo` (apenas em `bash`, `zsh`, etc.):

`sudo !!`

- Abrir o shell padrão com privilégios de Superuser e executar arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Abrir o shell padrão com privilégios de Superuser sem alterar o ambiente de execução:

`sudo --shell`

- Abrir o shell padrão como dado usuário, carregando o ambiente de execução deste usuário e lendo arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login --user={{usuário}}`

- Listar os comandos permitidos (e não permitidos) para o usuário atual:

`sudo --list`
