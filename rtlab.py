import sys
# from pcbnew import *
import pcbnew

if(pcbnew.Version()=="7.0.0"):
    version7 = True

def generateGerberforUV(plotControl, plotOptions, board):

    if(not version7):
        plotOptions.SetExcludeEdgeLayer(False)

    plotOptions.SetPlotViaOnMaskLayer(True)

    plotOptions.SetPlotValue(False)
    plotOptions.SetPlotReference(False)

    plotOptions.SetDisableGerberMacros(False)
    plotOptions.SetUseGerberX2format(False)
    plotOptions.SetIncludeGerberNetlistInfo(False)


    filler = pcbnew.ZONE_FILLER(board) # create the filler provide the board as a param
    filler.Fill(board.Zones()) # use the filler to re-fill all Zones on the board.
    
    plotControl.SetLayer(pcbnew.F_Cu)
    plotControl.OpenPlotfile("F.Cu.UV", pcbnew.PLOT_FORMAT_GERBER, "Top Copper UV")
    plotControl.PlotLayer()

    plotControl.SetLayer(pcbnew.B_Cu)
    plotControl.OpenPlotfile("B.Cu.UV", pcbnew.PLOT_FORMAT_GERBER, "Bottom Copper UV")
    plotControl.PlotLayer()

def generateGerber(plotControl, plotOptions, board):
    plotOptions.SetPlotFrameRef(False)
    # plotOptions.SetLineWidth(pcbnew.FromMM(0.35))

    plotOptions.SetAutoScale(False)
    plotOptions.SetScale(1)
    plotOptions.SetMirror(False)

    plotOptions.SetUseGerberAttributes(False)
    # plotOptions.SetUseGerberX2format(False)
    
    if(not version7):
        plotOptions.SetExcludeEdgeLayer(True)

    # plotOptions.SetUseAuxOrigin(True)
    plotOptions.SetUseAuxOrigin(False) # drill file and pdf should be the same

    # This by gerbers only (also the name is truly horrid!)
    plotOptions.SetSubtractMaskFromSilk(False)


    plotOptions.SetPlotReference(False)
    plotOptions.SetPlotInvisibleText(True)
    if(not version7):
        plotOptions.SetExcludeEdgeLayer(True)

    # Passermarken
    addUserEco1LayerToFiducials(board)
    plotControl.SetLayer(pcbnew.Eco1_User)
    plotControl.OpenPlotfile("Eco1.User", pcbnew.PLOT_FORMAT_GERBER, "LPKF Passermarken")
    plotControl.PlotLayer()

    #Copper top
    plotControl.SetLayer(pcbnew.F_Cu)
    plotControl.OpenPlotfile("F.Cu", pcbnew.PLOT_FORMAT_GERBER, "Top Copper")
    plotControl.PlotLayer()

    #Copper bot
    plotControl.SetLayer(pcbnew.B_Cu)
    plotControl.OpenPlotfile("B.Cu", pcbnew.PLOT_FORMAT_GERBER, "Bot Copper")
    plotControl.PlotLayer()

    #Edge cuts (Fraesungen)
    plotControl.SetLayer(pcbnew.Edge_Cuts)
    plotControl.OpenPlotfile("Edge.Cuts", pcbnew.PLOT_FORMAT_GERBER, "Cut layer")
    plotControl.PlotLayer()


    # drill files
    drlwriter = pcbnew.GERBER_WRITER( board )
    drlwriter.SetMapFileFormat( pcbnew.PLOT_FORMAT_PDF )

    mirror = False
    minimalHeader = False
    offset = pcbnew.wxPoint(0,0)
    # False to generate 2 separate drill files (one for plated holes, one for non plated holes)
    # True to generate only one drill file
    mergeNPTH = True
    # drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )
    if(not version7):
        drlwriter.SetOptions( offset)

    metricFmt = True
    drlwriter.SetFormat( metricFmt )

    genDrl = True
    genMap = True
    print('create drill and map files in %s' % (plotControl.GetPlotDirName() ))
    drlwriter.CreateDrillandMapFilesSet( plotControl.GetPlotDirName(), genDrl, genMap );

    # One can create a text file to report drill statistics
    rptfn = plotControl.GetPlotDirName() + 'drill_report.rpt'
    print('report: %s' % ( rptfn ))
    drlwriter.GenDrillReportFile( rptfn );

def addUserEco1LayerToFiducials(board):
    for fp in board.GetFootprints():
        fpRef = fp.GetReference()

        if(fpRef.startswith("FID")):
            for  fpPad in fp.Pads():
                layerSet = fpPad.GetLayerSet()
                if(layerSet.Contains(pcbnew.Eco1_User) == False):
                    layerSet.AddLayer(pcbnew.Eco1_User)
                    fpPad.SetLayerSet(layerSet)
