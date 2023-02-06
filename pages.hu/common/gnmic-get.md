# gnmic get

> A gnmi hálózati eszköz működési adatainak pillanatfelvételének lekérdezése. További információ: <https://gnmic.kmrd.dev/cmd/get>.

- Pillanatfelvétel készítése az eszköz állapotáról egy adott útvonalon:

`gnmic --address {{ip:port}} get --path {{path}}`

- Az eszköz állapotának lekérdezése több útvonalon:

`gnmic -a {{ip:port}} get --path {{path1}} --path {{path2}}`

- Az eszköz állapotának lekérdezése több közös előtaggal rendelkező útvonalon:

`gnmic -a {{ip:port}} get --prefix {{prefix}} --path {{path1}} --path {{path2}}`

- Az eszköz állapotának lekérdezése és a válasz kódolásának megadása (json_ietf):

`gnmic -a {{ip:port}} get --path {{path}} --encoding json_ietf`
