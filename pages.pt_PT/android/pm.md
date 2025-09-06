# pm

> Mostra informações sobre aplicações num dispositivo Android.
> Mais informações: <https://developer.android.com/tools/adb#pm>.

- Exibe uma lista com todas as aplicações instaladas:

`pm list packages`

- Exibe uma lista com todas as aplicações do sistema instaladas:

`pm list packages -s`

- Exibe uma lista todas as aplicações de terceiros instaladas:

`pm list packages -3`

- Exibe uma lista com todas as aplicações cujos nomes estejam incluídos em palavras-chave:

`pm list packages {{palavras_chave}}`

- Exibe o caminho para o APK de um app:

`pm path {{app}}`
