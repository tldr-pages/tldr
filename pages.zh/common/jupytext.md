# jupytext

> 将 Jupyter 笔记本转换为纯文本文件，然后再转换回去。
> 更多信息：<https://jupytext.readthedocs.io>.

- 将笔记本转换为成对的 `.ipynb`/`.py` 笔记本：

`jupytext --set-formats ipynb,py {{notebook.ipynb}}`

- 将笔记本转换为 `.py` 文件：

`jupytext --to py {{notebook.ipynb}}`

- 将 `.py` 文件转换为没有输出的笔记本：

`jupytext --to notebook {{notebook.py}}`

- 将 `.md` 文件转换为笔记本并运行它：

`jupytext --to notebook --execute {{notebook.md}}`

- 更新笔记本中的输入单元格并保留输出和元数据：

`jupytext --update --to notebook {{notebook.py}}`

- 更新笔记本的所有配对表示：

`jupytext --sync {{notebook.ipynb}}`
