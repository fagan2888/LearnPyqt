# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompleteTransactionDetails.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(1214, 121)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.l_variety = QtGui.QLabel(self.dockWidgetContents)
        self.l_variety.setObjectName(_fromUtf8("l_variety"))
        self.horizontalLayout_5.addWidget(self.l_variety)
        self.rb_variety_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_all.setChecked(True)
        self.rb_variety_all.setObjectName(_fromUtf8("rb_variety_all"))
        self.buttonGroup = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rb_variety_all)
        self.horizontalLayout_5.addWidget(self.rb_variety_all)
        self.rb_variety_stock = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_stock.setChecked(False)
        self.rb_variety_stock.setObjectName(_fromUtf8("rb_variety_stock"))
        self.buttonGroup.addButton(self.rb_variety_stock)
        self.horizontalLayout_5.addWidget(self.rb_variety_stock)
        self.rb_variety_other = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_other.setChecked(False)
        self.rb_variety_other.setObjectName(_fromUtf8("rb_variety_other"))
        self.buttonGroup.addButton(self.rb_variety_other)
        self.horizontalLayout_5.addWidget(self.rb_variety_other)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.l_orderType = QtGui.QLabel(self.dockWidgetContents)
        self.l_orderType.setObjectName(_fromUtf8("l_orderType"))
        self.horizontalLayout_5.addWidget(self.l_orderType)
        self.cb_orderType_stock = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_orderType_stock.setChecked(True)
        self.cb_orderType_stock.setObjectName(_fromUtf8("cb_orderType_stock"))
        self.horizontalLayout_5.addWidget(self.cb_orderType_stock)
        self.cb_orderType_etf_trade = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_orderType_etf_trade.setChecked(True)
        self.cb_orderType_etf_trade.setObjectName(_fromUtf8("cb_orderType_etf_trade"))
        self.horizontalLayout_5.addWidget(self.cb_orderType_etf_trade)
        self.cb_orderType_etf = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_orderType_etf.setChecked(True)
        self.cb_orderType_etf.setObjectName(_fromUtf8("cb_orderType_etf"))
        self.horizontalLayout_5.addWidget(self.cb_orderType_etf)
        self.cb_orderType_reverse = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_orderType_reverse.setChecked(True)
        self.cb_orderType_reverse.setObjectName(_fromUtf8("cb_orderType_reverse"))
        self.horizontalLayout_5.addWidget(self.cb_orderType_reverse)
        self.cb_orderType_other = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_orderType_other.setChecked(True)
        self.cb_orderType_other.setObjectName(_fromUtf8("cb_orderType_other"))
        self.horizontalLayout_5.addWidget(self.cb_orderType_other)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.l_tradeType = QtGui.QLabel(self.dockWidgetContents)
        self.l_tradeType.setObjectName(_fromUtf8("l_tradeType"))
        self.horizontalLayout_5.addWidget(self.l_tradeType)
        self.cb_tradeType_common = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_tradeType_common.setChecked(True)
        self.cb_tradeType_common.setObjectName(_fromUtf8("cb_tradeType_common"))
        self.horizontalLayout_5.addWidget(self.cb_tradeType_common)
        self.cb_tradeType_cancel = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_tradeType_cancel.setChecked(True)
        self.cb_tradeType_cancel.setObjectName(_fromUtf8("cb_tradeType_cancel"))
        self.horizontalLayout_5.addWidget(self.cb_tradeType_cancel)
        self.cb_tradeType_useless = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_tradeType_useless.setChecked(False)
        self.cb_tradeType_useless.setObjectName(_fromUtf8("cb_tradeType_useless"))
        self.horizontalLayout_5.addWidget(self.cb_tradeType_useless)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.l_market = QtGui.QLabel(self.dockWidgetContents)
        self.l_market.setObjectName(_fromUtf8("l_market"))
        self.horizontalLayout_4.addWidget(self.l_market)
        self.rb_market_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_market_all.setChecked(True)
        self.rb_market_all.setObjectName(_fromUtf8("rb_market_all"))
        self.buttonGroup_3 = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup_3.setObjectName(_fromUtf8("buttonGroup_3"))
        self.buttonGroup_3.addButton(self.rb_market_all)
        self.horizontalLayout_4.addWidget(self.rb_market_all)
        self.rb_market_SH = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_market_SH.setChecked(False)
        self.rb_market_SH.setObjectName(_fromUtf8("rb_market_SH"))
        self.buttonGroup_3.addButton(self.rb_market_SH)
        self.horizontalLayout_4.addWidget(self.rb_market_SH)
        self.rb_market_SZ = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_market_SZ.setChecked(False)
        self.rb_market_SZ.setObjectName(_fromUtf8("rb_market_SZ"))
        self.buttonGroup_3.addButton(self.rb_market_SZ)
        self.horizontalLayout_4.addWidget(self.rb_market_SZ)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.l_tradeTerminal = QtGui.QLabel(self.dockWidgetContents)
        self.l_tradeTerminal.setObjectName(_fromUtf8("l_tradeTerminal"))
        self.horizontalLayout_4.addWidget(self.l_tradeTerminal)
        self.rb_tradeTerminal_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_all.setChecked(True)
        self.rb_tradeTerminal_all.setObjectName(_fromUtf8("rb_tradeTerminal_all"))
        self.buttonGroup_2 = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rb_tradeTerminal_all)
        self.horizontalLayout_4.addWidget(self.rb_tradeTerminal_all)
        self.rb_tradeTerminal_self = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_self.setChecked(False)
        self.rb_tradeTerminal_self.setObjectName(_fromUtf8("rb_tradeTerminal_self"))
        self.buttonGroup_2.addButton(self.rb_tradeTerminal_self)
        self.horizontalLayout_4.addWidget(self.rb_tradeTerminal_self)
        self.rb_tradeTerminal_ip = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_ip.setChecked(False)
        self.rb_tradeTerminal_ip.setObjectName(_fromUtf8("rb_tradeTerminal_ip"))
        self.buttonGroup_2.addButton(self.rb_tradeTerminal_ip)
        self.horizontalLayout_4.addWidget(self.rb_tradeTerminal_ip)
        self.le_search = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_search.setDragEnabled(False)
        self.le_search.setReadOnly(False)
        self.le_search.setObjectName(_fromUtf8("le_search"))
        self.horizontalLayout_4.addWidget(self.le_search)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.l_stockCode = QtGui.QLabel(self.dockWidgetContents)
        self.l_stockCode.setObjectName(_fromUtf8("l_stockCode"))
        self.horizontalLayout_4.addWidget(self.l_stockCode)
        self.le_stockCode = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_stockCode.setObjectName(_fromUtf8("le_stockCode"))
        self.horizontalLayout_4.addWidget(self.le_stockCode)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_policyID = QtGui.QLabel(self.dockWidgetContents)
        self.l_policyID.setObjectName(_fromUtf8("l_policyID"))
        self.horizontalLayout_3.addWidget(self.l_policyID)
        self.le_policyID = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_policyID.setObjectName(_fromUtf8("le_policyID"))
        self.horizontalLayout_3.addWidget(self.le_policyID)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.l_ip = QtGui.QLabel(self.dockWidgetContents)
        self.l_ip.setObjectName(_fromUtf8("l_ip"))
        self.horizontalLayout_3.addWidget(self.l_ip)
        self.le_ip = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_ip.setObjectName(_fromUtf8("le_ip"))
        self.horizontalLayout_3.addWidget(self.le_ip)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.l_ETF = QtGui.QLabel(self.dockWidgetContents)
        self.l_ETF.setObjectName(_fromUtf8("l_ETF"))
        self.horizontalLayout_3.addWidget(self.l_ETF)
        self.le_etf = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_etf.setObjectName(_fromUtf8("le_etf"))
        self.horizontalLayout_3.addWidget(self.le_etf)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pb_search = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_search.setObjectName(_fromUtf8("pb_search"))
        self.horizontalLayout_3.addWidget(self.pb_search)
        self.pb_outputFile = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_outputFile.setObjectName(_fromUtf8("pb_outputFile"))
        self.horizontalLayout_3.addWidget(self.pb_outputFile)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "完整成交明细", None))
        self.l_variety.setText(_translate("DockWidget", "品种", None))
        self.rb_variety_all.setText(_translate("DockWidget", "全部", None))
        self.rb_variety_stock.setText(_translate("DockWidget", "股票", None))
        self.rb_variety_other.setText(_translate("DockWidget", "其他", None))
        self.l_orderType.setText(_translate("DockWidget", "委托类型", None))
        self.cb_orderType_stock.setText(_translate("DockWidget", "股票买卖", None))
        self.cb_orderType_etf_trade.setText(_translate("DockWidget", "ETF买卖", None))
        self.cb_orderType_etf.setText(_translate("DockWidget", "ETF申赎", None))
        self.cb_orderType_reverse.setText(_translate("DockWidget", "逆回购", None))
        self.cb_orderType_other.setText(_translate("DockWidget", "其他", None))
        self.l_tradeType.setText(_translate("DockWidget", "成交类型", None))
        self.cb_tradeType_common.setText(_translate("DockWidget", "普通", None))
        self.cb_tradeType_cancel.setText(_translate("DockWidget", "撤单", None))
        self.cb_tradeType_useless.setText(_translate("DockWidget", "废单", None))
        self.l_market.setText(_translate("DockWidget", "市场", None))
        self.rb_market_all.setText(_translate("DockWidget", "全部", None))
        self.rb_market_SH.setText(_translate("DockWidget", "沪市", None))
        self.rb_market_SZ.setText(_translate("DockWidget", "深市", None))
        self.l_tradeTerminal.setText(_translate("DockWidget", "交易终端", None))
        self.rb_tradeTerminal_all.setText(_translate("DockWidget", "全部", None))
        self.rb_tradeTerminal_self.setText(_translate("DockWidget", "自己", None))
        self.rb_tradeTerminal_ip.setText(_translate("DockWidget", "终端IP", None))
        self.l_stockCode.setText(_translate("DockWidget", "证券代码", None))
        self.l_policyID.setText(_translate("DockWidget", "PolicyID", None))
        self.l_ip.setText(_translate("DockWidget", "IP地址", None))
        self.l_ETF.setText(_translate("DockWidget", "所属ETF", None))
        self.pb_search.setText(_translate("DockWidget", "查询", None))
        self.pb_outputFile.setText(_translate("DockWidget", "导出", None))

