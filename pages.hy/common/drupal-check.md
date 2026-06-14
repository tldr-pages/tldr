# drupal-check

> Ստուգեք Drupal PHP կոդը հնացումների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mglaman/drupal-check#usage>:.

- Ստուգեք կոդը կոնկրետ գրացուցակում հնացումների համար.:

`drupal-check {{path/to/directory}}`

- Ստուգեք կոդը՝ բացառելով ստորակետերով բաժանված դիրեկտորիաների ցանկը.:

`drupal-check {{[-e|--exclude-dir]}} {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}`

- Մի ցուցադրեք առաջընթացի գոտի.:

`drupal-check --no-progress {{path/to/directory}}`

- Կատարեք ստատիկ վերլուծություն՝ վատ կոդավորման պրակտիկաները հայտնաբերելու համար.:

`drupal-check {{[-a|--analysis]}} {{path/to/directory}}`
