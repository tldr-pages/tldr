# ykman oath

> Manage the OATH YubiKey application.
> A `keyword` can be a part of the name or the issuer.
> More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- Display general information about the OATH application:

`ykman oath info`

- Change the password used to protect OATH accounts (add `--clear` to remove it):

`ykman oath access change`

- Add a new account (`--issuer` is optional):

`ykman oath accounts add --issuer {{issuer}} {{name}}`

- List all accounts (with their issuers):

`ykman oath accounts list`

- List all accounts with their current TOTP/HOTP codes (optionally filtering the list with a keyword):

`ykman oath accounts code {{keyword}}`

- Rename an account:

`ykman oath accounts rename {{keyword}} {{issuer:name|name}}`

- Delete an account:

`ykman oath accounts delete {{keyword}}`

- Delete all accounts and restore factory settings:

`ykman oath reset`
