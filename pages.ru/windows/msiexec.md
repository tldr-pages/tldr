# msiexec

> Установка, обновление, восстановление или удаление программ Windows через пакеты установки MSI и MSP.
> Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Установить программу из MSI-пакета:

`msiexec /package {{путь/до/файла.msi}}`

- Установить MSI-пакет с веб-сайта:

`msiexec /package {{https://example.com/installer.msi}}`

- Установить MSP-пакет с обновлением (патчем):

`msiexec /update {{путь/до/файла.msp}}`

- Удалить программу или обновление, используя соответствующий пакет MSI или MSP:

`msiexec /uninstall {{путь/до/файла}}`
