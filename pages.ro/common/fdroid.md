# fdroid

> F-Droid instrument de construire.
> F-Droid este un catalog instalabil de aplicații FOSS (Free and Open Source Software) pentru platforma Android.
> Mai multe informaţii: <https://f-droid.org/>

- Construiți o aplicație specifică:

`fdroid build {{app_id}}`

- Construiți o anumită aplicație într-un server de compilare VM:

`fdroid build {{app_id}} --server`

- Publicați aplicația în depozitul local:

`fdroid publish {{app_id}}`

- Instalați aplicația pe fiecare dispozitiv conectat:

`fdroid install {{app_id}}`

- Verificați dacă metadatele sunt formatate corect:

`fdroid lint --format {{app_id}}`

- Fixați formatarea automat (dacă este posibil):

`fdroid rewritemeta {{app_id}}`
