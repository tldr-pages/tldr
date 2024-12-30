# latexdiff

> 确定两个 LaTeX 文件之间的差异。
> 更多信息：<https://ctan.org/pkg/latexdiff>。

- 确定 LaTeX 文件不同版本之间的变化（生成的 LaTeX 文件可以编译以显示下划线标记的差异）：

`latexdiff {{old.tex}} {{new.tex}} > {{diff.tex}}`

- 通过加粗显示差异来确定 LaTeX 文件不同版本之间的变化：

`latexdiff --type=BOLD {{old.tex}} {{new.tex}} > {{diff.tex}}`

- 确定 LaTeX 文件不同版本之间的变化，并在方程中显示细微变化，包括添加和删除的图形：

`latexdiff --math-markup=fine --graphics-markup=both {{old.tex}} {{new.tex}} > {{diff.tex}}`