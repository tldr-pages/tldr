# փաթեթ գործիքների աղբանոց

> Շահարկել Android հավելվածների փաթեթները:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/bundletool>:.

- Ցուցադրել բազային մոդուլի `AndroidManifest.xml`-ը.:

`bundletool dump manifest --bundle {{path/to/bundle.aab}}`

- Ցուցադրել որոշակի արժեք `AndroidManifest.xml`-ից՝ օգտագործելով XPath:

`bundletool dump manifest --bundle {{path/to/bundle.aab}} --xpath {{/manifest/@android:versionCode}}`

- Ցուցադրել կոնկրետ մոդուլի `AndroidManifest.xml`-ը.:

`bundletool dump manifest --bundle {{path/to/bundle.aab}} --module {{name}}`

- Ցուցադրել բոլոր ռեսուրսները հավելվածի փաթեթում.:

`bundletool dump resources --bundle {{path/to/bundle.aab}}`

- Ցուցադրել կոնֆիգուրացիան որոշակի ռեսուրսի համար.:

`bundletool dump resources --bundle {{path/to/bundle.aab}} --resource {{type/name}}`

- Ցուցադրել որոշակի ռեսուրսի կոնֆիգուրացիան և արժեքները՝ օգտագործելով ID-ն.:

`bundletool dump resources --bundle {{path/to/bundle.aab}} --resource {{0x7f0e013a}} --values`

- Ցուցադրել փաթեթի կազմաձևման ֆայլի բովանդակությունը.:

`bundletool dump config --bundle {{path/to/bundle.aab}}`
