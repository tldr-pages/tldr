# բաժակ կտլ

> Թարմացրեք կամ հարցում կատարեք սերվերի `cupsd.conf`-ին:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-cupsctl.html>:.

- Ցուցադրել ընթացիկ կազմաձևման արժեքները.:

`cupsctl`

- Ցուցադրել որոշակի սերվերի կազմաձևման արժեքները.:

`cupsctl -h {{server[:port]}}`

- Միացնել գաղտնագրումը ժամանակացույցի հետ կապի վրա.:

`cupsctl -E`

- Միացնել կամ անջատել վրիպազերծման գրանցումը `error_log` ֆայլում՝:

`cupsctl {{--debug-logging|--no-debug-logging}}`

- Միացնել կամ անջատել հեռավոր կառավարումը.:

`cupsctl {{--remote-admin|--no-remote-admin}}`

- Վերլուծեք ընթացիկ վրիպազերծման գրանցման վիճակը.:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
