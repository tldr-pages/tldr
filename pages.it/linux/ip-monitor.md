# ip monitor

> Monitora la rete per cambiamenti di stato.
> Maggiori informazioni: <https://manned.org/ip-monitor>.

- Monitora l'intera rete per cambiamenti di stato:

`ip {{[mo|monitor]}}`

- Specifica il tipo da monitorare:

`ip {{[mo|monitor]}} {{link|address|route|neigh|rule|maddress|...}}`

- Riproduce un file di eventi (può essere generato con `rtmon`):

`ip {{[mo|monitor]}} {{[f|file]}} {{path/to/file}}`
