# zipgrep

> Գտեք նախշեր Zip արխիվում ֆայլերում՝ օգտագործելով ընդլայնված `regex` (աջակցում է `?`, `+`, `{}`, `()` և `|`):.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zipgrep>:.

- Որոնեք օրինաչափություն Zip արխիվում.:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}}`

- Տպել ֆայլի անունը և տողի համարը յուրաքանչյուր համընկնման համար.:

`zipgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{search_pattern}}" {{path/to/file.zip}}`

- Որոնեք գծեր, որոնք չեն համապատասխանում օրինաչափությանը.:

`zipgrep {{[-v|--invert-match]}} "{{search_pattern}}" {{path/to/file.zip}}`

- Որոնումից նշեք ֆայլերը Zip արխիվում.:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{file/to/search1}} {{file/to/search2}}`

- Բացառեք Zip արխիվի ներսում գտնվող ֆայլերը որոնումից.:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{[-x|--line-regexp]}} {{file/to/exclude1}} {{file/to/exclude2}}`
