# csvtool

> Կոմունալ՝ CSV ձևաչափված աղբյուրներից տվյալների զտման և արդյունահանման համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/maroofi/csvtool>:.

- Արտահանեք երկրորդ սյունակը CSV ֆայլից.:

`csvtool {{[-c|--column]}} {{2}} {{path/to/file.csv}}`

- CSV ֆայլից հանեք երկրորդ և չորրորդ սյունակները.:

`csvtool {{[-c|--column]}} {{2,4}} {{path/to/file.csv}}`

- Քաղեք տողեր CSV ֆայլից, որտեղ երկրորդ սյունակը ճիշտ համընկնում է `String`-ի հետ:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{^String$}}' {{path/to/file.csv}}`

- Տողեր հանեք CSV ֆայլից, որտեղ երկրորդ սյունակը սկսվում է `Bar`-ով:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{^Bar}}' {{path/to/file.csv}}`

- Գտեք տողեր CSV ֆայլում, որտեղ երկրորդ սյունակը ավարտվում է `Baz`-ով, այնուհետև հանեք երրորդ և վեցերորդ սյունակները.:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{Baz$}}' {{path/to/file.csv}} | csvtool {{[-e|--no-header]}} {{[-c|--column]}} {{3,6}}`
