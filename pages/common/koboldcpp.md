# koboldcpp

> An AI text-generation application for GGML and GGUF models.
> More information: <https://github.com/LostRuins/koboldcpp/wiki#command-line-arguments-reference>.

- Load one or more model files:

`koboldcpp {{[-m|--model]}} {{path/to/model_file}}`

- Set port to listen on (defaults to 5001):

`koboldcpp --port {{port}}`

- Set amount of threads to use:

`koboldcpp {{[-t|--threads]}} {{amount_of_threads}}`

- Launch web browser when boot is complete:

`koboldcpp --launch`

- Start without the GUI launcher:

`koboldcpp --skiplauncher`
