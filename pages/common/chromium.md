# chromium

> Open-source web browser principally developed and maintained by Google.
> More information: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open a specific URL or file:

`chromium {{https://example.com|path/to/file.html}}`

- Open in incognito mode:

`chromium --incognito {{example.com}}`

- Open in a new window:

`chromium --new-window {{example.com}}`

- Open in application mode (without toolbars, URL bar, buttons, etc.):

`chromium --app={{https://example.com}}`

- Use a proxy server:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Open with a custom profile directory:

`chromium --user-data-dir={{path/to/directory}}`

- Open without CORS validation (useful to test an API):

`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- Open with a DevTools window for each tab opened:

`chromium --auto-open-devtools-for-tabs`
