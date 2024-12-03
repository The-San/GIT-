import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QTextEdit,
)
from SampleModule import convert_to_grayscale, resize_image, move_image


class ImageProcessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(
            "Утилита работы с изображениями - Практикант: Щепетова Оксана Евгеньева"
        )
        self.setGeometry(100, 100, 600, 400)

        main_layout = QVBoxLayout()

        self.title_label = QLabel("Утилита работы с изображениями")
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(self.title_label)

        load_layout = QHBoxLayout()
        self.imagePathInput = QLineEdit(self)
        self.imagePathInput.setPlaceholderText("Выбранное изображение")
        load_layout.addWidget(self.imagePathInput)

        self.loadButton = QPushButton("Загрузить изображение", self)
        self.loadButton.clicked.connect(self.load_image)
        load_layout.addWidget(self.loadButton)

        main_layout.addLayout(load_layout)

        button_layout = QHBoxLayout()
        self.grayscaleButton = QPushButton("Конвертировать в черно-белое", self)
        self.grayscaleButton.clicked.connect(self.convert_image)
        button_layout.addWidget(self.grayscaleButton)

        self.resizeButton = QPushButton("Изменить размер", self)
        self.resizeButton.clicked.connect(self.resize_image)
        button_layout.addWidget(self.resizeButton)

        self.moveButton = QPushButton("Переместить изображение", self)
        self.moveButton.clicked.connect(self.move_image_dialog)
        button_layout.addWidget(self.moveButton)

        main_layout.addLayout(button_layout)

        self.info_text = QTextEdit(self)
        self.info_text.setReadOnly(True)
        main_layout.addWidget(self.info_text)

        self.setLayout(main_layout)

    def load_image(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть изображение",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)",
            options=options,
        )
        if filePath:
            self.imagePathInput.setText(filePath)
            self.info_text.append(f"Изображение загружено: {filePath}")

    def convert_image(self):
        try:
            image_path = self.imagePathInput.text()
            save_path = image_path.rsplit(".", 1)[0] + "_grayscale.png"
            convert_to_grayscale(image_path, save_path)
            self.info_text.append(
                f"Изображение конвертировано и сохранено: {save_path}"
            )
        except Exception as ex:
            self.info_text.append("Ошибка: " + str(ex))

    def resize_image(self):
        try:
            image_path = self.imagePathInput.text()
            save_path = image_path.rsplit(".", 1)[0] + "_resized.png"
            new_size = (200, 200)  # Пример нового размера (ширина, высота)
            resize_image(image_path, save_path, new_size)
            self.info_text.append(f"Изображение изменено и сохранено: {save_path}")
        except Exception as ex:
            self.info_text.append("Ошибка: " + str(ex))

    def move_image_dialog(self):
        try:
            image_path = self.imagePathInput.text()
            target_directory = QFileDialog.getExistingDirectory(
                self, "Выберите папку для перемещения изображения"
            )
            if target_directory:
                new_path = move_image(image_path, target_directory)
                self.info_text.append(f"Изображение перемещено в: {new_path}")
        except Exception as ex:
            self.info_text.append("Ошибка: " + str(ex))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImageProcessorApp()
    window.show()
    sys.exit(app.exec_())
