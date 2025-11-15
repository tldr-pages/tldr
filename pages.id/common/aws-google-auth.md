# aws-google-auth

> Dapatkan kredensial sementara (STS) bagi AWS menggunakan Google Apps sebagai penyedia akun layanan terfederasi (Single Sign-On).
> Informasi lebih lanjut: <https://github.com/cevoaustralia/aws-google-auth>.

- Masuk menggunakan akun SSO Google dengan data pengenal [u]sername, [I]DP, dan [S]P, kemudian atur [d]urasi akses kredensial sementara selama satu jam ke depan:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Masuk dengan men[a]nyakan peran (role) yang hendak digunakan dalam membuat kredensial (bila terdapat beberapa peran SAML yang tersedia):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Selesaikan kumpulan alias bagi akun AWS:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Tampilkan bantuan:

`aws-google-auth -h`
