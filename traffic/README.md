# Traffic Demos

## NOTE

Since the Transport Department overhauled their page and added security features, the code has been outdated. A workaround is being made.

New activate sequence (replace `<1,2,3,4>` with 1 [Hong Kong Island], 2 [Kowloon], 3 [Tsuen Wan] or 4 [Tuen Mun]; also note that \`r\`n is a magic word of **PS1**):
```
https://www.hkemobility.gov.hk/tc/traffic-information/live/webcast

document.querySelector('#app > div > main > div > div > div.row.main-panel-container.no-gutters > div.app-left-panel.white.col > div > div.flex-grow-container.pa-2.white > div.flex-grow-1.fill-height.overflow-y-auto.px-1 > div > div.pb-2.flex-shrink-0.v-item-group.theme--light.v-btn-toggle.v-btn-toggle--tile.teal--text.text--accent-3 > button:nth-child(<1,2,3,4>)').click()
```

The subprocess command becomes:
```
ffmpeg -headers "authority: www.hkemobility.gov.hk`r`nsec-ch-ua: 'Chromium';v='97', ' Not;A Brand';v='99'`r`nsec-ch-ua-mobile: ?0`r`nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4691.0 Safari/537.36`r`nsec-ch-ua-platform: 'Windows'`r`naccept: */*`r`nsec-fetch-site: same-origin`r`nsec-fetch-mode: cors`r`nsec-fetch-dest: empty`r`nreferer: https://www.hkemobility.gov.hk/tc/traffic-information/live/webcast`r`naccept-language: en-US,en;q=0.9`r`ncookie:  language=zh-HK`r`n" -i "<to be completed by selenium-wire>" -vsync 0 -vf fps=5 one%d.jpg
```

On subprocess exit (one security feature added is a two-minute timeout), call `ffmpeg` again.

## 1. Car count using the YOLOv3 library from [`arcgis.learn`](https://developers.arcgis.com/python/api-reference/arcgis.learn.toc.html)

[![Live Traffic View Using Object Detection & GeoEvent Server](https://img.youtube.com/vi/dG4d191XsqU/0.jpg)](https://www.youtube.com/watch?v=dG4d191XsqU "Live Traffic View Using Object Detection & GeoEvent Server")

The Python tool leverages the open-source YOLOv3 convolutional neural network (CNN) library bundled in the [`arcgis.learn` Python library](https://developers.arcgis.com/python/api-reference/arcgis.learn.toc.html). The neural network is designed for fast object detection.

<!-- A new `conda` environment is created. -->

### Instructions
For the detection to be useful, some work needs to be done beforehand. First, run the script and a GUI will open. Open a reference image, draw the polygons for each traffic lane, and the tool will turn them into pixel coordinates (masks).

![Fig. 1](img/define_polygons.png)  ![Fig. 2](img/define_polygons2.png)

![Fig. 3](img/define_polygons3.png) ![Fig. 4](img/define_polygons4.png) ![Fig. 5](img/define_polygons5.png)


| Camera code     | Traffic lane | Mapping       |
|-----------------|--------------|---------------|
| H106F | 1 | Connaught Rd Central near Exchange Square |
| H109F | 1 | Garden Road Flyover towards Cotton Tree Drive |
| H109F | 2 | Queensway heading towards Queen's Road Central |
| H207F | 1 | Cross Harbour Tunnel Hong Kong Side |
| H210F | 1 | Aberdeen Tunnel - Wan Chai Side (entering, southwards) |
| H210F | 2 | Aberdeen Tunnel - Wan Chai Side (exiting, northwards) |
| H210F | 3 | Wong Nai Chung Road / Queen's Road East |
| H801F | 1 | Island Eastern Corridor near Ka Wah Center towards Central / Causeway Bay (westwards) |
| H801F | 2 | Island Eastern Corridor near Ka Wah Center towards Eastern Harbour Crossing (eastwards) |
| H801F | 3 | Island Eastern Corridor near Ka Wah Center towards Shau Kei Wan / Chai Wan (eastwards) |
| K107F | 1 | Cross Harbour Tunnel Kownloon Side (exiting, northwards) |
| K107F | 2 | Cross Harbour Tunnel Kownloon Side (entering, southwards) |
| K109F | 1 | Chatham Road S near Prince Margaret Road (eastwards) |
| K109F | 2 | Chatham Road S near Prince Margaret Road towards West Kowloon Corridor (westwards) |
| K409F | 1 | Princess Margaret Road near Argyle Street towards Kowloon Tong (northwards) |
| K409F | 2 | Princess Margaret Road near Argyle Street towards Hong Hom (southwards) |
| K409F | 3 | Argyle Street Flyover near Princess Margaret Road (eastwards) |
| K502F | 1 | Waterloo Road Flyover (southwards) |
| K502F | 2 | Waterloo Road Flyover towards Lion Rock Tunnel (northwards) |
| K502F | 3 | Waterloo Road towards Cornwall Street (northwards) |
| K502F | 4 | Waterloo Road (northwards) |
| K614F | 1 | Clear Water Bay Road (eastwards) |
| K614F | 2 | Clear Water Bay Road towards Lung Cheung Road (westwards) |


<!-- lat	lng	TR119F Tuen Mun Road - Sam Shing Hui
lat	lng	TR116F Tuen Mun Road - Siu Lam Section
lat	lng	TR107F Tuen Mun Road - Sham Tseng Section
lat	lng	TR103F Tuen Mun Road - Yau Kom Tau Section
lat	lng	TR101F Tuen Mun Road - Chai Wan Kok
lat	lng	
lat	lng	TW103F Tsuen Wan Road near Tsuen Tsing Intchg
lat	lng	TW105F Kwai Tsing Road near Tsing Yi Bridge
lat	lng	TW102F Kwai Chung Road near Container Terminal
lat	lng	TW117F Castle Peak Road near Texaco Road North
lat	lng	TW120F Tsuen Wan Road near Tai Chung Road -->

**The polygon masks (2D NumPy array of True/False) have been pickled to a single file.** For each recognition, the Python tool tests whether the centres of the bounding boxes are inside each polygon, and updates the Feature Layer according to the camera code detected and vehicle position (traffic lane).

### Get training data

Obtaining training data is simple. It is simply extracting still images from a live video stream:
```
ffmpeg -i https://webcast.td.gov.hk/live/mp4:hk/~~~.m3u8?token=~~~ -vf fps=1 out%d.jpg
```
The exact m3u8 URL can be obtained using `selenium-wire` (see code for details).

### Future enhancements

Stream output video to a webpage for visualisation

## 2. TomTom Traffic Data

[![TomTom traffic layer updates every 0.5 minutes (that???s the limit)](https://img.youtube.com/vi/RaSymtkdyhA/0.jpg)](https://www.youtube.com/watch?v=RaSymtkdyhA "TomTom traffic layer updates every 0.5 minutes (that???s the limit)")

See [`tomtom_intermediate_traffic.py`](tomtom_intermediate_traffic.py). The script pushes live traffic data to ArcGIS Online every half minute. Enter your own ArcGIS login credentials and TomTom Intermediate Traffic API Key into the file. ArcGIS Pro is **not** necessary to run the script.

The Intermediate Traffic API returns a ProtoBuf like this:
```protobuf
location {
  openlr: "\013Q>\325\017\316\345#\235{\366\372\n\206#\t"
  lengthInMeters: 7223
}
speed {
  averageSpeedKmph: 40
  travelTimeSeconds: 648
  confidence: 98
  relativeSpeed: 0.716
  trafficCondition: FREE_TRAFFIC
}
sectionSpeed {
  startOffsetInMeters: 0
  speed {
    averageSpeedKmph: 22
    travelTimeSeconds: 160
    confidence: 97
    relativeSpeed: 0.452
    trafficCondition: FREE_TRAFFIC
  }
}
sectionSpeed {
  startOffsetInMeters: 967
  speed {
    averageSpeedKmph: 47
    travelTimeSeconds: 460
    confidence: 98
    relativeSpeed: 0.812
    trafficCondition: FREE_TRAFFIC
  }
}
sectionSpeed {
  startOffsetInMeters: 6980
  speed {
    averageSpeedKmph: 30
    travelTimeSeconds: 29
    confidence: 99
    relativeSpeed: 0.702
    trafficCondition: FREE_TRAFFIC
  }
}
```

If a road segment has **sectionSpeed**s, section speeds will be used while the overall speed will be ignored. The script should be able to split the road segment into fine sections properly according to the `startOffsetInMeters` attribute:

![Section speed](img/section_speed.png)

To install the dependencies, enter the following in the command line:
```
pip3 install -r requirements.txt
```

### Future enhancements

Set unmatched openLR to -1.

## 3. Traffic Emulation

This is for demo only: [https://demo2.hkgisportal.com/traffic_simulation/](https://demo2.hkgisportal.com/traffic_simulation/)

### Instructions

Gather the 3D models you want to use, normally one model should have more than one material, which is suboptimal since loading the textures degrade the performance. Therefore, it is required to **UV unwrap** each model and **texture bake** it into a small texture (e.g. 256 px * 256 px). For lights, use **combined bake** instead of texture bake. Export all models into GLB which is the only supported format (except raw glTF). You may use the open-source software Blender to complete this task: [Official Guide from Esri](https://www.esri.com/arcgis-blog/products/arcgis/3d-gis/gis-visualization-and-storytelling-in-3d/)

### Future enhancements

Refactor traffic lights:
* trafficlight_0.glb -> trafficlight_frame.glb + trafficlight_red_on.glb + trafficlight_yellow_off.glb + trafficlight_green_off.glb
* trafficlight_1.glb -> trafficlight_frame.glb + trafficlight_red_on.glb + trafficlight_yellow_on.glb + trafficlight_green_off.glb
* trafficlight_2.glb -> trafficlight_frame.glb + trafficlight_red_on.glb + trafficlight_yellow_off.glb + trafficlight_green_on.glb
* trafficlight_3.glb -> trafficlight_frame.glb + trafficlight_red_off.glb + trafficlight_yellow_on.glb + trafficlight_green_off.glb

More open-box options, highlight peak hours <!--, people left in queues, flying bus bug-->

### Common Questions

* How is the data historical traffic data collected?

The TomTom Traffic API is queried every half minute. The collected data is then grouped by road segment, date of week and the 10-minute time frame, in order to obtain the average speeds.

* Which time period is the historical traffic data collected?

We are at an early stage. We have been collecting data from TomTom since mid-August.
Where is the historical traffic data stored?
The data is hosted on ArcGIS Online as a Table Service.

* What is the algorithm in a nutshell?

There is a single **for-loop** to render the graphics that updates every 1 / frame-per-rate seconds. The displacement distances of each frame are calculated by the formulae: S = D / T; Dsegment = { [S * (1/60/60)] * 1000 } metres; Dframe = (Dsegment / fps) metres.

* How did you obatain the mesh model?

The mesh model is mostly customly made. A portion of the model is taken from the Lands Department.
