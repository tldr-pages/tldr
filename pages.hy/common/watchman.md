#պահապան

> Ծառայություն, որը դիտում է ֆայլերը և գործարկում է գործողություններ, երբ փոփոխություններ են տեղի ունենում:.
> Լրացուցիչ տեղեկություններ. <https://facebook.github.io/watchman/docs/cli-options>:.

- Եզրակացե՛ք նշված գրացուցակը պարունակող նախագծի արմատական գրացուցակը և դիտե՛ք դրա ֆայլերն ու ենթաթղթապանակները փոփոխությունների համար.:

`watchman watch-project {{path/to/directory}}`

- Ավելացրեք գործարկիչ հրաման գործարկելու համար, երբ դիտված գրացուցակում նշված ֆայլի անվան օրինակով ֆայլերը փոխվում են.:

`watchman -- trigger {{path/to/watched_directory}} {{trigger_name}} '{{pattern}}' -- {{command}}`

- Թվարկեք բոլոր դիտված գրացուցակները.:

`watchman watch-list`

- Ջնջել ժամացույցը գրացուցակում և դրա հետ կապված գործարկիչները.:

`watchman watch-del {{path/to/watched_directory}}`

- Ջնջել բոլոր դիտված գրացուցակները և գործարկիչները.:

`watchman watch-del-all`

- Թվարկեք բոլոր գործարկիչները դիտված գրացուցակի վրա.:

`watchman trigger-list {{path/to/watched_directory}}`

- Ջնջել գործարկիչը դիտված գրացուցակից.:

`watchman trigger-del {{path/to/watched_directory}} {{trigger_name}}`

- Ժամանակավորապես դադարեցրեք `watchman`-ը, մինչև հաջորդ անգամ կանչեք `watchman` հրամանը՝:

`watchman shutdown-server`
