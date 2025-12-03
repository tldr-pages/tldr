# beep

> Un'utilità per emettere un segnale acustico all'altoparlante del PC.
> Maggiori informazioni: <https://manned.org/man/beep>.

- Emetti un suono:

`beep`

- Emetti un suono che si ripete:

`beep -r {{ripetizioni}}`

- Emetti un suono a una specifica frequenza (Hz) e durata (millisecondi):

`beep -f {{frequenza}} -l {{durata}}`

- Riproduci ogni nuova frequenza e durata come un segnale acustico distinto:

`beep -f {{frequenza}} -l {{durata}} {{[-n|--new]}} -f {{frequenza}} -l {{durata}}`

- Suona la scala di do maggiore:

`beep -f {{262}} {{[-n|--new]}} -f {{294}} {{[-n|--new]}} -f {{330}} {{[-n|--new]}} -f {{349}} {{[-n|--new]}} -f {{392}} {{[-n|--new]}} -f {{440}} {{[-n|--new]}} -f {{494}} {{[-n|--new]}} -f {{523}}`
