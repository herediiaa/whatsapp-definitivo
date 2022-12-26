import pyautogui,time,sys #librerias

def leerParametro():
    #declaracion de variables globales
    global numerosTelefono #almacenamiento del numero de telefono
    global contenido
    parametro = sys.argv[1] # identifica el nombre del parametro
    path = "C:/Users/hered/OneDrive/Desktop/"+ parametro  #ESTA RUTA HAY QUE CONFIGURAR
    archivo=open(path,encoding='utf-8')#abre el parametro con su ruta completa(se puede cambiar) 
      
    contenido = archivo.read() #leemos el contenido del parametro.txt
    lista = contenido.split("\n")#hacemos una lista con todo lo que leyo del parametro.txt
    numerosTelefono = lista[0]#el primer item sera el numero de telefono
    archivo.close()#cerramos el archivo
def abrirWhatsapp():
    ubicacionLogoWhastapp = pyautogui.locateCenterOnScreen("media/logo.png") #busca el logo de la aplicacion en la pantalla
    pyautogui.leftClick(ubicacionLogoWhastapp) #clickea
def buscarContacto():
  
    #RECONOCIMIENTO DE LA BARRA DE BUSQUEDA
    
    #cuando entramos a la aplicacion la barra de busqueda tiene un fondo negro,
    #pero si clickeamos un fondo gris, por eso "reconocimiento de como esta la barra de busqueda"
    
    lupaNegra = pyautogui.locateOnScreen("media/lupaNegra.png") #foto del primer estado de la barra
    lupaGris = pyautogui.locateOnScreen("media/lupaGris.png")#foto del segundo
    
    #trato de sacar las coordenadas del primer estado
    try:
        x,y = pyautogui.center(lupaNegra) 
    except: 
        print("")
    #trato de sacar coordenadas del segundo estado
    try:
        a,b = pyautogui.center(lupaGris) 
    except:
        print("")
   
   #como no se cual de los dos estados existe. intento ir a los dos, sabiendo que solo va a ir uno.
   
    #lupa gris
    try: 
        A=int(a)
        B=int(b)
        pyautogui.leftClick(A,B) #me dirijo a la lupa gris
    except:
        print("")
  
    #lupa negra
    try:
        X= int(x)
        Y=int(y)
        pyautogui.leftClick(X,Y) #me dirijo a la lupa negra
    except:
        print("")
    
    
    #ESCRIBIR CONTACTO
def mandarMensaje():
    for number in numerosTelefono:
        pyautogui.typewrite(number,interval=0.25) #escribir el numero
        time.sleep(3.5) #esperar que lo encuentre
        pyautogui.press("Tab") #lo selecciono
        time.sleep(1)
        pyautogui.hotkey("enter")#entro al contacto
        time.sleep(2)#espero que cargue el chat

        with pyautogui.hold('ctrl'):
            time.sleep(0.5)
            pyautogui.press(['v']) 
        time.sleep(1)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(2)
        lupaGris = pyautogui.locateOnScreen("media/lupaGris.png")#foto del segundo
        time.sleep(0.5)
        o,p = pyautogui.center(lupaGris)
        O=int(o)
        P=int(p)
        time.sleep(0.5)
        pyautogui.leftClick(O,P) #me dirijo a la lupa gris
            
  
    
def whatappBot():
    leerParametro()
    abrirWhatsapp()
    time.sleep(1.5)#espero un segundo y medio
    buscarContacto()
    time.sleep(1)#espero un segundo
    mandarMensaje()
        
whatappBot()
