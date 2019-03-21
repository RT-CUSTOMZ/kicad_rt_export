#!/usr/bin/env python3
import sys
# from pcbnew import *
import pcbnew

import plot_pdf
import rtlab
# http://scottbezek.blogspot.com/2016/04/scripting-kicad-pcbnew-exports.html


filename=sys.argv[1] #e.g left-main/left-main.kicad_pcb

board = pcbnew.LoadBoard(filename)

pctl = pcbnew.PLOT_CONTROLLER(board)

popt = pctl.GetPlotOptions()

# popt.SetOutputDirectory("plot/")
popt.SetOutputDirectory(sys.argv[2])

plot_pdf.generatePdf(pctl, popt)

popt.SetMirror(False)

rtlab.generateGerber(pctl, popt, board)
