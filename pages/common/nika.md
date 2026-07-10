# nika

> Run AI workflows written as checkable YAML files.
> Workflows are audited (schema, permissions, cost) before any token is spent.
> More information: <https://docs.nika.sh>.

- Initialize the current repository (schema wiring, agent guides, editor rules):

`nika init`

- Audit a workflow without running it (schema, permissions, honest cost floor):

`nika check {{path/to/workflow.nika.yaml}}`

- Run a workflow:

`nika run {{path/to/workflow.nika.yaml}}`

- Run overriding a declared variable:

`nika run {{path/to/workflow.nika.yaml}} --var {{name}}={{value}}`

- Create a workflow from an embedded skeleton:

`nika new --from {{chain}} {{path/to/workflow.nika.yaml}}`

- Explain a diagnostic code:

`nika explain {{NIKA-1401}}`

- Verify the tamper-evident trace of the latest run:

`nika trace verify`

- Check provider credentials and local model servers:

`nika doctor`
