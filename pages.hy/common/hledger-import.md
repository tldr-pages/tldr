# hledger ներմուծում

> Ներմուծեք նոր գործարքներ մեկ կամ մի քանի տվյալների ֆայլերից հիմնական ամսագիր:.
> Լրացուցիչ տեղեկություններ. <https://hledger.org/hledger.html#import>:.

- Ներմուծեք նոր գործարքներ `bank.csv`-ից՝ օգտագործելով `bank.csv.rules`՝ փոխարկելու համար՝:

`hledger import {{path/to/bank.csv}}`

- Ցույց տվեք, թե ինչ կներմուծվի այս երկու ֆայլերից՝ առանց որևէ բան անելու.:

`hledger import {{path/to/bank1.csv}} {{path/to/bank2.csv}} --dry-run`

- Ներմուծեք նոր գործարքներ բոլոր CSV ֆայլերից՝ օգտագործելով նույն կանոնները բոլորի համար.:

`hledger import --rules-file {{common.rules}} *.csv`

- Ցույց տալ փոխակերպման սխալները կամ արդյունքները `bank.csv.rules`-ը խմբագրելիս:

`watchexec -- hledger {{[-f|--file]}} {{path/to/bank.csv}} print`

- Նշեք `bank.csv`-ի ընթացիկ տվյալները, ինչպես երևում է, կարծես արդեն ներմուծված է.:

`hledger import --catchup {{path/to/bank.csv}}`

- Նշեք `bank.csv`-ը որպես բոլորովին նոր, կարծես դեռ ներմուծված չէ:

`rm {{[-f|--force]}} .latest.bank.csv`
