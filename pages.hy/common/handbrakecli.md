#ձեռքի արգելակ

> Հրամանի տող ինտերֆեյս HandBrake վիդեո փոխակերպման և DVD ripping գործիքի համար:.
> Լրացուցիչ տեղեկություններ. <https://handbrake.fr/docs/en/latest/cli/command-line-reference.html>:.

- Վերափոխեք վիդեո ֆայլը MKV-ի (AAC 160 կբիթ աուդիո և x264 CRF20 տեսանյութ).:

`handbrakecli {{[-i|--input]}} {{input.avi}} {{[-o|--output]}} {{output.mkv}} {{[-e|--encoder]}} x264 {{[-q|--quality]}} 20 {{[-B|--ab]}} 160`

- Չափափոխել վիդեո ֆայլը 320x240:

`handbrakecli {{[-i|--input]}} {{input.mp4}} {{[-o|--output]}} {{output.mp4}} {{[-w|--width]}} 320 {{[-l|--height]}} 240`

- Ցուցակեք առկա նախադրյալները.:

`handbrakecli {{[-z|--preset-list]}}`

- Փոխարկեք AVI տեսանյութը MP4-ի, օգտագործելով Android-ի նախադրյալը.:

`handbrakecli {{[-Z|--preset]}} "Android" {{[-i|--input]}} {{input.ext}} {{[-o|--output]}} {{output.mp4}}`

- Տպեք DVD-ի բովանդակությունը՝ ստանալով CSS ստեղները գործընթացում.:

`handbrakecli {{[-i|--input]}} {{/dev/sr0}} {{[-t|--title]}} 0`

- Պատռեք DVD-ի առաջին կատարումը նշված սարքում: Աուդիոտրագները և ենթագրերի լեզուները նշված են որպես ցուցակներ.:

`handbrakecli {{[-i|--input]}} {{/dev/sr0}} {{[-t|--title]}} 1 {{[-o|--output]}} {{out.mkv}} {{[-f|--format]}} av_mkv {{[-e|--encoder]}} x264 {{[-s|--subtitle]}} {{1,4,5}} {{[-a|--audio]}} {{1,2}} {{[-E|--aencoder]}} copy {{[-q|--quality]}} {{23}}`
