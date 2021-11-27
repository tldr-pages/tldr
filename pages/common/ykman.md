# ykman

> The YubiKey Manager can be used to configure all aspects of the YubiKey.
> More information: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Get information from YubiKey:

`ykman info`

- Get information for a given application from YubiKey:

`ykman {{fido|oath|openpgp|otp|piv}} info`

- Get a list of enabled applications over NFC from YubiKey:

`ykman config nfc --list`

- Enable application over USB on YubiKey:

`ykman config usb --enable {{OTP|U2F|FIDO2|OATH|PIV|OPENPGP|HSMAUTH}}`
