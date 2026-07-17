# flatpak run

> Esegue applicazioni flatpak e runtime.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- Esegue un'applicazione installata:

`flatpak run {{com.example.app}}`

- Esegue un'applicazione installata da un ramo specifico, ad es. stable, beta, master:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- Esegue una shell interattiva all'interno di un flatpak:

`flatpak run --command={{sh}} {{com.example.app}}`

- Esegue un'applicazione installata con una versione di runtime specifica:

`flatpak run --runtime-version={{24.08|master|stable|...}} {{com.example.app}}`

- Esegue un'applicazione installata con un runtime diverso (ma stesso numero di versione):

`flatpak run --runtime={{org.freedesktop.Sdk}} {{com.example.app}}`
