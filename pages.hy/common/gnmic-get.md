# gnmic ստանալ

> Ստացեք gnmi ցանցային սարքի շահագործման տվյալների պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://gnmic.openconfig.net/cmd/get/>:.

- Ստացեք սարքի վիճակի պատկերը որոշակի ուղու վրա.:

`gnmic {{[-a|--address]}} {{ip:port}} get --path {{path}}`

- Հարցրեք սարքի վիճակը մի քանի ուղիներով.:

`gnmic {{[-a|--address]}} {{ip:port}} get --path {{path/to/file_or_directory1}} --path {{path/to/file_or_directory2}}`

- Հարցրեք սարքի վիճակը մի քանի ուղիներով ընդհանուր նախածանցով.:

`gnmic {{[-a|--address]}} {{ip:port}} get --prefix {{prefix}} --path {{path/to/file_or_directory1}} --path {{path/to/file_or_directory2}}`

- Հարցրեք սարքի վիճակը և նշեք պատասխանի կոդավորումը (json_ietf):

`gnmic {{[-a|--address]}} {{ip:port}} get --path {{path}} {{[-e|--encoding]}} json_ietf`
