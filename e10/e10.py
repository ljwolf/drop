"""
e10, choropleth mapping
levi john wolf
levi.john.wolf@gmail.com
"""
import folium
import random
import pandas as pd
import pysal as ps
import numpy as np
import json

def jsonmap(jsondata = 'e09.json', classification=None):
    f = open(str(jsondata), 'r')
    q = json.load(f)
    f.close()
    features = q['features']
    indices = []
    values = []
    for feature in features:
        indices.append(str(feature['properties']['UID']))
        values.append(feature['properties']['pct'])
    for i in range(len(values)):
        if values[i] != None:
            values[i] = float(format(values[i], ".2f"))
    df = pd.DataFrame({'pct': values, 'UID': indices})
    y = np.array(df.pct.tolist())
    tmap = folium.Map(location=[40,-100], zoom_start=4)
    if classification == 'fj':
        fisherjenks = ps.Fisher_Jenks(y, 5).bins
        tscale = fisherjenks[:-1]
        cname = 'Fisher Jenks'
    elif classification == 'ei':
        eqinterval = ps.Equal_Interval(y, 5).bins.tolist()
        tscale = eqinterval[:-1]
        cname = 'Equal Interval'
    elif classification == 'mb':
        maxbreaks = ps.Maximum_Breaks(y, 5).bins.tolist()
        tscale = maxbreaks[:-1]
        cname = 'Maximum Breaks'
    elif classification == 'q':
        quantiles = ps.Quantiles(y, 5).bins.tolist()
        tscale = quantiles[:-1]
        cname = 'Quantiles'
    
    if classification == None:
        tmap.geo_json(geo_path = 'e09.json', key_on = 'feature.properties.UID', data_out = 'data.json', data=df, columns = ['UID', 'pct'], fill_color='GnBu', fill_opacity=0.7, line_opacity=.2, legend_name='Percentage of Vote Defections (Folium)')
        tmap.create_map('e10_folium.html')
    else:
        tmap.geo_json(geo_path = 'e09.json', key_on = 'feature.properties.UID', data_out = 'data.json', data=df, columns = ['UID', 'pct'], fill_color='GnBu', fill_opacity=0.7, line_opacity=.2, threshold_scale=tscale, legend_name='Percentage of Vote Defections ('+cname+')')
        tmap.create_map('e10_'+cname+'.html')

if __name__ == '__main__':
    classlist = ['fj', 'ei', 'mb', 'q']
    print 'Generating maps. Please wait.'
    map(lambda x: jsonmap(classification=x),classlist)
    jsonmap()
