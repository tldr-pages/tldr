#ամաչկոտություն

> Նվագարկել և փոխարկել MIDI ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/timidity>:.

- Նվագարկել MIDI ֆայլ.:

`timidity {{path/to/file.mid}}`

- Նվագարկեք MIDI ֆայլը հանգույցով.:

`timidity {{[--l|--loop]}} {{path/to/file.mid}}`

- Նվագարկեք MIDI ֆայլը հատուկ ստեղնով (0 = C մաժոր/Ա մինոր, -1 = Ֆ մաժոր/Դ մինոր, +1 = Գ մաժոր/Է մինոր և այլն):

`timidity --force-keysig={{-flats|+sharps}} {{path/to/file.mid}}`

- Փոխակերպեք MIDI ֆայլը PCM (WAV) աուդիո.:

`timidity --output-mode={{w}} --output-file={{path/to/file.wav}} {{path/to/file.mid}}`

- Փոխակերպեք MIDI ֆայլը FLAC աուդիո.:

`timidity --output-mode={{F}} --output-file={{path/to/file.flac}} {{path/to/file.mid}}`
