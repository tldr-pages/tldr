# twine

> Segédprogram Python csomagok közzétételéhez a PyPI-n. További információ: <https://twine.readthedocs.io/en/stable/#commands>.

- Feltöltés a PyPI-ra:

`twine upload dist/*`

- Feltöltés a Test PyPI \[r\]epositoryba, hogy ellenőrizze, hogy minden rendben van-e:

`twine upload -r testpypi dist/*`

- Feltöltés a PyPI-be egy megadott \[u\]sername és \[p\]assword azonosítóval:

`twine upload -u {{username}} -p {{password}} dist/*`

- Feltöltés egy alternatív tároló URL címére:

`twine upload --repository-url {{repository_url}} dist/*`

- Ellenőrizze, hogy a disztribúció hosszú leírása helyesen jelenjen meg a PyPI-n:

`twine check dist/*`

- Feltöltés egy adott pypirc konfigurációs fájl használatával:

`twine upload --config-file {{configuration_file}} dist/*`

- A fájlok feltöltésének folytatása, ha már létezik egy (csak a PyPI-ba való feltöltéskor érvényes):

`twine upload --skip-existing dist/*`

- Feltöltés a PyPI-ba részletes információkat mutatva:

`twine upload --verbose dist/*`
