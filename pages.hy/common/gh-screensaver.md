# gh էկրանապահ

> Ընդլայնում GitHub CLI-ի համար, որն աշխատում է անիմացիոն տերմինալի էկրանապահիչներով:.
> Տես նաև՝ `gh extension`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/vilmibm/gh-screensaver>:.

- Գործարկեք պատահական էկրանապահիչ.:

`gh screensaver`

- Գործարկեք հատուկ էկրանապահիչ.:

`gh screensaver {{[-s|--saver]}} {{fireworks|life|marquee|pipes|pollock|starfield}}`

- Գործարկեք «marquee» էկրանապահիչը հատուկ տեքստով և տառատեսակով.:

`gh screensaver {{[-s|--saver]}} marquee -- --message="{{message}}" --font={{font_name}}`

- Գործարկեք «starfield» էկրանապահիչը որոշակի խտությամբ և արագությամբ.:

`gh screensaver {{[-s|--saver]}} starfield -- --density {{500}} --speed {{10}}`

- Ցուցակեք հասանելի էկրանապահները.:

`gh screensaver {{[-l|--list]}}`
