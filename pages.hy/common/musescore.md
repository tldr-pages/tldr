# musescore

> MuseScore թերթերի երաժշտության խմբագիր:.
> Տես նաև՝ `lilypond`:.
> Լրացուցիչ տեղեկություններ. <https://handbook.musescore.org/appendix/command-line-usage>:.

- Սահմանեք MP3-ի ելքային բիթային արագությունը կբիթ/վրկ-ով.:

`musescore {{[-b|--bitrate]}} {{bitrate}}`

- Սկսեք MuseScore-ը կարգաբերման ռեժիմում.:

`musescore {{[-d|--debug]}}`

- Միացնել փորձնական գործառույթները, ինչպիսիք են շերտերը.:

`musescore {{[-e|--experimental]}}`

- Արտահանել տվյալ ֆայլը նշված ելքային ֆայլ: Ֆայլի տեսակը կախված է տվյալ ընդլայնումից.:

`musescore {{[-o|--export-to]}} {{output_file}} {{input_file}}`

- Տպեք տարբերություն տրված միավորների միջև.:

`musescore --diff {{path/to/file1}} {{path/to/file2}}`

- Նշեք MIDI ներմուծման գործառնությունների ֆայլը.:

`musescore {{[-M|--midi-operations]}} {{path/to/file}}`
