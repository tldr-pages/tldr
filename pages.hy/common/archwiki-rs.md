# archwiki-rs

> Կարդացեք, որոնեք և ներբեռնեք էջերը ArchWiki-ից:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/lucifayr/archwiki-rs>:.

- Կարդացեք մի էջ ArchWiki-ից.:

`archwiki-rs read-page {{page_title}}`

- Կարդացեք ArchWiki-ից էջը նշված ձևաչափով.:

`archwiki-rs read-page {{page_title}} --format {{plain-text|markdown|html}}`

- Որոնեք ArchWiki-ում տրամադրված տեքստը պարունակող էջեր.:

`archwiki-rs search "{{search_text}}" --text-search`

- Ներբեռնեք ArchWiki-ի բոլոր էջերի տեղական պատճենը հատուկ գրացուցակում.:

`archwiki-rs local-wiki /{{path/to/local_wiki}} --format {{plain-text|markdown|html}}`
