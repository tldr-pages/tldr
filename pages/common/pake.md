# pake

> Turn any webpage into a desktop app with Rust/Tauri.
> More information: <https://github.com/tw93/Pake>.

- Package a web page:

`pake {{https://www.google.com/}}`

- Package a web page with specific window size:

`pake --width {{800}} --height {{600}} {{https://www.google.com/}}`

- Package a web page with a custom application name and icon:

`pake --name "Google" --icon "path/to/icon.ico" https://www.google.com/`

- Package a web page with non-resizable window:

`pake --no-resizable {{https://www.google.com/}}`

- Package a web page with fullscreen mode:

`pake --fullscreen {{https://www.google.com/}}`

- Package a web page with transparent title bar:

`pake --transparent {{https://www.google.com/}}`
