# gsutil

> Доступ до Google Cloud Storage.
> Ви можете використовувати `gsutil` для виконання широкого діапазону завдань із керування контейнерами (buckets) та об’єктами.
> Більше інформації: <https://cloud.google.com/storage/docs/gsutil>.

- Вивести всі контейнери (buckets) в проекті, до якого ви ввійшли:

`gsutil ls`

- Вивести об’єкти у контейнері (bucket):

`gsutil ls -r 'gs://{{bucket_name}}/{{prefix}}**'`

- Завантажити об'єкт із контейнера (bucket):

`gsutil cp gs://{{bucket_name}}/{{ім'я_об'єкта}} {{шлях/де/зберегти_розташування}}`

- Завантажити об’єкт у контейнер (bucket):

`gsutil cp {{місцезнаходження_об'єкта}} gs://{{destination_bucket_name}}/`

- Перейменувати або перемістіти об’єкти у контейнері (bucket):

`gsutil mv gs://{{bucket_name}}/{{старе_ім'я_об'єкта}} gs://{{bucket_name}}/{{нове_ім'я_об'єкта}}`

- Створити новий контейнер (bucket) в проекті, у який ви ввійшли:

`gsutil mb gs://{{bucket_name}}`

- Видалити контейнер (bucket) та видалити всі об’єкти в ньому:

`gsutil rm -r gs://{{bucket_name}}`
