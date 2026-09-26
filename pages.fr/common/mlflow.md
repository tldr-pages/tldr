# mlflow

> Plateforme de suivi d’expériences, de gestion de modèles et de déploiement pour les projets de machine learning.
> Plus d'informations : <https://mlflow.org/docs/latest/api_reference/cli.html>.

- Démarre uniquement l’interface web locale:

`mlflow ui --port 5000`

- Démarre un serveur accessible depuis le réseau local:

`mlflow server --host 0.0.0.0 --port 5000`

- Démarre un serveur en spécifiant des URI pour les données d'expériences et artefacts:

`mlflow server --backend-store-uri sqlite:///mlflow.db --artifacts-destination ./mlartifacts`

- Met à niveau le schéma d’une base de données MLflow après une mise à jour de MLflow:

`mlflow db upgrade sqlite:///mlflow.db`

- Exécute un point d’entrée avec des paramètres personnalisés:

`mlflow run . --entry-point train --parameter learning_rate=0.001 --parameter epochs=20`

- Télécharge tous les artefacts d’un run:

`mlflow artifacts download --run-id {{identifiant_du_run}} --dst-path ./artifacts`

- Démarre un serveur d’inférence pour un modèle enregistré dans un run:

`mlflow models serve --model-uri runs:/{{identifiant_du_run}}/model --port 5001`
