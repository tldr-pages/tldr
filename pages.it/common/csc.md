# csc

> Compilatore per Microsoft C#.
> Maggiori informazioni: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- Compila uno o più file C# in un eseguibile da command-line:

`csc {{percorso/del/file_input_a.cs}} {{percorso/del/file_input_b.cs}}`

- Specifica il nome del file output:

`csc /out:{{percorso/del/nome_file_output}} {{percorso/del/file_input.cs}}`

- Compila in una libreria `.dll` invece che in un eseguibile:

`csc /target:library {{percorso/del/file_input.cs}}`

- Referenzia un altro assembly:

`csc /reference:{{percorso/della/libreria.dll}} {{percorso/del/file_input.cs}}`

- Includi una risorsa:

`csc /resource:{{percorso/del/file_risorsa}} {{percorso/del/file_input.cs}}`

- Genera una documentazione XML automaticamente:

`csc /doc:{{percorso/della/documentazione.xml}} {{percorso/del/file_input.cs}}`

- Specifica un'icona:

`csc /win32icon:{{percorso/dell/icona.ico}} {{percorso/del/file_input.cs}}`

- Firma un assembly con un nome sicuro utilizzando una chiave:

`csc /keyfile:{{percorso/della/chiave.snk}} {{percorso/del/file_input.cs}}`
