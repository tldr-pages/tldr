# route

> Manipuleer handmatig de routetabellen.
> Vereist rootrechten.
> Meer informatie: <https://keith.github.io/xcode-man-pages/route.8.html>.

- Voeg een route toe naar een bestemming via een gateway:

`sudo route add "{{bestemming_ip_adres}}" "{{gateway_adres}}"`

- Voeg een route toe naar een /24 subnet via een gateway:

`sudo route add "{{subnet_ip_adres}}/24" "{{gateway_adres}}"`

- Voer uit in testmodus (doet niets, alleen afdrukken):

`sudo route -t add "{{bestemming_ip_adres}}/24" "{{gateway_adres}}"`

- Verwijder alle routes:

`sudo route flush`

- Verwijder een specifieke route:

`sudo route delete "{{bestemming_ip_adres}}/24"`

- Zoek en toon de route voor een bestemming (hostname of IP-adres):

`sudo route get "{{bestemming}}"`
