# state file generated using paraview version 5.8.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [942, 803]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999990905, 45.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.999999999990905, 45.5, 10000.0]
renderView1.CameraFocalPoint = [1.999999999990905, 45.5, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 12.499999999992724
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
arome_SP1_PrevisionFaiteLe_20201201T030000_PourLesHeures_07H12Hgrib2nc = NetCDFReader(FileName=['/home/willeiam/S9/Visu/Sceance_10Novembre/METEO_VISUALISATION_AVEC_DONNEES_Original/DATA/Arome_SP1_PrevisionFaiteLe_2020-12-01T03:00:00_PourLesHeures_07H12H.grib2.nc'])
arome_SP1_PrevisionFaiteLe_20201201T030000_PourLesHeures_07H12Hgrib2nc.Dimensions = '(latitude, longitude)'
arome_SP1_PrevisionFaiteLe_20201201T030000_PourLesHeures_07H12Hgrib2nc.SphericalCoordinates = 0
arome_SP1_PrevisionFaiteLe_20201201T030000_PourLesHeures_07H12Hgrib2nc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=arome_SP1_PrevisionFaiteLe_20201201T030000_PourLesHeures_07H12Hgrib2nc)
calculator1.ResultArrayName = 'celsius'
calculator1.Function = 'TMP_2maboveground - 273'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=calculator1)
extractSubset1.VOI = [0, 800, 0, 600, 0, 0]
extractSubset1.SampleRateI = 20
extractSubset1.SampleRateJ = 20

# create a new 'Calculator'
calculator2 = Calculator(Input=extractSubset1)
calculator2.ResultArrayName = 'Vecteur vent'
calculator2.Function = 'UGRD_10maboveground*iHat + VGRD_10maboveground*jHat'

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=calculator2)

# create a new 'Contour'
contour1 = Contour(Input=appendDatasets1)
contour1.ContourBy = ['POINTS', 'celsius']
contour1.Isosurfaces = [10.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Glyph'
glyph1 = Glyph(Input=contour1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Vecteur vent']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.GlyphTransform = 'Transform2'
glyph1.MaximumNumberOfSamplePoints = 500

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator2
calculator2Display = Show(calculator2, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'celsius'
celsiusLUT = GetColorTransferFunction('celsius')
celsiusLUT.RGBPoints = [-14.215597361326218, 0.231373, 0.298039, 0.752941, 2.0864304453134537, 0.865003, 0.865003, 0.865003, 18.388458251953125, 0.705882, 0.0156863, 0.14902]
celsiusLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'celsius'
celsiusPWF = GetOpacityTransferFunction('celsius')
celsiusPWF.Points = [-14.215597152709961, 0.0, 0.5, 0.0, 18.388458251953125, 1.0, 0.5, 0.0]
celsiusPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Slice'
calculator2Display.ColorArrayName = ['POINTS', 'celsius']
calculator2Display.LookupTable = celsiusLUT
calculator2Display.OSPRayScaleArray = 'celsius'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'None'
calculator2Display.ScaleFactor = 1.999999999998181
calculator2Display.SelectScaleArray = 'celsius'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'celsius'
calculator2Display.GaussianRadius = 0.09999999999990905
calculator2Display.SetScaleArray = ['POINTS', 'celsius']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'celsius']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 2.3525900722012016
calculator2Display.ScalarOpacityFunction = celsiusPWF
calculator2Display.IsosurfaceValues = [2.507110595703125]
calculator2Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [-13.078338623046875, 0.0, 0.5, 0.0, 18.092559814453125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [-13.078338623046875, 0.0, 0.5, 0.0, 18.092559814453125, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
calculator2Display.SliceFunction.Origin = [1.999999999990905, 45.5, 0.0]

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.LineWidth = 2.0
contour1Display.OSPRayScaleArray = 'celsius'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'Vecteur vent'
contour1Display.ScaleFactor = 2.0
contour1Display.SelectScaleArray = 'celsius'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'celsius'
contour1Display.GaussianRadius = 0.1
contour1Display.SetScaleArray = ['POINTS', 'celsius']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'celsius']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [10.0, 0.0, 0.5, 0.0, 10.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [10.0, 0.0, 0.5, 0.0, 10.001953125, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.AmbientColor = [0.0, 0.3333333333333333, 1.0]
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.DiffuseColor = [0.0, 0.3333333333333333, 1.0]
glyph1Display.OSPRayScaleArray = 'celsius'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 2.08750057220459
glyph1Display.SelectScaleArray = 'celsius'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'celsius'
glyph1Display.GaussianRadius = 0.1043750286102295
glyph1Display.SetScaleArray = ['POINTS', 'celsius']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'celsius']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [10.0, 0.0, 0.5, 0.0, 10.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [10.0, 0.0, 0.5, 0.0, 10.001953125, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for celsiusLUT in view renderView1
celsiusLUTColorBar = GetScalarBar(celsiusLUT, renderView1)
celsiusLUTColorBar.Position = [0.8715498938428875, 0.014943960149439602]
celsiusLUTColorBar.Title = 'celsius'
celsiusLUTColorBar.ComponentTitle = ''

# set color bar visibility
celsiusLUTColorBar.Visibility = 1

# show color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(calculator2)
# ----------------------------------------------------------------