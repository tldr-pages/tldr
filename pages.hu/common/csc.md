# csc

> A Microsoft C# fordító. További információ: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- Egy vagy több C# fájl fordítása CIL futtatható állományba:

`csc {{path/to/input_file_a.cs}} {{path/to/input_file_b.cs}}`

- Adja meg a kimeneti fájlnevet:

`csc /out:{{path/to/filename}} {{path/to/input_file.cs}}`

- Végrehajtható fájl helyett `.dll` könyvtárba fordítás:

`csc /target:library {{path/to/input_file.cs}}`

- Hivatkozás egy másik összeállításra:

`csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}`

- Erőforrás beágyazása:

`csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}`

- XML dokumentáció automatikus generálása:

`csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}`

- Ikon megadása:

`csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}`

- Az eredményül kapott összeállítás határozott elnevezése egy kulcsfájl segítségével:

`csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}`
