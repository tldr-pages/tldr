# firefox

> A free and open source web browser.
> More information at https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options.

- Open firefox at www.duckduckgo.com:

`firefox {{https://www.duckduckgo.com}}`

- Open it at a new window:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Open an incognito window:

`firefox --private-window`

- Search 'wikipedia' on your default search engine:

`firefox --search {{wikipedia}}`

- Launch firefox without extensions:

`firefox --safe-mode`

- Take a screenshot of a web page in headless mode:

`firefox --headless --screenshot {{path/to/output_file.png}}  {{https://example.com/}}`

- Use a specific profile directory to allow multiple separate instances of Firefox to run at once:

`firefox --new-instance --profile {{path/to/directory}} {{https://example.com/}}`
