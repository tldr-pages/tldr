# poetry

> Python தொகுதிகள் மற்றும் சார்புகளை நிர்வகிக்க.
> சில துணைக் கட்டளைகள் (`about`, `check`, `env` etc) தனித்தனி பயன்பாட்டு ஆவணங்களைக் கொண்டுள்ளன.
> இதையும் பார்க்கவும்: `asdf`, `pipenv`, `hatch`.
> மேலும் தகவல்: <https://python-poetry.org/docs/cli/>.

- குறிப்பிட்ட பெயருடன் புதிய Poetry திட்டத்தை அடைவில் உருவாக்கு:

`poetry new {{project_name}}`

- ஒரு சார்பையும் அதன் துணை சார்புகளையும் நிறுவி `pyproject.toml` கோப்பில் சேர்க்க:

`poetry add {{dependency}}`

- தற்போதைய அடைவில் உள்ள `pyproject.toml` கோப்பைப் பயன்படுத்தி திட்ட சார்புகளை நிறுவு:

`poetry install`

- தற்போதைய அடைவை புதிய Poetry திட்டமாக இன்டராக்டிவாக (அல்லது `-n` சேர்த்து non-interactive ஆக) தொடங்கு:

`poetry init`

- அனைத்து சார்புகளின் சமீபத்திய பதிப்பைப் பெற்று `poetry.lock` கோப்பை புதுப்பிக்க:

`poetry update`

- திட்டத்தின் virtual environment இல் ஒரு கட்டளையை இயக்கு:

`poetry run {{command}}`

- திட்டத்தின் பதிப்பை `pyproject.toml` கோப்பில் மாற்று:

`poetry version {{patch|minor|major|prepatch|preminor|premajor|prerelease}}`

- திட்டத்தின் virtual environment இல் ஒரு shell திறக்க (2.0 க்குக் கீழே உள்ள பதிப்புகளுக்கு `poetry shell` பயன்படுத்தவும்):

`eval "$(poetry env activate)"`
