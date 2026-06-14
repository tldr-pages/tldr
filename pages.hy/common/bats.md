# չղջիկներ

> Bash ավտոմատացված թեստավորման համակարգ. TAP (<https://testanything.org/>) համապատասխանող փորձարկման շրջանակ Bash-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://bats-core.readthedocs.io/en/stable/usage.html>:.

- Գործարկեք BATS թեստի սցենարը և արդյունքները թողարկեք TAP (Test Anything Protocol) ձևաչափով.:

`bats {{[-t|--tap]}} {{path/to/test.bats}}`

- Հաշվեք թեստային սցենարի թեստային դեպքերը, առանց որևէ թեստ գործարկելու.:

`bats {{[-c|--count]}} {{path/to/test.bats}}`

- Գործարկել BATS թեստային դեպքերը ռեկուրսիվ (`.bats` ընդլայնումով ֆայլեր).:

`bats {{[-r|--recursive]}} {{path/to/directory}}`

- Արդյունքների արդյունքները որոշակի ձևաչափով.:

`bats {{[-F|--formatter]}} {{pretty|tap|tap13|junit}} {{path/to/test.bats}}`

- Թեստերին ավելացրեք ժամանակային տեղեկատվություն.:

`bats {{[-T|--timing]}} {{path/to/test.bats}}`

- Զուգահեռաբար գործարկեք որոշակի թվով աշխատատեղեր (տեղադրելու համար պահանջվում է GNU `parallel`):

`bats {{[-j|--jobs]}} {{number}} {{path/to/test.bats}}`
