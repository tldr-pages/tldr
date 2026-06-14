# cdk

> AWS Cloud Development Kit:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>:.

- Թվարկեք կույտերը հավելվածում.:

`cdk ls`

- Սինթեզեք և տպեք CloudFormation ձևանմուշը նշված կույտ(ների) համար.:

`cdk synth {{stack_name}}`

- Տեղադրեք մեկ կամ մի քանի կույտ.:

`cdk deploy {{stack_name1 stack_name2 ...}}`

- Ոչնչացնել մեկ կամ մի քանի կույտեր.:

`cdk destroy {{stack_name1 stack_name2 ...}}`

- Համեմատեք նշված կույտը տեղակայված կույտի կամ տեղական CloudFormation ձևանմուշի հետ.:

`cdk diff {{stack_name}}`

- Ստեղծեք նոր CDK նախագիծ ընթացիկ գրացուցակում նշված լեզվի համար.:

`cdk init {{[-l|--language]}} {{language}}`

- Բացեք CDK API հղումը ձեր բրաուզերում.:

`cdk docs`
