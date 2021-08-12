# export

> Comandă pentru marcarea variabilelor shell în mediul curent pentru a fi exportate cu orice proces nou bifurcat copil.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/bash.html#index-export>

- Setați o nouă variabilă de mediu:

`export {{VARIABLE}}={{value}}`

- Eliminați o variabilă de mediu:

`export -n {{VARIABLE}}`

- Marcați o funcție shell pentru export:

`export -f {{FUNCTION_NAME}}`

- Adaugă ceva la variabila PATH:

`export PATH=$PATH:{{path/to/append}}`
