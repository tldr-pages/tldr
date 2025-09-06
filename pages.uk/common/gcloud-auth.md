# gcloud auth

> Видача та скасування авторизації для `gcloud` і керування обліковими даними.
> Дивіться також: `gcloud`.
> Більше інформації: <https://cloud.google.com/sdk/gcloud/reference/auth>.

- Авторизувати доступ до Google Cloud для `gcloud` CLI за допомогою облікових даних користувача Google Cloud і встановити поточний обліковий запис як активний:

`gcloud auth login`

- Авторизувати доступ до Google Cloud, подібно до `gcloud auth login`, але за допомогою облікових даних сервісного облікового запису:

`gcloud auth activate-service-account`

- Керувати Application Default Credentials (ADC) для хмарних клієнтських бібліотек:

`gcloud auth application-default`

- Вивести список облікових записів Google Cloud, які зараз автентифіковані у вашій системі:

`gcloud auth list`

- Вивести токен (token) доступу поточного облікового запису:

`gcloud auth print-access-token`

- Видалити облікові дані доступу до облікового запису:

`gcloud auth revoke`
