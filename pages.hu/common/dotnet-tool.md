# dotnet tool

> A .NET eszközök kezelése és a NuGetben közzétett eszközök keresése. További információ: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- Telepítsen egy globális eszközt (ne használja a `--global` címet a helyi eszközökhöz):

`dotnet tool install --global {{dotnetsay}}`

- A helyi eszközmanifesztben meghatározott eszközök telepítése:

`dotnet tool restore`

- Egy adott globális eszköz frissítése (helyi eszközökhöz ne használja a `--global` címet):

`dotnet tool update --global {{tool_name}}`

- Egy globális eszköz eltávolítása (helyi eszközökhöz ne használja a `--global` címet):

`dotnet tool uninstall --global {{tool_name}}`

- Telepített globális eszközök listázása (helyi eszközökhöz ne használja a `--global` címet):

`dotnet tool list --global`

- Eszközök keresése a NuGet-ben:

`dotnet tool search {{search_term}}`

- Súgó megjelenítése:

`dotnet tool --help`
