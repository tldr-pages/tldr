# fabric

> An open-source framework for augmenting humans using AI.
> Provides a modular framework for solving specific problems using a crowdsourced set of AI prompts.
> More information: <https://github.com/danielmiessler/fabric>.

- Run the setup to configure fabric:

`fabric --setup`

- List all available patterns:

`fabric --listpatterns`

- Run a pattern with input from a file:

`fabric --pattern {{pattern_name}} < {{path/to/input_file}}`

- Run a pattern on a YouTube video URL:

`fabric --youtube "{{https://www.youtube.com/watch?v=video_id}}" --pattern {{pattern_name}}`

- Chain patterns together by piping output from one to another:

`fabric --pattern {{pattern1}} | fabric --pattern {{pattern2}}`

- Run a custom user-defined pattern:

`fabric --pattern {{custom_pattern_name}}`

- Run a pattern and save the output to a file:

`fabric --pattern {{pattern_name}} --output {{path/to/output_file}}`

- Run a pattern with the specified variables:

`fabric --pattern {{pattern_name}} --variable "{{variable_name}}:{{value}}"`
