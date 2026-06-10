#տարբերություն-այնքան շքեղ

> Գունավորե՛ք `diff` ելքը ավելի շատ մարդկանց համար ընթեռնելի կերպով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/so-fancy/diff-so-fancy#-usage>:.

- Գունավորել `diff`:

`diff {{[-u|--unified]}} {{path/to/file1}} {{path/to/file2}} | diff-so-fancy`

- Սահմանեք `diff-so-fancy` արդյունքը՝ Git-ի ինտերակտիվ բեմադրության ընթացքում գունավորելու համար.:

`git config --global interactive.diffFilter "diff-so-fancy --patch"`
