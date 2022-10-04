# csc

> Compilatore per Microsoft C#.
> Maggiori informazioni: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- Compila uno o più file C# in un eseguibile da command-line:

`csc {{percorso/al/file_input_a.cs}} {{percorso/al/file_input_b.cs}}`

- Specifica il nome del file output:

`csc /out:{{percorso/al/nome_file_output}} {{percorso/al/file_input.cs}}`

- Compila in una libreria `.dll` invece che in un eseguibile:

`csc /target:library {{percorso/al/file_input.cs}}`

- Referenzia un altro assembly:

`csc /reference:{{percorso/a/libreria.dll}} {{percorso/al/file_input.cs}}`

- Includi una risorsa:

`csc /resource:{{percorso/al/file_risorsa}} {{percorso/al/file_input.cs}}`

- Genera una documentazione XML automaticamente:

`csc /doc:{{percorso/alla/documentazione.xml}} {{percorso/al/file_input.cs}}`

- Specifica un'icona:

`csc /win32icon:{{percorso/a/icona.ico}} {{percorso/al/file_input.cs}}`

- Firma un assembly con un nome sicuro utilizzando una chiave:

`csc /keyfile:{{percorso/a/chiave.snk}} {{percorso/al/file_input.cs}}`
