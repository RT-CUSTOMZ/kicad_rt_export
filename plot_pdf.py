import sys
# from pcbnew import *
import pcbnew

if(pcbnew.Version()=="7.0.0"):
    version7 = True

def generatePdf(plotControl, plotOptions, ):
    # Set some important plot options:
    plotOptions.SetPlotFrameRef(False)
    # plotOptions.SetLineWidth(pcbnew.FromMM(0.35))

    plotOptions.SetAutoScale(False)
    plotOptions.SetScale(1)
    plotOptions.SetMirror(False)
    plotOptions.SetUseGerberAttributes(True)
    if(not version7):
        plotOptions.SetExcludeEdgeLayer(False)

    plotOptions.SetScale(1)
    # plotOptions.SetUseAuxOrigin(True)
    plotOptions.SetUseAuxOrigin(False) # drill file and pdf should be the same

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

    # Once the defaults are set it become pretty easy...
    # I have a Turing-complete programming language here: I'll use it...
    # param 0 is a string added to the file base name to identify the drawing
    # param 1 is the layer ID
    plot_plan = [
        # ( "CuTop", F_Cu, "Top layer" ),
        ( "CuBottom", pcbnew.B_Cu, "Bottom layer" ),
        # ( "PasteBottom", B_Paste, "Paste Bottom" ),
        # ( "PasteTop", F_Paste, "Paste top" ),
        # ( "SilkTop", F_SilkS, "Silk top" ),
        # ( "SilkBottom", B_SilkS, "Silk top" ),
        # ( "MaskTop", F_Mask, "Mask top" ),
        # ( "MaskBottom", B_Mask, "Mask bottom" ),
        # ( "EdgeCuts", Edge_Cuts, "Edges" ),
    ]

    if(version7):
        layerselection = plotOptions.GetPlotOnAllLayersSelection()
        addedlayerselection = layerselection.addLayer(pcbnew.Edge_Cuts)
        plotOptions.SetPlotOnAllLayersSelection(addedlayerselection)

    for layer_info in plot_plan:
        plotControl.SetLayer(layer_info[1])
        plotControl.OpenPlotfile(layer_info[0], pcbnew.PLOT_FORMAT_PDF, layer_info[2])
        plotControl.PlotLayer()

    # plot Top inverted
    plotOptions.SetMirror(True)
    plotControl.SetLayer(pcbnew.F_Cu)
    plotControl.OpenPlotfile("CuTop", pcbnew.PLOT_FORMAT_PDF, "Top layer")
    plotControl.PlotLayer()
