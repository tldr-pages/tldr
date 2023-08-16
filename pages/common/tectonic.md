# tectonic

> A modern, self-contained TeX/LaTeX engine.
> More information: <https://tectonic-typesetting.github.io/book/latest>.

- Compile a standalone TeX/LaTeX file:

`tectonic -X compile {{path/to/file.tex}}`

- Compile a standalone TeX/LaTeX file with synctex data:

`tectonic -X compile --synctex {{path/to/file.tex}}`

- Initialize a tectonic project in the current directory:

`tectonic -X init`

- Initialize a tectonic project in the specified directory:

`tectonic -X new {{project_name}}`

- Build the project in the current directory:

`tectonic -X build`

- Start a watcher to build the project in the current directory on change:

`tectonic -X watch`
