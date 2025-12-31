# piper

> Un sistema neural rápido y local de conversión de texto a voz.
> Descarga y prueba modelos de habla desde <https://rhasspy.github.io/piper-samples>.
> Más información: <https://github.com/OHF-Voice/piper1-gpl>.

- Genera un archivo WAV utilizando un modelo de texto a voz (suponiendo un archivo de configuración en model_path + .json):

`echo {{Cosa a decir}} | piper -m {{ruta/a/modelo.onnx}} -f {{archivo_de_salida.wav}}`

- Genera un archivo WAV utilizando un modelo y especificando su archivo de [c]onfiguración JSON:

`echo {{'Lo que hay que decir'}} | piper -m {{ruta/a/modelo.onnx}} -c {{ruta/a/modelo.onnx.json}} -f {{archivo_de_salida.wav}}`

- Selecciona un locutor concreto en una voz con varios locutores especificando el número de identificación del locutor:

`echo {{'Warum?'}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{enojado.wav}}`

- Transmite la salida al reproductor multimedia mpv:

`echo {{'Hello world'}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- Habla el doble de rápido, con grandes espacios entre frases:

`echo {{'Hablando el doble de rápido. Con más drama!'}} | piper -m {{foo.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{drama.wav}}`
