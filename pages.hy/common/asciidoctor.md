#ասցիիդոկտոր

> Փոխարկել AsciiDoc ֆայլերը հրապարակվող ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>:.

- Փոխակերպեք կոնկրետ `.adoc` ֆայլը HTML-ի (լռելյայն ելքային ձևաչափ).:

`asciidoctor {{path/to/file.adoc}}`

- Փոխակերպեք կոնկրետ `.adoc` ֆայլը HTML-ի և կապեք CSS ոճի թերթիկը.:

`asciidoctor {{[-a|--attribute]}} stylesheet={{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- Փոխակերպեք կոնկրետ `.adoc` ֆայլը ներկառուցվող HTML-ի՝ հեռացնելով ամեն ինչ, բացի մարմնից:

`asciidoctor {{[-e|--embedded]}} {{path/to/file.adoc}}`

- Փոխակերպեք որոշակի `.adoc` ֆայլը PDF-ի, օգտագործելով `asciidoctor-pdf` գրադարանը՝:

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{path/to/file.adoc}}`
