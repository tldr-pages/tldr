# jdeps

> Java դասի կախվածության անալիզատոր:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jdeps.html>:.

- Վերլուծեք `.jar` կամ `.class` ֆայլի կախվածությունը.:

`jdeps {{path/to/file.class}}`

- Տպեք որոշակի `.jar` ֆայլի բոլոր կախվածությունների ամփոփագիրը.:

`jdeps {{path/to/file.jar}} -summary`

- Տպեք `.jar` ֆայլի դասի մակարդակի բոլոր կախվածությունները.:

`jdeps {{path/to/file.jar}} -verbose`

- Վերլուծության արդյունքները դուրս բերեք DOT ֆայլում որոշակի գրացուցակում.:

`jdeps {{path/to/file.jar}} -dotoutput {{path/to/directory}}`

- Ցուցադրել օգնությունը.:

`jdeps --help`
