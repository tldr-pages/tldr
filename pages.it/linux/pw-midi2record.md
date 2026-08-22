# pw-midi2record

> Registra clip MIDI 2.0 tramite PipeWire.
> Nota: Questo comando è un alias per `pw-cat --record --midi-clip`.
> Vedi anche: `pw-cat`, `pw-midi2play`, `pw-midirecord`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Registra un file clip MIDI 2.0 dalla sorgente predefinita:

`pw-midi2record {{percorso/del/file.mid}}`

- Registra un clip MIDI, forzando il formato MIDI da usare (predefinito: `ump`):

`pw-midi2record {{[-M|--force-midi]}} {{midi|ump}} {{percorso/del/file.mid}}`

- Mostra aiuto:

`pw-midi2record {{[-h|--help]}}`
