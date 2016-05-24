#Invoke file "PowerShell all_installations.ps1" in windows terminal
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | select DisplayName, Publisher, InstallDate
