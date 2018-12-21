# firewall-cmd

> The firewalld command line client.

- View the available firewall zones:

`firewall-cmd --get-active-zones`

- View the rules which are currently applied:

`firewall-cmd --list-all`

- Permanently open the port for a service in the specified zone (like port `443` when in the `public` zone):

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- Permanently close the port for a service in the specified zone (like port `80` when in the `public` zone):

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- Reload firewalld to force rule changes to take effect:

`firewall-cmd --reload`
