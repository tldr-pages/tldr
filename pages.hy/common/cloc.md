#ժամ

> Հաշվեք կոդի տողերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/AlDanial/cloc#options->:.

- Հաշվեք կոդերի բոլոր տողերը գրացուցակում.:

`cloc {{path/to/directory}}`

- Համեմատեք դիրեկտորիայի 2 կառուցվածք և հաշվեք դրանց միջև եղած տարբերությունները.:

`cloc --diff {{path/to/directory1}} {{path/to/directory2}}`

- Անտեսեք VCS-ի կողմից անտեսված ֆայլերը, ինչպիսիք են `.gitignore`-ում նշված ֆայլերը:

`cloc --vcs git {{path/to/directory}}`

- Ցուցադրել արդյունքները յուրաքանչյուր ֆայլի համար յուրաքանչյուր լեզվի փոխարեն.:

`cloc --by-file {{path/to/directory}}`
