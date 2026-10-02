# pw-config

> Elenca i percorsi di configurazione e le sezioni che verranno usate dal server PipeWire e dai client.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- Elenca tutti i file di configurazione che verranno usati:

`pw-config`

- Elenca tutti i file di configurazione che verranno usati dal server PipeWire PulseAudio:

`pw-config {{[-n|--name]}} pipewire-pulse.conf`

- Elenca tutte le sezioni di configurazione usate dal server PipeWire PulseAudio:

`pw-config {{[-n|--name]}} pipewire-pulse.conf list`

- Elenca i frammenti `context.properties` usati dai client JACK:

`pw-config {{[-n|--name]}} jack.conf list context.properties`

- Elenca il `context.properties` unificato usato dai client JACK:

`pw-config {{[-n|--name]}} jack.conf merge context.properties`

- Elenca i `context.modules` unificati usati dal server PipeWire e riformatta:

`pw-config {{[-n|--name]}} pipewire.conf {{[-r|--recurse]}} merge context.modules`

- Mostra aiuto:

`pw-config {{[-h|--help]}}`
