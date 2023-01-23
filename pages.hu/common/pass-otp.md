# pass otp

> Pass kiterjesztés az egyszeri jelszó (OTP) tokenek kezelésére. További információ: <https://github.com/tadfisher/pass-otp#readme>.

- Otpauth URI token kérése és egy új pass fájl létrehozása:

`pass otp insert {{path/to/pass}}`

- Otpauth URI token kérése és hozzáfűzése egy meglévő pass fájlhoz:

`pass otp append {{path/to/pass}}`

- 2FA-kód nyomtatása a jelszófájlban lévő OTP-token felhasználásával:

`pass otp {{path/to/pass}}`

- Másolás és nem nyomtat ki 2FA-kódot az OTP-token felhasználásával egy belépési engedélyfájlban:

`pass otp --clip {{path/to/pass}}`

- QR-kód megjelenítése a jelszófájlban tárolt OTP-token felhasználásával:

`pass otp uri --qrcode {{path/to/pass}}`

- OTP-titokérték kérése a kibocsátó és a számla megadásával (legalább egyet meg kell adni), és a meglévő pass fájlhoz való csatolás:

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{path/to/pass}}`
