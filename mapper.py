import argparse
from func import *
import sys

def isFile(file:str, format:str)->bool:
    f = file.split('.')
    if format[1:] in f[len(f)-1]:
        return True
    return False


def main():
    m = MyFunc()
    parser = argparse.ArgumentParser()
    parser.add_argument('option', type=str, help="""This is the option for outfile if 
                        'geotokml' it will output kml road
                        if 'kmltokml' it will output kml road
                        if 'kmltogeo' it will output geojson""")
    
    parser.add_argument('input_file', type=str, help="""Input file for convertion or export""")
    parser.add_argument('output_file', type=str, help="""Output File""")
    
    args = parser.parse_args()
    
    iFile=args.input_file
    oFile=args.output_file
    
    if args.option == 'kmltogeo':
        if (isFile(iFile, '.kml')) & (isFile(oFile,'.geojson')):
            
            m.kml_to_geojson(input_file=iFile, output_file=oFile)
            return
        print("Not Correct File Format")
        sys.exit()
        
        
        
    elif args.option == 'geotokml':
        if isFile(iFile, '.geojson') & isFile(oFile,'.kml'):
            m.export_from_polygon_or_kml(
                                    input_geometry=m.geojson_to_kml(input_file=iFile),
                                    output_file=oFile 
                                )
            return
        print("Not Correct File Format")
        sys.exit()
        
        
        
    elif args.option == 'kmltokml':
        if not isFile(iFile, '.kml') or isFile(oFile,'.kml'):
            m.export_from_polygon_or_kml(input_geometry=iFile, output_file=oFile )
            return
        print("Not Correct File Format")
        sys.exit()
        
        
        
if __name__=="__main__":
    main()