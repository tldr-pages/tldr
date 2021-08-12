# tshark

> Instrument de analiză a pachetelor, versiunea CLI a Wireshark.
> Mai multe informaţii: <https://tshark.dev/>

- Monitorizează totul pe localhost:

`tshark`

- Doar captura pachetele care se potrivesc cu un anumit filtru de captare:

`tshark -f '{{udp port 53}}'`

- Arată doar pachetele care se potrivesc cu un anumit filtru de ieșire:

`tshark -Y '{{http.request.method == "GET"}}'`

- decodează un port TCP utilizând un protocol specific (de exemplu HTTP):

`tshark -d tcp.port=={{8888}},{{http}}`

- Specificați formatul de ieșire capturat:

`tshark -T {{json|text|ps|…}}`

- Selectați câmpurile specifice de ieșire:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- Scrieți pachetul capturat într-un fișier:

`tshark -w {{path/to/file}}`

- Analizați pachetele dintr-un fișier:

`tshark -r {{filename}}.pcap`
