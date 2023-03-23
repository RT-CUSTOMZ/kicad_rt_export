import sys
# from pcbnew import *
import pcbnew

majorVersion = int(pcbnew.Version().split(".")[0])


def generatePdf(plotControl, plotOptions, ):
    # Set some important plot options:
    plotOptions.SetPlotFrameRef(False)
    # plotOptions.SetLineWidth(pcbnew.FromMM(0.35))

    plotOptions.SetAutoScale(False)
    plotOptions.SetScale(1)
    plotOptions.SetMirror(False)
    plotOptions.SetUseGerberAttributes(True)
    if (majorVersion < 7):
        plotOptions.SetExcludeEdgeLayer(False)

    plotOptions.SetScale(1)
    # plotOptions.SetUseAuxOrigin(True)
    plotOptions.SetUseAuxOrigin(False)  # drill file and pdf should be the same

    # This by gerbers only (also the name is truly horrid!)
    plotOptions.SetSubtractMaskFromSilk(False)

    #########################
    #### CuBottom.gbr    ####
    #### CuTop.gbr       ####
    #### EdgeCuts.gbr    ####
    #### MaskBottom.gbr  ####
    #### MaskTop.gbr     ####
    #### PasteBottom.gbr ####
    #### PasteTop.gbr    ####
    #### SilkBottom.gbr  ####
    #### SilkTop.gbr     ####
    #########################

    if (majorVersion >= 7):
        # Plot Bottom
        seq = pcbnew.LSEQ()
        seq.push_back(pcbnew.Edge_Cuts)
        seq.push_back(pcbnew.B_Cu)

        plotControl.OpenPlotfile(
            "CuBottom", pcbnew.PLOT_FORMAT_PDF, "Bottom layer")
        plotControl.PlotLayers(seq)

        # Plot Top inverted
        seq = pcbnew.LSEQ()
        seq.push_back(pcbnew.Edge_Cuts)
        seq.push_back(pcbnew.F_Cu)

        plotOptions.SetMirror(True)
        plotControl.OpenPlotfile("CuTop", pcbnew.PLOT_FORMAT_PDF, "Top layer")
        plotControl.PlotLayers(seq)

    else:
        # plot Bottom
        plotControl.SetLayer(pcbnew.B_Cu)
        plotControl.OpenPlotfile(
            "CuBottom", pcbnew.PLOT_FORMAT_PDF, "Bottom layer")
        plotControl.PlotLayer()

        # plot Top inverted
        plotOptions.SetMirror(True)
        plotControl.SetLayer(pcbnew.F_Cu)
        plotControl.OpenPlotfile("CuTop", pcbnew.PLOT_FORMAT_PDF, "Top layer")
        plotControl.PlotLayer()
