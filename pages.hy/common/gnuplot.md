# gnuplot

> Գրաֆիկ պլոտեր, որը թողարկում է մի քանի ձևաչափերով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/gnuplot>:.

- Սկսեք ինտերակտիվ գրաֆիկի գծագրման կեղևը.:

`gnuplot`

- Կազմեք գրաֆիկը նշված գրաֆիկի սահմանման ֆայլի համար.:

`gnuplot {{path/to/definition.plt}}`

- Սահմանեք ելքային ձևաչափը՝ կատարելով հրաման՝ նախքան սահմանման ֆայլը բեռնելը.:

`gnuplot -e "{{set output "path/to/file.png" size 1024,768}}" {{path/to/definition.plt}}`

- Gnuplot-ից դուրս գալուց հետո պահպանեք գրաֆիկի սյուժեի նախադիտման պատուհանը.:

`gnuplot {{[-p|--persist]}} {{path/to/definition.plt}}`
