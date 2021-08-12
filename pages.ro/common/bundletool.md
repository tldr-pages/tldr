# bundletool

> Instrument de linie de comandă pentru a manipula pachetele de aplicații Android.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/bundletool>

- Afișează ajutor pentru o subcomandă:

`bundletool help {{subcommand}}`

- Generați APK-uri dintr-un pachet de aplicații (solicitări pentru parola keystore):

`bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}`

- Generați APK-uri dintr-un pachet de aplicații care oferă parola keystore:

`bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} –ks-pass={{pass:the_password}} --output={{path/to/file.apks}}`

- Generați APK-uri, inclusiv un singur APK pentru utilizare universală:

`bundletool build-apks --bundle={{path/to/bundle.aab}} --mode={{universal}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}`

- Instalați combinația potrivită de APK-uri la un emulator sau dispozitiv:

`bundletool install-apks --apks={{path/to/file.apks}}`

- Estimați dimensiunea de descărcare a unei aplicații:

`bundletool get-size total --apks={{path/to/file.apks}}`

- Generați un fișier JSON specificație dispozitiv pentru un emulator sau dispozitiv:

`bundletool get-device-spec --output={{path/to/file.json}}`

- Verificați un pachet și afișați informații detaliate despre acesta:

`bundletool validate --bundle={{path/to/bundle.aab}}`
