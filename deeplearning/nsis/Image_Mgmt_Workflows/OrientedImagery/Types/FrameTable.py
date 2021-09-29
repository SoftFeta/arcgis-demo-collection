#------------------------------------------------------------------------------
# Copyright 2018 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
# Name: frametable.py
# Description: This is a custom OIC type. 
# Version: 2.3
# Date Created : 20181104
# Date updated : 20191126
# Requirements: ArcGIS Pro 2.2
# Author: Esri Imagery Workflows team
#------------------------------------------------------------------------------

import arcpy
import os
import orientedimagerytools as oitools

def __init__(self, nametype):
    self._name = nametype


def main(oicPath, oicParas, inputParams, defValues, log=None):
    try:
        csvPath = inputParams['file']
        if log:
            log.Message("Input file: {}".format(csvPath), log.const_general_text)
        oitools.importCSVtoFC(csvPath, oicPath, defValues, log)
        return ("Successfully added images from frame table.")
    except Exception as e:
        if log:
            log.Message("Error in adding images from frame table. {}".format(str(e)), log.const_critical_text)
        return ("Error in adding images from frame table")