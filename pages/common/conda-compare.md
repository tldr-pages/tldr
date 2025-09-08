# conda compare

> Compare packages between conda environments.
> More information: <https://docs.conda.io/projects/conda/en/stable/commands/compare.html>.

- Compare packages in the current directory to packages from the file `file.yml`:

`conda compare file.yml`

- Compare packages in environment [n]amed `myenv` to packages from the file `file.yml`:

`conda compare {{[-n|--name]}} myenv {{/path/to/file.yml}}`

- Compare packages in environment `myenv` at custom [p]ath (i.e. [p]refix) to packages from the file `file.yml`:

`conda compare {{[-p|--prefix]}} {{/path/to/myenv}} {{/path/to/file.yml}}`

- Display detailed [h]elp message:

`conda create {{[-h|--help]}}`
