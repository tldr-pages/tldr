# soupault

> Soupault is a static website generator based on HTML element tree rewriting.
> It can also be used as an HTML post-processor or metadata extractor.
> More information: <https://soupault.app>.

- Initialize a minimal website project in the current working directory:

`soupault --init`

- Build a website:

`soupault`

- Override default config file and directory locations:

`soupault --config {{config_path}} --site-dir {{input_dir}} --build-dir {{output_dir}}`

- Extract metadata into a JSON file without generating pages:

`soupault --index-only --dump-index-json {{path/to/file.json}}`

- Show the effective config (values from `soupault.toml` plus defaults):

`soupault --show-effective-config`
