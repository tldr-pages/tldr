# psexec

> Execute a command-line process on a remote machine.

> More information: <https://learn.microsoft.com/en-us/sysinternals/downloads/psexec>.

> Version 2.40

- Usage:

`psexec [\\computer[,computer2[,...] | @file]][-u user [-p psswd][-n s][-r servicename][-h][-l][-s|-e][-x][-i [session]][-c executable [-f|-v]][-w directory][-d][-<priority>][-a n,n,...] cmd [arguments]`

- Parameters / Descriptions:

`     computer :  The computer on which psexec will run command. Default = local system 
              To run against all computers in the current domain enter "\\*"`
               
`   @run_file : Run command on every computer listed in the text file specified.`

   `command :  Name of the program to execute on the remote machine.`

   `arguments : Arguments to pass (file paths must be absolute paths on the target system)`

   `-a n,n,... : Set processor affinity to n. Processors are numbered as 1,2,3,4 etc
              so to run the application on CPU 2 and CPU 4, enter: "-a 2,4"`

`   -c :        Copy the program (command)to the remote system for execution.`
   `-c -f :     Copy even if the file already exists on the remote system.`
   `-c -v :    Copy only if the file is a higher version or is newer than the remote copy.`
       `If you omit the -c option then the application must be in the system path on the remote system.`

   `-d :       Don’t wait for the application to terminate.
              Only use for non-interactive applications.`

   `-e :       Do NOT load the specified account’s profile.
              (In early versions of PSEXEC: Load the user account's profile, don’t use with -s)`

   `-f :       Copy the specified program even if the file already exists on the remote system.`

   `-h :        Run with the account's elevated token, if available. (Vista or higher)`

   `-i :        Interactive - Run the program so that it interacts with the desktop on the remote system.
              If no session is specified, the process runs in the console session.`

   `-l :        Limited - Run process as limited user.  Run with Low Integrity.
              Strips the Administrators group and allows only privileges assigned to the Users group.`

   `-n s :     Specify a timeout (s seconds) for connecting to the remote computer.`

   `-p psswd :  Specify a password for user (optional). Passed as clear text.
              If omitted, you will be prompted to enter a hidden password.`

   `-r :        The name of the remote service to create or interact with.`

   `-s :        Run remote process in the SYSTEM account (use with caution).`

   `-u user :   Specify a user name for login to remote computer(optional).`

   `-v :        Copy the specified file only if it has a higher version number or is newer
              than the one on the remote system.`

   `-w directory : Set the working directory of the process (relative to the remote computer).`

   `-x :        Display the UI on the Winlogon desktop (local system only).`

   `-low, -belownormal, -abovenormal, -high or -realtime :
              These options will run the process at a different priority.
              also -background (Vista and above) will run at low memory and I/O priority.`

   `-accepteula : Suppress the display of the license dialog.`

- Notes:

For PsExec to work, File and Printer sharing must be enabled on the remote computer. This can be done with netsh advfirewall or Group Policy (Local Computer Policy > User Configuration > Administrative Templates > Windows Components > Network Sharing)
You may also have to enable it under Control Panel > Network > Network Adapter > properties.

If you omit username the remote process will run in the same account from which you execute PsExec, but because the remote process is impersonating it will not have access to network resources on the remote system.

When you specify a username the remote process will execute in that account, and will have access to that account's network resources. If you do specify an alternative username/password, then PsExec will send the logon password in clear text. This can be a security risk if unauthorized network sniffers could intercept traffic between the local and remote system.

PsExec can be used to start GUI applications, but in that case the GUI will appear on the remote machine.

Input is passed to the remote system when you press the enter key - typing Ctrl-C will terminate the remote process.

PsExec does not require you to be an administrator of the local filesystem, with the correct password psexec will allow UserA to run commands as UserB - a Runas replacement.

If you kill a PsExec process, you might also need to manually remove the background service:
sc.exe \\workstation64 delete psexesvc

PsExec can also be used to start a process (on a remote or local machine) as SYSTEM, this is a very privileged account similar to root on a UNIX machine ~ use with extreme caution.

Error codes returned by PsExec are specific to the applications you execute, not PsExec.

