#գսուտիլ

> Մուտք գործեք Google Cloud Storage:.
> Դուք կարող եք օգտագործել `gsutil`՝ դույլերի և օբյեկտների կառավարման առաջադրանքների լայն շրջանակ կատարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/storage/docs/gsutil>:.

- Թվարկեք բոլոր դույլերը մի նախագծի մեջ, որում դուք մուտք եք գործել.:

`gsutil ls`

- Թվարկե՛ք առարկաները դույլով.:

`gsutil ls -r 'gs://{{bucket_name}}/{{prefix}}**'`

- Ներբեռնեք օբյեկտը դույլից.:

`gsutil cp gs://{{bucket_name}}/{{object_name}} {{path/to/save_location}}`

- Վերբեռնեք օբյեկտը դույլի մեջ.:

`gsutil cp {{object_location}} gs://{{destination_bucket_name}}/`

- Վերանվանեք կամ տեղափոխեք առարկաները դույլով.:

`gsutil mv gs://{{bucket_name}}/{{old_object_name}} gs://{{bucket_name}}/{{new_object_name}}`

- Ստեղծեք նոր դույլ այն նախագծում, որտեղ մուտք եք գործել.:

`gsutil mb gs://{{bucket_name}}`

- Ջնջել դույլը և հեռացնել դրա մեջ գտնվող բոլոր առարկաները.:

`gsutil rm -r gs://{{bucket_name}}`
