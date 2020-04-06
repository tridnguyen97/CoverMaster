import sys
import GUI
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GUI.main_window()

    main.show()

    sys.exit(app.exec_())
