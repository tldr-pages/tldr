# protontricks

> Um wrapper simples que executa comandos WineTricks para jogos habilitados para o Proton.
> Mais informações: <https://github.com/Matoking/protontricks>.

- Executa a GUI do Protontricks:

`protontricks --gui`

- Executa o WineTricks para um jogo específico:

`protontricks {{appid}} {{argumentos_do_winetricks}}`

- Executa um comando no diretório de instalação de um jogo:

`protontricks -c {{comando}} {{appid}}`

- [l]ista todos os jogos instalados:

`protontricks -l`

- Busca o App ID de um jogo pelo nome:

`protontricks -s {{nome_do_jogo}}`

- Mostra a mensagem de ajuda do Protontricks:

`protontricks --help`
