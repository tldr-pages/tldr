# դոպլերի գաղտնիքները

> Կառավարեք ձեր Doppler նախագծի գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.doppler.com/docs/accessing-secrets>:.

- Ստացեք բոլոր գաղտնիքները.:

`doppler secrets`

- Ստացեք մեկ կամ մի քանի գաղտնիքների արժեք(ներ).:

`doppler secrets get {{secrets}}`

- Վերբեռնեք գաղտնի ֆայլ.:

`doppler secrets upload {{path/to/file.env}}`

- Ջնջել մեկ կամ մի քանի գաղտնիքների արժեք(ներ).:

`doppler secrets delete {{secrets}}`

- Ներբեռնեք գաղտնիքները որպես `.env`:

`doppler secrets download --format=env --no-file > {{path/to/.env}}`
