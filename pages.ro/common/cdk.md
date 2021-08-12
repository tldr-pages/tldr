# cdk

> Un CLI pentru AWS Cloud Development Kit (CDK).
> Mai multe informaţii: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>

- Listează stivele din aplicație:

`cdk ls`

- Sintetizați și imprimați șablonul CloudForformation pentru stivele specificate:

`cdk synth {{stack_name}}`

- Implementați o listă de stive separate de spațiu:

`cdk deploy {{stack_name}}`

- Distruge o listă de stive separate de spațiu:

`cdk destroy {{stack_name}}`

- Comparați stiva specificată cu stiva implementată sau un șablon local CloudFormation:

`cdk diff {{stack_name}}`

- Creați un nou proiect CDK în directorul curent pentru o limbă specificată:

`cdk init -l {{language_name}}`

- Deschideți referința CDK API în browser-ul dvs.:

`cdk doc`
