setx VENIDIUM_ROOT "$env:HOMEDRIVE$env:HOMEPATH\.venidium\kition"

Write-Output "`n`nPlease wait. The installation will take some time`n`n"

Start-Process -WorkingDirectory (Get-Item .).FullName -FilePath "VenidiumSetup-0.3.73.exe" -ArgumentList "--silent" -Wait

Write-Output "`n`nPlease wait. Kition testnet is now being configured`n`n"

& "$env:localappdata\venidium-blockchain\app-0.3.73\resources\app.asar.unpacked\daemon\Venidium.exe" init
& "$env:localappdata\venidium-blockchain\app-0.3.73\resources\app.asar.unpacked\daemon\Venidium.exe" keys generate
& "$env:localappdata\venidium-blockchain\app-0.3.73\resources\app.asar.unpacked\daemon\Venidium.exe" configure --testnet true

Write-Output "`n`nLaunching Venidium Blockchain`n`n"

Start-Process -WorkingDirectory "$env:localappdata\venidium-blockchain\app-0.3.73" -FilePath "$env:localappdata\venidium-blockchain\Venidium.exe"

[Environment]::Exit(0)