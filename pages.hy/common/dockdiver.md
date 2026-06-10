# նավամատույց

> Docker ռեգիստրների հետ փոխգործակցության գործիք, ներառյալ պահեստների ցուցակագրումը և թափոնը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/MachiavelliII/dockdiver#instructions>:.

- Թվարկեք բոլոր պահեստները Docker ռեգիստրում.:

`dockdiver -url {{https://example.com}} -list`

- Թափել որոշակի պահոց լռելյայն ելքային գրացուցակում (docker_dump):

`dockdiver -url {{https://example.com}} -dump {{repository_name}}`

- Թափել բոլոր պահեստները հիմնական իսկորոշմամբ.:

`dockdiver -url {{https://example.com}} -dump-all -username {{username}} -password {{password}}`

- Թափել շտեմարան սակագնի սահմանաչափով և հարմարեցված միացքով (կանխադրված նավահանգիստը `5000` է):

`dockdiver -url {{https://example.com}} -dump {{repository_name}} -port {{port}} -rate {{requests_per_second}} -dir {{path/to/output_directory}}`

- Թափել բոլոր պահեստարանները, որոնք ունեն կրող նշան՝ թույլտվության համար.:

`dockdiver -url {{https://example.com}} -dump-all -bearer {{bearer_token}}`

- Ավելացրեք հատուկ վերնագրեր որպես JSON (օրինակ՝ '{"X-Custom": "Value"}'):

`dockdiver -url {{https://example.com}} -list -headers '{{{"X-Custom": "Value"}}}'`
