# բզգեպ

> Գտեք նմուշներ `bzip2` սեղմված ֆայլերում՝ օգտագործելով `grep`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bzgrep>:.

- Փնտրեք օրինաչափություն սեղմված ֆայլի մեջ.:

`bzgrep "{{search_pattern}}" {{path/to/file}}`

- Recursively որոնեք ֆայլերը bzip2 սեղմված `.tar` արխիվում օրինակի համար.:

`bzgrep {{[-r|--recursive]}} "{{search_pattern}}" {{path/to/tar_file}}`

- Տպեք [C] տեքստի 3 տող շուրջը, [B]նախօրոք կամ [A]յուրաքանչյուր համընկնումից հետո.:

`bzgrep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Տպել ֆայլի անունը և տողի համարը յուրաքանչյուր համընկնման համար.:

`bzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file}}`

- Որոնեք օրինակին համապատասխանող տողեր՝ տպելով միայն համապատասխան տեքստը.:

`bzgrep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Որոնեք `stdin` տողեր, որոնք չեն համապատասխանում օրինաչափությանը.:

`cat {{path/to/bz_compressed_file}} | bzgrep {{[-v|--invert-match]}} "{{search_pattern}}"`

- Օգտագործեք ընդլայնված `regex` (աջակցում է `?`, `+`, `{}`, `()`, և `|`), տառատեսակների համար ոչ զգայուն ռեժիմում.:

`bzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
