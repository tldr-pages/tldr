# lighthouse

> Analyzes web applications and web pages, collecting modern performance metrics and insights on developer best practices.
> More information: <https://github.com/GoogleChrome/lighthouse>.

- Generate an HTML report for a specific website and save it to a file in the current directory:

`lighthouse {{https://example.com}}`

- Generate a JSON report and print it:

`lighthouse --output {{json}} {{https://example.com}}`

- Generate a JSON report and save it to a specific file:

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- Generate a report using the browser in headless mode without logging to `stdout`:

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- Generate a report, using the HTTP header key/value pairs in the specified JSON file for all requests:

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- Generate a report for specific categories only:

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- Generate a report with device emulation and all throttling disabled:

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- Display help:

`lighthouse --help`
