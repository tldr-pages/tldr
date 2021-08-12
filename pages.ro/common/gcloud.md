# gcloud

> Instrumentul oficial CLI pentru Google Cloud Platform.
> Mai multe informaţii: <https://cloud.google.com/sdk/gcloud>

- Listează toate proprietățile în configurația activă a cuiva:

`gcloud config list`

- Conectați-vă la contul Google:

`gcloud auth login`

- Setați proiectul activ:

`gcloud config set project {{project_name}}`

- SSH într-o instanță mașină virtuală:

`gcloud compute ssh {{user}}@{{instance}} `

- Afișați toate instanțele Google Compute Engine într-un proiect. Instanțele din toate zonele sunt listate în mod implicit:

`gcloud compute instances list`

- Actualizați un fișier kubeconfig cu acreditările corespunzătoare pentru a indica kubectl la un anumit cluster în Google Kubernetes Engine:

`gcloud container clusters get-credentials {{cluster_name}}`

- Actualizaţi toate componentele CLI gcloud:

`gcloud components update`

- Arată ajutor pentru o anumită comandă:

`gcloud help {{command}}`
