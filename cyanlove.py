# -*- coding: utf-8 -*-
"""
/***************************************************************************
 cyanlove
                                 A QGIS plugin
 申少军的工具箱
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-10-19
        git sha              : $Format:%H$
        copyright            : (C) 2024 by cyan
        email                : shenshaojun@139.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .cyanlove_customdraw import cyanlove_customdraw
from .cyanlove_createpoint import cyanlove_createpoint
from .cyanlove_import_geometry import cyanlove_import_geometry
from .cyanlove_exportwkt import cyanlove_exportwkt
from .cyanlove_sqliteset import cyanlove_sqliteset
from .cyanlove_dockwidget import cyanloveDockWidget
# 初始化资源，没有这句，图标不会显示
from .resources import *

import os.path


class cyanlove:

    def __init__(self, iface):

        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'cyanlove_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr(u'&申少军工具箱')

        self.toolbar = self.iface.addToolBar(u'申少军工具箱')
        self.toolbar.setObjectName(u'申少军工具箱')

        self.pluginIsActive = False
        self.pluginIsActive2 = False
        self.pluginIsActive3 = False
        self.pluginIsActive4 = False
        self.pluginIsActive5 = False
        self.pluginIsActive6 = False

        self.dockwidget = None
        self.dockwidget2 = None  # 用于第2个窗口
        self.dockwidget3 = None  # 用于第3个窗口
        self.dockwidget4 = None  # 用于第4个窗口
        self.dockwidget5 = None  # 用于第4个窗口
        self.dockwidget6 = None  # 用于第4个窗口
    def tr(self, message):

        return QCoreApplication.translate('cyanlove', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):

        icon = QIcon(icon_path)

        action = QAction(icon, text, parent)

        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        icon_path1 = ':/plugins/cyanlove/icon/icon1.svg'
        icon_path2 = ':/plugins/cyanlove/icon/icon2.svg'
        icon_path3 = ':/plugins/cyanlove/icon/icon3.svg'
        icon_path4 = ':/plugins/cyanlove/icon/icon4.svg'
        icon_path5 = ':/plugins/cyanlove/icon/icon5.svg'
        icon_path6 = ':/plugins/cyanlove/icon/icon6.svg'
        icon_path7 = ':/plugins/cyanlove/icon/icon7.svg'
        icon_path8 = ':/plugins/cyanlove/icon/icon8.svg'
        main_menu = self.add_action(
            icon_path1,
            text=self.tr(u'栅格分析'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.add_action(
            icon_path2,
            text=self.tr(u'导出图层边界WKT集'),
            callback=self.run3,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path3,
            text=self.tr(u'导入文件绘制图形'),
            callback=self.run4,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path4,
            text=self.tr(u'数据库配置'),
            callback=self.run2_setsqlite,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path5,
            text=self.tr(u'创建点图层'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path6,
            text=self.tr(u'自定义/点/线/面图形绘制(CustomDraw)'),
            callback=self.run6,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path7,
            text=self.tr(u'绘制扇区图形(Sector)'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path8,
            text=self.tr(u'缓冲区计算'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path4,
            text=self.tr(u'包含关系计算'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path4,
            text=self.tr(u'相交关系计算'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path4,
            text=self.tr(u'图形合并计算'),
            callback=self.run5,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path4,
            text=self.tr(u'图形面积计算(Area)'),
            callback=self.run5,
            parent=self.iface.mainWindow())
    # --------------------------------------------------------------------------

    def onClosePlugin(self):
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)
        self.pluginIsActive = False

    def onClosePlugin2(self):
        self.dockwidget2.closingPlugin.disconnect(self.onClosePlugin2)
        self.pluginIsActive2 = False

    def onClosePlugin3(self):
        self.dockwidget3.closingPlugin.disconnect(self.onClosePlugin3)
        self.pluginIsActive3 = False

    def onClosePlugin4(self):
        self.dockwidget4.closingPlugin.disconnect(self.onClosePlugin4)
        self.pluginIsActive4 = False

    def onClosePlugin5(self):
        self.dockwidget5.closingPlugin.disconnect(self.onClosePlugin5)
        self.pluginIsActive5 = False

    def onClosePlugin6(self):
        self.dockwidget6.closingPlugin.disconnect(self.onClosePlugin6)
        self.pluginIsActive6 = False

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&申少军工具箱'),
                action)
            self.iface.removeToolBarIcon(action)

        del self.toolbar

    def run(self):

        if not self.pluginIsActive:
            self.pluginIsActive = True
            if self.dockwidget is None:
                self.dockwidget = cyanloveDockWidget()
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget)
            # 设置为浮动
            self.dockwidget.setFloating(True)
            # 设置为 位置X ,Y ,宽度 ,高度
            self.dockwidget.setGeometry(1250, 580, 270, 150)
            self.dockwidget.show()

    def run2_setsqlite(self):
        if not self.pluginIsActive2:
            self.pluginIsActive2 = True
            if self.dockwidget2 is None:
                self.dockwidget2 = cyanlove_sqliteset()
            self.dockwidget2.closingPlugin.connect(self.onClosePlugin2)
            self.iface.addDockWidget(Qt.AllDockWidgetAreas, self.dockwidget2)

            self.dockwidget2.show()

    def run3(self):
        if not self.pluginIsActive3:
            self.pluginIsActive3 = True
            if self.dockwidget3 is None:
                self.dockwidget3 = cyanlove_exportwkt()
            self.dockwidget3.closingPlugin.connect(self.onClosePlugin3)
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget3)
            # 设置为浮动
            self.dockwidget3.setFloating(True)
            self.dockwidget3.setGeometry(500, 400, 600, 160)
            self.dockwidget3.show()

    def run4(self):
        if not self.pluginIsActive4:
            self.pluginIsActive4 = True
            if self.dockwidget4 is None:
                self.dockwidget4 = cyanlove_import_geometry()
            self.dockwidget4.closingPlugin.connect(self.onClosePlugin4)
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget4)
            # 设置为浮动
            self.dockwidget4.setFloating(True)
            # 设置为 位置X ,Y ,宽度 ,高度
            self.dockwidget4.setGeometry(400, 300, 880, 240)
            self.dockwidget4.show()

    def run5(self):
        if not self.pluginIsActive5:
            self.pluginIsActive5 = True
            if self.dockwidget5 is None:
                self.dockwidget5 = cyanlove_createpoint()
            self.dockwidget5.closingPlugin.connect(self.onClosePlugin5)
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget5)
            # 设置为浮动
            self.dockwidget5.setFloating(True)
            # 设置为 位置X ,Y ,宽度 ,高度
            self.dockwidget5.setGeometry(400, 300, 750, 140)
            self.dockwidget5.show()

    def run6(self):
        if not self.pluginIsActive6:
            self.pluginIsActive6 = True
            if self.dockwidget6 is None:
                self.dockwidget6 = cyanlove_customdraw()
            self.dockwidget6.closingPlugin.connect(self.onClosePlugin6)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget6)
            self.dockwidget6.show()
