# ffplay

> Պարզ և շարժական մեդիա նվագարկիչ՝ օգտագործելով FFmpeg գրադարանները և SDL գրադարանը:.
> Լրացուցիչ տեղեկություններ. <https://ffmpeg.org/ffplay-all.html>:.

- Նվագարկել մեդիա ֆայլ.:

`ffplay {{path/to/file}}`

- Նվագարկեք աուդիո մեդիա ֆայլից առանց GUI-ի.:

`ffplay -nodisp {{path/to/file}}`

- Նվագարկեք `ffmpeg`-ից `stdin`-ով անցած մեդիա:

`ffmpeg -i {{path/to/file}} -c {{copy}} -f {{media_format}} - | ffplay -`

- Նվագարկեք տեսանյութ և ցույց տվեք շարժման վեկտորները իրական ժամանակում.:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{path/to/file}}`

- Ցուցադրել միայն վիդեո հիմնական կադրերը.:

`ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{path/to/file}}`
