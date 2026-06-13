# pacman-mirrors

> Gera uma lista de mirrors do pacman para o Manjaro Linux.
> Toda execução do pacman-mirrors requer que você sincronize seu bando de dados e atualize seu sistema usado `sudo pacman -Syyu`.
> Veja também: `pacman`.
> Mais informações: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Gera uma lista de mirrors usando as configurações padrão:

`sudo pacman-mirrors --fasttrack`

- Obtém o status dos mirrors atuais:

`pacman-mirrors --status`

- Exibe a branch atual:

`pacman-mirrors --get-branch`

- Muda para uma branch diferente:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Gera uma lista de mirror, usando apenas mirrors em seu país:

`sudo pacman-mirrors --geoip`
