# argos- թարգմանել

> Բաց կոդով անցանց թարգմանության գրադարան և Python-ով գրված CLI գործիք:.
> Լրացուցիչ տեղեկություններ. <https://argos-translate.readthedocs.io/en/latest/source/cli.html>:.

- Տեղադրեք թարգմանչական զույգեր իսպաներենից անգլերեն թարգմանության համար.:

`argospm install translate-es_en`

- Թարգմանեք որոշ տեքստ իսպաներենից (`es`) անգլերեն (`en`) (Նշում. Աջակցվում է միայն երկու տառային լեզվի կոդ):

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- Թարգմանեք տեքստային ֆայլ անգլերենից հինդի.:

`cat {{path/to/file.txt}} | argos-translate --from-lang en --to-lang hi`

- Թվարկեք բոլոր տեղադրված թարգմանչական զույգերը.:

`argospm list`

- Ցույց տալ թարգմանության զույգերը անգլերենից, որոնք հասանելի են տեղադրման համար.:

`argospm search --from-lang en`

- Թարմացրեք տեղադրված լեզվական փաթեթների զույգերը.:

`argospm update`

- Թարգմանել `ar`-ից `ru` (Նշում. Սա պահանջում է թարգմանության զույգերը `translate-ar_en` և `translate-en_ru` տեղադրել):

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`
