# whatweb

> Next-generation web scanner.
> More information: <https://github.com/urbanadventurer/WhatWeb/>.

- Scan websites/targets for web technologies:

`whatweb {{website1 website2 ...}}`

- Read targets/websites from a file:

`whatweb {{[-i|--input-file]}} {{targets_file}}`

- Scan a website/target in verbose mode:

`whatweb {{[-v|--verbose]}} {{example.com}}`

- Run an aggressive scan on a website:

`whatweb {{[-a|--aggression]}} 3 {{example.com}}`

- Scan a network and suppress errors:

`whatweb --no-errors {{192.168.0.0/24}}`

- List plugins:

`whatweb {{[-l|--list-plugins]}}`

- List plugin details:

`whatweb {{[-I|--info-plugins]}} {{plugin_name}}`
