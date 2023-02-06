# dotnet ef

> Tervezési idejű fejlesztési feladatok elvégzése az Entity Framework Core számára. További információ: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- Az adatbázis frissítése egy megadott migrációhoz:

`dotnet ef database update {{migration}}`

- Dobja el az adatbázist:

`dotnet ef database drop`

- Az elérhető `DbContext` típusok listája:

`dotnet ef dbcontext list`

- Kód generálása egy `DbContext` és egy adatbázis entitás típusaihoz:

`dotnet ef dbcontext scaffold {{connection_string}} {{provider}}`

- Új migráció hozzáadása:

`dotnet ef migrations add {{name}}`

- Az utolsó migráció eltávolítása, a legutóbbi migrációhoz elvégzett kódmódosítások visszaállítása:

`dotnet ef migrations remove`

- A rendelkezésre álló migrációk listája:

`dotnet ef migrations list`

- SQL-szkript generálása a migrációs tartományból:

`dotnet ef migrations script {{from_migration}} {{to_migration}}`
