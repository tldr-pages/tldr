# git bisect

> Bug taşıyan commit'i bulmak için ikili arama kullan.
> Git otomatik olarak commit çizelgesi içinde oradan oraya atlayarak yaramaz commit'i saptar.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-bisect>.

- Buglı bilinen bir commit'i ve (genelde eski olan) iyi bir commit'i belirterek ikiye bölme işlemini başlat:

`git bisect start {{kötü_commit}} {{iyi_commit}}`

- `git bisect`'in seçtiği her commit'i, mevcut soruna sebep olup olmadıklarını test ettikten sonra "bad" (kötü) veya "good" (iyi) olarak işaretle:

`git bisect {{good|bad}}`

- `git bisect` sorunlu commit'i saptadıktan sonra, ikiye bölme işlemini bitir ve depoyu bahsi geçen commit'den önceki dala geçir:

`git bisect reset`

- İkiye bölme işlemi sırasında bir commit'i atla:

`git bisect skip`
