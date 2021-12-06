Import-Module -Name ".\c\c.psm1"

function Show-Menu {
    param (
        [string]$Title = 'My Menu'
    )
    Clear-Host
    Write-Host "================ $Title ================"
    Write-Host "1: Press '1' for C."
    Write-Host "q: Must Press 'q' to Quit."
}
function selection {
    $selection = Read-Host "Please make a selection"
    switch ($selection) {
        '1' { .\test.ps1 } 
    }
    return $selection;
}
function game_loop {
    do {
        Show-Menu -Title Ruckus Advent
        $selection_ = selection
        pause
    }
    until ($selection_ -eq 'q')
}
function main {
    game_loop
}

main