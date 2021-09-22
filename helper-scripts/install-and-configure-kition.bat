@ECHO off
@setlocal EnableDelayedExpansion



@set LF=^


@SET command=#
@FOR /F "tokens=*" %%i in ('findstr -bv @ "%~f0"') DO SET command=!command!!LF!%%i
@powershell -noprofile -noexit -command !command! & goto:eof


# *** POWERSHELL CODE STARTS HERE *** #
setx VENIDIUM_ROOT "$env:HOMEDRIVE$env:HOMEPATH\.venidium\kition"

Write-Output "`n`nPlease wait. The installation will take some time`n`n"

Start-Process -WorkingDirectory (Get-Item .).FullName -FilePath "VenidiumSetup-0.4.0.exe" -ArgumentList "--silent" -Wait

Write-Output "`n`nPlease wait. Kition testnet is now being configured`n`n"

& "$env:localappdata\venidium-blockchain\app-0.4.0\resources\app.asar.unpacked\daemon\Venidium.exe" init
& "$env:localappdata\venidium-blockchain\app-0.4.0\resources\app.asar.unpacked\daemon\Venidium.exe" keys generate
& "$env:localappdata\venidium-blockchain\app-0.4.0\resources\app.asar.unpacked\daemon\Venidium.exe" configure --testnet true

Write-Output "`n`nLaunching Venidium Blockchain`n`n"

Start-Process -WorkingDirectory "$env:localappdata\venidium-blockchain\app-0.4.0" -FilePath "$env:localappdata\venidium-blockchain\Venidium.exe"

[Environment]::Exit(0)