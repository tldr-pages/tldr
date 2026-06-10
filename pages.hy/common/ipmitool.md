# ipmitool

> Ինտերֆեյս խելացի պլատֆորմի կառավարման ինտերֆեյսի (IPMI) հետ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ipmitool>:.

- Բացեք IPMI կեղևը տեղական սարքաշարի վրա.:

`sudo ipmitool shell`

- Բացեք IPMI կեղևը հեռավոր հոսթի վրա.:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
