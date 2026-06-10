#հանդիսանալ

> Բազմապատկերային տողերի փոխարինում և ֆայլերի վերանվանման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jlevy/repren>:.

- Կատարեք չոր գործարկում՝ վերանվանելով PNG-ների գրացուցակը բառացի տողի փոխարինմամբ.:

`repren {{[-n|--dry-run]}} --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- Կատարեք չոր գործարկում՝ վերանվանելով JPEG-ների գրացուցակը `regex`-ով:

`repren --rename {{[-n|--dry-run]}} --from '{{regex}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- Գտեք և փոխարինեք CSV ֆայլերի գրացուցակի բովանդակությունը.:

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- Միևնույն ժամանակ կատարեք ինչպես «գտնել և փոխարինել», այնպես էլ վերանվանել գործողությունը՝ օգտագործելով օրինաչափության ֆայլը.:

`repren {{[-p|--patterns]}} {{path/to/patfile.ext}} --full {{*.txt}}`

- Վերանվանել մեծատառերի անզգույշ՝:

`repren --rename {{[-i|--insensitive]}} {{[-p|--patterns]}} {{path/to/patfile.ext}} *`
