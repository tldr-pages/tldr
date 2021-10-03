# ssh_config

> Put ssh parameters in a configuration file
> More information: <https://www.openssh.com/>

- Create a section with host specific settings
- Put the following in ~/.ssh/config (user specific) or /etc/ssh/ssh_config (global)

```
Host {{your host alias}}
    HostName {{host IP address or FQDN}}
    IdentityFile {{file containing ssh private key for host}}
    User {{host user name}}
```