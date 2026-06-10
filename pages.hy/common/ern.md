#ern

> Electrode Native պլատֆորմի հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <https://native.electrode.io/reference/index-6>:.

- Ստեղծեք նոր `ern` հավելված (`MiniApp`):

`ern create-miniapp {{application_name}}`

- Գործարկեք մեկ կամ մի քանի `MiniApps` iOS/Android Runner հավելվածում՝:

`ern run-{{ios|android}}`

- Ստեղծեք էլեկտրոդի բնիկ կոնտեյներ.:

`ern create-container --miniapps /{{path/to/miniapp_directory}} --platform {{ios|android}}`

- Հրապարակեք էլեկտրոդի բնիկ կոնտեյներ տեղական Maven պահեստում.:

`ern publish-container --publisher {{maven}} --platform {{android}} --extra '{{{"groupId":"com.walmart.ern","artifactId":"quickstart"}}}'`

- Վերափոխեք iOS-ի կոնտեյները նախապես կազմված երկուական շրջանակի.:

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- Թվարկեք Electrode Native-ի բոլոր տեղադրված տարբերակները.:

`ern platform versions`

- Սահմանեք հատումների մակարդակը.:

`ern platform config set logLevel {{trace|debug}}`
