# iexplore

> Microsoft Internet Explorer.
> Note: This command is deprecated and no longer maintained, use modern browsers like `msedge` instead.
> More information: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/general-info/hh826025(v=vs.85)>.

- Open a specific URL or file:

`iexplore {{https://example.com|path\to\file.html}}`

- Open in InPrivate mode:

`iexplore -private {{example.com}}`

- Open in [k]iosk/application mode (without toolbars, URL bar, buttons, etc.):

`iexplore -k {{example.com}}`

- Open with [ext]ensions/add-ons disabled:

`iexplore -extoff {{example.com}}`
