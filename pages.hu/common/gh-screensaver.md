# gh screensaver

> A GitHub CLI kiterjesztése, amely animált terminál képernyővédőket futtat. Lásd még: `gh extension`. További információ: <https://github.com/vilmibm/gh-screensaver>.

- Véletlenszerű képernyőkímélő futtatása:

`gh screensaver`

- Egy adott képernyőkímélő futtatása:

`gh screensaver --saver {{fireworks|marquee|pipes|pollock|starfield}}`

- A "sávos" képernyőkímélő futtatása egy adott szöveggel és betűtípussal:

`gh screensaver --saver {{marquee}} -- --message="{{message}}" --font={{font_name}}`

- A "csillagmező" képernyőkímélő futtatása egy adott sűrűséggel és sebességgel:

`gh screensaver --saver {{starfield}} -- --density {{500}} --speed {{10}}`

- A rendelkezésre álló képernyőkímélők listája:

`gh screensaver --list`
