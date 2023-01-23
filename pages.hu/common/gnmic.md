# gnmic

> A gNMI parancssori kliens. A gNMI hálózati eszköz konfigurációjának kezelése és működési adatok megtekintése. További információ: <https://gnmic.kmrd.dev>.

- Az eszköz képességeinek lekérdezése:

`gnmic --address {{ip:port}} capabilities`

- Adjon meg egy felhasználónevet és jelszót az eszköz képességeinek lekérdezéséhez:

`gnmic --address {{ip:port}} --username {{username}} --password {{password}} capabilities`

- Pillanatkép lekérése az eszköz állapotáról egy adott útvonalon:

`gnmic -a {{ip:port}} get --path {{path}}`

- Az eszköz állapotának frissítése egy adott útvonalon:

`gnmic -a {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Feliratkozás a célállapot-frissítésekre egy adott elérési útvonalon lévő alfa alatt:

`gnmic -a {{ip:port}} subscribe --path {{path}}`
