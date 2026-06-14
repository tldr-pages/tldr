# zipalign

> Zip արխիվի հավասարեցման գործիք:.
> Android SDK-ի կառուցման գործիքների մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/zipalign>:.

- Zip ֆայլի տվյալները հավասարեցրեք 4 բայթ սահմանների վրա.:

`zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}`

- Ստուգեք, որ Zip ֆայլը ճիշտ հավասարեցված է 4 բայթ սահմանների վրա և ցուցադրեք արդյունքները մանրամասնորեն.:

`zipalign -v -c {{4}} {{path/to/input.zip}}`
