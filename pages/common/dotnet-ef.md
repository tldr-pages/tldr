# dotnet ef

> Perform design-time development tasks for Entity Framework Core.
> More information: <https://docs.microsoft.com/ef/core/cli/dotnet>.

- Update the database to a specified migration:

`dotnet ef database update`

- Drop the database:

`dotnet ef database drop`

- List available `DbContext` types:

`dotnet ef dbcontext list`

- Generate code for a `DbContext` and entity types for a database:

`dotnet ef dbcontext scaffold`

- Add a new migration:

`dotnet ef migrations add`

- Remove the last migration, rolling back the code changes that were done for the latest migration:

`dotnet ef migrations remove`

- List available migrations:

`dotnet ef migrations list`

- Generate a SQL script from migrations:

`dotnet ef migrations script`
