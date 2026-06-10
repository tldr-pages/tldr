# Cvs

> Համաժամանակյա տարբերակների համակարգ, վերանայման վերահսկման համակարգ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/cvs>:.

- Ստեղծեք նոր պահոց (պահանջում է `$CVSROOT` միջավայրի փոփոխականը, որպեսզի դրսից դրվի).:

`cvs -d {{path/to/repository}} init`

- Նախագիծ ավելացրեք պահեստում.:

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- Ստուգեք նախագիծը.:

`cvs checkout {{project_name}}`

- Ցույց տալ ֆայլերում կատարված փոփոխությունները.:

`cvs diff {{path/to/file}}`

- Ավելացնել ֆայլ.:

`cvs add {{path/to/file}}`

- Կատարել ֆայլ.:

`cvs commit -m "{{message}}" {{path/to/file}}`

- Թարմացրեք աշխատանքային գրացուցակը հեռավոր պահոցից.:

`cvs update`
