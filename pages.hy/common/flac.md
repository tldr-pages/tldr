# flac

> Կոդավորեք, վերծանեք և փորձարկեք FLAC ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://xiph.org/flac/documentation_tools_flac.html>:.

- Կոդավորեք WAV ֆայլը FLAC-ում (սա կստեղծի FLAC ֆայլ նույն տեղում, ինչ WAV ֆայլը):

`flac {{path/to/file.wav}}`

- Կոդավորեք WAV ֆայլը FLAC-ում՝ նշելով ելքային ֆայլը.:

`flac {{[-o|--output-name]}} {{path/to/output.flac}} {{path/to/file.wav}}`

- Վերծանեք FLAC ֆայլը WAV-ի վրա՝ նշելով ելքային ֆայլը.:

`flac {{[-d|--decode]}} {{[-o|--output-name]}} {{path/to/output.wav}} {{path/to/file.flac}}`

- Փորձեք FLAC ֆայլը ճիշտ կոդավորման համար.:

`flac {{[-t|--test]}} {{path/to/file.flac}}`
