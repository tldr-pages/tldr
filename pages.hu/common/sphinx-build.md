# sphinx-build

> Sphinx dokumentáció generátor. További információ: <http://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- Dokumentáció készítése:

`sphinx-build -b {{html|epub|text|latex|man|...}} {{path/to/source_dir}} {{path/to/build_dir}}`

- Dokumentációk készítése a readthedocs.io számára (a sphinx-rtd-theme pip csomagot igényli):

`sphinx-build -b {{html}} {{path/to/docs_dir}} {{path/to/build_dir}}`
