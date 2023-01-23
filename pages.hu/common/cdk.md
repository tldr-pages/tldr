# cdk

> CLI az AWS Cloud Development Kit (CDK) számára. További információ: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- Sorolja fel a stackeket az alkalmazásban:

`cdk ls`

- A megadott verem(ek) CloudFormation sablonjának szintetizálása és kinyomtatása:

`cdk synth {{stack_name}}`

- Telepítse a stackek szóközzel elválasztott listáját:

`cdk deploy {{stack_name}}`

- Megsemmisíti a vermek szóközzel elválasztott listáját:

`cdk destroy {{stack_name}}`

- A megadott verem összehasonlítása a telepített veremmel vagy egy helyi CloudFormation-sablonnal:

`cdk diff {{stack_name}}`

- Új CDK-projekt létrehozása az aktuális könyvtárban egy megadott nyelvhez:

`cdk init -l {{language_name}}`

- A CDK API-hivatkozás megnyitása a böngészőben:

`cdk docs`
