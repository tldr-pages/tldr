# cpdf

> Շահարկել PDF ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>:.

- Ընտրեք 1, 2, 3 և 6 էջերը սկզբնաղբյուր փաստաթղթից և գրեք դրանք նպատակակետ փաստաթղթում.:

`cpdf {{path/to/source_document.pdf}} {{1-3,6}} -o {{path/to/destination_document.pdf}}`

- Միավորել երկու փաստաթուղթ նորի մեջ.:

`cpdf -merge {{path/to/source_document_one.pdf}} {{path/to/source_document_two.pdf}} -o {{path/to/destination_document.pdf}}`

- Ցույց տալ փաստաթղթի էջանիշները.:

`cpdf -list-bookmarks {{path/to/document.pdf}}`

- Փաստաթուղթը բաժանեք տասը էջանոց կտորների՝ դրանք գրելով `chunk001.pdf`, `chunk002.pdf` և այլն:

`cpdf -split {{path/to/document.pdf}} -o {{path/to/chunk%%%.pdf}} -chunk {{10}}`

- Գաղտնագրեք փաստաթուղթը, օգտագործելով 128 բիթ կոդավորումը, տրամադրելով `fred` որպես սեփականատիրոջ գաղտնաբառ և `joe` որպես օգտվողի գաղտնաբառ.:

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{path/to/source_document.pdf}} -o {{path/to/encrypted_document.pdf}}`

- Փաստաթուղթը ապակոդավորել՝ օգտագործելով սեփականատիրոջ գաղտնաբառը `fred`:

`cpdf -decrypt {{path/to/encrypted_document.pdf}} owner={{fred}} -o {{path/to/decrypted_document.pdf}}`

- Ցույց տալ փաստաթղթի անոտացիաները.:

`cpdf -list-annotations {{path/to/document.pdf}}`

- Ստեղծեք նոր փաստաթուղթ գոյություն ունեցողից՝ լրացուցիչ մետատվյալներով.:

`cpdf -set-metadata {{path/to/metadata.xml}} {{path/to/source_document.pdf}} -o {{path/to/destination_document.pdf}}`
