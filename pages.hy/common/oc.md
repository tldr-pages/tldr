# oc

> OpenShift կոնտեյներային հարթակ CLI:.
> Թույլ է տալիս կիրառման և բեռնարկղերի կառավարում:.
> Լրացուցիչ տեղեկություններ. <https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/cli_tools/index>:.

- Մուտք գործեք OpenShift Container Platform սերվեր.:

`oc login`

- Ստեղծեք նոր նախագիծ.:

`oc new-project {{project_name}}`

- Անցում գոյություն ունեցող նախագծին.:

`oc project {{project_name}}`

- Ավելացրեք նոր հավելված նախագծին.:

`oc new-app {{repo_url}} --name {{application}}`

- Բացեք կեղևի հեռավոր նիստը կոնտեյների մեջ.:

`oc rsh {{pod_name}}`

- Թվարկեք պատյանները նախագծում.:

`oc get pods`

- Դուրս գալ ընթացիկ նստաշրջանից.:

`oc logout`
