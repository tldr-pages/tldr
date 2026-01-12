# Get-Clipboard

> Команда PowerShell для получения содержимого буфера обмена.
> Примечание: в качестве псевдонима для `Get-Clipboard` можно использовать `gcb`.
> Больше информации: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-clipboard>.

- Получить текст из буфера обмена:

`Get-Clipboard`

- Получить содержимое буфера обмена в определённом текстовом формате:

`Get-Clipboard -TextFormatType {{Text|Html|Rtf}}`

- Получить необработанное (raw) содержимое буфера обмена:

`Get-Clipboard -Raw`

- Извлечь изображение:

`Get-Clipboard -Format Image`

- Получить список путей к файлам, скопированным в Проводнике:

`Get-Clipboard -Format FileDropList`
