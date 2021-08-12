# handbrakecli

> Interfață linie de comandă la instrumentul de conversie video Frâna de mână.
> Mai multe informaţii: <https://handbrake.fr/>

- Conversia unui fișier video la MKV (audio AAC 160kbit și x264 CRF20 video):

`handbrakecli -i {{input.avi}} -o {{output.mkv}} -e x264 -q 20 -B 160`

- Redimensionarea unui fișier video la 320x240:

`handbrakecli -i {{input.mp4}} -o {{output.mp4}} -w 320 -l 240`

- Lista presetărilor disponibile:

`handbrakecli --preset-list`

- Conversia unui videoclip AVI la MP4 utilizând presetarea Android:

`handbrakecli --preset="Android" -i {{input.ext}} -o {{output.mp4}}`
