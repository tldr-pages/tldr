# chpasswd

> Verander de wachtwoorden van meerdere gebruikers via `stdin`.
> Zie ook: `passwd`.
> Meer informatie: <https://manned.org/chpasswd>.

- Verander het wachtwoord van een specifieke gebruiker:

`printf "{{gebruikersnaam}}:{{nieuw_wachtwoord}}" | sudo chpasswd`

- Verander de wachtwoorden van meerdere gebruikers (de invoertekst mag geen spaties bevatten):

`printf "{{gebruikersnaam_1}}:{{nieuw_wachtwoord_1}}\n{{gebruikersnaam_2}}:{{nieuw_wachtwoord_2}}" | sudo chpasswd`

- Verander het wachtwoord van een specifieke gebruiker en geef het op in versleutelde vorm:

`printf "{{gebruikersnaam}}:{{nieuw_versleuteld_wachtwoord}}" | sudo chpasswd {{[-e|--encrypted]}}`

- Verander het wachtwoord van een specifieke gebruiker en gebruik een specifieke versleuteling voor het opgeslagen wachtwoord:

`printf "{{gebruikersnaam}}:{{nieuw_wachtwoord}}" | sudo chpasswd {{[-c|--crypt-method]}} {{NONE|DES|MD5|SHA256|SHA512}}`
