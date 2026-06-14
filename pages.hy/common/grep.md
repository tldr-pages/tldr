#գրեպ

> Գտեք նախշեր ֆայլերում՝ օգտագործելով `regex`es:.
> Տես նաև՝ `rg`, `regex`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/grep/manual/grep.html>:.

- Որոնեք օրինաչափություն ֆայլերի մեջ.:

`grep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Որոնել ճշգրիտ տող (անջատում է `regex`es):

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Փնտրեք օրինաչափություն բոլոր ֆայլերում ռեկուրսիվ կերպով գրացուցակում, անտեսելով երկուական ֆայլերը.:

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- Տպեք [C] տեքստի 3 տող շուրջը, [B]նախօրոք կամ [A]յուրաքանչյուր համընկնումից հետո.:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Տպեք ֆայլի անունը և տողի համարը յուրաքանչյուր համընկնման համար գունավոր ելքով.:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Տպել միայն համապատասխան տեքստը.:

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Կարդացեք տվյալներ `stdin`-ից և մի տպեք տողեր, որոնք համապատասխանում են օրինաչափությանը.:

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`

- Օգտագործեք ընդլայնված `regex`es (աջակցում է `?`, `+`, `{}`, `()` և `|`), տառատեսակների համար ոչ զգայուն ռեժիմում.:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
