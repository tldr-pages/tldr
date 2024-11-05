# espeak

> Usa la sintesi vocale per parlare tramite il dispositivo audio di output predefinito.
> Maggiori informazioni: <https://espeak.sourceforge.net>.

- Pronuncia una frase ad alta voce:

`espeak "Mi piace andare in bici."`

- Pronuncia il contenuto di un file ad alta voce:

`espeak -f {{nome_file}}`

- Salva l'output su un file audio WAV, invece che parlare direttamente:

`espeak -w {{nome_file.wav}} "È GNU più Linux."`

- Usa una voce differente:

`espeak -v {{voce}}`
