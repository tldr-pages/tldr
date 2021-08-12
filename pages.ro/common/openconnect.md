# openconnect

> Un client VPN, pentru Cisco AnyConnect VPN și altele.
> Mai multe informaţii: <https://www.infradead.org/openconnect/manual.html>

- Conectează-te la un server:

`openconnect {{vpn.example.org}}`

- Conectați-vă la un server, furking în fundal:

`openconnect --background {{vpn.example.org}}`

- Terminați conexiunea care se execută în fundal:

`killall -SIGINT openconnect`

- Conectați-vă la un server, citirea opțiunilor dintr-un fișier de configurare:

`openconnect --config={{path/to/file}} {{vpn.example.org}}`

- Conectați-vă la un server și autentificați cu un anumit certificat de client SSL:

`openconnect --certificate={{path/to/file}} {{vpn.example.org}}`
