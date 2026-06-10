# xzgrep

> Որոնեք ֆայլեր, որոնք, հնարավոր է, սեղմված են `xz`, `lzma`, `gzip`, `bzip2`, `lzop` կամ `zstd`-ով՝ օգտագործելով `regex`:.
> Տես նաև՝ `grep`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xzgrep>:.

- Որոնեք օրինակ ֆայլի մեջ.:

`xzgrep "{{search_pattern}}" {{path/to/file}}`

- Որոնել ճշգրիտ տող (անջատում է `regex`):

`xzgrep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Որոնեք օրինաչափություն բոլոր ֆայլերում, որոնք ցույց են տալիս համընկնող տողերի համարները.:

`xzgrep {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file}}`

- Տպեք [C] տեքստի 3 տող շուրջը, [B]նախօրոք կամ [A]յուրաքանչյուր համընկնումից հետո.:

`xzgrep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Տպեք ֆայլի անունը և տողի համարը յուրաքանչյուր համընկնման համար գունավոր ելքով.:

`xzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Որոնեք օրինակին համապատասխանող տողեր՝ տպելով միայն համապատասխան տեքստը.:

`xzgrep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Օգտագործեք ընդլայնված `regex`-ը (աջակցում է `?`, `+`, `{}`, `()` և `|`), տառատեսակների համար ոչ զգայուն ռեժիմում.:

`xzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
