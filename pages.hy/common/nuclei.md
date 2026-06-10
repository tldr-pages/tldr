# միջուկներ

> Արագ և կարգավորելի խոցելիության սկաներ՝ օգտագործելով YAML-ի վրա հիմնված պարզ DSL:.
> Լրացուցիչ տեղեկություններ. <https://docs.projectdiscovery.io/opensource/nuclei/running>:.

- Թարմացրեք `nuclei` ձևանմուշները վերջին թողարկված տարբերակով (ներբեռնված է `~/nuclei-templates` macOS/Linux-ով կամ `%USERPROFILE%\nuclei-templates` Windows-ով):

`nuclei {{[-ut|-update-templates]}}`

- [l] թվարկեք բոլոր [t] ձևանմուշները ըստ հատուկ [p] արձանագրության [t] տեսակի.:

`nuclei -tl {{[-pt|-type]}} {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Գործարկեք ավտոմատ վեբ սկանավորում՝ օգտագործելով Wappalyzer տեխնոլոգիայի հայտնաբերումը կոնկրետ թիրախի [u]RL/հյուրընկալողի համար.:

`nuclei {{[-as|-automatic-scan]}} {{[-u|-target]}} {{example.com}}`

- Գործարկեք HTTP [p]rotocol [t]ype կաղապարներ հատուկ խստության, արտահանելով արդյունքները նշվող ֆայլեր որոշակի գրացուցակի ներսում.:

`nuclei {{[-s|-severity]}} {{high,critical,...}} {{[-pt|-type]}} http {{[-u|-target]}} {{https://example.com}} {{[-me|-markdown-export]}} {{path/to/directory}}`

- Գործարկեք բոլոր ձևանմուշները հատուկ դրույքաչափի սահմանաչափով, առավելագույն զանգվածային չափով և լուռ արդյունքով (ցուցադրված են միայն բացահայտումները).:

`nuclei {{[-rl|-rate-limit]}} {{150}} {{[-bs|-bulk-size]}} {{25}} {{[-c|-concurrency]}} {{25}} -silent {{[-u|-target]}} {{https://example.com}}`

- Գործարկել հատուկ միջուկներով փաթեթավորված աշխատանքային հոսք թիրախի դեմ.:

`nuclei {{[-w|-workflows]}} {{workflows/wordpress-workflow.yaml}} {{[-u|-target]}} {{https://example.com}}`

- Գործարկեք մեկ կամ մի քանի հատուկ ձևանմուշներ կամ գրացուցակներ `stderr`-ում մանրամասն ելքով ձևանմուշներով և հայտնաբերված խնդիրներ/խոցելիություններ դուրս բերեք ֆայլում՝:

`nuclei {{[-t|-templates]}} {{path/to/nuclei-templates/http}} {{[-u|-target]}} {{https://example.com}} {{[-v|-verbose]}} {{[-o|-output]}} {{path/to/results}}`

- Օգտագործեք AI հուշում` թիրախը սկանավորելու համար դինամիկ ձևանմուշ ստեղծելու համար (projectdiscovery cloud pdcp API բանալին պետք է կազմաձևվի `nuclei -auth`-ի միջոցով):

`nuclei {{[-u|-target]}} {{https://example.com}} {{[-ai|-prompt]}} "{{find admin login endpoints}}"`
