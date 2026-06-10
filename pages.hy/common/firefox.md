# firefox

> Ազատ և բաց կոդով վեբ զննարկիչ:.
> Լրացուցիչ տեղեկություններ. <https://wiki.mozilla.org/Firefox/CommandLineOptions>:.

- Գործարկեք Firefox-ը և բացեք վեբ էջ.:

`firefox {{https://www.duckduckgo.com}}`

- Բացեք նոր պատուհան.:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Բացեք անձնական (ինկոգնիտո) պատուհան.:

`firefox --private-window`

- Որոնեք «վիքիպեդիա»՝ օգտագործելով լռելյայն որոնման համակարգը.:

`firefox --search "{{wikipedia}}"`

- Գործարկեք Firefox-ը անվտանգ ռեժիմով, բոլոր ընդլայնումներն անջատված են.:

`firefox --safe-mode`

- Վերցրեք վեբ էջի սքրինշոթը առանց գլխի ռեժիմով.:

`firefox --headless --screenshot {{path/to/output_file.png}} {{https://example.com/}}`

- Օգտագործեք հատուկ պրոֆիլ, որպեսզի թույլ տաք Firefox-ի մի քանի առանձին օրինակներ միանգամից գործարկել.:

`firefox --profile {{path/to/directory}} {{https://example.com/}}`

- Սահմանեք Firefox-ը որպես լռելյայն դիտարկիչ.:

`firefox --setDefaultBrowser`
