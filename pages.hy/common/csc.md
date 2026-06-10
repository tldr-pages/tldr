# csc

> Microsoft C# կոմպիլյատոր:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>:.

- Կազմել մեկ կամ մի քանի C# ֆայլ CIL գործարկիչում.:

`csc {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- Նշեք ելքային ֆայլի անունը.:

`csc /out:{{path/to/file}} {{path/to/input_file.cs}}`

- Կազմել `.dll` գրադարանում՝ գործարկվողի փոխարեն.:

`csc /target:library {{path/to/input_file.cs}}`

- Հղում մեկ այլ ժողովի.:

`csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}`

- Տեղադրել ռեսուրս.:

`csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}`

- Ավտոմատ կերպով ստեղծել XML փաստաթղթեր.:

`csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}`

- Նշեք պատկերակը.:

`csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}`

- Հստակ անվանեք ստացված ժողովը բանալի ֆայլով.:

`csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}`
