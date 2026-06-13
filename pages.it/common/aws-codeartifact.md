# aws codeartifact

> Gestisce repository CodeArtifact, domini, pacchetti, versioni di pacchetti e asset.
> CodeArtifact è un repository di artefatti compatibile con gestori di pacchetti e strumenti di build popolari come Maven, Gradle, npm, Yarn, Twine, pip, NuGet e SwiftPM.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/codeartifact/>.

- Elenca i domini disponibili per il tuo account AWS:

`aws codeartifact list-domains`

- Genera credenziali per un gestore di pacchetti specifico:

`aws codeartifact login --tool {{npm|pip|twine}} --domain {{tuo_dominio}} --repository {{nome_repository}}`

- Ottieni l'URL endpoint di un repository CodeArtifact:

`aws codeartifact get-repository-endpoint --domain {{tuo_dominio}} --repository {{nome_repository}} --format {{npm|pypi|maven|nuget|generic}}`

- Visualizza l'aiuto:

`aws codeartifact help`

- Visualizza l'aiuto per un sottocomando specifico:

`aws codeartifact {{sottocomando}} help`
