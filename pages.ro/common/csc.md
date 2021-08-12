# csc

> Compilatorul Microsoft C#.
> Mai multe informaţii: <https://docs.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>

- Compilați unul sau mai multe fișiere C# la un executabil CIL:

`csc {{path/to/input_file_a.cs}} {{path/to/input_file_b.cs}}`

- Specificați numele fișierului de ieșire:

`csc /out:{{path/to/filename}} {{path/to/input_file.cs}}`

- Compilați într-o bibliotecă `.dll` în loc de un executabil:

`csc /target:library {{path/to/input_file.cs}}`

- Referință la un alt ansamblu:

`csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}`

- Încorporarea unei resurse:

`csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}`

- Generarea automată a documentației XML:

`csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}`

- Specificați o pictogramă:

`csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}`

- Denumiți cu tărie ansamblul rezultat cu un fișier-cheie:

`csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}`
