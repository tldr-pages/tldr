# ykman fido

> Կառավարեք YubiKey FIDO հավելվածները:.
> Լրացուցիչ տեղեկություններ. <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>:.

- Ցուցադրել ընդհանուր տեղեկություններ FIDO2 հավելվածի մասին.:

`ykman fido info`

- Փոխեք FIDO փին.:

`ykman fido access change-pin`

- Ցուցակեք YubiKey-ում պահվող ռեզիդենտ հավատարմագրերը.:

`ykman fido credentials list`

- Ջնջել բնակության հավատարմագիրը YubiKey-ից.:

`ykman fido credentials delete {{id}}`

- Նշեք YubiKey-ում պահված մատնահետքերը (պահանջվում է մատնահետքի սենսորով բանալի).:

`ykman fido fingerprints list`

- Ավելացնել նոր մատնահետք YubiKey-ին.:

`ykman fido fingerprints add {{name}}`

- Ջնջել մատնահետքը YubiKey-ից.:

`ykman fido fingerprints delete {{name}}`

- Ջնջեք FIDO-ի բոլոր հավատարմագրերը (դա պետք է անեք PIN-ի կրկնակի փորձերի քանակը գերազանցելուց հետո).:

`ykman fido reset`
