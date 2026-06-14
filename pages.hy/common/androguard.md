# androguard

> Android հավելվածների հակադարձ ինժեներ: Գրված է Python-ով։
> Լրացուցիչ տեղեկություններ. <https://github.com/androguard/androguard>:.

- Ցուցադրել Android հավելվածի մանիֆեստը.:

`androguard axml {{path/to/app}}.apk`

- Ցուցադրել հավելվածի մետատվյալները (տարբերակի և հավելվածի ID).:

`androguard apkid {{path/to/app}}.apk`

- Decompile Java կոդը հավելվածից.:

`androguard decompile {{path/to/app}}.apk --output {{path/to/directory}}`
