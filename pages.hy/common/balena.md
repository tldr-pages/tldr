#բալենա

> Փոխազդեք balenaCloud-ի, openBalena-ի և balena API-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.balena.io/reference/balena-cli/latest/>:.

- Մուտք գործեք balenaCloud հաշիվ.:

`balena login`

- Ստեղծեք balenaCloud կամ openBalena հավելված.:

`balena app create {{app_name}}`

- Թվարկեք բոլոր balenaCloud կամ openBalena հավելվածները հաշվի մեջ.:

`balena apps`

- Թվարկեք balenaCloud կամ openBalena հաշվի հետ կապված բոլոր սարքերը.:

`balena devices`

- Ֆլեշեք balenaOS պատկերը տեղական սկավառակի վրա.:

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
