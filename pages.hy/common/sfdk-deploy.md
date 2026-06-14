# sfdk տեղակայում

> Տեղադրեք կառուցման արդյունքները սարքի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.deploy.adoc>:.

- Տեղադրեք՝ օգտագործելով նշված մեթոդը (`pkcon`, `rsync`, `sdk`, `zypper`, `zypper-dup` կամ `manual`):

`sfdk deploy --{{method}}`

- Նախադիտեք տեղակայումը առանց փոփոխությունները կիրառելու.:

`sfdk deploy --{{method}} {{[-n|--dry-run]}}`

- Տեղադրեք ֆայլերը գլոբալ օրինակով `package*`:

`sfdk deploy --{{method}} "+package*"`

- Տեղադրեք բոլոր ֆայլերը, բացառությամբ `ignore*`-ի՝:

`sfdk deploy --{{method}} "-ignore*"`

- Ապատեղակայել՝ օգտագործելով նշված մեթոդը (`pkcon`, `rpm`, `rsync`, `sdk` կամ `zypper`):

`sfdk undeploy --{{method}}`
