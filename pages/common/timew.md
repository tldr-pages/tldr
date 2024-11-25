# timew

> A time tracking tool used to measure the duration of activities.
> More information: <https://timewarrior.net/docs>.

- Start tracking an activity:

`timew start`

- Tag current activity:

`timew tag {{activity_tag}}`

- Start and tag a new activity being tracked:

`timew start {{activity_tag}}`

- Stop current activity:

`timew stop`

- Track an activity in the past:

`timew track {{start_time} - {{end_time}} {{activity_tag}}`

- View tracked items of the day:

`timew summary`

- View report for last day, week, current month etc:

`timew summary :{{today|yesterday|week|lastweek|month|lastmonth|year|lastyear}}`
