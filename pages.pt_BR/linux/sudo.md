# sudo

> Utilizado para realizar comandos como superuser, o equivalente ao "administrador" do Windows.
> Para mais detalhes, acesse [este site](https://manned.org/sudo).

- Um caso geral pode ser descrito como:

`sudo {{comando}}`

- Por exemplo, para remover um diretório read-only (i.e. protegida com permissão apenas de leitura), é necessário o uso de sudo, como segue:

`sudo rm -r {{pasta}}`

- Para atualizações do sistema em distribuições Linux baseadas em Arch.

`sudo pacman -Syu`
