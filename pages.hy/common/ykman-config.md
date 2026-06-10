# ykman կազմաձևում

> Միացնել կամ անջատել YubiKey հավելվածները:.
> Նշում. դուք կարող եք օգտագործել `ykman info`՝ ներկայումս միացված հավելվածները տեսնելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>:.

- Միացրեք հավելվածը USB-ի կամ NFC-ի միջոցով (`--enable`-ը կարող է օգտագործվել մի քանի անգամ՝ ավելի շատ հավելվածներ նշելու համար):

`ykman config {{usb|nfc}} {{[-e|--enable]}} {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Անջատեք հավելվածը USB-ի կամ NFC-ի միջոցով (`--disable`-ը կարող է օգտագործվել մի քանի անգամ՝ ավելի շատ հավելվածներ նշելու համար):

`ykman config {{usb|nfc}} {{[-d|--disable]}} {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Անջատեք բոլոր հավելվածները NFC-ով.:

`ykman config nfc {{[-D|--disable-all]}}`
