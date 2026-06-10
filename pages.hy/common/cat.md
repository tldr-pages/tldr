# կատու

> Տպել և միացնել ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/cat.1posix>:.

- Տպեք ֆայլի բովանդակությունը `stdout`-ում՝:

`cat {{path/to/file}}`

- Միացրեք մի քանի ֆայլ ելքային ֆայլի մեջ.:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- Մի քանի ֆայլ միացրեք ելքային ֆայլին.:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- Պատճենեք ֆայլի բովանդակությունը ելքային ֆայլում՝ առանց բուֆերացման.:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Ֆայլում գրեք `stdin`.:

`cat - > {{path/to/file}}`
