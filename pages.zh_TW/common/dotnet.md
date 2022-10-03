# dotnet

> 適用於 .NET Core 的跨平台 .NET 命令列工具。
> 此命令也有關於其子命令的文件，例如：`dotnet build`.
> 更多資訊：<https://learn.microsoft.com/dotnet/core/tools/>.

- 初始化一個新的 .NET 專案：

`dotnet new {{模板名稱}}`

- 還原 NuGet 套件：

`dotnet restore`

- 在當前目錄中構建並執行 .NET 項目：

`dotnet run`

- 運行 .NET 應用程式（只需要執行環境，其餘命令需要 .NET Core SDK）:

`dotnet {{路徑/到/應用程式.dll}}`
