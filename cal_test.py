import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Ui_cal_test
import time
import random


class Test_Window(QMainWindow, Ui_cal_test.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(640, 480)
        self.setWindowTitle('口算模拟')
        # self.timer = QTimer()

        self.symbol_n = ['+', '-', '×', '÷']
        self.symbol_m = [
            'symbol_1', 'symbol_2', 'symbol_3', 'symbol_4', 'symbol_5',
            'symbol_6', 'symbol_7', 'symbol_8', 'symbol_9', 'symbol_10',
            'symbol_11', 'symbol_12', 'symbol_13', 'symbol_14', 'symbol_15',
            'symbol_16', 'symbol_17', 'symbol_18', 'symbol_19', 'symbol_20'
        ]
        self.num1_m = [
            'num_1_1',
            'num_1_2',
            'num_1_3',
            'num_1_4',
            'num_1_5',
            'num_1_6',
            'num_1_7',
            'num_1_8',
            'num_1_9',
            'num_1_10',
            'num_1_11',
            'num_1_12',
            'num_1_13',
            'num_1_14',
            'num_1_15',
            'num_1_16',
            'num_1_17',
            'num_1_18',
            'num_1_19',
            'num_1_20',
        ]
        self.num2_m = [
            'num_2_1',
            'num_2_2',
            'num_2_3',
            'num_2_4',
            'num_2_5',
            'num_2_6',
            'num_2_7',
            'num_2_8',
            'num_2_9',
            'num_2_10',
            'num_2_11',
            'num_2_12',
            'num_2_13',
            'num_2_14',
            'num_2_15',
            'num_2_16',
            'num_2_17',
            'num_2_18',
            'num_2_19',
            'num_2_20',
        ]
        self.answer_m = [
            'answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5',
            'answer_6', 'answer_7', 'answer_8', 'answer_9', 'answer_10',
            'answer_11', 'answer_12', 'answer_13', 'answer_14', 'answer_15',
            'answer_16', 'answer_17', 'answer_18', 'answer_19', 'answer_20'
        ]
        self.set_symbol()
        self.set_numbers()
        self.Line_edit_empty()
        self.btn_submit.clicked.connect(self.answer_config)
        self.btn_start.clicked.connect(self.start_config)
        self.btn_submit.setEnabled(False)

    def Line_edit_empty(self):
        for i in range(20):
            exec("self.%s.setEnabled(False)" % self.answer_m[i])

    def start_config(self):
        self.btn_start.setEnabled(False)
        self.btn_submit.setEnabled(True)
        self.counter = 0
        self.time1 = time.time()
        for i in range(20):
            exec("self.%s.setEnabled(True)" % self.answer_m[i])
        self.set_symbol()
        self.set_numbers()

    def set_symbol(self):
        for i in self.symbol_m:
            exec("self.%s.setText('%s')" %
                 (i, self.symbol_n[random.randint(0, 3)]))

    def set_numbers(self):
        for i in range(20):
            if eval('self.%s.text()' % self.symbol_m[i]) == '+':
                exec("self.%s.setText('%s')" %
                     (self.num1_m[i], str(random.randint(1, 99))))
                exec("self.%s.setText('%s')" %
                     (self.num2_m[i], str(random.randint(1, 99))))
            if eval('self.%s.text()' % self.symbol_m[i]) == '-':
                S1 = random.randint(1, 99)
                S2 = random.randint(1, S1)
                exec("self.%s.setText('%s')" % (self.num1_m[i], str(S1)))
                exec("self.%s.setText('%s')" % (self.num2_m[i], str(S2)))
            if eval('self.%s.text()' % self.symbol_m[i]) == '×':
                S1 = random.randint(1, 99)
                S2 = random.randint(1, 11)
                exec("self.%s.setText('%s')" % (self.num1_m[i], str(S1)))
                exec("self.%s.setText('%s')" % (self.num2_m[i], str(S2)))
            if eval('self.%s.text()' % self.symbol_m[i]) == '÷':
                S1 = random.randint(1, 9)
                S2 = random.randint(1, 11)
                S1 = S1 * S2
                exec("self.%s.setText('%s')" % (self.num1_m[i], str(S1)))
                exec("self.%s.setText('%s')" % (self.num2_m[i], str(S2)))

    def answer_config(self):
        for i in range(20):
            if len(eval("self.%s.text()" % self.answer_m[i])) == 0:
                QMessageBox.warning(self, '有题目未答完', '禁止提交!',
                                    QMessageBox.Yes | QMessageBox.Cancel)
                break
            else:
                if eval('self.%s.text()' % self.symbol_m[i]) == '+':
                    S1 = int(eval("self.%s.text()" % self.num1_m[i]))
                    S2 = int(eval("self.%s.text()" % self.num2_m[i]))
                    C = int((eval("self.%s.text()" % self.answer_m[i])))
                    if C == S1 + S2:
                        self.counter += 1
                if eval('self.%s.text()' % self.symbol_m[i]) == '-':
                    S1 = int(eval("self.%s.text()" % self.num1_m[i]))
                    S2 = int(eval("self.%s.text()" % self.num2_m[i]))
                    C = int(eval("self.%s.text()" % self.answer_m[i]))
                    if C == S1 - S2:
                        self.counter += 1
                if eval('self.%s.text()' % self.symbol_m[i]) == '×':
                    S1 = int(eval("self.%s.text()" % self.num1_m[i]))
                    S2 = int(eval("self.%s.text()" % self.num2_m[i]))
                    C = int(eval("self.%s.text()" % self.answer_m[i]))
                    if C == S1 * S2:
                        self.counter += 1
                if eval('self.%s.text()' % self.symbol_m[i]) == '÷':
                    S1 = int(eval("self.%s.text()" % self.num1_m[i]))
                    S2 = int(eval("self.%s.text()" % self.num2_m[i]))
                    C = int(eval("self.%s.text()" % self.answer_m[i]))
                    if C == S1 / S2:
                        self.counter += 1
        self.time2 = time.time()
        self.time_show = int(self.time2 - self.time1)
        self.score.setText(str(self.counter * 5) + '分')
        self.time_cost.setText(str(self.time_show) + '秒')
        QMessageBox.information(self, '你的得分：', '得分： '+self.score.text(),
                                QMessageBox.Yes | QMessageBox.Cancel)
        for i in range(20):
            exec("self.%s.clear()" % self.answer_m[i])
        self.start_config()
        self.Line_edit_empty()
        self.btn_start.setEnabled(True)
        self.btn_submit.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test_Window()
    win.show()

    sys.exit(app.exec_())
