# hledger եկամուտների հաշվետվություն

> Ցույց տալ եկամուտների ներհոսքերը և ծախսերի ելքերը հաշվետու ժամանակաշրջանում:.
> Գումարները ցուցադրվում են նորմալ դրական նշանով, ինչպես սովորական ֆինանսական հաշվետվություններում:.
> Լրացուցիչ տեղեկություններ. <https://hledger.org/hledger.html#incomestatement>:.

- Ցույց տալ եկամուտներն ու ծախսերը (փոփոխություններ `Revenue` և `Expense` հաշիվներում).:

`hledger {{[is|incomestatement]}}`

- Ցույց տալ եկամուտներն ու ծախսերը ամեն ամիս.:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}}`

- Ցուցադրել ամսական եկամուտները/ծախսերը/ընդհանուրները, առաջինը՝ ամենամեծը, ամփոփված 2 մակարդակի վրա.:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}}`

- Նույնը, ինչ վերևում, և ստեղծեք HTML ելք `is.html`-ում:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}} {{[-o|--output-file]}} is.html`
