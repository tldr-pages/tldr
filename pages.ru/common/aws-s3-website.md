# aws s3 website

> Настраивать конфигурацию веб-сайта для бакета.
> Больше информации: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

- Настроить бакет как статический веб-сайт:

`aws s3 website {{s3://имя-бакета}} --index-document {{index.html}}`

- Настроить страницу ошибки для веб-сайта:

`aws s3 website {{s3://имя-бакета}} --index-document {{index.html}} --error-document {{error.html}}`
