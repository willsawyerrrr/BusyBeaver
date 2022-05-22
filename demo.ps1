function Open-File {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string] $Filename,

        [Parameter()]
        [int] $LineNumber = 1
    )

    Write-Host "`tDo you want to open " -NoNewline
    Write-Host "$Filename" -ForegroundColor red -NoNewline
    Write-Host "? [y/n] " -NoNewline
    $Open = Read-Host
    if ($Open -eq "Y" -or $Open -eq "y") {
        Write-Host "`t`tOpening " -NoNewline
        Write-Host "$Filename" -ForegroundColor red -NoNewline
        Write-Host "...`n"
        vim $Filename +$LineNumber
    } else {
        Write-Host "`t`tSkipping " -NoNewline
        Write-Host "$Filename" -ForegroundColor red -NoNewline
        Write-Host "...`n"
    }
}

function Run-Program {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string] $Filename,

        [Parameter()]
        [string] $Args = ""
    )

    Write-Host "`tDo you want to demonstrate " -NoNewline
    Write-Host "$Filename" -ForegroundColor red -NoNewline
    if ($Args) {
        Write-Host " with the arguments: " -NoNewline
        Write-Host "$Args" -ForegroundColor red -NoNewline
    }
    Write-Host "? [y/n] " -NoNewline
    $Run = Read-Host
    if ($Run -eq "Y" -or $Run -eq "y") {
        Write-Host "`t`tRunning " -NoNewline
        Write-Host "$Filename" -ForegroundColor red -NoNewline
        Write-Host "...`n"
        python $Filename $Args
    } else {
        Write-Host "`t`tSkipping " -NoNewline
        Write-Host "$Filename" -ForegroundColor red -NoNewline
        Write-Host "...`n"
    }
}

function Next-Section {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string] $Section
    )

    Write-Host "`nPress <Enter> to move onto Section $Section... " -NoNewline
    Read-Host
    Start-Sleep 1
    Clear-Host
}

Clear-Host
Write-Host "Press <Enter> to begin demonstration... " -NoNewline
Read-Host
Start-Sleep 1
Clear-Host



Write-Host "Part I) Turing Machine Simulator`n"

Write-Host "`n`ta) List the states for each of the example Turing Machines.`n"
Open-File -Filename "states.txt"

Write-Host "`n`tb) Change the run command so that one can observe the configuration of the machine at each transition.`n"
Open-File -Filename "turing_machine.py" -LineNumber 143

Write-Host "`n`tc) Describe the computation performed by each of the example Turing Machines.`n"
Open-File -Filename "descriptions.txt"

Next-Section -Section "II"



Write-Host "Part II) Turing Machine Arithmetic`n"

Write-Host "`n`ta) Create a Turing Machine that computes the addition of two unary numbers.`n"
Open-File -Filename "adder.py"
Run-Program -Filename "adder.py" -Args "110111"
Run-Program -Filename "adder.py" -Args "11101111"

Write-Host "`n`tb) Create a Turing Machine that computes the multiplication of two unary numbers.`n"
Open-File -Filename "multiplier.py"
Run-Program -Filename "multiplier.py" -Args "110111"
Run-Program -Filename "multiplier.py" -Args "111011111"

Next-Section -Section "III"



Write-Host "Part III) Busy Beaver`n"

Write-Host "`n`ta) Modify the Turing Machine so that it uses a double-sided infinite tape.`n"
Open-File -Filename "double_sided.py" -LineNumber 177

Write-Host "`n`tb) Why is using Python generators advantageous in Turing Machine simulations?`n"
Open-File -Filename "generators.txt"

Write-Host "`n`tc) Program a Turing Machine to run the given 2-card Busy Beaver program. How many ones does it produce?`n"
Open-File -Filename "two_card.py"
Run-Program -Filename "two_card.py"

Write-Host "`n`td) How does this result compare to the known programs?`n"
Open-File -Filename "comparison.txt"

Clear-Host
Write-Host "Part III) Busy Beaver`n"

Write-Host "`n`te) Write three- and four-card Busy Beaver programs. Demonstrate the number of '1's they produce.`n"
Open-File -Filename "three_card.py"
Run-Program -Filename "three_card.py"
Open-File -Filename "four_card.py"
Run-Program -Filename "four_card.py"

Write-Host "`n`tf) Can you find a new five-card Busy Beaver program?`n"
Open-File -Filename "five_card.txt"
Run-Program -Filename "five_card.py"



Clear-Host
Get-Content -Path "end_demo.txt"
Read-Host

