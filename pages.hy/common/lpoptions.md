# lpoptions

> Ցուցադրել կամ սահմանել տպիչի ընտրանքները և կանխադրվածները:.
> Տես նաև՝ `lpadmin`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-lpoptions.html>:.

- Սահմանեք լռելյայն տպիչը.:

`lpoptions -d {{printer}}/{{instance}}`

- Թվարկեք տպիչի հատուկ ընտրանքները որոշակի տպիչի համար.:

`lpoptions -d {{printer}} -l`

- Սահմանեք նոր տարբերակ կոնկրետ տպիչի վրա.:

`lpoptions -d {{printer}} -o {{option}}`

- Հեռացրեք որոշակի տպիչի ընտրանքները.:

`lpoptions -d {{printer}} -x`
