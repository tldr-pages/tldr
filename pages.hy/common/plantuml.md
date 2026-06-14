# plantuml

> Ստեղծեք UML դիագրամներ պարզ տեքստի լեզվից և դրանք ներկայացրեք տարբեր ձևաչափերով:.
> Լրացուցիչ տեղեկություններ. <https://plantuml.com/en/command-line>:.

- Տրամադրել դիագրամները լռելյայն ձևաչափով (PNG).:

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- Ներկայացրեք դիագրամը տրված ձևաչափով (օրինակ՝ `png`, `pdf`, `svg`, `txt`):

`plantuml -t {{format}} {{diagram.puml}}`

- Ներկայացրեք գրացուցակի բոլոր դիագրամները.:

`plantuml {{path/to/diagrams}}`

- Դիագրամ ներկայացրեք ելքային գրացուցակում.:

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- Ներկայացրեք դիագրամ՝ առանց դիագրամի սկզբնական կոդը պահելու (Նշում. այն պահվում է լռելյայն, երբ `-nometadata` տարբերակը նշված չէ):

`plantuml -nometadata {{diagram.png}} > {{diagram.puml}}`

- Առբերեք աղբյուրը `plantuml` դիագրամի մետատվյալներից.:

`plantuml -metadata {{diagram.png}} > {{diagram.puml}}`

- Ներկայացրեք դիագրամ կազմաձևման ֆայլով.:

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- Ցուցադրել օգնությունը.:

`plantuml -help`
