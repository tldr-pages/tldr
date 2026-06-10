#շշուկ

> Փոխարկեք աուդիո ֆայլերը `txt`, `vtt`, `srt`, `tsv` և `json`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/openai/whisper>:.

- Փոխակերպեք հատուկ աուդիո ֆայլը տվյալ ֆայլի բոլոր ձևաչափերին.:

`whisper {{path/to/audio.mp3}}`

- Փոխակերպեք աուդիո ֆայլ, որը նշում է փոխարկված ֆայլի ելքային ձևաչափը.:

`whisper {{path/to/audio.mp3}} --output_format {{txt}}`

- Փոխակերպեք աուդիո ֆայլը ՝ օգտագործելով փոխակերպման հատուկ մոդել.:

`whisper {{path/to/audio.mp3}} --model {{tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}}`

- Փոխակերպեք աուդիո ֆայլը՝ նշելով, թե որ լեզվով է աուդիո ֆայլը՝ փոխակերպման ժամանակը նվազեցնելու համար.:

`whisper {{path/to/audio.mp3}} --language {{english}}`

- Փոխակերպեք աուդիո ֆայլը և պահեք այն որոշակի վայրում.:

`whisper {{path/to/audio.mp3}} --output_dir "{{path/to/output}}"`

- Փոխակերպեք աուդիո ֆայլը հանգիստ ռեժիմով.:

`whisper {{path/to/audio.mp3}} --verbose {{False}}`
