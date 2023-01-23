# netselect

> Sebességteszt a gyors hálózati szerver kiválasztásához. További információ: <https://github.com/apenwarr/netselect>.

- Válassza a legkisebb késleltetésű kiszolgálót:

`sudo netselect {{host_1}} {{host_2}}`

- Névszerverek felbontásának és statisztikáinak megjelenítése:

`sudo netselect -vv {{host_1}} {{host_2}}`

- Maximális TTL (time to live) meghatározása:

`sudo netselect -m {{10}} {{host_1}} {{host_2}}`

- A leggyorsabb N szerver kiírása a hosztok közül:

`sudo netselect -s {{N}} {{host_1}} {{host_2}} {{host_3}}`

- Az elérhető opciók listája:

`netselect`
