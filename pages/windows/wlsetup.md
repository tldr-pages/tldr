# wlsetup

> Install the Windows Live Essentials package into your computer.
> Note: Windows Live Essentials have been deprecated in favor of Microsoft 365.
> More information: <https://archive.org/details/windows_live_essentials_2012_qfe4_image>.

- Run the installer in normal, interactive GUI mode:

`wlsetup`

- Run the installer in unattended [q]uiet mode, running in background:

`wlsetup /q`

- Install the package with specific language support:

`wlsetup /language:{{language_code1,language_code2,...}}`

- Save the installation logs to a specific directory:

`wlsetup /log: "{{path\to\directory}}"`

- Enable verbose logging and save to a specific directory:

`wlsetup /verbose /log: "{{path\to\directory}}"`
