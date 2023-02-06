# locust

> Terheléstesztelő eszköz, amellyel meghatározható, hogy egy rendszer hány egyidejű felhasználót tud kezelni. További információ [: https://locust.io](https://locust.io).

- "example.com" terheléses tesztelése webes felülettel a locustfile.py segítségével:

`locust --host={{http://example.com}}`

- Használjon másik tesztfájlt:

`locust --locustfile={{test_file.py}} --host={{http://example.com}}`

- Futtassa a tesztet webes felület nélkül, másodpercenként 1 felhasználó létrehozásával, amíg 100 felhasználó nem lesz:

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- Indítsuk el a locustot master módban:

`locust --master --host={{http://example.com}}`

- Csatlakoztassuk a locust slave-et a masterhez:

`locust --slave --host={{http://example.com}}`

- Csatlakoztassa a locust slave-et a masterhez egy másik gépen:

`locust --slave --master-host={{master_hostname}} --host={{http://example.com}}`
