# tftp

> Trivial File Transfer Protocol-client.
> Meer informatie: <https://manned.org/tftp>.

- Maak verbinding met een TFTP-server door het IP-adres en de poort op te geven:

`tftp {{server_ip}} {{poort}}`

- Maak verbinding met een TFTP-server en voer een TFTP-[c]ommando uit:

`tftp {{server_ip}} -c {{commando}}`

- Maak verbinding met een TFTP-server met IPv6 en forceer dat de oorspronkelijke poort binnen een [R]ange ligt:

`tftp {{server_ip}} -6 -R {{poort}}:{{poort}}`

- [Interactief] Stel de overdrachtsmodus in op binaire of ASCII via de tftp-client:

`mode {{binary|ascii}}`

- [Interactief] Download een bestand van een server via de tftp-client:

`get {{bestand}}`

- [Interactief] Upload een bestand naar een server via de tftp-client:

`put {{bestand}}`

- [Interactief] Verlaat de tftp-client:

`quit`
