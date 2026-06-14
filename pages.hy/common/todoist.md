# todoist

> Մուտք գործեք <https://todoist.com> հրամանի տողից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sachaos/todoist#usage>:.

- Ավելացրեք առաջադրանք.:

`todoist {{[a|add]}} "{{task_name}}"`

- Ավելացրեք բարձր առաջնահերթ խնդիր պիտակի, նախագծի և ժամկետի հետ.:

`todoist {{[a|add]}} "{{task_name}}" --priority {{1}} --label-ids "{{label_id}}" --project-name "{{project_name}}" --date "{{tmr 9am}}"`

- Արագ ռեժիմով ավելացրեք բարձր առաջնահերթ խնդիր պիտակի, նախագծի և ժամկետի հետ.:

`todoist {{[q|quick]}} '#{{project_name}} "{{tmr 9am}}" p{{1}} {{task_name}} @{{label_name}}'`

- Թվարկեք բոլոր առաջադրանքները վերնագրով և գույնով.:

`todoist --header --color list`

- Թվարկեք բոլոր առաջնահերթ խնդիրները.:

`todoist {{[l|list]}} --filter p{{1}}`

- Թվարկեք այսօրվա առաջադրանքները բարձր առաջնահերթությամբ, որոնք ունեն նշված պիտակը.:

`todoist {{[l|list]}} --filter '(@{{label_name}} | {{today}}) & p{{1}}'`
