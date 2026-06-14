# pygbag

> Փաթեթավորեք Pygame նախագծերը որպես WebAssembly՝ վեբ բրաուզերներում գործարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/pygame-web/pygbag#pygbag>:.

- Փաթեթավորեք Pygame նախագիծը և սկսեք տեղական թեստային սերվեր.:

`pygbag {{path/to/project_folder}}`

- Փաթեթ՝ օգտագործելով Python մոդուլի շարահյուսությունը.:

`python -m pygbag {{path/to/project_folder}}`

- Փաթեթավորեք և կառուցեք առանց փորձարկման սերվերը գործարկելու.:

`pygbag {{path/to/project_folder}} --build`

- Փաթեթ հատուկ ձևանմուշով.:

`pygbag {{path/to/project_folder}} --template {{template_name.tmpl}}`

- Փաթեթավորեք և ստեղծեք ZIP արխիվ <https://itch.io>-ի համար:

`pygbag {{path/to/project_folder}} --archive`

- Օպտիմալացումով փաթեթն անջատված է.:

`pygbag {{path/to/project_folder}} --no_opt`

- Նշեք հատուկ նավահանգիստ փորձարկման սերվերի համար.:

`pygbag {{path/to/project_folder}} --port {{8080}}`

- Ցուցադրել օգնությունը.:

`pygbag {{[-h|--help]}}`
