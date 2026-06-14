# tuc

> Կտրեք տեքստը (կամ բայթերը), որտեղ սահմանազատիչը համընկնում է, այնուհետև պահեք ցանկալի մասերը:.
> `cut`-ի ավելի հարմար և հզոր տարբերակ՝ խելամիտ լռելյայններով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/riquito/tuc#help>:.

- Կտրեք և վերադասավորեք դաշտերը.:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} '{{ }}' {{[-f|--fields]}} {{3,2,1}}`

- Փոխարինեք `space` սահմանազատիչը սլաքով.:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} ' ' {{[-r|--replace-delimiter]}} ' ➡ '`

- Պահպանեք մի շարք դաշտեր.:

`echo "foo bar    baz" | tuc {{[-d|--delimiter]}} ' ' {{[-f|--fields]}} {{2:}}`

- Կտրեք՝ օգտագործելով `regex`:

`echo "a,b, c" | tuc {{[-e|--regex]}} '{{[, ]+}}' {{[-f|--fields]}} {{1,3}}`

- Թողարկեք JSON ելք.:

`echo "foo bar baz" | tuc {{[-d|--delimiter]}} '{{ }}' --json`
