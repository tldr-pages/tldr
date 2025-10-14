# chromium

> Веб-браузер с открытым исходным кодом, в основном разрабатываемый и поддерживаемый Google.
> Примечание: Возможно, вам потребуется заменить команду `chromium` на желаемый веб-браузер, такой как `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera` или `vivaldi`.
> Больше информации: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Открыть указанный URL-адрес или файл:

`chromium {{https://example.com|путь/к/файлу.html}}`

- Открыть в режиме инкогнито (используйте `--inprivate` для Microsoft Edge):

`{{chromium --incognito|msedge --inprivate}} {{example.com}}`

- Открыть в новом окне:

`chromium --new-window {{example.com}}`

- Открыть в режиме приложения (без панелей инструментов, адресной строки, кнопок и т.д.):

`chromium --app {{https://example.com}}`

- Использовать прокси-сервер:

`chromium --proxy-server "{{socks5://hostname:66}}" {{example.com}}`

- Открыть с пользовательским каталогом профиля:

`chromium --user-data-dir {{путь/к/каталогу}}`

- Открыть без проверки CORS (полезно для тестирования API):

`chromium --user-data-dir {{путь/к/каталогу}} --disable-web-security`

- Открыть с окном DevTools для каждой новой вкладки:

`chromium --auto-open-devtools-for-tabs`
