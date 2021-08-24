# gmssl

> GmSSL is a crypto toolkit supporting SM1, SM2, SM3, SM4, SM9, and ZUC/ZUC256
> More information: <http://gmssl.org/>.

- Generate an SM3 hash for a file:

`gmssl sm3 <file>`

- Encrypt a file using the SM4 cipher:

`gmssl sms4 -e -in <file> -out <outputfile>.sms4`

- Decrypt a file using the SM4 cipher:

`gmssl sms4 -d -in <file>.sms4`

- Generate an SM2 private key:

`gmssl sm2 -genkey -out <key>.pem`

- Generate an SM2 public key from an existing private key:

`gmssl sm2 -pubout -in <key>.pem -out <key.pub>.pem`

- Encrypt a file using the ZUC cipher:

`gmssl zuc -e -in <file> -out <outputfile>.zuc`

- Decrypt a file using the ZUC cipher:

`gmssl zuc -d -in <file>.zuc`

- Print version:

`gmssl version`
