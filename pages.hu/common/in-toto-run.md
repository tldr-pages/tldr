# in-toto-run

> Link metaadatok generálása az ellátási lánc lépésének végrehajtása során. További információ: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>.

- Egy git-repó megjelölése és az így kapott linkfájl aláírása:

`in-toto-run -n {{tag}} --products {{.}} -k {{key_file}} -- {{git tag v1.0}}`

- Egy tarball létrehozása, a fájlok anyagként való tárolása és a tarball termékként való tárolása:

`in-toto-run -n {{package}} -m {{project}} -p {{project.tar.gz}} -- {{tar czf project.tar.gz project}}`

- Aláírt igazolások generálása a felülvizsgálati munkákhoz:

`in-toto-run -n {{review}} -k {{key_file}} -m {{document.pdf}} -x`

- A kép beolvasása a Trivy segítségével és linkfájl létrehozása:

`in-toto-run -n {{scan}} -k {{key_file}} -p {{report.json}} -- {{/bin/sh -c "trivy -o report.json -f json <IMAGE>"}}`
