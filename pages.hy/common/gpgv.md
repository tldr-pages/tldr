# gpgv

> Ստուգեք OpenPGP ստորագրությունները:.
> Նշում. `gpgv`-ը կարդում է վստահելի pubkey-ները `~/.gnupg/trustedkeys.kbx`-ից՝ `--keyring` տարբերակի բացակայության դեպքում:.
> Տես նաև՝ `gpg`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>:.

- Ստուգեք մաքրված կամ ներդիրով ստորագրված ֆայլը (ստորագրությունը ներկառուցված է հենց ֆայլում).:

`gpgv {{path/to/file.asc}}`

- Ստուգեք անջատված ստորագրությունը (`.asc` կամ `.sig`) դրա համապատասխան տվյալների ֆայլում.:

`gpgv {{path/to/signature.asc}} {{path/to/data_file}}`

- Ստուգեք անջատված ստորագրությունը՝ օգտագործելով հատուկ հանրային ստեղնաշար կամ արտահանված հանրային բանալի ֆայլ (`.gpg` կամ `.kbx`):

`gpgv --keyring {{path/to/pubkey_or_keyring.gpg}} {{path/to/signature.asc}} {{path/to/data_file}}`

- Ստուգեք անջատված ստորագրությունը՝ օգտագործելով հատուկ հանրային բանալի ֆայլ՝ պարզ տեքստային ձևաչափով (`.txt`):

`gpg --dearmor {{[-o|--output]}} {{path/to/pubkey.gpg}} {{path/to/pubkey.txt}} && gpgv --keyring {{path/to/pubkey.gpg}} {{path/to/signature.asc}} {{path/to/data_file}}`
