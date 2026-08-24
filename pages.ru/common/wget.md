# wget

> Скачивать файлы из интернета.
> Поддерживает HTTP, HTTPS и FTP.
> Смотрите также: `wcurl`, `curl`.
> Больше информации: <https://www.gnu.org/software/wget/manual/wget.html>.

- Скачать содержимое URL в файл (в данном случае с именем "foo"):

`wget {{https://example.com/foo}}`

- Скачать содержимое URL в файл (в данном случае с именем "bar"):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Скачать одну веб-страницу и все её ресурсы с интервалом в 3 секунды между запросами (скрипты, таблицы стилей, изображения и т.д.):

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/some_page.html}}`

- Скачать все перечисленные файлы в каталоге и его подкаталогах (не скачивает встроенные элементы страницы):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/some_path/}}`

- Ограничить скорость скачивания и количество попыток подключения:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/some_path/}}`

- Скачать файл с HTTP-сервера, используя базовую аутентификацию (также работает для FTP):

`wget --user {{имя_пользователя}} --password {{пароль}} {{https://example.com}}`

- Продолжить незавершённое скачивание:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Скачать все URL, сохранённые в текстовом файле, в указанный каталог:

`wget {{[-P|--directory-prefix]}} {{путь/к/каталогу}} {{[-i|--input-file]}} {{путь/к/URLs.txt}}`
