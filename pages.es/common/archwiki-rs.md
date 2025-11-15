# archwiki-rs

> Lee, busca y descarga páginas de la ArchWiki.
> Más información: <https://gitlab.com/lucifayr/archwiki-rs>.

- Lee una página de la ArchWiki:

`archwiki-rs read-page {{título_de_página}}`

- Lee una página de la ArchWiki en el formato especificado:

`archwiki-rs read-page {{título_de_página}} --format {{plain-text|markdown|html}}`

- Busca páginas en ArchWiki con el texto proporcionado:

`archwiki-rs search "{{texto_a_buscar}}" --text-search`

- Descarga una copia local de todas las páginas de ArchWiki en un directorio específico:

`archwiki-rs local-wiki {{ruta/a/wiki_local}} --format {{plain-text|markdown|html}}`
