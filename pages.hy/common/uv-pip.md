# ուլտրամանուշակագույն պիպ

> Ապահովում է pip-ի նման հրամաններ փաթեթների տեղադրման, տեղահանման և կառավարման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-pip>:.

- Տեղադրեք փաթեթ.:

`uv pip install {{package}}`

- Տեղադրեք փաթեթներ պահանջների ֆայլից.:

`uv pip install {{[-r|--requirements]}} {{requirements.txt}}`

- Տեղադրեք փաթեթ հատուկ տարբերակով.:

`uv pip install {{package==1.2.3}}`

- Ապատեղադրել փաթեթը.:

`uv pip uninstall {{package}}`

- Կողպեք կախվածությունները `pyproject.toml`-ից մինչև `requirements.txt`:

`uv pip compile pyproject.toml {{[-o|--output-file]}} requirements.txt`

- Տեղադրված փաթեթների ցանկ.:

`uv pip list`

- Ցույց տալ տեղեկատվություն տեղադրված փաթեթի մասին.:

`uv pip show {{package}}`

- Համաժամեցրեք միջավայրը պահանջների ֆայլի հետ (տեղադրեք/տեղահանեք՝ ճշգրիտ համապատասխանելու համար).:

`uv pip sync {{requirements.txt}}`
