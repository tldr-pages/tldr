# sfdk undeploy

> Undeploy build-ի արդյունքները սարքից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.undeploy.adoc>:.

- Ապատեղակայել՝ օգտագործելով նշված մեթոդը (`pkcon`, `rpm`, `rsync`, `sdk` կամ `zypper`):

`sfdk undeploy --{{method}}`

- Նախադիտեք undeploy-ը առանց փոփոխությունները կիրառելու.:

`sfdk undeploy --{{method}} {{[-n|--dry-run]}}`

- Ապատեղակայել ֆայլերը գլոբալ օրինակով `package*`:

`sfdk undeploy --{{method}} "+package*"`

- Ապատեղակայել բոլոր ֆայլերը՝ բացառությամբ `ignore*`-ի՝:

`sfdk undeploy --{{method}} "-ignore*"`
