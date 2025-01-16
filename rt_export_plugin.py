from __future__ import absolute_import

import os
import sys

import pcbnew

from . import plot_pdf
from . import rtlab

if __name__ == "__main__":
    # Circumvent the "scripts can't do relative imports because they are not
    # packages" restriction by asserting dominance and making it a package!
    dirname = os.path.dirname(os.path.abspath(__file__))
    __package__ = os.path.basename(dirname)
    sys.path.insert(0, os.path.dirname(dirname))
    __import__(__package__)

class RtExportPlugin(pcbnew.ActionPlugin):

    def defaults(self):
        """
        Method defaults must be redefined
        self.name should be the menu label to use
        self.category should be the category (not yet used)
        self.description should be a comprehensive description
          of the plugin
        """
        self.name = "Generate RT manufactoring data"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(
                os.path.dirname(__file__), 'icon.png')
        self.description = "Generate manufactoring data for RT Lab manufactoring process."

    def Run(self):
        pcb_file_name = pcbnew.GetBoard().GetFileName()
        if not pcb_file_name:
            ibom.logerror('Please save the board file before generating manufactoring data.')
            return
        print(pcb_file_name)

        board = pcbnew.LoadBoard(pcb_file_name)
        pctl = pcbnew.PLOT_CONTROLLER(board)
        popt = pctl.GetPlotOptions()

        popt.SetOutputDirectory("export/")

        plot_pdf.generatePdf(pctl, popt)
        popt.SetMirror(False)
        rtlab.generateGerber(pctl, popt, board)
        # rtlab.generateGerberforUV(pctl, popt, board)

