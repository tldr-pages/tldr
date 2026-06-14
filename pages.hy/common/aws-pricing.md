# aws-ի գներ

> Հարցման ծառայություններ, ապրանքներ և գնային տեղեկատվություն Amazon Web Services-ից:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/pricing/>:.

- Նշեք որոշակի տարածաշրջանի սպասարկման կոդերը.:

`aws pricing describe-services --region {{us-east-1}}`

- Թվարկեք ատրիբուտները տվյալ ծառայության կոդի համար որոշակի տարածաշրջանում.:

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Տպել գնային տեղեկատվությունը որոշակի տարածաշրջանում սպասարկման կոդի համար.:

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Նշեք արժեքները որոշակի հատկանիշի համար որոշակի տարածաշրջանում սպասարկման կոդի համար.:

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- Տպել գնային տեղեկատվությունը ծառայության կոդի համար՝ օգտագործելով զտիչներ, օրինակ՝ տեսակը և գտնվելու վայրը.:

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`
