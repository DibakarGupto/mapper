from .function import MyFunc
doc ="""
Usable For Converting 
1-->> .kml file Polygon to .geojson
2-->> .kml Polygon to extract road file in .kml format
3-->> .geojson Polygon to extract road file in .kml format
Usage....
1-->> python main.py 'kmltogeo "input_file_dir.kml" "output_file_dir.geojson"
2-->> python main.py 'kmltokml' "input_file_dir.kml" "output_file_dir.kml"
3-->> python main.py 'geotokml' "input_file_dir.kml" "output_file_dir.kml"
for help
       -->> python main.py -h 
                  or
            python main.py --help
"""
print(doc)