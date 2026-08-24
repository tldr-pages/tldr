# asciidoctor

> Преобразователь AsciiDoc файлов в другие форматы для публикации.
> Больше информации: <https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>.

- Преобразовать данный `.adoc` файл в HTML (выходной формат по умолчанию):

`asciidoctor {{путь/к/файлу.adoc}}`

- Преобразовать данный `.adoc` файл в HTML и привязать таблицу стилей CSS:

`asciidoctor {{[-a|--attribute]}} stylesheet={{путь/к/таблице_стилей.css}} {{путь/к/файлу.adoc}}`

- Преобразовать данный `.adoc` файл во встраиваемый HTML, убрав всё, кроме самого текста:

`asciidoctor {{[-e|--embedded]}} {{путь/к/файлу.adoc}}`

- Преобразовать данный `.adoc` файл в PDF с помощью библиотеки `asciidoctor-pdf`:

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{путь/к/файлу.adoc}}`
