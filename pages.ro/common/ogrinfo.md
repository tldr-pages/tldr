# ogrinfo

> Listați informații despre o sursă de date acceptată de OGER.
> Mai multe informaţii: <https://gdal.org/programs/ogrinfo.html>

- Lista straturilor unui GeoPackage:

`ogrinfo {{input}}.gpkg`

- Obțineți informații detaliate despre un anumit strat al unui GeoPackage:

`ogrinfo {{input}}.gpkg {{layer_name}}`

- Afișați doar informații sumare despre un anumit strat al unui GeoPackage:

`ogrinfo -so {{input}}.gpkg {{layer_name}}`
