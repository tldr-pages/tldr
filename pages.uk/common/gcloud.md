# gcloud

> Офіційний CLI інструмент для Google Cloud Platform.
> Примітка: підкоманди `gcloud` мають власну документацію щодо використання.
> Більше інформації: <https://cloud.google.com/sdk/gcloud>.

- Вивести всі властивості в активній конфігурації:

`gcloud config list`

- Увійти в обліковий запис Google:

`gcloud auth login`

- Встановити активний проект:

`gcloud config set project {{назва_проекту}}`

- SSH в екземпляр віртуальної машини:

`gcloud compute ssh {{користувач}}@{{екземпляр}}`

- Вивести всі екземпляри Google Compute Engine у проекті (за замовчуванням виводяться екземпляри з усіх зон):

`gcloud compute instances list`

- Оновити файл kubeconfig відповідними обліковими даними, щоб вказати `kubectl` на певний кластер у Google Kubernetes Engine (GKE):

`gcloud container clusters get-credentials {{назва_кластера}}`

- Оновити усі компоненти `gcloud`:

`gcloud components update`

- Вивести довідки для заданої команди:

`gcloud help {{команда}}`
