# git bisect

> Gebruik binair zoeken om de commit te vinden die een bug heeft geïntroduceerd.
> Git springt automatisch heen en weer in de commitgrafiek om de foutieve commit te vinden.
> Meer informatie: <https://git-scm.com/docs/git-bisect>.

- Start een bisect op een commitbereik dat is begrensd door een bekende, foutieve commit en een bekende, schone (meestal oudere) commit:

`git bisect start {{foutieve_commit}} {{schone_commit}}`

- Voor elke commit die `git bisect` selecteert, markeer het als "bad" of "good" na het testen voor het probleem:

`git bisect {{good|bad}}`

- Sluit de bisect-sessie en keer terug naar de vorige branch:

`git bisect reset`

- Sla een commit over tijdens een bisect (b.v. een commit die de tests faalt vanwege een ander probleem):

`git bisect skip`

- Toon een log van wat er tot nu toe is gedaan:

`git bisect log`
