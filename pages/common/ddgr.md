# ddgr

> ddgr is a cmdline utility to search DuckDuckGo (html version) from the terminal.
> More information: <https://github.com/jarun/ddg>

- To initiate an interactive mode:

`ddgr`

- Search DuckDuckGo for a keyword:

`ddgr {{keyword}}`

- To limit the search results number:

`ddgr -n {{N}} {{keyword}}`

- To show complete URL in search results:

`ddgr -x {{keyword}}`

- Search DuckDuckGo for a keyword and open the first result in a browser:

`ddgr !w {{keyword}}`

<!-- bash-specific, need to escape ! on bash -->
`ddgr \!w {{keyword}}`

- Website specific search:

`ddgr -w {{site}} {{keyword}}`

- Search for a specific file type:

`ddgr {{keyword}} filetype:{{filetype}}`

- Region specific search:

`ddgr -r {{region}} {{keyword}}`

Regions can be found at <https://duckduckgo.com/duckduckgo-help-pages/settings/params/>

- For more help in interactive mode:

`?`
