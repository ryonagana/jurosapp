#!/bin/bash
RESPATH="resources/"



pyside-uic resources/calculardatas.ui > resources/calculardatas.py
pyside-uic resources/calcularjuros.ui > resources/calculardatas.py
pyside-uic resources/descontos.ui > resources/descontos.py
pyside-uic resources/about.ui > resources/about.py
pyside-uic resources/jurossimples.ui > resources/jurossimples.py
pyside-uic resources/mainwindow.ui > resources/mainwindow.py

zip -r resources.uipack resources/*.py resources.uipack
mv resources.uipack res/resources.uipack










