# archwiki-rs

> Read, search and download pages from the ArchWiki.
> More information: <https://gitlab.com/lucifayr/archwiki-rs>.

- Read a page from the ArchWiki:

`archwiki-rs read-page {{page_title}}`

- Read a page from the ArchWiki in the specified format:

`archwiki-rs read-page {{page_title}} --format {{plain-text|markdown|html}}`

- Search the ArchWiki for pages containing the provided text:

`archwiki-rs search "{{search_text}}" --text-search`

- Download a local copy of all ArchWiki pages into a specific directory:

`archwiki-rs local-wiki {{/path/to/local_wiki}} --format {{plain-text|markdown|html}}`
