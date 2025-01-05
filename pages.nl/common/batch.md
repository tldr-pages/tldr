# batch

> Voer commando's uit op een later tijdstip wanneer de systeembelasting het toelaat.
> Resultaten worden verzonden naar de e-mail van de gebruiker.
> Bekijk ook: `at`, `atq`, `atrm` `mail`.
> Meer informatie: <https://manned.org/batch>.

- Start de `atd` daemon:

`systemctl start atd`

- Voer commando's uit vanaf `stdin` (druk op `Ctrl + D` om te stoppen):

`batch`

- Voer een commando uit vanaf `stdin`:

`echo "{{./make_db_backup.sh}}" | batch`
