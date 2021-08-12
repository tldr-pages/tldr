# mosquitto_pub

> Un simplu MQTT versiunea 3.1.1 client care va publica un singur mesaj pe un subiect și de ieșire.
> Mai multe informaţii: <https://mosquitto.org/man/mosquitto_pub-1.html>

- Publicarea unei temperaturi de 32 pe tema `senzorii/temperatura` la 192.168.1.1 (valori implicite la `localhost`) cu calitatea serviciului (`Qos`) setata la 1:

`mosquitto_pub -h {{192.168.1.1}} -t {{sensors/temperature}} -m {{32}} -q {{1}}`

- Publicați datele privind marcajele temporale și temperatura pe tema `senzorii/temperatură' către o gazdă la distanță pe un port non-standard:

`mosquitto_pub -h {{192.168.1.1}} -p {{1885}} -t {{sensors/temperature}} -m "{{1266193804 32}}"`

- Publicați starea comutatorului de lumină și păstrați mesajul pe tema `switches/kitchen_lights/status` la o gazdă de la distanță, deoarece poate exista o perioadă lungă de timp între evenimentele întrerupătorului de lumină:

`mosquitto_pub -r -h "{{iot.eclipse.org}}" -t {{switches/kitchen_lights/status}} -m "{{on}}"`

- Trimiteți conținutul unui fișier (`data.txt`) ca mesaj și publicați-l la subiectul `senzorii/temperatură`:

`mosquitto_pub -t {{sensors/temperature}} -f {{data.txt}}`

- Trimiteți conținutul unui fișier (`data.txt`), citind din stdin și trimite întreaga intrare ca mesaj și publicați-l la subiectul `senzorii/temperatură`:

`mosquitto_pub -t {{sensors/temperature}} -s < {{data.txt}}`

- Citiți datele delimitate de linie nouă din stdin ca mesaj și publicați-le în `senzorii/temperatură` subiect:

`{{echo data.txt}} | mosquitto_pub -t {{sensors/temperature}} -l`
