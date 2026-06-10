# phpstan

> PHP ստատիկ վերլուծության գործիք կոդի մեջ սխալներ հայտնաբերելու համար:.
> Լրացուցիչ տեղեկություններ. <https://phpstan.org/user-guide/command-line-usage>:.

- Վերլուծեք մեկ կամ մի քանի գրացուցակներ.:

`phpstan analyse {{path/to/directory1 path/to/directory2 ...}}`

- Վերլուծեք գրացուցակը, օգտագործելով կազմաձևման ֆայլը.:

`phpstan analyse {{path/to/directory}} {{[-c|--configuration]}} {{path/to/config}}`

- Վերլուծեք՝ օգտագործելով կանոնների հատուկ մակարդակ (0-10, ավելի բարձր՝ ավելի խիստ).:

`phpstan analyse {{path/to/directory}} {{[-l|--level]}} {{level}}`

- Նշեք ավտոմատ բեռնման ֆայլ, որը պետք է բեռնվի վերլուծելուց առաջ.:

`phpstan analyse {{path/to/directory}} {{[-a|--autoload-file]}} {{path/to/autoload_file}}`

- Վերլուծության ընթացքում նշեք հիշողության սահմանաչափը.:

`phpstan analyse {{path/to/directory}} --memory-limit {{memory_limit}}`

- Ցուցադրել վերլուծության համար առկա տարբերակները.:

`phpstan analyse --help`
