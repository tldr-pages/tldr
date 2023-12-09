# ykman fido

> Beheer YubiKey FIDO applicaties.
> Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- Toon algemene informatie over de FIDO2 applicatie:

`ykman fido info`

- Verander de FIDO pin:

`ykman fido access change-pin`

- Toon resident credentials opgeslagen op de YubiKey:

`ykman fido credentials list`

- Verwijder een resident credential van de YubiKey:

`ykman fido credentials delete {{id}}`

- Toon vingerafdrukken opgeslagen op de YubiKey (vereist een sleutel met een vingerafdruk sensor):

`ykman fido fingerprints list`

- Voeg een nieuwe vingerafdruk toe aan de YubiKey:

`ykman fido fingerprints add {{naam}}`

- Verwijder een vingerafdruk van de YubiKey:

`ykman fido fingerprints delete {{naam}}`

- Wis alle FIDO credentials (je moet dit doen nadat je het aantal pogingen voor de pin hebt overschreden):

`ykman fido reset`
