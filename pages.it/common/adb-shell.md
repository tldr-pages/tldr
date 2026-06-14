# adb shell

> Esegue comandi shell su un dispositivo o emulatoro Android connesso.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Avvia un shell interattivo remoto sull'emulatore o dispositivo:

`adb shell`

- Visualizza la documentazione per mostrare le proprietà di sistema Android:

`tldr {{[-p|--platform]}} android getprop`

- Visualizza la documentazione per il package manager Android:

`tldr {{[-p|--platform]}} android pm`

- Visualizza la documentazione per inviare codici di evento e eventi del touchscreen:

`tldr {{[-p|--platform]}} android input`

- Visualizza la documentazione per l'activity manager Android:

`tldr {{[-p|--platform]}} android am`

- Elenca i comandi shell Android documentati:

`tldr {{[-p|--platform]}} android {{[-l|--list]}}`
