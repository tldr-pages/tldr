# sg

> Ast-grep-ը գործիք է կոդի կառուցվածքային որոնման, ծածկույթի և վերաշարադրման համար:.
> Լրացուցիչ տեղեկություններ. <https://ast-grep.github.io/guide/introduction.html>:.

- Սկանավորեք հնարավոր հարցումները՝ օգտագործելով ինտերակտիվ ռեժիմը.:

`sg scan --interactive`

- Վերագրեք կոդը ընթացիկ գրացուցակում՝ օգտագործելով նախշերը.:

`sg run --pattern '{{foo}}' --rewrite '{{bar}}' --lang {{python}}`

- Պատկերացրեք հնարավոր փոփոխությունները՝ առանց դրանք կիրառելու.:

`sg run --pattern '{{useState<number>($A)}}' --rewrite '{{useState($A)}}' --lang {{typescript}}`

- Արդյունքները թողարկեք որպես JSON, հանեք տեղեկատվությունը `jq`-ի միջոցով և ինտերակտիվ կերպով դիտեք այն՝ օգտագործելով `jless`:

`sg run --pattern '{{Some($A)}}' --rewrite '{{None}}' --json | jq '{{.[].replacement}}' | jless`
