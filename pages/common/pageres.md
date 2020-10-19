# pageres

> Capture screenshots of websites in various resolutions.
> More information: <https://github.com/sindresorhus/pageres-cli>.

- Take multiple screenshots of multiple URLs at different resolutions:

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- Provide specific options for a URL, overriding global options:

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop`

- Provide a custom filename template:

`pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}`

- Capture a specific element on a page:

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- Hide a specific element:

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- Capture a screenshot of a local file:

`pageres {{local_file_path.html}} {{1366x768}}`
