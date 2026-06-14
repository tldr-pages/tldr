# git check-անտեսել

> Վերլուծել և վրիպազերծել Git անտեսել/բացառել (`.gitignore`) ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-check-ignore>:.

- Ստուգեք՝ արդյոք ֆայլը կամ գրացուցակը անտեսված է.:

`git check-ignore {{path/to/file_or_directory}}`

- Ստուգեք, թե արդյոք բազմաթիվ ֆայլեր կամ գրացուցակներ անտեսված են.:

`git check-ignore {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Օգտագործեք երթուղիների անունները, յուրաքանչյուր տողի համար, `stdin`-ից:

`git < {{path/to/file_list}} check-ignore --stdin`

- Մի ստուգեք ինդեքսը (օգտագործվում է վրիպազերծելու համար, թե ինչու են ուղիները հետևվել և չեն անտեսվել).:

`git check-ignore --no-index {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ներառեք մանրամասներ յուրաքանչյուր ուղու համապատասխան օրինաչափության մասին.:

`git check-ignore {{[-v|--verbose]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
