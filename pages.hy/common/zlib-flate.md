# zlib-flate

> Raw zlib սեղմման և ապակոմպրեսիայի ծրագիր:.
> `qpdf`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zlib-flate>:.

- Կոմպրես ֆայլ.:

`zlib-flate < {{path/to/input_file}} -compress > {{path/to/compressed.zlib}}`

- Ապասեղմեք ֆայլը.:

`zlib-flate < {{path/to/compressed.zlib}} -uncompress > {{path/to/output_file}}`

- Սեղմեք ֆայլը նշված սեղմման մակարդակով: 0=Ամենաարագ (ամենավատ), 9=Ամենադանդաղ (Լավագույն):

`zlib-flate < {{path/to/input_file}} -compress={{compression_level}} > {{path/to/compressed.zlib}}`
