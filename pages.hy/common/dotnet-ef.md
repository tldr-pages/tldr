# dotnet էֆ

> Կատարել նախագծման ժամանակի մշակման առաջադրանքներ Entity Framework Core-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/ef/core/cli/dotnet>:.

- Թարմացրեք տվյալների բազան նշված միգրացիայի մեջ.:

`dotnet ef database update {{migration}}`

- Բաց թողեք տվյալների բազան.:

`dotnet ef database drop`

- Հասանելի `DbContext` տեսակների ցանկ՝:

`dotnet ef dbcontext list`

- Ստեղծեք կոդ `DbContext`-ի և տվյալների բազայի միավորի տեսակների համար.:

`dotnet ef dbcontext scaffold {{connection_string}} {{provider}}`

- Ավելացնել նոր միգրացիա.:

`dotnet ef migrations add {{name}}`

- Հեռացրեք վերջին միգրացիան՝ հետ գլորելով կոդի փոփոխությունները, որոնք կատարվել են վերջին միգրացիայի համար.:

`dotnet ef migrations remove`

- Ցուցակեք մատչելի միգրացիաները.:

`dotnet ef migrations list`

- Ստեղծեք SQL սցենար միգրացիոն տիրույթից.:

`dotnet ef migrations script {{from_migration}} {{to_migration}}`
