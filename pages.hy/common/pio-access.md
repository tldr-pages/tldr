# pio մուտք

> Սահմանեք գրանցամատյանում հրապարակված ռեսուրսների (փաթեթների) հասանելիության մակարդակը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/access/>:.

- Օգտատիրոջը հասանելիություն տրամադրեք ռեսուրսին՝:

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- Հեռացրեք օգտվողի մուտքը ռեսուրս.:

`pio access revoke {{username}} {{resource_urn}}`

- Ցուցադրել բոլոր ռեսուրսները, որոնց հասանելի է օգտվողը կամ թիմը, և մուտքի մակարդակը.:

`pio access list {{username}}`

- Սահմանափակել մուտքը ռեսուրս կոնկրետ օգտվողների կամ թիմի անդամների համար.:

`pio access private {{resource_urn}}`

- Թույլ տալ բոլոր օգտվողներին մուտք գործել ռեսուրս.:

`pio access public {{resource_urn}}`
