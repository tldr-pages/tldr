# mosquitto_sub

> Un client simplu MQTT versiunea 3.1.1, care se va abona la subiecte și va imprima mesajele pe care le primește.
> Mai multe informaţii: <https://mosquitto.org/man/mosquitto_sub-1.html>

- Abonați-vă la subiectul `senzorii/temperatură' informații cu calitatea serviciului (`Qos`) setat la 1. (Numele de gazdă implicit este `localhost` și portul 1883):

`mosquitto_sub -t {{sensors/temperature}} -q {{1}}`

- Abonați-vă la toate mesajele de stare broker publicarea pe portul `iot.eclipse.org` 1885 și imprimați mesaje publicate verbosely:

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t {{\$SYS/#}}`

- Abonați-vă la mai multe subiecte care se potrivesc unui anumit model. (+ ia orice nume metric):

`mosquitto_sub -t {{sensors/machines/+/temperature/+}}`
