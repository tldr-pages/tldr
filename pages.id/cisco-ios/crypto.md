# crypto

> Atur konfigurasi kriptografi.
> Gunakan mode konfigurasi untuk mengakses perintah ini..
> Informasi lebih lanjut: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- Buat sebuah kunci `rsa` baru:

`crypto key generate rsa`

- Gunakan suatu nilai modulus bagi kunci baru:

`crypto key generate rsa modulus {{1024}}`

- Hapus seluruh kunci yang tersimpan:

`crypto key zeroize`
