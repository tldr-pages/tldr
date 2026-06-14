#խողովակավոր

> Արագ, տեղական նյարդային տեքստի խոսքի համակարգ:.
> Փորձեք և ներբեռնեք խոսքի մոդելները <https://rhasspy.github.io/piper-samples>-ից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/OHF-Voice/piper1-gpl>:.

- Արտադրեք WAV [f]ile՝ օգտագործելով տեքստը-խոսք [m]մոդելը (ենթադրելով կազմաձևման ֆայլ՝ model_path + `.json`):

`echo {{Thing to say}} | piper -m {{path/to/model.onnx}} -f {{outputfile.wav}}`

- Արտադրեք WAV [f]ile՝ օգտագործելով [m]model և նշելով դրա JSON [c]onfig ֆայլը.:

`echo {{Thing to say}} | piper -m {{path/to/model.onnx}} -c {{path/to/model.onnx.json}} -f {{outputfile.wav}}`

- Ընտրեք որոշակի բարձրախոս մի քանի բարձրախոսներով ձայնով` նշելով խոսնակի ID համարը.:

`echo {{Warum?}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{angry.wav}}`

- Հեռարձակեք ելքը mpv մեդիա նվագարկիչ.:

`echo {{Hello world}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- Խոսեք երկու անգամ ավելի արագ, նախադասությունների միջև հսկայական բացերով.:

`echo {{Speaking twice the speed. With added drama!}} | piper -m {{file.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{drama.wav}}`
