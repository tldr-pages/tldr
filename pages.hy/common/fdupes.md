# fdupes

> Գտնում է կրկնօրինակ ֆայլեր մի շարք գրացուցակներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/adrianlopezroche/fdupes#introduction>:.

- Որոնեք մեկ գրացուցակ.:

`fdupes {{path/to/directory}}`

- Որոնեք բազմաթիվ դիրեկտորիաներ.:

`fdupes {{path/to/directory1 path/to/directory2 ...}}`

- Որոնել գրացուցակը ռեկուրսիվ կերպով.:

`fdupes {{[-r|--recurse]}} {{path/to/directory}}`

- Որոնեք բազմաթիվ դիրեկտորիաներ, մեկը՝ ռեկուրսիվ.:

`fdupes {{path/to/directory1}} {{[-R|--recurse:]}} {{path/to/directory2}}`

- Որոնեք ռեկուրսիվորեն՝ համարելով կոշտ հղումները որպես կրկնօրինակներ.:

`fdupes {{[-rH|--recurse --hardlinks]}} {{path/to/directory}}`

- Ռեկուրսիվորեն փնտրեք կրկնօրինակներ և ցուցադրեք ինտերակտիվ հուշում, որպեսզի ընտրեք, թե որոնք պետք է պահեք՝ ջնջելով մյուսները.:

`fdupes {{[-rd|--recurse --delete]}} {{path/to/directory}}`

- Որոնեք ռեկուրսիվ և ջնջեք կրկնօրինակները՝ առանց հուշելու.:

`fdupes {{[-rdN|--recurse --delete --noprompt]}} {{path/to/directory}}`
