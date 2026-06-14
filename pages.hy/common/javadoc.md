# javadoc

> Ստեղծեք Java API-ի փաստաթղթեր HTML ձևաչափով սկզբնական կոդից:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javadoc.html>:.

- Ստեղծեք փաստաթղթեր Java-ի սկզբնական կոդի համար և արդյունքը պահեք գրացուցակում.:

`javadoc -d {{path/to/directory}}/ {{path/to/java_source_code}}`

- Ստեղծեք փաստաթղթեր հատուկ կոդավորմամբ.:

`javadoc -docencoding {{UTF-8}} {{path/to/java_source_code}}`

- Ստեղծեք փաստաթղթեր, բացառությամբ որոշ փաթեթների.:

`javadoc -exclude {{package_list}} {{path/to/java_source_code}}`
