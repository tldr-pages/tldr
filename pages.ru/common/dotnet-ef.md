# dotnet ef

> Выполнять задачи разработки для Entity Framework Core.
> Больше информации: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- Обновить базу данных до указанной миграции:

`dotnet ef database update {{миграция}}`

- Удалить базу данных:

`dotnet ef database drop`

- Вывести список доступных типов `DbContext`:

`dotnet ef dbcontext list`

- Сгенерировать код для `DbContext` и типов сущностей на основе базы данных:

`dotnet ef dbcontext scaffold {{строка_подключения}} {{провайдер}}`

- Добавить новую миграцию:

`dotnet ef migrations add {{имя}}`

- Удалить последнюю миграцию, откатив изменения кода, сделанные для неё:

`dotnet ef migrations remove`

- Вывести список доступных миграций:

`dotnet ef migrations list`

- Сгенерировать SQL-скрипт из диапазона миграций:

`dotnet ef migrations script {{начальная_миграция}} {{конечная_миграция}}`
