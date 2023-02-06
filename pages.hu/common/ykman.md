# ykman

> A YubiKey Manager a YubiKey minden aspektusának konfigurálására használható. További információ: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Információk beszerzése a YubiKey-ről:

`ykman info`

- Információk lekérése egy adott alkalmazáshoz a YubiKey-ről:

`ykman {{fido|oath|openpgp|otp|piv}} info`

- Az NFC-n keresztül engedélyezett alkalmazások listájának lekérése a YubiKey-ről:

`ykman config nfc --list`

- Alkalmazás engedélyezése USB-n keresztül a YubiKey-n:

`ykman config usb --enable {{OTP|U2F|FIDO2|OATH|PIV|OPENPGP|HSMAUTH}}`
