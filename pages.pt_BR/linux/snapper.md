# snapper

> Utilitário que cria, compara e reverte snapshots com suporte a linhas de tempo de snapshots automáticos.
> Mais informações: 
> - <https://en.opensuse.org/Portal:Snapper>.
> - <https://wiki.archlinux.org/title/Snapper_(Portugu%C3%AAs)>.
> - <http://snapper.io/manpages/snapper.html>.

- Criar uma nova configuração chamada config:

`sudo snapper -c config create-config /caminho/para/subvolume`

- Tirar um snapshot manual do subvolume especificado por config, com descriç:

`sudo snapper -c config create --description desc`

- Criar um snapshot pré e pós dado um certo comando:

`sudo snapper -c config create --command comando`

- Listar todas as configurações que foram criadas:

`sudo snapper list-configs`

- Listar snapshots tirados de uma determinada config:

`sudo snapper -c config list`

- Excluir um snapshot de número N e configuração config:

`sudo snapper -c config delete N`

- Excluir um snapshot de número N e configuração config e imediatamente liberar espaço:

`sudo snapper -c config delete --sync N`

- Excluir snapshots dentro do intervalo dentro de X a Y:

`sudo snapper -c config delete X-Y`
