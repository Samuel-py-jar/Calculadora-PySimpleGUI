import PySimpleGUI as sg
def tema():
    sg.theme('DarkBlack1')
def main():

 menu = [['MENU', [ [['Tema',  ['branco','escuro'] ]], 'Info' , 'Sair'  ]  ]]
 dele=False
 n = ""
 tela=[
      [sg.Menu(menu)],
      [sg.Text("                                                                     ",size=(21,1),font=("Helvetica",14), background_color = "white",text_color = "black",key="_DISPLAY_")],
      [sg.Text("                                                          ",size=(16,1),font=("Helvetica",18),background_color = "white",text_color = "black",key="_DISPLAY2_")],
      [sg.Button("1",size=(4,2),font = ("Helvetica",15),key="num1"),
      sg.Button("2",size=(4,2),font = ("Helvetica",15),key="num2"),
      sg.Button("3",size=(4,2),font = ("Helvetica",15),key="num3"),
      sg.Button("=",size=(4,2),font = ("Helvetica",15),key="cal")],
      [sg.Button("4",size=(4,2),font = ("Helvetica",15),key="num4"),
      sg.Button("5",size=(4,2),font = ("Helvetica",15),key="num5"),
      sg.Button("6",size=(4,2),font = ("Helvetica",15),key="num6"),
      sg.Button("+",size=(4,2),font = ("Helvetica",15),key="mais")],
      [sg.Button("7",size=(4,2),font = ("Helvetica",15),key="num7"),
      sg.Button("8",size=(4,2),font = ("Helvetica",15),key="num8"),
      sg.Button("9",size=(4,2),font = ("Helvetica",15),key="num9"),
      sg.Button("-",size=(4,2),font = ("Helvetica",15),key="menos")],
      [sg.Button("del",size=(4,2),font = ("Helvetica",15),key="_del_"),
      sg.Button("0",size=(4,2),font = ("Helvetica",15),key="zero"),
      sg.Button("×",size=(4,2),font = ("Helvetica",15),key="mult"),
      sg.Button("÷",size=(4,2),font = ("Helvetica",15),key="_divi_")]
 ]
 
 window=sg.Window(title="Calculadora")
 form=window.Layout(tela).Finalize()
 
 while True:
   event,values=window.Read()               
   if event == 'num1':
       n += "1"
   if event == 'num2':
       n += "2"
   if event == 'num3':
   	n += "3"
   if event == 'num4':
       n += "4"
   if event == 'num5':
       n += "5"
   if event == 'num6':
   	n += "6"
   if event == 'num7':
   	n += "7"
   if event == 'num8':
       n += "8"
   if event == 'num9':
       n += "9"
   if event == 'zero':
   	n += "0"
   if event == '_divi_':
   	n += "/"
   	quanto=1
   if event == 'mult':
   	n += "X"
   	quanto=1
   if event == 'mais':
   	n += "+"
   	quanto=1
   if event == 'menos':
   	n += "-"
   	quanto=1
   if event == '_del_':
   	dele=True
   	n = ""
   if event == "branco":
       form.FindElement("mais").Update(button_color = ("Black","white"))
       form.FindElement("menos").Update(button_color = ("Black","white"))
       form.FindElement("_divi_").Update(button_color = ("Black","white"))
       form.FindElement("_del_").Update(button_color = ("Black","white"))
       form.FindElement("num4").Update(button_color = ("Black","white"))
       form.FindElement("num3").Update(button_color = ("Black","white"))
       form.FindElement("num2").Update(button_color = ("Black","white"))
       form.FindElement("num1").Update(button_color = ("Black","white"))
       form.FindElement("num8").Update(button_color = ("Black","white"))
       form.FindElement("num7").Update(button_color = ("Black","white"))
       form.FindElement("num6").Update(button_color = ("Black","white"))
       form.FindElement("num5").Update(button_color = ("Black","white"))
       form.FindElement("num9").Update(button_color = ("Black","white"))
       form.FindElement("zero").Update(button_color = ("Black","white"))
       form.FindElement("mult").Update(button_color = ("Black","white")) 
       form.FindElement("cal").Update(button_color = ("Black","white")) 
   if event == "escuro":
       form.FindElement("mais").Update(button_color = ("white","Black"))
       form.FindElement("menos").Update(button_color = ("white","Black"))
       form.FindElement("_divi_").Update(button_color = ("white","Black"))
       form.FindElement("_del_").Update(button_color = ("white","Black"))
       form.FindElement("num4").Update(button_color = ("white","Black"))
       form.FindElement("num3").Update(button_color = ("white","Black"))
       form.FindElement("num2").Update(button_color = ("white","Black"))
       form.FindElement("num1").Update(button_color = ("white","Black"))
       form.FindElement("num8").Update(button_color = ("white","Black"))
       form.FindElement("num7").Update(button_color = ("white","Black"))
       form.FindElement("num6").Update(button_color = ("white","Black"))
       form.FindElement("num5").Update(button_color = ("white","Black"))
       form.FindElement("num9").Update(button_color = ("white","Black"))
       form.FindElement("zero").Update(button_color = ("white","Black"))
       form.FindElement("mult").Update(button_color = ("white","Black"))
       form.FindElement("cal").Update(button_color = ("white","Black"))

   if event == "Info":
       sg.Popup("calculadora feita por Raís do código e galera do github[ninguém ainda]\ncriado por: Raís do Código\nversão: 0.1.0\nlicença: MIT\nCalculadora simples feita com o pacote PySimpleGUI e construído junto com contribuições [........]",title = "informações do desenvolvedor")
   
   if  event == "del":
                form.FindElement('_DISPLAY2_').Update(value="                                                                                      ")
                form.FindElement('_DISPLAY_').Update(value="                                                                                                      ") 
   form.FindElement('_DISPLAY_').Update(value=n)
   if event == 'cal':
        blz=True
        if n == "":
            sg.Popup("Ops,voce digitou errado!\nErro:Nada foi digitado!",title="ERRO")
            blz=False
            n=""
        opa = '+' in n
        opam = '-' in n
        opad = '/' in n
        opamu = 'X' in n
        if opa == True:
            local1 = n.find('+')
            opera="+"
        elif opam == True:
            local1 = n.find('-')
            opera="-"
        elif opad == True:
            local1 = n.find('/')
            opera="/"
        elif opamu == True:
            local1 = n.find('X')
            opera="X"
        local1=n.find(opera)
        local2 = local1 + 1
        lado1=n[:local1]
        lado2=n[local2:]    
        if blz == True:    
            lado1=float(lado1)
            lado2=float(lado2)
            ok = '+' in n
            okm = '-' in n
            okd = '/' in n
            okmm = 'X' in n
            if ok == True:
                resul = lado1 + lado2
             
            elif okm == True:
                resul = lado1 - lado2 
             
            elif okd == True:
                resul = lado1 / lado2 
               
            elif okmm == True:
                resul = lado1 * lado2
            n=""
            form.FindElement('_DISPLAY2_').Update(value=resul)  
            form.FindElement('_DISPLAY_').Update(value=resul)
            n=str(resul)             
   if event == sg.WIN_CLOSED or event == 'Sair':
        window.Close()
        break
main()	
