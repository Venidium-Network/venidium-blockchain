Write-Output "setting up env vars"
$env:VENIDIUM_ROOT = "$env:HOMEDRIVE$env:HOMEPATH\.venidium\kition\"
[Environment]::SetEnvironmentVariable('VENIDIUM_ROOT', $env:VENIDIUM_ROOT, 'User')

Write-Output "Please wait. The installation will take some time"

Start-Process -WorkingDirectory (Get-Item .).FullName -FilePath "VenidiumSetup-1.0.3.exe" -ArgumentList "--silent" -Wait

Write-Output "Please wait. Kition testnet is now being configured"

& "$env:localappdata\venidium-blockchain\app-1.0.3\resources\app.asar.unpacked\daemon\Venidium.exe" init

$env:KEYS = & "$env:localappdata\venidium-blockchain\app-1.0.3\resources\app.asar.unpacked\daemon\Venidium.exe" keys show

if ( "$env:KEYS" -eq 'There are no saved private keys' )
{
    Write-Output "There are no keys"
    Write-Output "Generating new key"
    & "$env:localappdata\venidium-blockchain\app-1.0.3\resources\app.asar.unpacked\daemon\Venidium.exe" keys generate
}

& "$env:localappdata\venidium-blockchain\app-1.0.3\resources\app.asar.unpacked\daemon\Venidium.exe" configure --testnet true

Write-Output "Launching Venidium Blockchain"

Start-Process -WorkingDirectory "$env:localappdata\venidium-blockchain\app-1.0.3" -FilePath "$env:localappdata\venidium-blockchain\Venidium.exe"

# [Environment]::Exit(0)