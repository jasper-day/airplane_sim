function Compile {
    param (
            [Parameter(Mandatory=$true)]
            [string]$filePath
          )
        $newFilePath = $filePath -replace '\.ui$', '.py'
        $finalFilePath = $filePath -replace '\.ui$', 'c.py'

        Write-Host "Input file: $filePath"
        Write-Host "Final file: $finalFilePath"

        & .\venv\Scripts\pyside6-uic.exe $filePath -o $newFilePath

        Get-Content $newFilePath | Set-Content -Encoding utf8 $finalFilePath
        Remove-Item $newFilePath
}

