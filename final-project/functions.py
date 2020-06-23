import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from flask import redirect, render_template, request, session
import pygal

#Error message
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("error.html", top=code, bottom=escape(message)), code


##Url del dataset base
def concat(month,day):
    first = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/'
    rule =  '2020-0'+str(month)+'-01'
    end = '-CasosConfirmados-totalRegional.csv'
    data = pd.read_csv(first+rule+end, encoding='utf8')
    data['fecha'] = str(month)+'/1/2020'
    data.drop(data.index[-1], inplace=True)
    for i  in range(2,day+1):
        if i <10:
            date = '2020-0'+str(month)+'-0'+str(i)
        if 10<= i <=day:   
            date = '2020-0'+str(month)+'-'+str(i)
        filename = first+date+end
        temp_data = pd.read_csv(filename, encoding='utf8')
        temp_data['fecha'] = str(month) +'/'+str(i) +'/2020'
        temp_data.columns = data.columns
        temp_data.drop(temp_data.index[-1], inplace=True)
        data = pd.concat([data,temp_data])
        data = data.reset_index(drop=True)
        data['Region'] = data['Region'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        data['Region'] = data['Region'].str.replace("  "," ")
        data.columns = data.columns.str.replace('  ', ' ')
    return data

def grouped(data):
    grouped_data = data.groupby(['Region','fecha']).sum().sort_values(data.columns[1])
    return grouped_data

def by_region(data,region):
    data = data.loc[region]
    return data

def maxday(data):
    return data.iloc[:,1:5].idxmax()

def plot_new(data):
    graph = pygal.Line(legend_box_size=5,legend_at_bottom=True)
    graph.x_labels = list(data.fecha.values)
    graph.add(data.columns[2], data['Casos nuevos totales'].astype('int').tolist())
    graph.add(data.columns[1], data['Casos nuevos con sintomas'].astype('int').tolist())
    graph.add(data.columns[2], data['Casos nuevos sin sintomas*'].astype('int').tolist())
    graph.add(data.columns[1], data['Fallecidos'].astype('int').tolist())
    graph = graph.render_data_uri()
    return graph

def plot_total(data):
    graph = pygal.Line(legend_box_size=5,legend_at_bottom=True)
    graph.x_labels = list(data.fecha.values)
    graph.add(data.columns[1], data['Casos totales acumulados'].astype('int').tolist())
    graph = graph.render_data_uri()
    return graph


