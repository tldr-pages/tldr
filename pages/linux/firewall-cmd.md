# firewall-cmd

> The firewalld client.
> View and adapt the runtime or permanent firewall configuration state.
> More information: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- View all available firewall zones and rules in their runtime configuration state:

`firewall-cmd --list-all-zones`

- Permanently move the interface into the block zone, effectively blocking all communication:

`firewall-cmd --permanent --zone {{block}} --change-interface {{enp1s0}}`

- Permanently open the port for a service in the specified zone (like port 443 when in the `public` zone):

`firewall-cmd --permanent --zone {{public}} --add-service {{https}}`

- Permanently close the port for a service in the specified zone (like port 80 when in the `public` zone):

`firewall-cmd --permanent --zone {{public}} --remove-service {{http}}`

- Permanently forward a port for incoming packets in the specified zone (like port 443 to 8443 when entering the `public` zone):

`firewall-cmd --permanent --zone {{public}} --add-rich-rule 'rule family "{{ipv4|ipv6}}" forward-port port "{{443}}" protocol "{{udp|tcp}}" to-port "{{8443}}"'`

- Reload firewalld to lose any runtime changes and force the permanent configuration to take effect immediately:

`firewall-cmd --reload`

- Save the runtime configuration state to the permanent configuration:

`firewall-cmd --runtime-to-permanent`

- Enable panic mode in case of Emergency. All traffic is dropped, any active connection will be terminated:

`firewall-cmd --panic-on`
