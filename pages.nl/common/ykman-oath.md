# ykman oath

> Beheer de OATH YubiKey applicatie.
> Een `keyword` kan onderdeel zijn van de naam of van de indiener.
> Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- Toon algemene informatie over de OATH applicatie:

`ykman oath info`

- Verander het wachtwoord dat de OATH accounts beschermd (voeg `--clear` toe om het te verwijderen):

`ykman oath access change`

- Voeg een nieuw account toe (`--issuer` is optioneel):

`ykman oath accounts add --issuer {{indiener}} {{naam}}`

- Toon alle accounts (met hun indiener):

`ykman oath accounts list`

- Toon alle accounts met hun huidige TOTP/HOTP codes (optioneel kan deze lijst gefilterd worden met een keyword):

`ykman oath accounts code {{keyword}}`

- Hernoem een account:

`ykman oath accounts rename {{keyword}} {{indiener:naam|naam}}`

- Verwijder een account:

`ykman oath accounts delete {{keyword}}`

- Verwijder alle accounts en herstel de fabrieksinstellingen:

`ykman oath reset`
