# asciidoctor

> Преобразователь AsciiDoc файлов в другие форматы для публикации.
> Дополнительная информация: <https://docs.asciidoctor.org>.

- Преобразовать данный `.adoc` файл в HTML (формат на выходе по умолчанию):

`asciidoctor {{path/to/file.adoc}}`

- Преобразовать данный `.adoc` файл в HTML и привязать к таблице стилей CSS:

`asciidoctor -a stylesheet={{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- Преобразовать данный `.adoc` файл во встраиваемый HTML, убрав всё кроме самого текста:

`asciidoctor --embedded {{path/to/file.adoc}}`

- Преобразовать данный `.adoc` файл в PDF с помощью библиотеки `asciidoctor-pdf`:

`asciidoctor --backend={{pdf}} --require={{asciidoctor-pdf}} {{path/to/file.adoc}}`
