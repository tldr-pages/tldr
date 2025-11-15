# gpg-card

> Administrate OpenPGP and PIV smart cards.
> Similar to `gpg --card-edit`.
> More information: <https://manned.org/gpg-card>.

- Start in interactive mode:

`gpg-card`

- Invoke one or more commands non-interactively:

`gpg-card {{command1}} -- {{command2}} -- {{command3}}`

- Show information about a smart card:

`gpg-card list`

- Retrieve the public key using the URL stored on an OpenPGP card:

`gpg-card fetch`

- Set the URL used by the `fetch` command:

`gpg-card url`

- Change or unblock PINs (uses the default action for the card in non-interactive mode):

`gpg-card passwd`

- Toggle the forcesig flag of an OpenPGP card (i.e. require entering the user PIN for signing):

`gpg-card forcesig`

- Factory reset a smart card (i.e. delete all data and reset PINs):

`gpg-card factory-reset`
