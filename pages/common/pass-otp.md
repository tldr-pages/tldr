# pass-otp

> A pass extension for managing one-time-password (OTP) tokens.
> More information: <https://github.com/tadfisher/pass-otp#readme>.

- Prompt for an otpauth URI token and create a new pass file:

`pass otp insert {{path/to/pass}}`

- Promt for an otpauth URI token and append to an existing pass file:

`pass otp append {{path/to/pass}}`

- Print a 2FA code using the OTP token in a pass file:

`pass otp {{path/to/pass}}`

- Copy and don't print a 2FA code using the OTP token in a pass file:

`pass otp --clip {{path/to/pass}}`

- Display a QR code using the OTP token stored in a pass file:

`pass otp uri --qrcode {{path/to/pass}}`

- Promt for an OTP secret value specifying issuer and account (at least one must be specified) and append to existing pass file:

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{path/to/pass}}`
