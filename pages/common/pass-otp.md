# pass-otp

> A pass extension for managing one-time-password (OTP) tokens.
> More information: <https://github.com/tadfisher/pass-otp#readme>.

- Prompt for an otpauth URI token and CREATE a new pass file:

`pass otp insert {{pass_path}}`

- Promt for an otpauth URI token and APPEND to an existing pass file:

`pass otp append {{pass_path}}`

- Print a 2FA code using the OTP token in a pass file:

`pass otp {{pass_path}}`

- Copy and don't print a 2FA code using the OTP token in a pass file:

`pass otp --clip {{pass_path}}

- Display a QR code using the OTP token stored in a pass file:

`pass otp uri --qrcode {{pass_path}}`

- Promt for an OTP secret value specifying issuer and account (at least one must be specified) and APPEND to existing pass file:

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{pass_path}}`
