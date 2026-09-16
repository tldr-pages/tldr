# mlflow

> A platform to track experiments, manage models, and deploy machine learning projects.
> Some subcommands, such as `server`, `run`, `db`, `artifacts`, and `models`, have their own documentation.
> More information: <https://mlflow.org/docs/latest/api_reference/cli.html>.

- Start only the local web interface:

`mlflow ui --port 5000`

- Start a server accessible from the local network:

`mlflow server --host 0.0.0.0 --port 5000`

- Start a server by specifying URIs for experiment data and artifacts:

`mlflow server --backend-store-uri sqlite:///mlflow.db --artifacts-destination ./mlartifacts`

- Upgrade the schema of an MLflow database after an MLflow update:

`mlflow db upgrade sqlite:///mlflow.db`

- Run an entry point with custom parameters:

`mlflow run . --entry-point train --parameter learning_rate=0.001 --parameter epochs=20`

- Download all artifacts from a run:

`mlflow artifacts download --run-id {{run_id}} --dst-path ./artifacts`

- Start an inference server for a model saved in a run:

`mlflow models serve --model-uri runs:/{{run_id}}/model --port 5001`
