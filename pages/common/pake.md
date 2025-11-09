# pake

> Turn any webpage into a desktop app with Rust/Tauri.
> More information: <https://github.com/tw93/Pake>.

- Package a web page:

`pake {{https://www.example.com/}}`

- Package a web page with a specific window size:

`pake --width {{800}} --height {{600}} {{https://www.example.com/}}`

- Package a web page with a custom application name and icon:

`pake --name {{application_name}} --icon {{path/to/icon.ico}} {{https://www.example.com/}}`

- Package a web page with a non-resizable window:

`pake --no-resizable {{https://www.example.com/}}`

- Package a web page with fullscreen mode:

`pake --fullscreen {{https://www.example.com/}}`

- Package a web page with a transparent title bar:

`pake --transparent {{https://www.example.com/}}`
