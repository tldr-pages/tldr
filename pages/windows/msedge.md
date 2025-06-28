# msedge

> Modern web browser developed by Microsoft based on the Chromium web browser developed by Google.
> This command is available instead as `microsoft-edge` for other platforms.
> Note: Additional command arguments from `chromium` may also be usable to control Microsoft Edge.
> More information: <https://microsoft.com/edge>.

- Open a specific URL or file:

`msedge {{https://example.com|path/to/file.html}}`

- Open in InPrivate mode:

`msedge --inprivate {{example.com}}`

- Open in a new window:

`msedge --new-window {{example.com}}`

- Open in application mode (without toolbars, URL bar, buttons, etc.):

`msedge --app {{https://example.com}}`

- Use a proxy server:

`msedge --proxy-server "{{socks5://hostname:66}}" {{example.com}}`

- Open with a custom profile directory:

`msedge --user-data-dir {{path/to/directory}}`

- Open without CORS validation (useful to test an API):

`msedge --user-data-dir {{path/to/directory}} --disable-web-security`

- Open with a DevTools window for each tab opened:

`msedge --auto-open-devtools-for-tabs`
