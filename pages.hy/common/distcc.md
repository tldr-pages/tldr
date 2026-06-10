# distcc

> Բաշխված C/C++/ObjC կոմպիլյացիայի հաճախորդ, որն աշխատում է `distccd`-ով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/distcc>:.

- Կազմեք սկզբնաղբյուր ֆայլ՝ օգտագործելով այնպիսի կոմպիլյատոր, ինչպիսին `gcc`ն է:

`distcc {{gcc}} -c {{path/to/source.c}} -o {{path/to/output.o}}`

- Սահմանեք հեռավոր հոսթեր՝ կոմպիլյացիան տարածելու համար.:

`export DISTCC_HOSTS="localhost {{ip1 ip2 ...}}"`

- Կազմեք նախագիծ `make`-ով՝ օգտագործելով `distcc`:

`make {{[-j|--jobs]}} {{parallel_jobs}} CC="distcc {{gcc}}"`

- Ցուցադրել ընթացիկ `distcc` հյուրընկալողների ցանկը՝:

`distcc --show-hosts`

- Ցուցադրել օգնությունը.:

`distcc --help`

- Ցուցադրման տարբերակը:

`distcc --version`
