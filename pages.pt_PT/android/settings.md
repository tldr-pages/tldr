# settings

> Exibe, edita e apaga configurações do sistema Android.
> Mais informações: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Exibir a lista de configurações no namespace `global`:

`settings list {{global}}`

- Obter o valor de uma configuração específica:

`settings get {{global}} {{airplane_mode_on}}`

- Editar o valor de uma configuração:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Apagar uma configuração:

`settings delete {{secure}} {{screensaver_enabled}}`
