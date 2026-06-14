# վերօգտագործում

> Գործիք՝ REUSE առաջարկություններին համապատասխանելու համար:.
> Լրացուցիչ տեղեկություններ. <https://reuse.readthedocs.io/en/stable/man/index.html>:.

- Ընթացիկ նախագծի REUSE-ի համապատասխանության համար (տարբերակի վերահսկման տեղյակ).:

`reuse lint`

- Նշված գրացուցակից REUSE-ի համապատասխանության համար.:

`reuse --root {{path/to/directory}} lint`

- Ֆայլին ավելացրեք հեղինակային իրավունքի հայտարարություն.:

`reuse annotate {{[-c|--copyright]}} "{{your_name}} <{{your_email}}>" --fallback-dot-license {{path/to/file}}`

- Ավելացնել լիցենզիայի տվյալները ֆայլին.:

`reuse annotate {{[-l|--license]}} {{spdx_identifier}} --fallback-dot-license {{path/to/file}}`

- Ներբեռնեք լիցենզիան իր SPDX նույնացուցիչով և տեղադրեք այն LICENSES գրացուցակում.:

`reuse download {{spdx-identifier}}`

- Ներբեռնեք նախագծում հայտնաբերված բոլոր բացակայող լիցենզիաները.:

`reuse download --all`
