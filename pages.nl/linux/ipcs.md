# ipcs

> Toon informatie over het gebruik van System V IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays.
> Bekijk ook: `lsipc` voor een flexibeler tool, `ipcmk` voor het maken van IPC-faciliteiten, en `ipcrm` voor het verwijderen ervan.
> Meer informatie: <https://manned.org/ipcs>.

- Toon informatie over alle actieve IPC-faciliteiten:

`ipcs`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`ipcs {{--shmems|--queues|--semaphores}}`

- Toon volledige details over de resource met een specifieke [i]D:

`ipcs {{--shmems|--queues|--semaphores}} --id {{resource_id}}`

- Toon [l]imieten in [b]ytes of in een leesbaar formaat:

`ipcs --limits {{--bytes|--human}}`

- Toon s[u]mmary over huidig gebruik:

`ipcs --summary`

- Toon [c]reator's en owner's UIDs en PIDs voor alle IPC-faciliteiten:

`ipcs --creator`

- Toon de [p]ID van de laatste operatoren voor alle IPC-faciliteiten:

`ipcs --pid`

- Toon laatste toegang[s]tijden voor alle IPC-faciliteiten:

`ipcs --time`
