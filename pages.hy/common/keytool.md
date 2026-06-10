# բանալի գործիք

> Վկայագրի կառավարման օգտակար ծրագիր, որը ներառված է Java-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/keytool.html>:.

- Ստեղծեք բանալիների պահեստ.:

`keytool -genkeypair -v -keystore {{path/to/file.keystore}} -alias {{key_name}}`

- Փոխել keystore գաղտնաբառը:

`keytool -storepasswd -keystore {{path/to/file.keystore}}`

- Փոխեք բանալիի գաղտնաբառը հատուկ բանալիների պահեստում.:

`keytool -keypasswd -alias {{key_name}} -keystore {{path/to/file.keystore}}`
