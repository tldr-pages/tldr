# keytool

> A certificate management utility included with Java.
> More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/keytool.html>.

- Create a keystore:

`keytool -genkeypair -v -keystore {{path/to/file.keystore}} -alias {{key_name}}`

- Change a keystore password:

`keytool -storepasswd -keystore {{path/to/file.keystore}}`

- Change a key's password inside a specific keystore:

`keytool -keypasswd -alias {{key_name}} -keystore {{path/to/file.keystore}}`
