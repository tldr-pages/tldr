# react-native

> React-ի միջոցով հայրենի հավելվածներ ստեղծելու շրջանակ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/react-native-community/cli/blob/main/docs/commands.md>:.

- Նախաձեռնեք նոր React Native նախագիծը նույն անունով գրացուցակում.:

`react-native init {{project_name}}`

- Սկսեք մետրոյի փաթեթը.:

`react-native start`

- Սկսեք մետրոյի փաթեթը մաքուր քեշով.:

`react-native start --reset-cache`

- Կառուցեք ընթացիկ հավելվածը և գործարկեք այն միացված Android սարքի կամ էմուլյատորի վրա.:

`react-native run-android`

- Կառուցեք ընթացիկ հավելվածը և գործարկեք այն iOS սիմուլյատորի վրա.:

`react-native run-ios`

- Ստեղծեք ընթացիկ հավելվածը `release` ռեժիմում և գործարկեք այն միացված Android սարքի կամ էմուլյատորի վրա.:

`react-native run-android --variant={{release}}`

- Սկսեք `logkitty`-ը և տպեք տեղեկամատյանները `stdout`-ում՝:

`react-native log-android`

- Սկսեք `tail system.log` iOS սիմուլյատորի համար և տպեք գրանցամատյանները `stdout`-ում:

`react-native log-ios`
