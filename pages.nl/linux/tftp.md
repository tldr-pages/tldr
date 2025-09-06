# tftp

> Trivial File Transfer Protocol client.
> Meer informatie: <https://manned.org/tftp.1>.

- Maak verbinding met een TFTP-server door het IP-adres en de poort op te geven:

`tftp {{server_ip}} {{poort}}`

- Maak verbinding met een TFTP-server en voer een TFTP-[c]ommand uit:

`tftp {{server_ip}} -c {{commando}}`

- Maak verbinding met een TFTP-server met IPv6 en forceer dat de oorspronkelijke poort binnen een [R]ange ligt:

`tftp {{server_ip}} -6 -R {{poort}}:{{poort}}`

- Stel de overdrachtsmodus in op binaire of ASCIi via de tftp-client:

`mode {{binary|ascii}}`

- Download een bestand van een server via de tftp-client:

`get {{file}}`

- Upload een bestand naar een server via de tftp-client:

`put {{file}}`

- Verlaat de tftp-client:

`quit`
