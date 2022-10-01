import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication


class Doviz(QDialog):

    def __init__(self):
        super(Doviz, self).__init__()
        loadUi("currency_interface.ui", self)
        self.result_button.clicked.connect(self.currency_excange)

    def currency_excange(self):
        amount = self.amount.text()

        if self.amount.text().find(',') > 0:
            amount = self.amount.text().replace(",", ".")

        url = "https://kur.doviz.com"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        if self.currency.currentText() == "TRY":
            cur = soup.find("td", {"data-socket-key": self.currency_2.currentText()}).text
            cur = cur.replace(",", ".")
            self.result.setText("Sonuç : " + str(round(float(amount) / float(cur), 4)))

        elif self.currency_2.currentText() == "TRY":
            cur = soup.find("td", {"data-socket-key": self.currency.currentText()}).text
            cur = cur.replace(",", ".")
            self.result.setText("Sonuç : " + str(round(float(amount) * float(cur), 4)))
        else:
            cur = soup.find("td", {"data-socket-key": self.currency.currentText()}).text
            cur2 = soup.find("td", {"data-socket-key": self.currency_2.currentText()}).text
            cur = cur.replace(",", ".")
            cur2 = cur2.replace(",", ".")
            self.result.setText("Sonuç : " + str(round(float(amount) * (float(cur) / float(cur2)), 4)))


app = QApplication(sys.argv)
doviz = Doviz()
doviz.setWindowTitle("Döviz Çevirici")
doviz.setFixedHeight(670)
doviz.setFixedWidth(810)
doviz.show()
sys.exit(app.exec())
