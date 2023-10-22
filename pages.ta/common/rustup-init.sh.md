# rustup-init.sh

> `rustup` மற்றும் ரஸ்ட் கருவித்தொகுப்பை நிறுவுவதற்கான ஸ்கிரிப்ட்.
> மேலும் விவரத்திற்கு: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- `rustup` மற்றும் இயல்புநிலை ரஸ்ட் கருவித்தொகுப்பை நிறுவ, `rustup-init` ஐப் பதிவிறக்கி இயக்கவும்:

`curl https://sh.rustup.rs -sSf | sh -s`

- பதிவிறக்கி, `rustup-init` ஐ இயக்கி, அதற்கு வாதங்களை அனுப்பவும்:

`curl https://sh.rustup.rs -sSf | sh -s -- {{வாதங்கள்}}`

- `rustup-init` ஐ இயக்கி, நிறுவுவதற்கான கூடுதல் கூறுகள் அல்லது இலக்குகளைக் குறிப்பிடவும்:

`rustup-init.sh --target {{இலக்கு}} --component {{கூறு}}`

- `rustup-init` ஐ இயக்கி, நிறுவ வேண்டிய இயல்புநிலை கருவித்தொகுப்பைக் குறிப்பிடவும்:

`rustup-init.sh --default-toolchain {{கருவித்தொகுப்பு}}`

- `rustup-init` ஐ இயக்கவும் மற்றும் எந்த கருவித்தொகுப்பையும் நிறுவ வேண்டாம்:

`rustup-init.sh --default-toolchain {{none}}`

- `rustup-init` ஐ இயக்கி, நிறுவல் சுயவிவரத்தைக் குறிப்பிடவும்:

`rustup-init.sh --profile {{minimal|default|complete}}`

- உறுதிப்படுத்தலைக் கேட்காமல் `rustup-init` ஐ இயக்கவும்:

`rustup-init.sh -y`
