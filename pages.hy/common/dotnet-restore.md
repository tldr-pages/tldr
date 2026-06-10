# dotnet-ի վերականգնում

> Վերականգնում է .NET նախագծի կախվածությունները և գործիքները:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>:.

- Վերականգնել կախվածությունը .NET նախագծի կամ լուծման համար ընթացիկ գրացուցակում.:

`dotnet restore`

- Վերականգնել կախվածությունը .NET նախագծի կամ լուծման համար որոշակի վայրում.:

`dotnet restore {{path/to/project_or_solution}}`

- Վերականգնել կախվածությունները՝ առանց HTTP հարցումների քեշավորման.:

`dotnet restore --no-http-cache`

- Ստիպեք լուծել բոլոր կախվածությունները, նույնիսկ եթե վերջին վերականգնումը հաջող էր.:

`dotnet restore --force`

- Վերականգնել կախվածությունները՝ օգտագործելով փաթեթի աղբյուրի ձախողումները որպես նախազգուշացումներ.:

`dotnet restore --ignore-failed-sources`

- Վերականգնել կախվածությունները հատուկ խոսակցական մակարդակով.:

`dotnet restore {{[-v|--verbosity]}} {{quiet|minimal|normal|detailed|diagnostic}}`
