# scanimage

> Képek szkennelése a Scanner Access Now Easy API-val. További információ: <http://sane-project.org/man/scanimage.1.html>.

- Az elérhető szkennerek listázása a céleszköz csatlakoztatásának és felismerésének biztosítása érdekében:

`scanimage -L`

- Szkenneljen be egy képet, és mentse el egy fájlba:

`scanimage --format={{pnm|tiff|png|jpeg}} > {{path/to/new_image}}`
