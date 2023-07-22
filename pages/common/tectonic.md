# tectonic

> A modern, self-contained TeX/LaTeX engine.
> More information: <https://github.com/tectonic-typesetting/tectonic>.

- Compile a standalone TeX/LaTeX file:

`tectonic -X compile {{file.tex}}`

- Compile standalone with synctex data:

`tectonic -X compile --synctex {{file.tex}}`

- Initialize a tectonic project in the current directory:

`tectonic -X init`

- Create a tectonic project in the specified directory:

`tectonic -X new {{project_name}}`

- Build the existing project in the current directory:

`tectonic -X build`

- Start a watcher to build the project in the current directory on change:

`tectonic -X watch`
