# lightgbm

> Gradient boosting framework using tree-based learning algorithms.
> More information: <https://lightgbm.readthedocs.io/en/latest/Quick-Start.html>.

- Train a model with a configuration file:

`lightgbm config={{path/to/config.txt}}`

- Train a model with specific parameters:

`lightgbm --boosting_type={{gbdt}} --objective={{binary}} --data={{path/to/train.txt}} --valid={{path/to/valid.txt}} --num_iterations={{100}} --learning_rate={{0.1}} --num_leaves={{31}}`

- Train a model with cross-validation:

`lightgbm --data={{path/to/train.txt}} --valid={{path/to/valid.txt}} --is_provide_training_metric={{1}} --num_iterations={{100}} --cv_folds={{5}}`

- Run only prediction from an existing model:

`lightgbm --task=predict --data={{path/to/test.txt}} --input_model={{path/to/model.txt}} --output_result={{path/to/predict.txt}}`

- Display help:

`lightgbm --help`
