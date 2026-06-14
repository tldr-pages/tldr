#մոնոպ

> Գտնում և ցուցադրում է տեսակների և մեթոդների ստորագրությունները .NET հավաքների ներսում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/monop>:.

- Ցույց տալ .NET Framework-ի ներկառուցված Type-ի կառուցվածքը.:

`monop {{System.String}}`

- Թվարկե՛ք ժողովի տեսակները.:

`monop -r:{{path/to/assembly.exe}}`

- Ցույց տալ տիպի կառուցվածքը կոնկրետ ժողովում.:

`monop -r:{{path/to/assembly.dll}} {{Namespace.Path.To.Type}}`

- Ցուցադրել միայն նշված տեսակի մեջ սահմանված անդամներին.:

`monop -r:{{path/to/assembly.dll}} {{[-d|--declared-only]}} {{Namespace.Path.To.Type}}`

- Ցույց տալ մասնավոր անդամներին.:

`monop -r:{{path/to/assembly.dll}} {{[-p|--private]}} {{Namespace.Path.To.Type}}`

- Թաքցնել հնացած անդամներին.:

`monop -r:{{path/to/assembly.dll}} {{[-f|--filter-obsolete]}} {{Namespace.Path.To.Type}}`

- Թվարկեք մյուս հավաքները, որոնց հղում է կատարում նշված ժողովը.:

`monop -r:{{path/to/assembly.dll}} --refs`
