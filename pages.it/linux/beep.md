# beep

> Un'utilità per emettere un segnale acustico all'altoparlante del PC.
> Maggiori informazioni: <https://github.com/spkr-beep/beep>.

- Emetti un suono:

`beep`

- Emetti un suono che si ripete:

`beep -r {{ripetizioni}}`

- Emetti un suono a una specifica frequenza (Hz) e durata (millisecondi):

`beep -f {{frequenza}} -l {{durata}}`

- Riproduci ogni nuova frequenza e durata come un segnale acustico distinto:

`beep -f {{frequenza}} -l {{durata}} -n -f {{frequenza}} -l {{durata}}`

- Suona la scala di do maggiore:

`beep -f {{262}} -n -f {{294}} -n -f {{330}} -n -f {{349}} -n -f {{392}} -n -f {{440}} -n -f {{494}} -n -f {{523}}`
