# jupyter

> Aplicação web para criar e compartilhar documentos que contem código, visualizações e anotações.
> Usado principalmente para análise de dados, computação científica e aprendizado de máquinas (machine learning).
> Mais informações: <https://jupyter.org>.

- Inicia um servidor de notebooks Jupyter no diretório atual:

`jupyter notebook`

- Abre um caderno Jupyter específico:

`jupyter notebook {{exemplo.ipynb}}`

- Exporta um caderno Jupyter específico para outro formato:

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{exemplo.ipynb}}`

- Inicia um servidor em uma porta específica:

`jupyter notebook --port={{porta}}`

- Lista de servidores de notebooks atualmente em funcionamento:

`jupyter notebook list`

- Para o servidor atualmente em funcionamento:

`jupyter notebook stop`

- Inicia o JupyterLab, se instalado, no diretório atual:

`jupyter lab`
