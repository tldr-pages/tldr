# keytool

> Keytool is a certificate management utility included with Java.
> More information: <https://docs.oracle.com/javase/8/docs/technotes/tools/windows/keytool.html>.

- Create a keystore:

`keytool -genkey -v -keystore {{keystore_name}}.keystore -alias {{key_name}}`

- Change a keystore password:

`keytool -storepasswd -keystore {{keystore_name}}.keystore`

- Change a key's password inside a keystore:

`keytool -keypasswd  -alias {{key_name}} -keystore {{keystore_name}}.keystore`
