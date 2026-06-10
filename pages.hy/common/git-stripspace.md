# git stripspace

> Կարդացեք տեքստը (օրինակ՝ կատարել հաղորդագրություններ, նշումներ, պիտակներ և մասնաճյուղերի նկարագրություններ) `stdin`-ից և մաքրեք այն Git-ի կողմից օգտագործվող ձևով:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-stripspace>:.

- Կտրեք բացատը ֆայլից.:

`cat {{path/to/file}} | git stripspace`

- Կտրեք բացատը և Git մեկնաբանությունները ֆայլից.:

`cat {{path/to/file}} | git stripspace {{[-s|--strip-comments]}}`

- Ֆայլի բոլոր տողերը փոխարկեք Git մեկնաբանությունների.:

`git < {{path/to/file}} stripspace {{[-c|--comment-lines]}}`
