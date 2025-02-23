import osmnx as ox
import numpy as np
import geopandas as gpan
from shapely import Polygon


class MyFunc():
    @staticmethod
    def geojson_to_kml(input_file:str)->Polygon:
        """
        This Function will take a geojson file as input 
        and will save a kml file in output_file
        input_file: str data representing the file location path
        output_file: str data represents the file ouput path
        """
        iFile = gpan.read_file(input_file, driver='GEOJSON')
        return iFile.geometry[0]

    @staticmethod
    def kml_to_geojson(input_file:str, output_file:str):
        """
        This Function will take a kml file as input 
        and will save a geojson file in output_file
        input_file: str data representing the file location path
        output_file: str data represents the file ouput path
        """
        iFile = gpan.read_file(input_file, driver='KML')
        iFile.to_file(output_file, driver="GeoJSON")
    @staticmethod   
    def kml_to_polygon(input_file:str) -> Polygon:
        """
        This Function will take a kml file as input 
        and will return a Polygon output
        input_file: str data representing the file location path
        
        """
        iFile = gpan.read_file(input_file, driver='KML')
        return iFile.geometry[0]

        
    @staticmethod                           
    def export_from_point(lat:float, long:float, distance:int, output_file:str): 
        """This Function will take a lattitude, longitude and distance as input
        This function also take a str for output file name
        lattitude: float 
        longitude: float
        distance: int 
        output_file: str
        
        """                               
        gdf = ox.features.features_from_point(center_point=(lat,long),
                                            tags={
                                                "highway":[
                                                    "trunk",
                                                    "primary",
                                                    "secondary",
                                                    "tertiary",
                                                    "unclassified",
                                                    "primary-link",
                                                    "secondary-link",
                                                    "tertiary-link"
                                                    ]
                                                },
                                            dist=3000)

        gdf.to_file('op.kml', driver="KML")
        
        
    @staticmethod  
    def export_from_polygon(poly:Polygon, output_file:str):
        """This Function will take a Polygon as input
        This function also take a str for output file name
        poly: Polygon
        output_file: str
        """
        gdf = ox.features.features_from_polygon(polygon=poly,
                                                        tags={
                                                            "highway":
                                                                [
                                                                    "trunk",
                                                                    "primary",
                                                                    "secondary",
                                                                    "tertiary",
                                                                    "unclassified",
                                                                    "primary-link",
                                                                    "secondary-link",
                                                                    "tertiary-link"
                                                                ]
                                                            }
                                                        )
        try:
            gdf.to_file(output_file, driver="KML", mode='a')
        except FileNotFoundError:
            gdf.to_file(output_file, driver="KML", mode='w')



    @staticmethod    
    def export_from_polygon_or_kml(input_geometry:Polygon|str, output_file:str ):
        """This Function will take a kml File or Polygon as input
        This function also take a str for output file name
        """
        if isinstance(input_geometry,Polygon):
            """
            Check The Input File Format for Polygon Data Type
            """
            
            poly = input_geometry
            MyFunc.export_from_polygon(poly=poly, output_file=output_file)
            return 
        elif isinstance(input_geometry,str):
            """
            Check The Input File Format for str Data Type
            """
            
            poly=MyFunc.kml_to_polygon(input_file=input_geometry)
            MyFunc.export_from_polygon(poly=poly, output_file=output_file)
            
        else:
            
            raise("Uncorrect Input File Format")
            
            
            
            

        
 