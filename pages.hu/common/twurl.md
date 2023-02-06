# twurl

> Curl-szerű parancs, de kifejezetten a Twitter API-ra szabva. További információ: <https://github.com/twitter/twurl>.

- A `twurl` engedélyezése a Twitter-fiókhoz való hozzáférésre:

`twurl authorize --consumer-key {{twitter_api_key}} --consumer-secret {{twitter_api_secret}}`

- Tegyen GET-kérést egy API végponthoz:

`twurl -X GET {{twitter_api_endpoint}}`

- POST-kérés készítése egy API-végponthoz:

`twurl -X POST -d '{{endpoint_params}}' {{twitter_api_endpoint}}`

- Média feltöltése a Twitterre:

`twurl -H "{{twitter_upload_url}}" -X POST "{{twitter_upload_endpoint}}" --file "{{path/to/media.jpg}}" --file-field "media"`

- Hozzáférés egy másik Twitter API tárhelyhez:

`twurl -H {{twitter_api_url}} -X GET {{twitter_api_endpoint}}`

- Alias létrehozása egy kért erőforráshoz:

`twurl alias {{alias_name}} {{resource}}`
