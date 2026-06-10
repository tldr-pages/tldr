#ֆլատ

> Google-ի անվճար, բաց կոդով և միջպլատֆորմային բջջային հավելվածի SDK-ն:.
> Որոշ ենթահրամաններ, ինչպիսիք են `pub`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/flutter/flutter/blob/master/docs/tool/README.md>:.

- Նախաձեռնեք նոր Flutter նախագիծը նույն անունով գրացուցակում.:

`flutter create {{project_name}}`

- Ստուգեք, արդյոք բոլոր արտաքին գործիքները ճիշտ են տեղադրված.:

`flutter doctor`

- Թվարկեք կամ փոխեք Flutter ալիքը.:

`flutter channel {{stable|beta|dev|master}}`

- Գործարկեք Flutter-ը բոլոր սկսված էմուլյատորների և միացված սարքերի վրա.:

`flutter run -d all`

- Գործարկել թեստերը տերմինալում նախագծի արմատից.:

`flutter test {{test/example_test.dart}}`

- Ստեղծեք թողարկման APK, որը ուղղված է ժամանակակից սմարթֆոնների մեծամասնությանը.:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- Ջնջել `build` և `.dart_tool` գրացուցակները.:

`flutter clean`

- Ցուցադրել օգնություն կոնկրետ հրամանի վերաբերյալ.:

`flutter help {{command}}`
