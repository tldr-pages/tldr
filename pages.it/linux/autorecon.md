# autorecon

> Uno strumento multi-threaded di ricognizione di rete che esegue l'enumerazione automatica dei servizi.
> Maggiori informazioni: <https://github.com/Tib3rius/AutoRecon>.

- Esegui la ricognizione su uno o più host di destinazione (i risultati dettagliati della scansione verranno salvati in `./results`):

`sudo autorecon {{host_o_ip1,host_o_ip2,...}}`

- Esegui la ricognizione su target specificati in un file:

`sudo autorecon {{[-t|--target-file]}} {{percorso/del/file}}`

- Salva i risultati in una directory diversa:

`sudo autorecon {{[-o|--output]}} {{percorso/dei/risultati}} {{host_o_ip1,host_o_ip2,...}}`

- Limita la scansione a porte e protocolli specifici (`T` per TCP, `U` per UDP, `B` per entrambi):

`sudo autorecon {{[-p|--ports]}} {{T:21-25,80,443,U:53,B:123}} {{host_o_ip1,host_o_ip2,...}}`
