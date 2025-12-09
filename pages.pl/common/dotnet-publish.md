# dotnet publish

> Opublikuj aplikację .NET i jej zależności w celu wdrożenia na docelowym systemie.
> Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Opublikuj projekt w konfiguracji wydania:

`dotnet publish --configuration Release {{ścieżka/do/projektu_lub_solucji}}`

- Opublikuj projekt z dołączonym wybranym środowiskiem uruchomieniowym:

`dotnet publish --self-contained true --runtime {{identyfikator_runtime}} {{ścieżka/do/projektu_lub_solucji}}`

- Zapakuj aplikację do pojedyńczego pliku uruchomieniowego dla konkretnej platformy:

`dotnet publish --runtime {{identyfikator_runtime}} -p:PublishSingleFile=true {{ścieżka/do/projektu_lub_solucji}}`

- Pomiń nieużywane biblioteki aby obniżyć rozmiar wdrażanej aplikacji:

`dotnet publish --self-contained true --runtime {{identyfikator_runtime}} -p:PublishTrimmed=true {{ścieżka/do/projektu_lub_solucji}}`

- Kompiluj projekt bez przywracania zależności:

`dotnet publish --no-restore {{ścieżka/do/projektu_lub_solucji}}`

- Wybierz katalog docelowy:

`dotnet publish --output {{ściezka/do/katalogu}} {{ścieżka/do/projektu_lub_solucji}}`
