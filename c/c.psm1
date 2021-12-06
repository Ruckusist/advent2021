function run_c_program {
    Write-Host "Starting C Program..."
    cd c
    gcc test.c -o test
    .\test.exe
    del test.exe
    cd ..
    Write-Host "Finished C Program..."
    return 0;
}