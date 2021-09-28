##############################################
#
#	KML to EXIF
#
#	Author:		Alex Poon (Esri China (H.K.))
#	Date:		  Sep 28, 2021
#	Last update:   Sep 28, 2021
#
##############################################
import arcpy

from re import findall
from subprocess import check_output
import xml.etree.ElementTree as ET

class Toolbox(object):
	def __init__(self):
		self.label =  "KML to EXIF"
		self.alias  = "KMLToExif"

		# List of tool classes associated with this toolbox
		self.tools = [KMLToExif] 

class KMLToExif(object):
	def __init__(self):
		self.label	   = "KML to EXIF"
		self.description = "Propagate EXIF metadata of image files from a KML file."

	def getParameterInfo(self):
		# Input
		in_kml = arcpy.Parameter(
			displayName="Input KML File",
			name="in_kml",
			datatype="DEFile",
			parameterType="Required",
			direction="Input")
		in_kml.filter.list = ['kml','xml']

		parameters = [in_kml]
		
		return parameters


	def execute(self, parameters, messages):
		try:
			a = check_output('conda install -y pil piexif')
		except:
			pass

		from PIL import Image

		##########################################
		tree = ET.parse(parameters[0].valueAsText)
		ns = findall(r'\{.*?\}',tree.getroot().tag)[0]

		for photo in tree.findall(f'.//{ns}PhotoOverlay'):
			_,_,_,heading,tilt,roll = [float(x.text) for x in x.find(findall(r'\{.*?\}',root.tag)[0]+'Camera').getchildren()]
			x,y,z = [float(x) for x in photo.find(f'{ns}Point').getchildren()[0].text.split(',')    # KML always use (lng, lat)