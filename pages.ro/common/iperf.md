# iperf

> Măsurați lățimea de bandă a rețelei între computere.
> Mai multe informaţii: <https://iperf.fr>

- Rulați pe server:

`iperf -s`

- Rulați pe server folosind modul UDP și setați portul serverului pentru a asculta pe 5001:

`iperf -u -s -p {{5001}}`

- Rulați pe client:

`iperf -c {{server_address}}`

- Rulați pe client la fiecare 2 secunde:

`iperf -c {{server_address}} -i {{2}}`

- Rulați pe client cu 5 fire paralele:

`iperf -c {{server_address}} -P {{5}}`

- Rulați pe client folosind modul UDP:

`iperf -u -c {{server_address}} -p {{5001}}`
