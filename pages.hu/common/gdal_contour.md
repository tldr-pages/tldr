# gdal_contour

> Kontúrvonalak és sokszögek létrehozása digitális domborzati modellből. További információ: <https://gdal.org/programs/gdal_contour.html>.

- Hozzon létre egy vektoros adatkészletet 100 méteres \[i\]ntervallumra kiterjedő kontúrvonalakkal, miközben a magassági tulajdonságot "ele"-ként adja meg:

`gdal_contour -a {{ele}} -i {{100.0}} {{path/to/input.tif}} {{path/to/output.gpkg}}`

- Vektoros adatállomány létrehozása 100 méteres \[i\]ntervallumra kiterjedő \[p\]oligonokkal:

`gdal_contour -i {{100.0}} -p {{path/to/input.tif}} {{path/to/output.gpkg}}`
