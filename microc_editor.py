import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                             QFileDialog, QMessageBox, QSplitter, QStatusBar)

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ruta_archivo = None
        self.guardado = True
        self.ignore_text_changes = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MicroC Editor - Automatas y Lenguajes")
        self.setGeometry(100, 100, 800, 600)

        # Crear widgets
        self.text_edit = QTextEdit()
        self.text_edit.setFontFamily("Courier New")
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.result_edit = QTextEdit()
        self.result_edit.setReadOnly(True)
        self.result_edit.setFontFamily("Courier New")

        # Layout
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.text_edit)
        splitter.addWidget(self.result_edit)
        self.setCentralWidget(splitter)

        # Barra de estado
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.actualizar_barra_estado()

        # Menús
        self.crear_menu()

    def crear_menu(self):
        menu_bar = self.menuBar()

        # Menú Archivo
        archivo_menu = menu_bar.addMenu("Archivo")
        nuevo_action = QAction("Nuevo", self)
        nuevo_action.triggered.connect(self.nuevo)
        archivo_menu.addAction(nuevo_action)
        abrir_action = QAction("Abrir", self)
        abrir_action.triggered.connect(self.abrir)
        archivo_menu.addAction(abrir_action)
        guardar_action = QAction("Guardar", self)
        guardar_action.triggered.connect(self.guardar)
        archivo_menu.addAction(guardar_action)
        archivo_menu.addSeparator()
        salir_action = QAction("Salir", self)
        salir_action.triggered.connect(self.salir)
        archivo_menu.addAction(salir_action)

        # Menú Editar
        editar_menu = menu_bar.addMenu("Editar")
        editar_action = QAction("Editar", self)
        editar_action.triggered.connect(self.habilitar_edicion)
        editar_menu.addAction(editar_action)

        # Menú Compilar
        compilar_menu = menu_bar.addMenu("Compilción")
        compilar_action = QAction("Compilar", self)
        compilar_action.triggered.connect(self.compilar)
        compilar_menu.addAction(compilar_action)

        # Menú Ayuda
        ayuda_menu = menu_bar.addMenu("Ayuda")

        ayuda_action = QAction("Acerca de", self)
        ayuda_action.triggered.connect(self.mostrar_ayuda)
        ayuda_menu.addAction(ayuda_action)

        github_proyecto = QAction("GitHub", self)
        github_proyecto.triggered.connect(self.github_proyecto)
        ayuda_menu.addAction(github_proyecto)

    def actualizar_barra_estado(self):
        mensaje = self.ruta_archivo if self.ruta_archivo else "Nuevo archivo"
        self.status_bar.showMessage(mensaje)

    def on_text_changed(self):
        if not self.ignore_text_changes:
            self.guardado = False

    def nuevo(self):
        self.ignore_text_changes = True
        self.text_edit.clear()
        self.ignore_text_changes = False
        self.text_edit.setReadOnly(False)
        self.ruta_archivo = None
        self.guardado = True
        self.actualizar_barra_estado()

    def abrir(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", "", "Archivos C (*.c);;Todos los archivos (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                self.ignore_text_changes = True
                self.text_edit.setPlainText(content)
                self.ignore_text_changes = False
                self.text_edit.setReadOnly(True)
                self.ruta_archivo = file_name
                self.guardado = True
                self.actualizar_barra_estado()
            except Exception as e:
                self.result_edit.append(f"Error al abrir el archivo: {str(e)}")

    def guardar(self):
        if not self.ruta_archivo:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Guardar como", "", "Archivos C (*.c);;Todos los archivos (*)", options=options)
            if not file_name:
                return
            self.ruta_archivo = file_name
        try:
            with open(self.ruta_archivo, 'w') as file:
                file.write(self.text_edit.toPlainText())
            self.guardado = True
            self.actualizar_barra_estado()
        except Exception as e:
            self.result_edit.append(f"Error al guardar el archivo: {str(e)}")

    def salir(self):
        if not self.guardado:
            respuesta = QMessageBox.question(
                self, "Guardar cambios", "¿Desea guardar los cambios antes de salir?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            if respuesta == QMessageBox.Save:
                self.guardar()
                if not self.guardado:
                    return
            elif respuesta == QMessageBox.Cancel:
                return
        QApplication.quit()

    def habilitar_edicion(self):
        self.text_edit.setReadOnly(False)
        self.guardado = False

    def compilar(self):
        if not self.text_edit.toPlainText().strip():
            self.result_edit.append("Error: No hay código para compilar.")
            return
        self.result_edit.append("Compilando... [PENDIENTE]")

    def mostrar_ayuda(self):
        QMessageBox.information(self, "Ayuda", "Proyecto para el curso de Automatas y Lenguajes, creado por Luis Holtman.")

    def github_proyecto(self):
        url = QUrl("https://github.com/SimplementeHoltman/microc-editor")
        QDesktopServices.openUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
