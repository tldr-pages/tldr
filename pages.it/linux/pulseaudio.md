# pulseaudio

> Programma che permette di gestire il daemon audio di sistema.
> Maggiori informazioni: <https://manned.org/pulseaudio>.

- Controlla se PulseAudio è in esecuzione. Se il programma non è attivo viene restituito un exit code diverso da 0:

`pulseaudio --check`

- Esegue il daemon di PulseAudio in background:

`pulseaudio --start`

- Interrompe l'esecuzione del daemon di PulseAudio:

`pulseaudio {{[-k|--kill]}}`

- Mostra i moduli disponibili:

`pulseaudio --dump-modules`

- Carica un modulo all'interno del daemon in esecuzione con gli argomenti specificati:

`pulseaudio {{[-L|--load]}} "{{nome_modulo}} {{argomenti}}"`
