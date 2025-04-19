# sphinx-build

> Sphinx documentation generator.
> More information: <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- Build documentation:

`sphinx-build {{[-b|--builder]}} {{html|epub|text|latex|man|...}} {{path/to/source_dir}} {{path/to/build_dir}}`

- Build documentations intended for readthedocs.io (requires the sphinx-rtd-theme pip package):

`sphinx-build {{[-b|--builder]}} {{html}} {{path/to/docs_dir}} {{path/to/build_dir}}`
