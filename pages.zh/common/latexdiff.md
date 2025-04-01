# latexdiff

> 确定两个 LaTeX 文件之间的差异。
> 更多信息：<https://ctan.org/pkg/latexdiff>。

- 确定两个不同版本的 LaTeX 文件之间的差异（生成的 LaTeX 文件可以编译，以显示下划线标注的差异）：

`latexdiff {{old.tex}} {{new.tex}} > {{diff.tex}}`

- 确定两个不同版本的 LaTeX 文件之间的差异，并以粗体突出显示差异：

`latexdiff --type=BOLD {{old.tex}} {{new.tex}} > {{diff.tex}}`

- 确定两个不同版本的 LaTeX 文件之间的差异，并在公式中以添加和删除的图形显示细微差异：

`latexdiff --math-markup=fine --graphics-markup=both {{old.tex}} {{new.tex}} > {{diff.tex}}`
