# Test-NetConnection

> Display diagnostic information for a connection.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- Test a connection and display detailed results:

`Test-NetConnection -InformationLevel Detailed`

- Test a connection to a remote host using the specified port number:

`Test-NetConnection -ComputerName {{ip_or_hostname}} -Port {{port_number}}`
