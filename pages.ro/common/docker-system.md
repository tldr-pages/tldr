# docker system

> Gestionați datele Docker și afișați informații la nivel de sistem.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/system/>

- Arată ajutor:

`docker system`

- Arată utilizarea discului docker:

`docker system df`

- Afișați informații detaliate despre utilizarea discului:

`docker system df --verbose`

- Eliminați datele neutilizate:

`docker system prune`

- Eliminați datele neutilizate create create mai mult de o anumită perioadă de timp în trecut:

`docker system prune --filter="until={{hours}}h{{minutes}}m"`

- Afișează evenimente în timp real din demonul Docker:

`docker system events`

- Afișează evenimente în timp real din containere transmise ca JSON Lines valide:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Afișează informații la nivel de sistem:

`docker system info`
