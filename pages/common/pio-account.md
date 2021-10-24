# pio account

> Manage your PlatformIO account in the command-line.
> More information: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- Register a new PlatformIO account:

`pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- Permanently delete your PlatformIO account and related data:

`pio account destroy`

- Log in to your PlatformIO account:

`pio account login --username {{username}} --password {{password}}`

- Log out of your PlatformIO account:

`pio account logout`

- Update your PlatformIO profile:

`pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- Show detailed information about your PlatformIO account:

`pio account show`

- Reset your password using your username or email:

`pio account forgot --username {{username_or_email}}`
