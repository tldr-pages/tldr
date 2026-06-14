# pdftk

> PDF գործիքակազմ:.
> Լրացուցիչ տեղեկություններ. <https://www.pdflabs.com/docs/pdftk-man-page/>:.

- Քաղեք 1-3, 5 և 6-10 էջերը PDF ֆայլից և պահեք դրանք որպես մեկ այլ:

`pdftk {{path/to/input}}.pdf cat 1-3 5 6-10 output {{path/to/output}}.pdf`

- Միավորել (միավորել) PDF ֆայլերի ցանկը և արդյունքը պահպանել որպես մեկ այլ.:

`pdftk {{path/to/file1}}.pdf {{path/to/file2}}.pdf cat output {{path/to/output}}.pdf`

- Բաժանեք PDF ֆայլի յուրաքանչյուր էջ առանձին ֆայլի մեջ՝ տվյալ ֆայլի անվան ելքային օրինակով.:

`pdftk {{path/to/input}}.pdf burst output {{path/to/out_%d}}.pdf`

- Պտտեցնել բոլոր էջերը 180 աստիճանով ժամացույցի սլաքի ուղղությամբ.:

`pdftk {{path/to/input}}.pdf cat 1-endsouth output {{path/to/output}}.pdf`

- Պտտեք երրորդ էջը 90 աստիճանով ժամացույցի սլաքի ուղղությամբ և թողեք մյուսները անփոփոխ.:

`pdftk {{path/to/input}}.pdf cat 1-2 3east 4-end output {{path/to/output}}.pdf`

- Տեղադրեք երկու PDF ֆայլ երկկողմանի փաստաթղթի միակողմանի սկանավորմամբ, որտեղ հետևի կողմերը սկանավորվեցին հետից առջև.:

`pdftk A={{path/to/fronts}}.pdf B={{path/to/backs}}.pdf shuffle A1-end Bend-1 output {{path/to/output}}.pdf`
