# pm

> Mostra informações sobre aplicações num dispositivo Android.
> Mais informações: <https://developer.android.com/studio/command-line/adb#pm>.

- Exibir uma lista com todas as aplicações instaladas:

`pm list packages`

- Exibir uma lista com todas as aplicações do sistema instaladas:

`pm list packages -s`

- Exibir uma lista todas as aplicações de terceiros instaladas:

`pm list packages -3`

- Exibir uma lista com todas as aplicações cujos nomes estejam incluídos em palavras-chave:

`pm list packages {{palavras_chave}}`

- Exibir o caminho para o APK de um app:

`pm path {{app}}`
