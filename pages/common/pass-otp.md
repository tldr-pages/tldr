# pass otp

> A pass extension for managing one-time-password (OTP) tokens.
> More information: <https://manned.org/pass-otp>.

- Prompt for an otpauth URI token and create a new pass file:

`pass otp insert {{path/to/pass}}`

- Prompt for an otpauth URI token and append to an existing pass file:

`pass otp append {{path/to/pass}}`

- Print a 2FA code using the OTP token in a pass file:

`pass otp {{path/to/pass}}`

- Copy and don't print a 2FA code using the OTP token in a pass file:

`pass otp {{[-c|--clip]}} {{path/to/pass}}`

- Display a QR code using the OTP token stored in a pass file:

`pass otp uri {{[-q|--qrcode]}} {{path/to/pass}}`

- Prompt for an OTP secret value specifying issuer and account (at least one must be specified) and append to existing pass file:

`pass otp append {{[-s|--secret]}} {{[-i|--issuer]}} {{issuer_name}} {{[-a|--account]}} {{account_name}} {{path/to/pass}}`
