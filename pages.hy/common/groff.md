#գրոֆ

> GNU-ի փոխարինում `troff` և `nroff` տիպային կոմունալ ծրագրերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/groff/manual/groff.html.node/Groff-Options.html>:.

- Ձևաչափեք ելքը PostScript տպիչի համար՝ ելքը պահելով ֆայլում.:

`groff {{path/to/input.roff}} > {{path/to/output.ps}}`

- Պատկերացրեք մարդու էջը ASCII ելքային սարքի միջոցով և ցուցադրեք այն փեյջերի միջոցով.:

`groff -man -T ascii {{path/to/manpage.1}} | less --RAW-CONTROL-CHARS`

- Տրամադրել մարդու էջը HTML ֆայլի մեջ.:

`groff -man -T html {{path/to/manpage.1}} > {{path/to/manpage.html}}`

- Մուտքագրեք roff ֆայլը, որը պարունակում է [t]աղյուսակներ և [p] նկարներ՝ օգտագործելով [me] մակրո հավաքածուն, PDF՝ պահպանելով ելքը.:

`groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{path/to/input.me}} > {{path/to/output.pdf}}`

- Գործարկեք `groff` հրամանը նախապրոցեսորային և մակրո ընտրանքներով, որոնք գուշակված են `grog` կոմունալ ծրագրի կողմից:

`eval "$(grog -T utf8 {{path/to/input.me}})"`
