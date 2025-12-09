# batch

> Voer commando's uit op een later tijdstip wanneer de systeembelasting het toelaat.
> Resultaten worden verzonden naar de e-mail van de gebruiker.
> Zie ook: `at`, `atq`, `atrm` `mail`.
> Meer informatie: <https://manned.org/batch>.

- Voer commando's uit vanaf `stdin` (druk op `<Ctrl d>` om te stoppen):

`batch`

- Voer een commando uit vanaf `stdin`:

`echo "{{./make_db_backup.sh}}" | batch`
