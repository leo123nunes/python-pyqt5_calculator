from PyQt5.QtWidgets import QMainWindow, QPushButton, QSizePolicy, QWidget, QGridLayout, QLineEdit

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')

        self.setFixedSize(400, 400)

        self.BTN_FONT_SIZE = '20px'
        self.DISPLAY_FONT_SIZE = '40px'

        self.DISPLAY_TEXT_COLOR = '#ffffffff'
        self.DISPLAY_BACKGROUND_COLOR = '#646464'

        self.BTN_NUMERIC_TEXT_COLOR = '#ffffffff'
        self.BTN_NUMERIC_BACKGROUND_COLOR = '#646464'

        self.BTN_OPERATION_TEXT_COLOR = '#ffffffff'
        self.BTN_OPERATION_BACKGROUND_COLOR = '#c44d00'

        self.BTN_CLEAR_TEXT_COLOR = '#ffffffff'
        self.BTN_CLEAR_BACKGROUND_COLOR = '#c0a400'

        self.BTN_RESULT_TEXT_COLOR = '#ffffffff'
        self.BTN_RESULT_BACKGROUND_COLOR = '#c44d00'

        self.BTN_ERASE_TEXT_COLOR = '#ffffffff'
        self.BTN_ERASE_BACKGROUND_COLOR = '#c44d00'

        self.widget = QWidget()

        self.grid = QGridLayout()

        self.widget.setLayout(self.grid)

        self.setCentralWidget(self.widget)

        self.init_display()

        self.init_btns()

    def init_display(self):
        self.display = QLineEdit()

        self.display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.display.setTextMargins(10, 0, 10, 0)

        self.display.setMaxLength(15)

        self.display.setDisabled(True)

        self.display.setStyleSheet(F"font-size: {self.DISPLAY_FONT_SIZE}; color: {self.DISPLAY_TEXT_COLOR}; background-color: {self.DISPLAY_BACKGROUND_COLOR}")

        self.display.setText('0') 

        self.grid.addWidget(self.display, 0, 0, 1, 5)

    def init_btns(self):
        self.create_btn('7', 1, 0, 1, 1, 'numeric')
        self.create_btn('8', 1, 1, 1, 1, 'numeric')
        self.create_btn('9', 1, 2, 1, 1, 'numeric')
        self.create_btn('/', 1, 3, 1, 1, 'operation')
        self.create_btn('C', 1, 4, 1, 1, 'clear')
        self.create_btn('4', 2, 0, 1, 1, 'numeric')
        self.create_btn('5', 2, 1, 1, 1, 'numeric')
        self.create_btn('6', 2, 2, 1, 1, 'numeric')
        self.create_btn('*', 2, 3, 1, 1, 'operation')
        self.create_btn('<-', 2, 4, 1, 1, 'erase')
        self.create_btn('1', 3, 0, 1, 1, 'numeric')
        self.create_btn('2', 3, 1, 1, 1, 'numeric')
        self.create_btn('3', 3, 2, 1, 1, 'numeric')
        self.create_btn('-', 3, 3, 1, 1, 'operation')
        self.create_btn('=', 3, 4, 2, 1, 'result')
        self.create_btn('0', 4, 0, 1, 1, 'numeric')
        self.create_btn(',', 4, 1, 1, 1, 'numeric')
        self.create_btn('%', 4, 2, 1, 1, 'operation')
        self.create_btn('+', 4, 3, 1, 1, 'operation')

    def create_btn(self, btn_text, btn_row, btn_col, btn_size_row, btn_size_column, funcionality):
        btn = QPushButton(btn_text)

        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        def display_add_digit():
            if self.display.text() == '0':
                self.display.setText(btn_text)
            else:
                self.display.setText(self.display.text() + btn_text)

        def display_result():

            result = self.eval_result_verify_error(self.display.text().replace(',','.'))

            self.display.setText(result.replace('.',','))

        def display_cls():

            if self.display.text() != '0':
                self.display.setText('0')

        def display_erase():

            result = self.display.text()[:-1]

            if result == '':
                self.display.setText('0')
            else:
                self.display.setText(result)
        
        if funcionality == 'numeric':
            btn.setStyleSheet(f'color: {self.BTN_NUMERIC_TEXT_COLOR}; background-color: {self.BTN_NUMERIC_BACKGROUND_COLOR}; font-size: {self.BTN_FONT_SIZE};')

            btn.clicked.connect(display_add_digit)
        elif funcionality == 'operation':
            btn.setStyleSheet(f'color: {self.BTN_OPERATION_TEXT_COLOR}; background-color: {self.BTN_OPERATION_BACKGROUND_COLOR}; font-size: {self.BTN_FONT_SIZE};')

            btn.clicked.connect(display_add_digit)
        elif funcionality == 'clear':
            btn.setStyleSheet(f'color: {self.BTN_CLEAR_TEXT_COLOR}; background-color: {self.BTN_CLEAR_BACKGROUND_COLOR}; font-size: {self.BTN_FONT_SIZE};')

            btn.clicked.connect(display_cls)
        elif funcionality == 'erase':
            btn.setStyleSheet(f'color: {self.BTN_ERASE_TEXT_COLOR}; background-color: {self.BTN_ERASE_BACKGROUND_COLOR}; font-size: {self.BTN_FONT_SIZE};')

            btn.clicked.connect(display_erase)
        elif funcionality == 'result':
            btn.setStyleSheet(f'color: {self.BTN_RESULT_TEXT_COLOR}; background-color: {self.BTN_RESULT_BACKGROUND_COLOR}; font-size: {self.BTN_FONT_SIZE};')

            btn.clicked.connect(display_result)
        else:
            raise TypeError(f'Unknown button type error: {funcionality}')

        self.grid.addWidget(btn, btn_row, btn_col, btn_size_row, btn_size_column)

    def eval_result_verify_error(self, text):
        try:
            
            return str(eval(text))

        except SyntaxError as e:
            
            return 'Syntax Error'





