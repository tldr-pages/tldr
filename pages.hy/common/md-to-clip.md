# md-to-clip

> Փոխարկել tldr-էջերը հրամանի տողի միջերեսի էջերի:.
> Տես նաև՝ `clip-view`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>:.

- Փոխակերպեք tldr-pages ֆայլերը և պահեք նույն դիրեկտորիաներում.:

`md-to-clip {{path/to/page1.md path/to/page2.md ...}}`

- Փոխակերպեք tldr-pages ֆայլերը և պահեք հատուկ գրացուցակում.:

`md-to-clip --output-directory {{path/to/directory}} {{path/to/page1.md path/to/page2.md ...}}`

- Փոխակերպեք tldr-էջ ֆայլը `stdout`:

`md-to-clip --no-file-save <(echo '{{page-content}}')`

- Փոխակերպեք tldr-pages ֆայլերը՝ ճանաչելով լրացուցիչ տեղապահներ հատուկ կազմաձևից.:

`md-to-clip --special-placeholder-config {{path/to/config.yaml}} {{path/to/page1.md path/to/page2.md ...}}`

- Ցուցադրել օգնությունը.:

`md-to-clip --help`

- Ցուցադրման տարբերակը:

`md-to-clip --version`
