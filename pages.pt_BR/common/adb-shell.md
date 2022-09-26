# adb shell

> Android Debug Bridge Shell: Executar remotamente comandos shell em instâncias do emulador Android ou dispositivos Android conectados.
> Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Inicia um shell interativo remoto no emulador/dispositivo:

`adb shell`

- Obtém todas as propriedades do emulador ou dispositivo:

`adb shell getprop`

- Reverte todas as permissões de tempo de execução para o padrão:

`adb shell pm reset-permissions`

- Revoga uma permissão perigosa para um aplicação:

`adb shell pm revoke {{pacote}} {{permissao}}`

- Aciona um evento:

`adb shell input keyevent {{keycode}}`

- Limpa os dados da aplicação no emulador/dispositivo:

`adb shell pm clear {{pacote}}`

- Inicia uma atividade no emulator/dispositivo:

`adb shell am start -n {{pacote}}/{{atividade}}`

- Inicia atividade "home" no emulator/dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
