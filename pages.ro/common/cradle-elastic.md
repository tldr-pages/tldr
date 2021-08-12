# cradle elastic

> Gestionați instanțele ElasticSearch pentru o instanță Cradle.
> Mai multe informaţii: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>

- Trunchierea indexului ElasticSearch:

`cradle elastic flush`

- Trunchierea indexului ElasticSearch pentru un anumit pachet:

`cradle elastic flush {{package_name}}`

- Trimiteți schema ElasticSearch:

`cradle elastic map`

- Trimiteți schema ElasticSearch pentru un anumit pachet:

`cradle elastic map {{package_name}}`

- Populați indicii ElasticSearch pentru toate pachetele:

`cradle elastic populate`

- Populați indicii ElasticSearch pentru un anumit pachet:

`cradle elastic populate {{package_name}}`
