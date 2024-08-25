[ENV=VAL ...] proctl <flag>

-initialize      -i @project_name       initialize a git repo for a project
-list-licenses   -ll                    list available licenses
-list-languages  -lL                    list available languages
-current-license -c                     show current active project license
-pick-license    -pl                    pick a license in a FZF menu
-pick-language   -pL                    pick a language in a FZF menu
-preview-license -P @license_name       preview a license template
-remove-license  -r                     remove all licenses from the current project
-search-license  -sl '<query | patten>' search for license
    -search-language -sL '<query | patten>' search for language
-template-help   -T                     print help for templating
-new-template    -t                     create a new license template
-delete-license  -R @license_name ...   delete a license from templates
-new-config      -C                     create a default config overwriting current one
-check-conflict  -k                     check if current licene(s) are conflicting

-help            -h                     show this helpful list of commands

PROCTL_COLOURS=0|[1]                    turn colour on (1) or off (0) [1]
