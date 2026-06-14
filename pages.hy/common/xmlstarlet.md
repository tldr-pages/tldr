# xmlstarlet

> XML/XSLT գործիքակազմ:.
> Նշում. Դուք հավանաբար պետք է իմանաք XPath-ը՝ <https://developer.mozilla.org/en-US/docs/Web/XPath>:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/docs.php>:.

- Ձևաչափեք XML փաստաթուղթը և տպեք `stdout`:

`xmlstarlet format {{path/to/file.xml}}`

- XML փաստաթուղթը կարող է փոխանցվել նաև `stdin`-ից՝:

`{{cat path/to/file.xml}} | xmlstarlet format`

- Տպեք բոլոր հանգույցները, որոնք համապատասխանում են տվյալ XPath-ին.:

`xmlstarlet select --template --copy-of {{xpath}} {{path/to/file.xml}}`

- Տեղադրեք հատկանիշ բոլոր համապատասխան հանգույցներին և տպեք `stdout` (աղբյուր ֆայլը անփոփոխ է).:

`xmlstarlet edit --insert {{xpath}} --type attr --name {{attribute_name}} --value {{attribute_value}} {{path/to/file.xml}}`

- Թարմացրեք տեղում գտնվող բոլոր համապատասխան հանգույցների արժեքը (աղբյուրի ֆայլը փոխվել է).:

`xmlstarlet edit --inplace --update {{xpath}} --value {{new_value}} {{file.xml}}`

- Ջնջել բոլոր համապատասխան հանգույցները տեղում (աղբյուր ֆայլը փոխվել է).:

`xmlstarlet edit --inplace --delete {{xpath}} {{file.xml}}`

- Փախչել կամ անջատել հատուկ XML նիշերը տվյալ տողի մեջ.:

`xmlstarlet [un]escape {{string}}`

- Նշեք տրված գրացուցակը որպես XML (բաց թողեք փաստարկը ընթացիկ գրացուցակը ցուցակագրելու համար).:

`xmlstarlet ls {{path/to/directory}}`
