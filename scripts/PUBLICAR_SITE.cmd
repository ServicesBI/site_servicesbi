@echo off
rem Mesmo que o botao "Subir site" da Central de comando do site.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0publicar_online.ps1"
