# elasticsearch-saml-metadata

> Генерировать метаданные поставщика услуг SAML для настройки поставщика удостоверений SAML.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/saml-metadata>.

- Сгенерировать метаданные SAML для конкретной области и вывести их в `stdout`:

`elasticsearch-saml-metadata --realm {{имя_области}}`

- Сгенерировать метаданные SAML и записать их в конкретный файл:

`elasticsearch-saml-metadata --realm {{имя_области}} --out {{путь/к/файлу.xml}}`

- Показать справку:

`elasticsearch-saml-metadata {{[-h|--help]}}`
