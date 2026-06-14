#խոպան

> SOPS (Secrets operationS). պարզ և ճկուն գործիք գաղտնիքները կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/getsops/sops>:.

- Գաղտնագրեք ֆայլը.:

`sops -e {{path/to/file.json}} > {{path/to/file.enc.json}}`

- Ֆայլի վերծանումը՝ `stdout`:

`sops -d {{path/to/file.enc.json}}`

- Թարմացրեք հայտարարված բանալիները `sops` ֆայլում՝:

`sops updatekeys {{path/to/file.enc.yaml}}`

- Պտտեցնել տվյալների բանալիները `sops` ֆայլի համար.:

`sops -r {{path/to/file.enc.yaml}}`

- Փոխեք ֆայլի ընդլայնումը գաղտնագրվելուց հետո.:

`sops -d --input-type json {{path/to/file.enc.json}}`

- Քաղեք ստեղները՝ անվանելով դրանք, և զանգվածի տարրերը՝ համարակալելով դրանք.:

`sops -d --extract '["an_array"][1]' {{path/to/file.enc.json}}`

- Ցույց տալ տարբերությունը երկու `sops` ֆայլերի միջև.:

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`
