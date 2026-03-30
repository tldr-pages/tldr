# brew install

> Instala una fórmula o cask de Homebrew.
> Más información: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Instala una fórmula o cask:

`brew install {{formula|cask}}`

- Compila e instala una fórmula desde el código fuente (las dependencias se seguirán instalando desde bottles):

`brew install {{[-s|--build-from-source]}} {{formula}}`

- Descarga el manifiesto, muestra lo que se instalaría pero sin instalar nada:

`brew install {{[-n|--dry-run]}} {{formula|cask}}`
