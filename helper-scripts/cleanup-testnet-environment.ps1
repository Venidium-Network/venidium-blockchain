$quit = 0

function Simple-Menu {
    Param(
        [Parameter(Position=0, Mandatory=$True)]
        [string[]]$MenuItems,
        [string] $Title
    )

    $header = $null
    if (![string]::IsNullOrWhiteSpace($Title)) {
        $len = [math]::Max(($MenuItems | Measure-Object -Maximum -Property Length).Maximum, $Title.Length)
        $header = '{0}{1}{2}' -f $Title, [Environment]::NewLine, ('-' * $len)
    }

    # possible choices: didits 1 to 9, characters A to Z
    $choices = (49..57) + (65..90) | ForEach-Object { [char]$_ }
    $i = 0
    $items = ($MenuItems | ForEach-Object { '[{0}]  {1}' -f $choices[$i++], $_ }) -join [Environment]::NewLine

    # display the menu and return the chosen option
    while ($true) {
        cls
        if ($header) { Write-Host $header -ForegroundColor Yellow }
        Write-Host $items
        Write-Host

        $answer = (Read-Host -Prompt 'Please make your choice').ToUpper()
        $index  = $choices.IndexOf($answer[0])

        if ($index -ge 0 -and $index -lt $MenuItems.Count) {
            return $MenuItems[$index]
        }
        else {
            Write-Warning "Invalid choice.. Please try again."
            Start-Sleep -Seconds 2
        }
    }
}

$cleanupMenu = 'Cleanup the whole venidium directory (highly recommended)', 'Cleanup only the Mainnet directory (not recommended)', 'Quit'
$cleanup = Simple-Menu -MenuItems $cleanupMenu -Title "Cleanup files/directories"
switch ($cleanup) {
    'Cleanup the whole venidium directory (highly recommended)' {
        Remove-Item $env:HOMEDRIVE$env:HOMEPATH\.venidium\ -Recurse
    }
    'Cleanup only the Mainnet directory (not recommended)' {
        Remove-Item $env:HOMEDRIVE$env:HOMEPATH\.venidium\mainnet\ -Recurse
    }
    'Quit' {
        $quit = 1
    }
}

if ($quit -eq 1) {
    [Environment]::Exit(1)
}

$cleanupMenu = 'Cleanup VENIDIUM_ROOT environment variable (highly recommended)', 'Quit'
$cleanup = Simple-Menu -MenuItems $cleanupMenu -Title "Cleanup env vars"
switch ($cleanup) {
    'Cleanup VENIDIUM_ROOT environment variable (highly recommended)' {
        Invoke-Command -ScriptBlock {
            cmd.exe /C 'setx.exe VENIDIUM_ROOT ""'
        }
        Invoke-Command -ScriptBlock {
            cmd.exe /C 'REG" delete "HKCU\Environment" /F /V "VENIDIUM_ROOT"'
        }
        [Environment]::SetEnvironmentVariable('VENIDIUM_ROOT', $null, 'User')
    }
    'Quit' {
        [Environment]::Exit(1)
    }
}

Write-Output "System is ready for mainnet"
Write-Output "You can now use the official installer"
