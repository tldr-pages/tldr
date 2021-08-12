# drupal-check

> Verificați codul PHP Drupal pentru deprecieri.
> Mai multe informaţii: <https://github.com/mglaman/drupal-check>

- Verificați codul dintr-un anumit director pentru deprecieri:

`drupal-check {{path/to/directory}}`

- Verificați codul cu excepția unei liste separate prin virgulă de directoare:

`drupal-check --exclude-dir {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}`

- Nu afișa o bară de progres:

`drupal-check --no-progress {{path/to/directory}}`

- Efectuați analize statice pentru a detecta practicile proaste de codificare:

`drupal-check --analysis {{path/to/directory}}`
