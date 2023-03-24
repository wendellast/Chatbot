



def datahoje():
    from datetime import date
    dataatual =  date.today()
    diassemana = ('Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo')
    meses = ('Zero','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    resposta(f"Hoje é {diassemana[dataatual.weekday()]}")
    diatexto = f'{dataatual.day} de '
    mesatual = (meses[dataatual.month])
    datatexto = dataatual.strftime(" de %Y")
    resposta(f'Dia {diatexto} {mesatual} {datatexto}')

def bateria(): # No momento funcionameto em notebook
    try:
        bateria = psutil.sensors_battery()
        carga = bateria.percent
        bp = str(bateria.percent)
        bpint = "{:.0f}".format(float(bp))
        resposta("A bateria está em:" +bpint +'%')
        if carga <= 20:
            resposta('Ela está em nivel crítico')
            resposta('Por favor, coloque o carregador')
        elif carga == 100:
            resposta('Ela está totalmente carregada')
            resposta('Retire o carregador da tomada')
    except:
        resposta('Desculpa')
        resposta('Seu dispositivo atual não está usando bateria')
        resposta('Por isso é impossivel informar a quantidade de carga')

def cpu ():
    usocpuinfo = str(psutil.cpu_percent())
    usodacpu  = "{:.0f}".format(float(usocpuinfo))
    resposta('O uso do processador está em ' +usodacpu +'%')
    
def temperaturadacpu():
    tempcpu = psutil.sensors_temperatures()
    cputemp = tempcpu['coretemp'][0]
    temperaturacpu = cputemp.current
    cputempint = "{:.0f}".format(float(temperaturacpu))
    if temperaturacpu >= 20 and temperaturacpu < 40:
        resposta('Estamos trabalhado em um nível agradavel')
        resposta('A temperatura está em ' +cputempint +'°')

    elif temperaturacpu >= 40 and temperaturacpu < 58:
        resposta('Estamos operando em nivel rasoável')
        resposta('A temperatura é de ' +cputempint +'°')

    elif temperaturacpu >= 58 and temperaturacpu < 70:
        resposta('A temperatura da CPU está meio alta')
        resposta('Algum processo do sistema está causando aquecimento')
        resposta('Fique de olho')
        resposta('A temperatura está em ' +cputempint +'°')

    elif temperaturacpu >= 70 and temperaturacpu != 80:
        resposta('Atenção')
        resposta('Temperatura de ' +cputempint +'°')
        resposta('Estamos em nivel crítico')
        resposta('Desligue o sistema imediatamente')

# função de boas vindas, fases do dia
def BoasVindas():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        resposta('Bom dia')

    elif Horario >= 12 and Horario < 18:
        resposta('Boa tarde')

    elif Horario >= 18 and Horario != 0:
        resposta('Boa noite')
	
def tempo(): 
    try:
        #Procure no google maps as cordenadas da sua cidade e coloque no "lat" e no "lon"(Latitude,Longitude)
        api_url = "https://fcc-weather-api.glitch.me/api/current?lat=14º 13 30&lon=42º 46 53"
        data = requests.get(api_url)
        data_json = data.json()
        if data_json['cod'] == 200:
            main = data_json['main']
            wind = data_json['wind']
            weather_desc = data_json['weather'][0]
            temperatura =  str(main['temp'])
            tempint = "{:.0f}".format(float(temperatura))
            vento = str(wind['speed'])
            ventoint = "{:.0f}".format(float(vento))
            dicionario = {
                'Rain' : 'chuvoso',
                'Clouds' : 'nublado',
                'Thunderstorm' : 'com trovoadas',
                'Drizzle' : 'com garoa',
                'Snow' : 'com possibilidade de neve',
                'Mist' : 'com névoa',
                'Smoke' : 'com muita fumaça',
                'Haze' : 'com neblina',
                'Dust' : 'com muita poeira',
                'Fog' : 'com névoa',
                'Sand' : 'com areia',
                'Ash' : 'com cinza vulcanica no ar',
                'Squall' : 'com rajadas de vento',
                'Tornado' : 'com possibilidade de tornado',
                'Clear' : 'com céu limpo'
                }
            tipoclima =  weather_desc['main']
            if data_json['name'] == "Shuzenji":
                resposta('Erro')
                resposta('Não foi possivel verificar o clima')
                resposta('Tente novamente o comando')
            else:
                resposta(f'Verificando clima para a cidade de {data_json["name"]}')
                resposta(f'O clima hoje está {dicionario[tipoclima]}')
                resposta(f'A temperatura é de {tempint}°')
                resposta(f'O vento está em {ventoint} kilometros por hora')
                resposta(f'E a umidade é de {str(main["humidity"])}%')
    
    except: 
        resposta('Não foi possível realizar essa tarefa')
        resposta('Erro na conexão')

def AteMais():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        resposta('Tenha um ótimo dia')

    elif Horario >= 12 and Horario < 18:
        resposta('Tenha uma ótima tarde')

    elif Horario >= 18 and Horario != 0:
        resposta('Boa noite')


   
def localizacao():
	try:
		EndereçoIP = get('https://api.ipify.org').text
		url = 'https://get.geojs.io/v1/ip/geo/'+EndereçoIP+'.json'
		geo_reqeust = get(url)
		geo_data = geo_reqeust.json()
		city = geo_data['city']
		resposta('Sua localização é '+str(city))
	except:
		resposta('Falha ao verificar a localização')