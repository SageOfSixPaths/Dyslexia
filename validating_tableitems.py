#! /usr/bin/env python
#
# show validating int, float, date QTable items
#
# 2005-01-23    initial version    hp

import sys
from types import IntType, FloatType
from qt import *
from qttable import *

class TableItem(QTableItem):
    def __init__(self, table, et, text = ""):
        self.warnColor = QColor(230,124,127)
        QTableItem.__init__(self, table, et, text)

    def paint(self, p, cg, cr, selected):
        g = QColorGroup(cg)
        warn = False
        col = self.col()
        value = self.value()
        if col == 0:
            # date column
            if value != None and value < QDate.currentDate():
                warn = True
        else:
            # int or float column
            if value < 0:
                warn = True
        if warn:
            g.setColor(QColorGroup.Base, self.warnColor)
        QTableItem.paint(self, p, g, cr, selected)


class IntTableItem(TableItem):
    def __init__(self, table, value = None, bottom = None, top = None):
        self.top = top
        self.bottom = bottom
        TableItem.__init__(self, table, QTableItem.OnTyping)
        if value != None:
            self.setValue(value)
        # we do not want this item to be replaced
        self.setReplaceable(False)

    def value(self):
        return self.text().toInt()[0]

    def setValue(self, value):
        assert(type(value) == IntType)
        if self.bottom != None and value < self.bottom:
            value = int(self.bottom)
        if self.top != None and value > self.top:
            value = int(self.top)
        self.setText(str(value))

    def createEditor(self):
        le = QLineEdit(self.text(), self.table().viewport())
        ival = QIntValidator(le)
        if self.bottom != None:
            ival.setBottom(self.bottom)
        if self.top != None:
            ival.setTop(self.top)
        le.setValidator(ival)
        return le

    def setContentFromEditor(self, w):
        self.setValue(w.text().toInt()[0])


class FloatTableItem(TableItem):
    def __init__(self, table, value = None, bottom = None, top = None, decimals = None):
        self.decimals = decimals
        self.top = top
        self.bottom = bottom
        TableItem.__init__(self, table, QTableItem.OnTyping)
        if value != None:
            self.setValue(value)
        # we do not want this item to be replaced
        self.setReplaceable(False)

    def value(self):
        return self.text().toDouble()[0]

    def setValue(self, value):
        assert(type(value) in (IntType, FloatType))
        if self.bottom != None and value < self.bottom:
            value = float(self.bottom)
        if self.top != None and value > self.top:
            value = float(self.top)
        if self.decimals != None:
            self.setText("%.*f" % (self.decimals, value))
        else:
            self.setText(str(value))

    def createEditor(self):
        le = QLineEdit(self.text(), self.table().viewport())
        dval = QDoubleValidator(le)
        if self.bottom != None:
            dval.setBottom(self.bottom)
        if self.top != None:
            dval.setTop(self.top)
        if self.decimals != None:
            dval.setDecimals(self.decimals)
        le.setValidator(dval)
        return le

    def setContentFromEditor(self, w):
        self.setValue(w.text().toDouble()[0])


class DateTableItem(TableItem):
    def __init__(self, table, date = None):
        self.format = Qt.LocalDate
        TableItem.__init__(self, table, QTableItem.OnTyping)
        self.setValue(date)
        self._de = None
        # we do not want this item to be replaced
        self.setReplaceable(False)

    def value(self):
        return self.date

    def setValue(self, date):
        if date != None and date.isValid():
            self.date = date
            value = date.toString(self.format)
        else:
            self.date = None
            value = ""
        self.setText(value)

    def createEditor(self):
        date = self.value()
        if date != None and date.isValid():
            date = date.fromString(self.format)
        else:
            date = QDate.currentDate()
        self._de = QDateEdit(date, self.table().viewport())
        self._de.setAutoAdvance(True)
        return self._de

    def setContentFromEditor(self, w):
        # the user changed the value in the dateedit, so synchronize the
        # value of the item (its text), with the value of the dateedit
        if w.inherits("QDateEdit"):
            self.setValue(w.date())
            #self.setText(w.date().toString(self.format))
        else:
            TableItem.setContentFromEditor(self, w)


if __name__ == '__main__':
    ROWS = 10
    COLS = 3
    TOP = 99999
    BOTTOM = -99999
    DECIMALS = 3
    app = QApplication(sys.argv)
    t = QTable(ROWS, COLS)
    h = t.horizontalHeader()
    h.setLabel(0, "Date Editor")
    h.setLabel(1, "Int Validator")
    h.setLabel(2, "Float Validator")
    for i in range(ROWS):
        item = DateTableItem(t)
        t.setItem(i, 0, item)
        item = IntTableItem(t, i, BOTTOM, TOP)
        t.setItem(i, 1, item)
        item = FloatTableItem(t, i, BOTTOM, TOP, DECIMALS)
        t.setItem(i, 2, item)
    t.resize(t.sizeHint())
    t.show()
    app.setMainWidget(t)
    app.exec_loop()
