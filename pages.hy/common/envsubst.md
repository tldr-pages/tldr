# envsubst

> Փոխարինում է շրջակա միջավայրի փոփոխականները իրենց արժեքներով shell ֆորմատի տողերում:.
> Փոխարինվող փոփոխականները պետք է լինեն `${var}` կամ `$var` ձևաչափով:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gettext/manual/gettext.html#envsubst-Invocation>:.

- Փոխարինեք շրջակա միջավայրի փոփոխականները `stdin`-ում և թողարկեք `stdout`:

`echo '{{$HOME}}' | envsubst`

- Փոխարինեք միջավայրի փոփոխականները մուտքային ֆայլում և թողարկեք `stdout`:

`envsubst < {{path/to/input_file}}`

- Փոխարինեք միջավայրի փոփոխականները մուտքային ֆայլում և ելք դեպի ֆայլ.:

`envsubst < {{path/to/input_file}} > {{path/to/output_file}}`

- Փոխարինեք միջավայրի փոփոխականները մուտքային ֆայլում բացատով առանձնացված ցուցակից.:

`envsubst < {{path/to/input_file}} '{{$USER $SHELL $HOME}}'`
