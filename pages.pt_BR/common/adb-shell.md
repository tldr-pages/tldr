# adb shell

> Android Debug Bridge Shell: Executar remotamente comandos shell em instâncias do emulador Android ou dispositivos Android conectados.
> Mais informações: <https://developer.android.com/studio/command-line/adb?hl=pt-br>.

- Iniciar um shell interativo remoto no emulador/dispositivo:

`adb shell`

- Obter todas as propriedades do emulador ou dispositivo:

`adb shell getprop`

- Reverter todas as permissões de tempo de execução para o padrão:

`adb shell pm reset-permissions`

- Revogar uma permissão perigosa para um aplicação:

`adb shell pm revoke {{pacote}} {{permissao}}`

- Acionar um evento:

`adb shell input keyevent {{keycode}}`

- Limpar os dados da aplicação no emulador/dispositivo:

`adb shell pm clear {{pacote}}`

- Iniciar uma atividade no emulator/dispositivo:

`adb shell am start -n {{pacote}}/{{atividade}}`

- Iniciar atividade "home" no emulator/dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
