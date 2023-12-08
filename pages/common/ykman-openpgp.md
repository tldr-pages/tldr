# ykman openpgp

> Manage the OpenPGP YubiKey application.
> Note: you need to use `gpg --card-edit` for some settings.
> More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- Display general information about the OpenPGP application:

`ykman openpgp info`

- Set the number of retry attempts for the User PIN, Reset Code, and Admin PIN, respectively:

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- Change the User PIN, Reset Code or Admin PIN:

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- Factory reset the OpenPGP application (you have to do this after exceeding the number of Admin PIN retry attempts):

`ykman openpgp reset`
