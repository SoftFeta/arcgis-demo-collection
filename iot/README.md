# Internet of Things Demos

## Sensors Dashboard

[https://demo2.hkgisportal.com/sensors2/](https://demo2.hkgisportal.com/sensors2/)

<img src="img/screenshot.png" width="600px"></img>

This is a clone of the [Coolmaps NYC Work Orders](https://coolmaps.esri.com/NYC/NYCHA/dashboard/) app, with the residential block changed to the newly-built eResidence in To Kwa Wan, Kowloon, Hong Kong. A GeoEvent Server installation is required.

Some data wrangling is needed. For example, the ArcGIS Pro geoprocessing tool **Polygon Neighbours** is used to find neighbouring units of selected flats. A ModelBuilder is made to automate data preprocessing. You can re-run the workflow using it for any other building.

## GeoEvent Sever Settings

*Engineering rooms* mapping used in the sample. For the time being only 4 endpoints (coloured) are used:

![mapping](img/mapping.png)

*Engineering rooms* input connector settings of GeoEvent Server used in the sample:

![settings](img/input_settings.png)

*Engineering rooms* output connector settings of GeoEvent Server used in the sample:

![settings](img/output_settings.png)

*Engineering rooms* service settings of GeoEvent Server used in the sample:

![settings](img/service_settings.png)

*CHILLER PLANT* Field Calculator settings of GeoEvent Server used in the sample:

![settings](img/field_calculator_settings.png)

*Engineering rooms* Field Enricher settings of GeoEvent Server used in the sample:

![settings](img/field_enricher_settings.png)

*Engineering rooms* Field Mapper settings of GeoEvent Server used in the sample:

![settings](img/field_mapper_settings.png)

## Sensor Readings

To change the readings of sensors (for demonstration only), run `python `[**outside_controller.py**](outside_controller.py). No remote desktop is needed.

