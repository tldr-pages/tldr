# hledger տպագիր

> Ցուցադրել ամսագրի ամբողջական գրառումները, որոնք ներկայացնում են գործարքները:.
> Լրացուցիչ տեղեկություններ. <https://hledger.org/hledger.html#print>:.

- Ցուցադրել բոլոր գործարքները լռելյայն ամսագրի ֆայլում.:

`hledger print`

- Ցուցադրել գործարքները՝ ցանկացած ենթադրյալ գումարներով կամ ծախսերով, որոնք բացահայտված են.:

`hledger print {{[-x|--explicit]}} --infer-costs`

- Ցուցադրել գործարքները երկու նշված ֆայլերից, որոնց գումարները փոխարկվում են արժեքի.:

`hledger print {{[-f|--file]}} {{path/to/2023.journal}} {{[-f|--file]}} {{path/to/2024.journal}} {{[-B|--cost]}}`

- Ցույց տալ `$` գործարքներն այս ամիս այն հաշիվներում, որոնց անունը պարունակում է `food`, բայց ոչ `groceries`:

`hledger print cur:\\$ food not:groceries date:thismonth`

- Ցույց տալ 50 և ավելի գումարի գործարքները, որոնց նկարագրության մեջ `whole foods` է.:

`hledger print amt:'>50' desc:'whole foods'`

- Ցույց տալ մաքրված գործարքները՝ `EUR` գումարներով կլորացված և տասնորդական ստորակետերով.:

`hledger print {{[-C|--cleared]}} --commodity '1000, EUR' --round hard`

- Գործարքները գրեք `foo.journal`-ից որպես CSV ֆայլ.:

`hledger print {{[-f|--file]}} {{path/to/foo.journal}} {{[-o|--output-file]}} {{path/to/output_file.csv}}`
