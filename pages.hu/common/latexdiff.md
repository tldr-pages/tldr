# latexdiff

> Két LaTeX-fájl közötti különbségek meghatározása. További információ: <https://ctan.org/pkg/latexdiff>.

- Meghatározza a változásokat egy LaTeX-fájl különböző változatai között (az így kapott LaTeX-fájlt össze lehet állítani, hogy a különbségek aláhúzva jelenjenek meg):

`latexdiff {{old.tex}} {{new.tex}} > {{diff.tex}}`

- Egy LaTeX-fájl különböző verziói közötti változások meghatározása a különbségek vastag betűvel történő kiemelésével:

`latexdiff --type=BOLD {{old.tex}} {{new.tex}} > {{diff.tex}}`

- Egy LaTeX-fájl különböző verziói közötti változások meghatározása, és a kisebb változások megjelenítése az egyenletekben hozzáadott és törölt grafikákkal:

`latexdiff --math-markup=fine --graphics-markup=both {{old.tex}} {{new.tex}} > {{diff.tex}}`
