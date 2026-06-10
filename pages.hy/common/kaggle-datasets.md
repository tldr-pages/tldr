# kaggle տվյալների հավաքածու

> Կառավարեք Kaggle տվյալների հավաքածուները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>:.

- Թվարկեք բոլոր տվյալների հավաքածուները, որոնք պատկանում են օգտվողին կամ կազմակերպությանը.:

`kaggle {{[d|datasets]}} list --user {{username}}`

- Որոնել տվյալների հավաքածուն ըստ անունով.:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} "{{dataset_name}}"`

- Ներբեռնեք տվյալների հավաքածու.:

`kaggle {{[d|datasets]}} download "{{dataset_name}}"`

- Ստեղծեք հանրային տվյալների բազա.:

`kaggle {{[d|datasets]}} create {{[-p|--path]}} {{path/to/dataset}} {{[-u|--public]}}`

- Ներբեռնեք տվյալների բազայի մետատվյալները.:

`kaggle {{[d|datasets]}} metadata {{dataset_name}}`

- Նախաձեռնել մետատվյալները տվյալների բազայի համար.:

`kaggle {{[d|datasets]}} init {{[-p|--path]}} {{path/to/dataset}}`

- Ջնջել տվյալների հավաքածու.:

`kaggle {{[d|datasets]}} delete {{dataset_name}}`
