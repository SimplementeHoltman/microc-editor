# MicroC Editor - Proyecto en Python

Este proyecto es un editor básico para código MicroC desarrollado en Python utilizando el framework **PyQt5**. La aplicación permite editar, guardar, abrir y compilar código MicroC, aunque la funcionalidad de compilación está en desarrollo. La interfaz gráfica es intuitiva y cuenta con menús y áreas de texto para facilitar la edición y visualización del código.

---

## Características Principales

- **Interfaz gráfica** desarrollada con PyQt5.
- **Edición de código**: Área de texto para escribir y modificar código MicroC.
- **Guardar y abrir archivos**: Soporte para guardar y abrir archivos `.c`.
- **Compilación**: Funcionalidad en desarrollo para compilar código MicroC.
- **Manejo de estados**: Rastrea si el archivo ha sido guardado y muestra la ruta del archivo actual.
- **Diálogos integrados**: Usa `QFileDialog` para abrir y guardar archivos de manera nativa.

---

## Requisitos

- **Python 3.7 o superior**.
- **PyQt5**: Biblioteca para la creación de interfaces gráficas.

---

## Instrucciones para Clonar y Ejecutar el Proyecto

### 1. Clonar el Repositorio

Para descargar el proyecto, abre una terminal y ejecuta el siguiente comando:

```bash
git clone https://github.com/SimplementeHoltman/microc-editor
```

### 2. Navegar al Directorio del Proyecto

Una vez clonado el repositorio, ingresa al directorio del proyecto:

```bash
cd microc-editor
```

### 3. Instalar Dependencias

Asegúrate de tener Python 3.7 o superior instalado. Luego, instala las dependencias necesarias:

```bash
pip install PyQt5
```

### 4. Ejecutar la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
python microc_editor.py
```
