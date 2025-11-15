# bluebuild

> Build Containerfiles and custom images based on your `recipe.yml`.
> More information: <https://github.com/blue-build/cli>.

- Build a recipe:

`bluebuild build {{path/to/recipe.yml}}`

- Validate a recipe:

`bluebuild validate {{path/to/recipe.yml}}`

- Generate a Containerfile:

`bluebuild generate {{[-o|--output]}} {{Containerfile}} {{path/to/recipe.yml}}`

- Generate an ISO from a recipe:

`bluebuild generate-iso --output-dir {{path/to/output_directory}} --iso-name {{iso_name.iso}} recipe {{path/to/recipe.yml}}`

- Display help:

`bluebuild {{[-h|--help]}}`
