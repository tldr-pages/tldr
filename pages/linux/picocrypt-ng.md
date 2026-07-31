# Picocrypt-NG CLI

> Picocrypt New Generation (Active fork of the now archived, Picocrypt)
> A fast, feature-rich tool to encrypt files with multiple security options.
> More information: <https://github.com/Picocrypt-NG/Picocrypt-NG>.

- Encrypt a file with only a password:

`picocrypt-ng encrypt -p {{PASSWORD}} -i {{PATH-TO-FILE}}`

- Decrypt a file with only a password:
    
`picocrypt-ng decrypt -p {{PASSWORD}} -i {{PATH-TO-FILE}}`    

- Encrypt a file with a password and a keyfile:

`picocrypt-ng encrypt -p {{PASSWORD}} -i {{PATH-TO-FILE}} -k {{PATH-TO-KEYFILE}}`

- Encrypt a file with a password, keyfile and deniability (Hides the fact that your file is encrypted):

`picocrypt-ng encrypt -p {{PASSWORD}} --deniability -i {{PATH-TO-FILE}} -k {{PATH-TO-KEYFILE}}`

- Decrypt a file with a password and a keyfile:

`picocrypt-ng decrypt -p {{PASSWORD}} -i {{PATH-TO-FILE}} -k {{PATH-TO-KEYFILE}}`

- Decrypt a file with a password and a keyfile and deniability: 

`picocrypt-ng decrypt -p {{PASSWORD}} --deniability  -i {{PATH-TO-FILE}} -k {{PATH-TO-KEYFILE}}`
