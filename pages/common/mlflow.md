# mlflow

> Track machine learning experiments, package projects, and deploy models.
> More information: <https://mlflow.org/docs/latest/api_reference/cli.html>.

- Start the tracking UI server on a specific host and port:

`mlflow ui --host {{127.0.0.1}} --port {{5000}}`

- Start the full tracking server with a specific backend database and artifact directory:

`mlflow server --backend-store-uri {{sqlite:///mlflow.db}} --default-artifact-root {{path/to/artifacts_directory}}`

- Run an MLflow project from a local directory or Git repository URI:

`mlflow run {{uri}} --experiment-name {{experiment_name}}`

- Serve a registered or local model as a REST API endpoint on a specific port:

`mlflow models serve --model-uri {{runs:/run_id/model}} --port {{5001}}`

- Upgrade an MLflow tracking database schema to the latest revision:

`mlflow db upgrade {{database_uri}}`

- Permanently delete run metadata and artifacts for soft-deleted runs:

`mlflow gc --backend-store-uri {{sqlite:///mlflow.db}}`

- Print diagnostic information including Python environment and MLflow version:

`mlflow doctor`
