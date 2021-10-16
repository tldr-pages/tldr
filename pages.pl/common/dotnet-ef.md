# dotnet ef

> Narzędzia projektowania dla Entity Framework Core.
> Więcej informacji: <https://docs.microsoft.com/ef/core/cli/dotnet>.

- Zaaktualizuj bazę danych do wybranej migracji:

`dotnet ef database update {{migration}}`

- Wyczyść bazę danych:

`dotnet ef database drop`

- Wyświetl dostępne `DbContext`:

`dotnet ef dbcontext list`

- Wygeneruj kod dla `DbContext` oraz typów encji bazy danych:

`dotnet ef dbcontext scaffold {{connection_string}} {{provider}}`

- Dodaj nową migrację:

`dotnet ef migrations add {{name}}`

- Usuń poprzednią migrację, cofa zmiany w kodzie stworzone dla poprzedniej migracji:

`dotnet ef migrations remove`

- Wyświetl dostępne migracje:

`dotnet ef migrations list`

- Wygeneruj skrypt SQL dla zakresu migracji:

`dotnet ef migrations script {{from_migration}} {{to_migration}}`
