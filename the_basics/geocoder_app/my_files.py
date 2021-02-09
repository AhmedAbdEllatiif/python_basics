from flask import send_file
import os 
from werkzeug.utils import secure_filename
import pandas
from geopy.geocoders import ArcGIS
import datetime


def handle_file(file):
    global converted_name
    filename,file_ext = os.path.splitext(file.filename)
    converted_name = "converted-{}{}".format(filename,file_ext)
    if file_ext != '.csv':
        return False , 'Only Support Files with Extention .CSV'
    has_address,df = has_column_address(file.filename)
    if has_address: 
        return True , df
    else:
        return False , 'csv file must include column address or Address'


def has_column_address(file):
    nom = ArcGIS()
    global df
    df = pandas.read_csv(file)
    df_port = pandas.DataFrame() 
    for col in df.columns:
        if str(col).lower() == 'address':
            df["full_Address"] = df["Address"] + ', ' + df['City'] + ', ' + df['State'] + ', ' + df['Country']
            df['coordinates'] = df["Address"].apply(nom.geocode)
            df['Longitude'] =  df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df['Latitude'] =  df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            df = df.drop('coordinates',1)
            df = df.drop('full_Address',1)
            return True ,df
    return False, None
    
    
    
def save_file():
    datename = datetime.datetime.now().strftime("%H-%M %Y-%m-%d {}".format(converted_name))
    upload_path = os.path.join('uploads',datename)
    df.to_csv(upload_path,index=None)
    return send_file(upload_path, attachment_filename=datename, as_attachment=True, cache_timeout=-1)
    