# perl

> De Perl 5-interpeter.
> Zie ook: `perldoc`.
> Meer informatie: <https://perldoc.perl.org/perl>.

- Toon regels van `stdin` die overeenko[m]en met `regex1` en hoofdletterongevoel[i]g `regex2`:

`perl -n -e 'print if m/regex1/ and m/regex2/i'`

- G[E]ef de eerste overeenkomende groep op, met behulp van `regex`, waarbij de spatie in `regex` wordt genegeerd ([x]):

`perl -n -E 'say $1 if m/{{voor}} ( {{groep_regex}} ) {{na}}/x'`

- Ter plaatse ([i]), met backup, vervang ([s]) alle voorkomens ([g]) van `regex` met een vervanging:

`perl -i'.bak' -p -e 's/regex/{{vervanging}}/g' {{pad/naar/bestanden}}`
