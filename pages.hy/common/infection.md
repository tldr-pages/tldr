#վարակ

> PHP-ի մուտացիայի փորձարկման շրջանակ:.
> Լրացուցիչ տեղեկություններ. <https://infection.github.io/guide/command-line-options.html>:.

- Վերլուծեք կոդը՝ օգտագործելով կազմաձևման ֆայլը (կամ ստեղծեք մեկը, եթե այն գոյություն չունի).:

`infection`

- Օգտագործեք որոշակի քանակությամբ թելեր.:

`infection {{[-j|--threads]}} {{number_of_threads}}`

- Նշեք նվազագույն մուտացիայի միավորի ցուցիչ (MSI):

`infection --min-msi {{percentage}}`

- Նշեք MSI ծածկված նվազագույն ծածկագիրը.:

`infection --min-covered-msi {{percentage}}`

- Օգտագործեք հատուկ թեստային շրջանակ (կանխադրված է PHPUnit):

`infection --test-framework {{phpunit|phpspec}}`

- Փոխեք միայն կոդերի տողերը, որոնք ծածկված են թեստերով.:

`infection --only-covered`

- Ցուցադրել մուտացիայի կոդը, որը կիրառվել է.:

`infection {{[-s|--show-mutations]}}`

- Նշեք մատյանների խոսակցականությունը.:

`infection --log-verbosity {{default|all|none}}`
