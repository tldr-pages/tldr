# gnmic set

> A gnmi hálózati eszköz konfigurációjának módosítása. További információ: <https://gnmic.kmrd.dev/cmd/set>.

- Egy útvonal értékének frissítése:

`gnmic --address {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Egy elérési útvonal értékének frissítése egy json fájl tartalmának megfelelően:

`gnmic -a {{ip:port}} set --update-path {{path}} --update-file {{filepath}}`

- Egy elérési útvonal értékének cseréje egy json fájl tartalmának megfelelően:

`gnmic -a {{ip:port}} set --replace-path {{path}} --replace-file {{filepath}}`

- A csomópont törlése egy adott elérési útvonalon:

`gnmic -a {{ip:port}} set --delete {{path}}`
