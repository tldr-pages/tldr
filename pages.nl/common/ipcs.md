# ipcs

> Toon informatie over het gebruik van XSI IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays.
> Meer informatie: <https://manned.org/ipcs.1p>.

- Toon informatie over alle IPC:

`ipcs -a`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`ipcs {{-m|-q|-s}}`

- Toon informatie over de maximaal toegestane grootte in [b]ytes:

`ipcs -b`

- Toon de gebruikersnaam en groepsnaam van de [c]reator voor alle IPC-faciliteiten:

`ipcs -c`

- Toon de [p]ID van de laatste operatoren voor alle IPC-faciliteiten:

`ipcs -p`

- Toon toegang[s]tijden voor alle IPC-faciliteiten:

`ipcs -t`

- Toon [o]utstanding gebruik voor actieve berichtenwachtrijen en gedeelde geheugensegmenten:

`ipcs -o`
