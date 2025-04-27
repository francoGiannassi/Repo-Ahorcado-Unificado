@echo off
echo Ejecutando los Unit Tests...
cd backend
python -m unittest test_ahorcado.py
if %errorlevel% neq 0 (
    echo Error al ejecutar los Unit Tests.
    pause
    exit /b %errorlevel%
)
cd ..

echo Ejecutando los Aceptance Tests...
cd frontend
npm run test
if %errorlevel% neq 0 (
    echo Error al ejecutar los Aceptance Tests.
    pause
    exit /b %errorlevel%
)
echo Todos los tests se ejecutaron correctamente.
pause