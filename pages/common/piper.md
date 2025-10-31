# piper

> A fast, local neural text to speech system.
> Try out and download speech models from <https://rhasspy.github.io/piper-samples>.
> More information: <https://github.com/OHF-Voice/piper1-gpl>.

- Output a WAV [f]ile using a text-to-speech [m]odel (assuming a configuration file at model_path + .json):

`echo {{Thing to say}} | piper -m {{path/to/model.onnx}} -f {{outputfile.wav}}`

- Output a WAV [f]ile using a [m]odel and specifying its JSON [c]onfig file:

`echo {{Thing to say}} | piper -m {{path/to/model.onnx}} -c {{path/to/model.onnx.json}} -f {{outputfile.wav}}`

- Select a particular speaker in a voice with multiple speakers by specifying the speaker's ID number:

`echo {{Warum?}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{angry.wav}}`

- Stream the output to the mpv media player:

`echo {{Hello world}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- Speak twice as fast, with huge gaps between sentences:

`echo {{Speaking twice the speed. With added drama!}} | piper -m {{file.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{drama.wav}}`
