# pass otp

> Միանգամյա գաղտնաբառի (OTP) նշանները կառավարելու համար անցուղու ընդլայնում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pass-otp>:.

- Հուշեք otpauth URI նշան և ստեղծեք նոր անցագրի ֆայլ.:

`pass otp insert {{path/to/pass}}`

- Հուշեք otpauth URI նշան և միացրեք առկա անցագրի ֆայլին.:

`pass otp append {{path/to/pass}}`

- Տպեք 2FA կոդը՝ օգտագործելով OTP նշանը անցումային ֆայլում.:

`pass otp {{path/to/pass}}`

- Պատճենեք և մի տպեք 2FA ծածկագիրը՝ օգտագործելով OTP նշանը անցագրի ֆայլում.:

`pass otp {{[-c|--clip]}} {{path/to/pass}}`

- Ցուցադրել QR կոդը՝ օգտագործելով անցումային ֆայլում պահվող OTP նշանը.:

`pass otp uri {{[-q|--qrcode]}} {{path/to/pass}}`

- Հուշեք OTP գաղտնի արժեք, որը նշում է թողարկողը և հաշիվը (առնվազն մեկը պետք է նշվի) և կցեք առկա անցագրի ֆայլին.:

`pass otp append {{[-s|--secret]}} {{[-i|--issuer]}} {{issuer_name}} {{[-a|--account]}} {{account_name}} {{path/to/pass}}`
