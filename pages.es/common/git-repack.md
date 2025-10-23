# git repack

> Empaqueta los objetos no empaquetados en un repositorio de Git.  
> Más información: <https://git-scm.com/docs/git-repack>.

- Empaqueta los objetos no empaquetados en el directorio actual:

`git repack`

- También elimina los objetos redundantes después de empaquetar:

`git repack -d`

- Empaqueta todos los objetos en un solo paquete:

`git repack -a`

- Limita el empaquetado solo a los objetos locales:

`git repack -l`
