# jarsigner

> Ստորագրեք և հաստատեք Java արխիվի (`.jar`) ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jarsigner.html>:.

- Ստորագրեք `.jar` ֆայլը՝:

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- Ստորագրեք `.jar` ֆայլը հատուկ ալգորիթմով.:

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- Ստուգեք `.jar` ֆայլի ստորագրությունը.:

`jarsigner -verify {{path/to/file.jar}}`
