# docker մուտք

> Մուտք գործեք Docker ռեեստր:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/login/>:.

- Ինտերակտիվ կերպով մուտք գործեք ռեեստր.:

`docker login`

- Մուտք գործեք գրանցամատյան հատուկ օգտվողի անունով (օգտատիրոջը կառաջարկվի գաղտնաբառ).:

`docker login {{[-u|--username]}} {{username}}`

- Մուտք գործեք գրանցամատյան օգտանունով և գաղտնաբառով.:

`docker login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} {{server}}`

- Մուտք գործեք գրանցամատյան՝ `stdin`-ից գաղտնաբառով.:

`echo "{{password}}" | docker login {{[-u|--username]}} {{username}} --password-stdin`
