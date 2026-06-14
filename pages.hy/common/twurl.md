#պտույտ

> Curl նման հրաման, բայց հատուկ հարմարեցված Twitter API-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/twitter/twurl#getting-started>:.

- Թույլատրել `twurl`-ին Twitter-ի հաշիվ մուտք գործելու համար.:

`twurl authorize {{[-c|--consumer-key]}} {{twitter_api_key}} {{[-s|--consumer-secret]}} {{twitter_api_secret}}`

- GET հարցում կատարեք API-ի վերջնակետին.:

`twurl {{[-X|--request-method]}} GET {{twitter_api_endpoint}}`

- Կատարեք POST հարցում API-ի վերջնակետին.:

`twurl {{[-X|--request-method]}} POST {{[-d|--data]}} '{{endpoint_params}}' {{twitter_api_endpoint}}`

- Վերբեռնեք մեդիա Twitter.:

`twurl {{[-H|--host]}} "{{twitter_upload_url}}" {{[-X|--request-method]}} POST "{{twitter_upload_endpoint}}" {{[-f|--file]}} "{{path/to/media.jpg}}" {{[-F|--file-field]}} "media"`

- Մուտք գործեք Twitter API-ի մեկ այլ հոսթ.:

`twurl {{[-H|--host]}} {{twitter_api_url}} {{[-X|--request-method]}} GET {{twitter_api_endpoint}}`

- Ստեղծեք այլանուն պահանջվող ռեսուրսի համար.:

`twurl alias {{alias_name}} {{resource}}`
