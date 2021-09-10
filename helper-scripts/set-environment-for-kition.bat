setx VENIDIUM_ROOT %HOMEDRIVE%%HOMEPATH%\.venidium\kition
md %HOMEDRIVE%%HOMEPATH%\.venidium %VENIDIUM_ROOT%

%localappdata%\venidium-blockchain\app-0.3.52\resources\app.asar.unpacked\daemon\Venidium.exe init
%localappdata%\venidium-blockchain\app-0.3.52\resources\app.asar.unpacked\daemon\Venidium.exe configure --testnet true
