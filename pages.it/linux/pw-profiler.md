# pw-profiler

> Profila un'istanza locale o remota.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- Profila l'istanza predefinita, registrando in `profile.log` (vengono generati anche file `gnuplot` e un file HTML per la visualizzazione dei risultati):

`pw-profiler`

- Cambia il file di output del log:

`pw-profiler {{[-o|--output]}} {{percorso/del/file.log}}`

- Profila un'istanza remota:

`pw-profiler {{[-r|--remote]}} {{nome_remoto}}`

- Mostra aiuto:

`pw-profiler {{[-h|--help]}}`
