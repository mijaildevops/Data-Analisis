import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import seaborn as sns; sns.set(color_codes=True)
from seaborn import kdeplot
import matplotlib.pyplot as plt

# carga DataFrame
df = pd.read_csv("CSV-JoeBin.csv")

# Nuevo data frame solo con dos columnas
DataAnalis = df[["usertweet", "TweetMsg"]]
print (DataAnalis.head(10))
print ('')

# Remover index si contine el Texto
# utilizamos or (|)
df3 = DataAnalis.drop(
    DataAnalis[DataAnalis['TweetMsg'].str.contains('@ONU_es @free_equal @ONU_derechos')].index | 
    DataAnalis[DataAnalis['TweetMsg'].str.contains('@BarcelonaSC')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('LigaPro')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('Alineación confirmada')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('¡Nuestra armadura de hoy!')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('¡Hoy juega el Ídolo!')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('PRÓXIMO PARTIDO')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('LDU_Oficial')].index |
    DataAnalis[DataAnalis['TweetMsg'].str.contains('Escoge el diseño que más te guste')].index
    
    )
print(df3.head(10))

print('Total de elemetos Data-Frame(df)', len(df))
print('Total de elemetos Data-Frame(df)', len(df3))

#Eliminar caracteres especiales y urls
df4 = df3.TweetMsg.str.replace('http\S+',"").str.replace('@',"").str.replace('?',"").str.replace('!',"").str.replace('(',"").str.replace(')',"").str.replace('#',"").str.replace(':',"").str.replace('¡',"").str.replace('.',"").str.replace(',',"").str.replace('/',"").str.replace('-',"").str.replace('_',"").str.replace('+',"").str.replace('“',"").str.replace('"',"").str.replace("'","").str.replace("|","")
print (df4.head(10))
print ('')

# Variables Globales 
msg = 1
item = []
tweet = []
NPLpolarity = []

# variables Sentimiento
Neutro=0
Positivo=0
Malo=0

# recorrer cada elemento del data frame
for ind in df4.index: 
    print (msg)
    try:
        print(df4[ind]) 
        t=TextBlob(df4[ind])
        #ten=t.translate(to="en")
        #print (ten)
        polarity= t.polarity
        print (polarity)
        #input()
    except:
        print("Error")
        polarity= "Error"
    
    # agregar resultados a Lista de objetos
    tweet.append(df4[ind])
    NPLpolarity.append(t.polarity)
    item.append(msg)

    # Agrupar Polaridad del mensaje analizado
    if (t.polarity == 0):
        Neutro += 1

    if (t.polarity > 0 ):
        Positivo += 1

    if (t.polarity < 0 and t.polarity < 1):
        Malo += 1
       
    msg += 1
     
# Nuevo Data-Frame con la Polaridad Incluida
dfresultado = pd.DataFrame({'tweet': item, 'msg': tweet, 'NPLpolarity': NPLpolarity})
print(dfresultado.head(10))


# Graficar lmplot
g=sns.lmplot(x='tweet', y='NPLpolarity', data=dfresultado.head(150), line_kws={'color': 'red'})
plt.savefig('data-lmplot.png', dpi=300)
plt.show()

# Graficar Pie chart
sizes = [Neutro,Malo, Positivo]
labels = ['Neutro','Malo', 'Positivo']
cols = ['c','b','r']
explode=(0,0.1,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Analisis de Sentimientos')
plt.savefig('data-Pie.png', dpi=300)
plt.show()

# Save new data Frame
dfresultado.to_csv('CSV-Resultado.csv')
