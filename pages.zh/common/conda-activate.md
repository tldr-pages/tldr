# conda activate

> 激活一个 conda 环境。
> 另请参阅：使用 `conda deactivate` 来取消激活环境。
> 更多信息：<https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>.

- 激活现存名为 `myenv` 的环境：

`conda activate myenv`

- 激活位于特定路径的环境：

`conda activate {{路径/到/我的环境}}`

- 将 `myenv` 环境堆积在先前的环境上，让两个环境的程序库/命令/变量都能够被访问：

`conda activate --stack myenv`

- 启动干净的 `myenv` 环境，不执行堆积（先前环境中的程序库/命令/变量将不可访问）：

`conda activate --no-stack myenv`

- 展示帮助：

`conda activate {{[-h|--help]}}`
