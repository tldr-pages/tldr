# mosquitto_pub

> Egy egyszerű MQTT 3.1.1-es verziójú kliens, amely egyetlen üzenetet tesz közzé egy témában és kilép. További információ: <https://mosquitto.org/man/mosquitto_pub-1.html>.

- Közzétesz egy 32-es hőmérsékleti értéket a `sensors/temperature` témában a 192.168.1.1.1 (alapértelmezés szerint `localhost`) címen, a szolgáltatásminőség (`QoS`) 1-re van állítva:

`mosquitto_pub -h {{192.168.1.1}} -t {{sensors/temperature}} -m {{32}} -q {{1}}`

- Időbélyeg és hőmérsékleti adatok közzététele a `sensors/temperature` témában egy távoli állomáson, egy nem szabványos porton:

`mosquitto_pub -h {{192.168.1.1}} -p {{1885}} -t {{sensors/temperature}} -m "{{1266193804 32}}"`

- Közzéteszi a fénykapcsoló állapotát és megtartja az üzenetet a `switches/kitchen_lights/status` témakörben egy távoli állomásnak, mivel a fénykapcsoló eseményei között hosszú idő telhet el:

`mosquitto_pub -r -h "{{iot.eclipse.org}}" -t {{switches/kitchen_lights/status}} -m "{{on}}"`

- Egy fájl (`data.txt`) tartalmának üzenetben történő elküldése és közzététele a `sensors/temperature` témában:

`mosquitto_pub -t {{sensors/temperature}} -f {{data.txt}}`

- Egy fájl (`data.txt`) tartalmának elküldése a `stdin` címről történő beolvasással, majd a teljes bemenet elküldése üzenetként és közzététele a `sensors/temperature` témában:

`mosquitto_pub -t {{sensors/temperature}} -s < {{data.txt}}`

- Újsorral elválasztott adatok beolvasása a `stdin` címről üzenetként, és közzéteszi a `sensors/temperature` témában:

`{{echo data.txt}} | mosquitto_pub -t {{sensors/temperature}} -l`
