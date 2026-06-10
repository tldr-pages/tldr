# whatweb

> Հաջորդ սերնդի վեբ սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/urbanadventurer/WhatWeb#usage>:.

- Վեբ տեխնոլոգիաների համար կայքերի/թիրախների սկանավորում.:

`whatweb {{website1 website2 ...}}`

- Կարդացեք թիրախները/վեբ կայքերը ֆայլից.:

`whatweb {{[-i|--input-file]}} {{targets_file}}`

- Սկանավորեք կայք/թիրախը մանրամասն ռեժիմով.:

`whatweb {{[-v|--verbose]}} {{example.com}}`

- Կայքում ագրեսիվ սկանավորում կատարեք.:

`whatweb {{[-a|--aggression]}} 3 {{example.com}}`

- Սկանավորեք ցանցը և ճնշեք սխալները.:

`whatweb --no-errors {{192.168.0.0/24}}`

- Ցուցակ պլագիններ.:

`whatweb {{[-l|--list-plugins]}}`

- Ցուցակեք հավելվածի մանրամասները.:

`whatweb {{[-I|--info-plugins]}} {{plugin_name}}`
