# pw-midi2play

> Riproduce clip MIDI 2.0 tramite PipeWire.
> Nota: Questo comando è un alias per `pw-cat --playback --midi-clip`.
> Vedi anche: `pw-cat`, `pw-midi2record`, `pw-midiplay`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Riproduce un file clip MIDI 2.0 sulla destinazione predefinita:

`pw-midi2play {{percorso/del/file.mid}}`

- Riproduce un clip MIDI, forzando il formato MIDI da usare (predefinito: `ump`):

`pw-midi2play {{[-M|--force-midi]}} {{midi|ump}} {{percorso/del/file.mid}}`

- Mostra aiuto:

`pw-midi2play {{[-h|--help]}}`
