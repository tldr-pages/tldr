# pm

> Executa ações e consultas em pacotes de apps instalados no dispositivo.
> Esse comando pode ser usado através de `adb shell`, excluindo a necessidade de prefixar ele com `adb`.
> Mais informações: <https://developer.android.com/studio/command-line/adb#pm>.

- Exibir uma lista com todos os apps instalados:

`pm list packages`

- Exibir uma lista com todos os apps do sistema instalado:

`pm list packages -s`

- Exibir uma lista com todos os apps de terceiros instalados:

`pm list packages -3`

- Exibir uma lista com todos os apps cujos nomes estejam incluídos em `{{keywords}}`:

`pm list packages {{keywords}}`

- Exibir o caminho para o APK de um app:

`pm path {{app}}`
