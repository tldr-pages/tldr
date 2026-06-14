# փոխանցում-հեռակառավարում

> Հեռակառավարման ծրագիր `transmission-daemon`-ի և `transmission`-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/transmission-remote>:.

- Փոխանցման մեջ ավելացրեք հեղեղի ֆայլ կամ մագնիսի հղում և ներբեռնեք նշված գրացուցակ.:

`transmission-remote {{hostname}} {{[-a|--all]}} {{torrent|url}} {{[-w|--download-dir]}} /{{path/to/download_directory}}`

- Փոխեք լռելյայն ներբեռնման գրացուցակը.:

`transmission-remote {{hostname}} {{[-w|--download-dir]}} /{{path/to/download_directory}}`

- Թվարկեք բոլոր հեղեղները.:

`transmission-remote {{hostname}} {{[-l|--list]}}`

- Սկսեք torrent 1-ը և 2-ը, դադարեցրեք torrent 3-ը:

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1,2" {{[-s|--start]}} {{[-t|--torrent]}} 3 {{[-S|--stop]}}`

- Հեռացրեք torrent 1-ը և 2-ը, ինչպես նաև ջնջեք տեղական տվյալները torrent 2-ի համար.:

`transmission-remote {{hostname}} {{[-t|--torrent]}} 1 {{[-r|--remove]}} {{[-t|--torrent]}} 2 {{[-rad|--remove-and-delete]}}`

- Դադարեցրեք բոլոր հեղեղները.:

`transmission-remote {{hostname}} {{[-t|--torrent]}} {{all}} {{[-S|--stop]}}`

- Տեղափոխեք հեղեղները 1-10 և 15-20 նոր գրացուցակ (որը կստեղծվի, եթե այն գոյություն չունի).:

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1-10,15-20" --move /{{path/to/new_directory}}`
