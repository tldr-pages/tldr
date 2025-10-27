# Doskey

>Gerencie macros, comandos do Windows e linhas de comando.
> Mais informações: https://learn.microsoft.com/windows-server/administration/windows-commands/doskey .

- Listar macros disponíveis:
doskey /macros

- Crie uma nova macro:
doskey {{name}} = "{{command}}"

- Crie uma nova macro para um executável específico:
doskey /exename={{executable}} {{name}} = "{{command}}"

- Remover uma macro:
doskey {{name}} =

- Exibir todos os comandos armazenados na memória:
doskey /history

- Salve macros em um arquivo para portabilidade:
doskey /macros > {{path\to\macinit_file}}

- Carregar macros de um arquivo:
doskey /macrofile = {{path\to\macinit_file}}
