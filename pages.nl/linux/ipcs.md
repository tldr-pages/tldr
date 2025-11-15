# ipcs

> Toon informatie over het gebruik van System V IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays.
> Zie ook: `lsipc` voor een flexibeler tool, `ipcmk` voor het maken van IPC-faciliteiten, en `ipcrm` voor het verwijderen ervan.
> Meer informatie: <https://manned.org/ipcs>.

- Toon informatie over alle actieve IPC-faciliteiten:

`ipcs`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`ipcs {{--shmems|--queues|--semaphores}}`

- Toon volledige details over de resource met een specifieke ID:

`ipcs {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- Toon limieten in [b]ytes of in een leesbaar formaat:

`ipcs {{[-l|--limits]}} {{--bytes|--human}}`

- Toon samenvatting over huidig gebruik:

`ipcs {{[-u|--summary]}}`

- Toon creator's en owner's UIDs en PIDs voor alle IPC-faciliteiten:

`ipcs {{[-c|--creator]}}`

- Toon de PID van de laatste operatoren voor alle IPC-faciliteiten:

`ipcs {{[-p|--pid]}}`

- Toon laatste toegangstijden voor alle IPC-faciliteiten:

`ipcs {{[-t|--time]}}`
