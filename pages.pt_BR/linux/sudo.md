# sudo

> Utilizado para realizar comandos como superuser, o equivalente ao "administrador" do Windows.
> Para mais detalhes, acesse [este site](https://manned.org/sudo).

- Um caso geral pode ser descrito como:

`sudo <comando>`

> Casos mais específicos podem se utilizar das flags de sudo, como -e, que permitem edição de arquivos.
> Contudo, na grande maioria das vezes, essas flags não são necessárias. Para aprender sobre elas, refira-se ao site citado acima.

> Exemplos de uso:

- Para remover um diretório read-only (i.e. protegida com permissão apenas de leitura), é necessário o uso de sudo, como segue:

`sudo rm -r <pasta>`

> *Note que o uso do sudo depende do input da senha do usuário.*

- Para atualizações do sistema em distribuições Linux baseadas em Arch.

`sudo pacman -Syu`

> *No exemplo, o sudo é necessário para que a atualização tenha efeito sob todos os arquivos do sistema.*
