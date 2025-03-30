import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Dark Calculator')
        self.setFixedSize(300, 400)
        
        # 颜色配置
        self.num_color = "rgb(50, 50, 50)"
        self.op_color = "rgb(255, 165, 0)"
        self.text_color = "rgb(255, 255, 255)"
        
        # 主布局
        grid = QGridLayout()
        self.setLayout(grid)
        
        # 显示框
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(f"background: {self.num_color}; color: {self.text_color}; font-size: 24px;")
        grid.addWidget(self.display, 0, 0, 1, 4)
        
        # 按钮布局
        buttons = [
            ('C', 1, 0), ('√', 1, 1), ('x²', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), 
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.on_click)
            btn.setFixedSize(60, 60)
            
            # 设置不同按钮样式
            if text in {'C', '√', 'x²'}:
                btn.setStyleSheet(f"background: {self.op_color}; color: {self.text_color};")
            elif text.isdigit() or text == '.':
                btn.setStyleSheet(f"background: {self.num_color}; color: {self.text_color};")
            else:
                btn.setStyleSheet(f"background: {self.op_color}; color: {self.text_color};")
                
            # 调整等号大小
            if text == '=':
                btn.setFixedSize(60, 60)
                grid.addWidget(btn, row, col, 1, 2)
            else:
                grid.addWidget(btn, row, col)

    def on_click(self):
        btn = self.sender()
        text = btn.text()
        
        if text == '=':
            try:
                result = eval(self.display.text().replace('×', '*').replace('÷', '/'))
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif text == 'C':
            self.display.clear()
        elif text == '√':
            try:
                num = float(self.display.text())
                self.display.setText(str(math.sqrt(num)))
            except:
                self.display.setText("Error")
        elif text == 'x²':
            try:
                num = float(self.display.text())
                self.display.setText(str(num**2))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.setStyleSheet("background: rgb(30, 30, 30);")  # 设置窗口背景色
    calc.show()
    sys.exit(app.exec_())
