# pm

> Executa ações e consultas em pacotes de apps instalados no dispositivo.
> Mais informações: <https://developer.android.com/studio/command-line/adb#pm>.

- Exibe uma lista com todos os apps instalados:

`pm list packages`

- Exibe uma lista com todos os apps do sistema instalado:

`pm list packages -s`

- Exibe uma lista com todos os apps de terceiros instalados:

`pm list packages -3`

- Exibe uma lista com todos os apps cujos nomes estejam incluídos em palavras-chave:

`pm list packages {{palavras_chave}}`

- Exibe o caminho para o APK de um app:

`pm path {{app}}`
