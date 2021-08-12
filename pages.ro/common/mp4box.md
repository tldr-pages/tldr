# mp4box

> MPEG-4 Systems Toolbox - Muxes fluxuri în container MP4.
> Mai multe informaţii: <https://gpac.wp.imt.fr/mp4box>

- Afișați informații despre un fișier MP4 existent:

`mp4box -info {{filename}}`

- Adăugați un fișier de subtitrare SRT într-un fișier MP4:

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Combinați audio de la un fișier și video de la altul:

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`
