# monop

> Megkeresi és megjeleníti a .NET-összeállításokban található típusok és metódusok aláírásait. További információ: <https://manned.org/monop>.

- Megjeleníti a .NET Framework beépített Type-jának szerkezetét:

`monop {{System.String}}`

- Listázza ki a típusokat egy assemblyben:

`monop -r:{{path/to/assembly.exe}}`

- Megjeleníti egy Type szerkezetét egy adott assemblyben:

`monop -r:{{path/to/assembly.dll}} {{Namespace.Path.To.Type}}`

- Csak a megadott Type-ban definiált tagok megjelenítése:

`monop -r:{{path/to/assembly.dll}} --only-declared {{Namespace.Path.To.Type}}`

- Privát tagok megjelenítése:

`monop -r:{{path/to/assembly.dll}} --private {{Namespace.Path.To.Type}}`

- Elrejti az elavult tagokat:

`monop -r:{{path/to/assembly.dll}} --filter-obsolete {{Namespace.Path.To.Type}}`

- A megadott összeállításban hivatkozott más összeállítások listázása:

`monop -r:{{path/to/assembly.dll}} --refs`
