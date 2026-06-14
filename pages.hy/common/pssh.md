# pssh

> Զուգահեռ SSH ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pssh>:.

- Գործարկեք հրաման երկու հոստերի վրա և տպեք դրա ելքը յուրաքանչյուր սերվերի վրա.:

`pssh {{[-i|--inline]}} {{[-H|--host]}} "{{host1}} {{host2}}" {{hostname --ip-addresses}}`

- Գործարկեք հրաման և պահեք ելքը առանձին ֆայլերում.:

`pssh {{[-H|--host]}} {{host1}} {{[-H|--host]}} {{host2}} {{[-o|--outdir]}} {{path/to/output_directory}} {{hostname --ip-addresses}}`

- Գործարկեք հրաման մի քանի հոսթների վրա, որոնք նշված են նոր տողով առանձնացված ֆայլում.:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{hostname --ip-addresses}}`

- Գործարկեք հրամանը որպես root (սա պահանջում է արմատային գաղտնաբառը).:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-A|--askpass]}} {{[-l|--user]}} {{root_username}} {{hostname --ip-addresses}}`

- Գործարկեք հրաման լրացուցիչ SSH փաստարկներով.:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-x|--extra-arg]}} "{{-O VisualHostKey=yes}}" {{hostname --ip-addresses}}`

- Գործարկեք հրաման, որը սահմանափակում է զուգահեռ կապերի քանակը մինչև 10:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-p|-par]}} {{10}} '{{cd dir; ./script.sh; exit}}'`
