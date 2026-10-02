# piper

> Een snel, lokaal neuraal tekst-naar-spraaksysteem.
> Probeer en download spraakmodellen op <https://rhasspy.github.io/piper-samples>.
> Meer informatie: <https://github.com/OHF-Voice/piper1-gpl>.

- Genereer een WAV-[f]ile met een tekst-naar-spraak-[m]odel (uitgaande van een configuratiebestand op model_pad + `.json`):

`echo {{Te zeggen tekst}} | piper -m {{pad/naar/model.onnx}} -f {{uitvoerbestand.wav}}`

- Genereer een WAV-[f]ile met een [m]odel en specificeer het bijbehorende JSON-[c]onfiguratiebestand:

`echo {{Te zeggen tekst}} | piper -m {{pad/naar/model.onnx}} -c {{pad/naar/model.onnx.json}} -f {{uitvoerbestand.wav}}`

- Selecteer een specifieke spreker in een stem met meerdere sprekers door het ID-nummer van de spreker op te geven:

`echo {{Warum?}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{angry.wav}}`

- Stream de uitvoer naar de mpv-mediaspeler:

`echo {{Hello world}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- Spreek twee keer zo snel, met grote pauzes tussen zinnen:

`echo {{Speaking twice the speed. With added drama!}} | piper -m {{file.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{drama.wav}}`
