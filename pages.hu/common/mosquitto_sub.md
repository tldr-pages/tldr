# mosquitto_sub

> Egy egyszerű MQTT 3.1.1-es verziójú kliens, amely feliratkozik a témákra és kinyomtatja a kapott üzeneteket. További információ: <https://mosquitto.org/man/mosquitto_sub-1.html>.

- Feliratkozás a `sensors/temperature` témakörre, a szolgáltatás minősége (`QoS`) 1-re van állítva. (Az alapértelmezett hosztnév: `localhost` és az 1883-as port):

`mosquitto_sub -t {{sensors/temperature}} -q {{1}}`

- Feliratkozás a `iot.eclipse.org` 1885 porton közzétett összes bróker státuszüzenetre, és a közzétett üzenetek szó szerinti nyomtatása:

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t {{\$SYS/#}}`

- Feliratkozás egy adott mintának megfelelő több témára. (+ bármilyen metrikus nevet elfogad):

`mosquitto_sub -t {{sensors/machines/+/temperature/+}}`
