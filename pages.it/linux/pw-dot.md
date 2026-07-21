# pw-dot

> Crea file `.dot` del grafico di PipeWire.
> Vedi anche: `dot`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- Genera un grafico nel file `pw.dot`:

`pw-dot`

- Legge oggetti da un file JSON `pw-dump`:

`pw-dot {{[-j|--json]}} {{percorso/del/file.json}}`

- Specifica un file di output, mostrando tutti i tipi di oggetti:

`pw-dot {{[-o|--output]}} {{percorso/del/file.dot}} {{[-a|--all]}}`

- Stampa il grafico `.dot` su `stdout`, mostrando tutte le proprietà degli oggetti:

`pw-dot {{[-o|--output]}} - {{[-d|--detail]}}`

- Genera un grafico da un'istanza remota, mostrando solo gli oggetti collegati:

`pw-dot {{[-r|--remote]}} {{nome_remoto}} {{[-s|--smart]}}`

- Dispone il grafico da sinistra a destra, invece del predefinito dall'alto verso il basso:

`pw-dot {{[-L|--lr]}}`

- Dispone il grafico usando angoli di 90 gradi nei bordi:

`pw-dot {{[-9|--90]}}`

- Mostra aiuto:

`pw-dot {{[-h|--help]}}`
