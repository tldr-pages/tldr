# բն

> Android Asset Packaging Tool. կազմել և փաթեթավորել Android հավելվածի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/aapt>:.

- Թվարկեք APK արխիվում պարունակվող ֆայլերը.:

`aapt list {{path/to/app}}.apk`

- Ցուցադրել հավելվածի մետատվյալները (տարբերակ, թույլտվություններ և այլն).:

`aapt dump badging {{path/to/app}}.apk`

- Ստեղծեք նոր APK արխիվ նշված գրացուցակից ֆայլերով.:

`aapt package -F {{path/to/app}}.apk {{path/to/directory}}`
