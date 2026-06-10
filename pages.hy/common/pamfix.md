# pamfix

> Ուղղել սխալները PAM, PBM, PGM և PPM ֆայլերում:.
> Տես նաև՝ `pamfile`, `pamvalidate`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamfix.html>:.

- Ուղղեք Netpbm ֆայլը, որը բացակայում է իր վերջին մասը.:

`pamfix {{[-t|-truncate]}} {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- Ուղղեք Netpbm ֆայլը, որտեղ պիքսելների արժեքները գերազանցում են պատկերի `maxval`-ը՝ նվազեցնելով վիրավորական պիքսելների արժեքները.:

`pamfix {{[-cl|-clip]}} {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- Ուղղեք Netpbm ֆայլը, որտեղ պիքսելների արժեքները գերազանցում են պատկերի `maxval`-ը՝ ավելացնելով այն.:

`pamfix {{[-ch|-changemaxval]}} {{path/to/corrupted.pam|pbm|pgm|ppm}} > {{path/to/output.pam|pbm|pgm|ppm}}`
