# tcptraceroute

> TCP csomagokat használó traceroute implementáció. További információ: <https://github.com/mct/tcptraceroute>.

- Nyomon követi az útvonalat egy állomáshoz:

`tcptraceroute {{host}}`

- Adja meg a célportot és a csomag hosszát bájtban:

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- Adja meg a helyi forrásportot és a forráscímet:

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- Az első és a maximális TTL beállítása:

`tcptraceroute {{host}} -f {{first_ttl}} -m {{max_ttl}}`

- Adja meg a várakozási időt és a lekérdezések számát ugrásonként:

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- Az interfész megadása:

`tcptraceroute {{host}} -i {{interface}}`
