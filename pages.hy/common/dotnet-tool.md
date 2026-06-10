# dotnet գործիք

> Կառավարեք .NET գործիքները և որոնեք հրապարակված գործիքները NuGet-ում:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/core/tools/global-tools>:.

- Տեղադրեք գլոբալ գործիք (մի օգտագործեք `--global` տեղական գործիքների համար).:

`dotnet tool install {{[-g|--global]}} {{dotnetsay}}`

- Տեղադրեք գործիքներ, որոնք սահմանված են տեղական գործիքի մանիֆեստում.:

`dotnet tool restore`

- Թարմացրեք հատուկ գլոբալ գործիք (մի օգտագործեք `--global` տեղական գործիքների համար).:

`dotnet tool update {{[-g|--global]}} {{tool_name}}`

- Տեղահանեք գլոբալ գործիք (մի օգտագործեք `--global` տեղական գործիքների համար).:

`dotnet tool uninstall {{[-g|--global]}} {{tool_name}}`

- Ցուցակեք տեղադրված գլոբալ գործիքները (մի օգտագործեք `--global` տեղական գործիքների համար).:

`dotnet tool list {{[-g|--global]}}`

- Որոնման գործիքներ NuGet-ում.:

`dotnet tool search {{search_term}}`

- Ցուցադրել օգնությունը.:

`dotnet tool {{[-h|--help]}}`
