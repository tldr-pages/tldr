#պերլ

> Perl 5 լեզվի թարգմանիչը:.
> Տես նաև՝ `perldoc`:.
> Լրացուցիչ տեղեկություններ. <https://perldoc.perl.org/perl>:.

- Տպեք տողեր `stdin` [m]-ից՝ կցելով `regex1`-ը և մեծատառերի [i]անզգայուն `regex2`:

`perl -n -e 'print if m/regex1/ and m/regex2/i'`

- Ասեք ([-E]) առաջին համընկնող խումբը՝ օգտագործելով `regex`, անտեսելով բացատը ([x]) `regex`-ում:

`perl -n -E 'say $1 if m/{{before}} ( {{group_regex}} ) {{after}}/x'`

- [i]n-տեղ, կրկնօրինակով, [s]փոխարինել `regex`-ի բոլոր դեպքերը ([g]) փոխարինողով՝:

`perl -i'.bak' -p -e 's/regex/{{replacement}}/g' {{path/to/files}}`
