# instaloader

> Download foto's, video's, bijschriften en andere metadata van Instagram.
> Opmerking: je moet Instagram-inloggegevens opgeven als je media in hoge kwaliteit wilt downloaden.
> Meer informatie: <https://instaloader.github.io/cli-options.html>.

- Download een profiel:

`instaloader {{profiel_naam}}`

- Download highlights:

`instaloader --highlights {{profiel_naam}}`

- Download berichten met geotags (indien beschikbaar), zonder gebruikersinteractie:

`instaloader {{[-q|--quiet]}} {{[-G|--geotags]}} {{profiel_naam}}`

- Specificeer een user agent voor HTTP-verzoeken:

`instaloader --user-agent {{user_agent}} {{profiel_naam}}`

- Specificeer inloggegevens en download berichten (handig voor privéprofielen):

`instaloader {{[-l|--login]}} {{gebruikersnaam}} {{[-p|--password]}} {{wachtwoord}} {{profiel_naam}}`

- Sla een doel over als het eerst gedownloade bestand al gevonden is (handig om Instagram-archieven bij te werken):

`instaloader {{[-F|--fast-update]}} {{profiel_naam}}`

- Download verhalen en IGTV-video's (inloggen vereist):

`instaloader {{[-l|--login]}} {{gebruikersnaam}} {{[-p|--password]}} {{wachtwoord}} {{[-s|--stories]}} --igtv {{profiel_naam}}`

- Download alle soorten berichten (inloggen vereist):

`instaloader {{[-l|--login]}} {{gebruikersnaam}} {{[-p|--password]}} {{wachtwoord}} {{[-s|--stories]}} --igtv --highlights {{profiel_naam}}`
