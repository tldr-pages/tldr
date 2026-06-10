# phpmd

> PHP խառնաշփոթ դետեկտոր. ստուգեք ընդհանուր հնարավոր խնդիրների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/phpmd/phpmd#command-line-options>:.

- Ցուցադրել հասանելի կանոնակարգերի և ձևաչափերի ցանկը.:

`phpmd`

- Սկանավորեք ֆայլը կամ գրացուցակը ստորակետերով բաժանված կանոնների օգտագործմամբ խնդիրների համար.:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}}`

- Նշեք կանոնների նվազագույն առաջնահերթության շեմը.:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --minimumpriority {{priority}}`

- Վերլուծության մեջ ներառեք միայն նշված ընդլայնումները.:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --suffixes {{extensions}}`

- Բացառեք նշված ստորակետերով առանձնացված գրացուցակները.:

`phpmd {{path/to/file_or_directory1,path/to/file_or_directory2,...}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --exclude {{directory_patterns}}`

- Արդյունքները թողարկեք ֆայլ՝ `stdout`-ի փոխարեն:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --reportfile {{path/to/report_file}}`

- Անտեսեք նախազգուշացնող PHPDoc մեկնաբանությունների օգտագործումը.:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --strict`
