# ykman openpgp

> Beheer de OpenPGP YubiKey applicatie.
> Opmerking: je dient `gpg --card-edit` te gebruiken voor sommige instellingen.
> Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- Toon algemene informatie over de OpenPGP applicatie:

`ykman openpgp info`

- Stel het aantal herstelpogingen in voor de gebruikers pin, herstelcode en admin pin:

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- Verander de gebruikers pin, herstelcode of admin pin:

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- Herstel de OpenPGP applicatie naar fabrieksinstellingen (je moet dit doen nadat je het aantal pogingen voor de Admin pin hebt overschreden):

`ykman openpgp reset`
