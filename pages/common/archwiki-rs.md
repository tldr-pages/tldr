# archwiki-rs

> A CLI tool to read pages from the ArchWiki.
> More information: <https://gitlab.com/lucifayr/archwiki-rs>.

- Read a page from the ArchWiki:

`archwiki-rs read-page {{page-title}}`

- Read a page from the ArchWiki in the specified format:

`archwiki-rs read-page {{page-title}} --format {{plain-text|markdown|html}}`

- Search the ArchWiki for pages containing the text "/usr/share":

`archwiki-rs search "/usr/share" --text-search`

- Download a local copy of all ArchWiki pages:

`archwiki-rs local-wiki ~/archwiki-html --format html`
