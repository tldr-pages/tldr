# pass otp

> O extensie de trecere pentru gestionarea tokenurilor one-time password (OTP).
> Mai multe informaţii: <https://github.com/tadfisher/pass-otp#readme>

- Solicitați un simbol URI otpauth și creați un nou fișier de trecere:

`pass otp insert {{path/to/pass}}`

- Se solicită un token URI otpauth și se adaugă la un fișier de trecere existent:

`pass otp append {{path/to/pass}}`

- Imprimați un cod 2FA folosind tokenul OTP într-un fișier de trecere:

`pass otp {{path/to/pass}}`

- Copiați și nu imprimați un cod 2FA folosind tokenul OTP într-un fișier de trecere:

`pass otp --clip {{path/to/pass}}`

- Afișează un cod QR folosind tokenul OTP stocat într-un fișier de trecere:

`pass otp uri --qrcode {{path/to/pass}}`

- Solicitare pentru o valoare secretă OTP specificând emitentul și contul (cel puțin unul trebuie specificat) și adăugare la fișierul de trecere existent:

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{path/to/pass}}`
