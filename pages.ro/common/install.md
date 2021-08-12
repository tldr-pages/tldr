# install

> Copiați fișiere și setați atributele.
> Copiați fișiere (adesea executabile) într-o locație de sistem, cum ar fi `/usr/local/bin`, dați-le permisiunile/dreptul de proprietate corespunzătoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/install>

- Copiați fișierele la destinație:

`install {{path/to/source}} {{path/to/destination}}`

- Copiați fișierele la destinație, stabilind proprietatea lor:

`install -o {{user}} {{path/to/source}} {{path/to/destination}}`

- Copiați fișierele la destinație, setând proprietatea lor de grup:

`install -g {{user}} {{path/to/source}} {{path/to/destination}}`

- Copierea fişierelor la destinaţie, setarea lor `mod':

`install -m {{+x}} {{path/to/source}} {{path/to/destination}}`

- Copiați fișierele și aplicați timpii de accesare/modificare a sursei la destinație:

`install -p {{path/to/source}} {{path/to/destination}}`
