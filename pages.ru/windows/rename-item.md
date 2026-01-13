# Rename-Item

> Команда PowerShell для переименования элемента.
> Примечание: в качестве псевдонимов для `Rename-Item` можно использовать `ren` и `rni`.
> Больше информации: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/rename-item>.

- Переименовать файл:

`Rename-Item -Path "{{путь\к\файлу}}" -NewName "{{новое_имя_файла}}"`

- Переименовать каталог:

`Rename-Item -Path "{{путь\к\каталогу}}" -NewName "{{новое_имя_каталога}}"`

- Переименовать и переместить файл:

`Rename-Item -Path "{{путь\к\файлу}}" -NewName "{{путь\к\новому_имени_файла}}"`

- Принудительно переименовать файл:

`Rename-Item -Path "{{путь\к\файлу}}" -NewName "{{новое_имя_файла}}" -Force`

- Запросить подтверждение перед переименованием файла:

`Rename-Item -Path "{{путь\к\файлу}}" -NewName "{{новое_имя_файла}}" {{[-Confirm|-cf]}}`
