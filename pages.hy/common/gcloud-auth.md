# gcloud auth

> Տրամադրել և չեղարկել թույլտվությունը `gcloud`-ին և կառավարել հավատարմագրերը:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/auth>:.

- Թույլատրեք Google Cloud մուտքը `gcloud` CLI-ի համար Google Cloud-ի օգտատերերի հավատարմագրերով և ընթացիկ հաշիվը սահմանեք որպես ակտիվ.:

`gcloud auth login`

- Թույլատրել Google Cloud-ի մուտքը, որը նման է `gcloud auth login`-ին, բայց ծառայության հաշվի հավատարմագրերով.:

`gcloud auth activate-service-account`

- Կառավարեք հավելվածի լռելյայն հավատարմագրերը (ADC) Cloud Client գրադարանների համար.:

`gcloud auth application-default`

- Ցուցադրել Google Cloud հաշիվների ցանկը, որոնք ներկայումս վավերացված են ձեր համակարգում.:

`gcloud auth list`

- Ցուցադրել ընթացիկ հաշվի մուտքի նշանը.:

`gcloud auth print-access-token`

- Հեռացրեք մուտքի հավատարմագրերը հաշվի համար.:

`gcloud auth revoke`
