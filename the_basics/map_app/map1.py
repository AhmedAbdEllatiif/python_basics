import folium
import pandas
 
# To read Volcanoes from Volcanoes.txt file
df = pandas.read_csv("files/Volcanoes.txt")
lats = list(df["LAT"])
lons = list(df["LON"])
names = list(df["NAME"])
elves = list(df["ELEV"])


# return color according to volcano elevation
def color_picker(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return 'orange'  
    else: 
        return 'red'
    
 
# To build maker    
def markerBuilder(lat,lon,name,elevation):
    location = f'{lat} , {lon}' 
    html = f'<h4>{name}:</h4> <a href="https://www.google.com/search?q=volcanic {name}&tbm=isch" target="_blank">Google It!</a><br><br> Name: {name}<br>Elevation: {str(el)} meters <br>location: [{location}]'
    iframe = folium.IFrame(html,width=300,height=110)
    popup = folium.Popup(iframe, max_width=300)
   
    return folium.CircleMarker(location = [lat, lon] ,
                                 radius= 10,
                                 popup = popup,
                                 tooltip = f"Volcanic: {name}",
                                 fill= True,
                                 stroke = True,
                                 fill_color = color_picker(el),  
                                 color="grey",fill_opacity=0.7 )
    
    
 
# FeatureGroup groups
fg_v = folium.FeatureGroup(name="Volcanoes")
fg_pop = folium.FeatureGroup(name="Population")

for lat ,lon ,name ,el in zip(lats,lons,names,elves):
   
    marker = markerBuilder(lat= lat,lon= lon,name= name, elevation=el)
    
    fg_v.add_child(marker)

    # Add Population layer
    #fg_pop.add_child(folium.GeoJson(data=open('files/world.json','r', encoding= 'utf-8-sig').read()
    #                            ,style_function = lambda x: {'fillColor':'yellow' 
    #                                                         if x['properties']['POP2005'] < 10000000 
    #                                                         else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
    #                                                         else 'red'})) 
    # (x) here represents features in the json file
  
 
 
map = folium.Map(zoom_start=6,tiles="Stamen Terrain")
map.add_child(fg_v)
#map.add_child(fg_pop)
map.add_child(folium.LayerControl()) 
map.save("Map1.html")









