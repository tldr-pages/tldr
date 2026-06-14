# vgmstream_cli

> Նվագարկեք տեսախաղերում օգտագործվող աուդիո ձևաչափերի լայն տեսականի և փոխարկեք դրանք `wav`-ի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md>:.

- Վերծանեք `adc` ֆայլը `wav`: (Լռակյաց ելքային անունը `input.wav` է):

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}}`

- Տպեք մետատվյալներ՝ առանց աուդիո վերծանման.:

`vgmstream_cli {{path/to/input.adc}} -m`

- Ապակոդավորեք աուդիո ֆայլ առանց հանգույցների.:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -i`

- Ապակոդավորեք երեք օղակներով, այնուհետև ավելացրեք 3 վրկ ուշացում, որին հաջորդում է 5 վրկ մարում:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -l {{3.0}} -f {{5.0}} -d {{3.0}}`

- Փոխակերպեք բազմաթիվ ֆայլեր `bgm_(original name).wav`-ի (կանխադրված `-o` նախշը `?f.wav` է):

`vgmstream_cli -o {{path/to/bgm_?f.wav}} {{path/to/file1.adc path/to/file2.adc ...}}`

- Անվերջ նվագարկեք պտտվող ֆայլը (`channels` և `rate`-ը պետք է համապատասխանեն մետատվյալներին):

`vgmstream_cli {{path/to/input.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`
