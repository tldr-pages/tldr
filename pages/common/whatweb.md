# whatweb

> Next-generation web scanner.
> More information: <https://morningstarsecurity.com/research/whatweb>.

- Scan websites/targets for web technologies:

`whatweb {{website1 website2 ...}}`

- Read targets/websites from a file:

`whatweb -i {{targets_file}}`

- Scan a website/target in verbose mode:

`whatweb -v {{example.com}}`

- Run an aggressive scan on a website:

`whatweb -a 3 {{example.com}}`

- Scan a network and suppress errors:

`whatweb --no-errors {{192.168.0.0/24}}`

- List plugins:

`whatweb -l`

- List plugin details:

`whatweb -I {{plugin_name}}`
