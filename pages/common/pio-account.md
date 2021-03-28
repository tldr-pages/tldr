# pio account

> Manage your PlatformIO account in the command line.
> More information: <https://docs.platformio.org/en/latest/core/userguide/account/index.html>.

- Register a new PlatformIO account:

`pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- Permanently delete your PlatformIO account and related data:

`pio account destroy`

- Login to your PlatformIO account:

`pio account login --username {{username}} --password {{password}}`

- Logout of your PlatformIO account:

`pio account logout`

- Update your PlatformIO profile:

`pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- Show detailed information about your PlatformIO account:

`pio account show`

- Reset your password using your username or email:

`pio account forgot --username {{username_or_email}}`
