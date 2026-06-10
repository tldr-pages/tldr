#մուտագեն

> Իրական ժամանակի ֆայլերի համաժամացման և ցանցի վերահասցեավորման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://mutagen.io/documentation/introduction/>:.

- Սկսեք համաժամացման նիստ տեղական գրացուցակի և հեռավոր հոսթի միջև.:

`mutagen sync create --name={{session_name}} /{{path/to/local_directory}}/ {{user}}@{{host}}:/{{path/to/remote_directory}}/`

- Սկսեք համաժամացման նիստ տեղական գրացուցակի և Docker կոնտեյների միջև.:

`mutagen sync create --name={{session_name}} /{{path/to/local_directory}}/ docker://{{user}}@{{container_name}}/{{path/to/remote_directory}}/`

- Դադարեցրեք ընթացիկ նստաշրջանը.:

`mutagen sync terminate {{session_name}}`

- Նախագիծ սկսել.:

`mutagen project start`

- Դադարեցնել նախագիծը.:

`mutagen project terminate`

- Թվարկեք ընթացիկ նախագծի ընթացիկ նիստերը.:

`mutagen project list`
