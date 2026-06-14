# diff-pdf

> Համեմատեք երկու PDF ֆայլ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/vslavik/diff-pdf>:.

- Համեմատեք PDF ֆայլերը՝ նշելով փոփոխությունները՝ օգտագործելով վերադարձի կոդերը (`0` = տարբերություն չկա, `1` = PDF-ները տարբերվում են):

`diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}`

- Համեմատեք PDF ֆայլերը՝ դուրս բերելով PDF՝ տեսողականորեն ընդգծված տարբերություններով.:

`diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}`

- Համեմատեք PDF-ները՝ դիտելով տարբերությունները պարզ GUI-ում.:

`diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}`
