# route

> Az útválasztási táblázatok kézi manipulálása. Szükséges, hogy root legyen. További információ: <https://www.manpagez.com/man/8/route/>.

- Útvonal hozzáadása egy célállomáshoz egy átjárón keresztül:

`sudo route add "{{destination_ip_address}}" "{{gateway_address}}"`

- Útvonal hozzáadása egy átjárón keresztül egy /24 alhálózathoz:

`sudo route add "{{subnet_ip_address}}/24" "{{gateway_address}}"`

- Futtatás teszt üzemmódban (nem csinál semmit, csak nyomtat):

`sudo route -t add "{{destination_ip_address}}/24" "{{gateway_address}}"`

- Minden útvonal eltávolítása:

`sudo route flush`

- Egy adott útvonal törlése:

`sudo route delete "{{destination_ip_address}}/24"`

- Egy célállomás (hostnév vagy IP-cím) útvonalának keresése és megjelenítése:

`sudo route get "{{destination}}"`
