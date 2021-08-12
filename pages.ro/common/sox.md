# sox

> Sound Exchange: redați, înregistrați și convertiți fișiere audio.
> Formatele audio sunt identificate de extensie.
> Mai multe informaţii: <http://sox.sourceforge.net>

- Îmbinați două fișiere audio într-unul singur:

`sox -m {{input_audiofile1}} {{input_audiofile2}} {{output_audiofile}}`

- Decupați un fișier audio la orele specificate:

`sox {{input_audiofile}} {{output_audiofile}} trim {{start}} {{end}}`

- Normalizarea unui fișier audio (ajustați volumul la nivelul maxim de vârf, fără tăiere):

`sox --norm {{input_audiofile}} {{output_audiofile}}`

- Inversați și salvați un fișier audio:

`sox {{input_audiofile}} {{output_audiofile}} reverse`

- Imprimarea datelor statistice ale unui fișier audio:

`sox {{input_audiofile}} -n stat`

- Măriți volumul unui fișier audio cu 2x:

`sox -v 2.0 {{input_audiofile}} {{output_audiofile}}`
