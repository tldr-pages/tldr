# փաթեթ գործիք

> Շահարկել Android հավելվածների փաթեթները:.
> Որոշ ենթահրամաններ, ինչպիսիք են `validate`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/bundletool>:.

- Ցուցադրել օգնություն ենթահրամանի համար.:

`bundletool help {{subcommand}}`

- Ստեղծեք APK-ներ հավելվածների փաթեթից (հուշումներ keystore-ի գաղտնաբառը).:

`bundletool build-apks --bundle {{path/to/bundle.aab}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --output {{path/to/file.apks}}`

- Ստեղծեք APK-ներ հավելվածի փաթեթից, որը տալիս է keystore գաղտնաբառը.:

`bundletool build-apks --bundle {{path/to/bundle.aab}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --ks-pass {{pass:the_password}} --output {{path/to/file.apks}}`

- Ստեղծեք APK-ներ, ներառյալ միայն մեկ APK համընդհանուր օգտագործման համար.:

`bundletool build-apks --bundle {{path/to/bundle.aab}} --mode {{universal}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --output {{path/to/file.apks}}`

- Տեղադրեք APK-ների ճիշտ համակցությունը էմուլյատորի կամ սարքի վրա.:

`bundletool install-apks --apks {{path/to/file.apks}}`

- Գնահատեք հավելվածի ներբեռնման չափը.:

`bundletool get-size total --apks {{path/to/file.apks}}`

- Ստեղծեք սարքի ճշգրտման JSON ֆայլ էմուլատորի կամ սարքի համար.:

`bundletool get-device-spec --output {{path/to/file.json}}`

- Ստուգեք փաթեթը և ցուցադրեք դրա մասին մանրամասն տեղեկատվություն.:

`bundletool validate --bundle {{path/to/bundle.aab}}`
