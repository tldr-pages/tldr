# bluebuild

> ساخت Containerfileها و تصاویر سفارشی بر اساس `recipe.yml`.
> اطلاعات بیشتر: <https://github.com/blue-build/cli#how-to-use>.

- ساخت یک دستور ساخت:

`bluebuild build {{path/to/recipe.yml}}`

- اعتبارسنجی یک دستور ساخت:

`bluebuild validate {{path/to/recipe.yml}}`

- تولید یک Containerfile:

`bluebuild generate {{[-o|--output]}} {{Containerfile}} {{path/to/recipe.yml}}`

- تولید یک ISO از دستور ساخت:

`bluebuild generate-iso --output-dir {{path/to/output_directory}} --iso-name {{iso_name.iso}} recipe {{path/to/recipe.yml}}`

- نمایش راهنما:

`bluebuild {{[-h|--help]}}`
