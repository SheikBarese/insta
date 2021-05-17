import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



#abrir a pagina do instagram no chrome
url_insta = "https://www.instagram.com"


option = Options()
option.add_argument('--window-size=1920,1080') 
option.add_argument('--start-maximized') 
#option.add_argument('--headless') nao funciona 
    

# esperar o conteudo da pagina carregar
time.sleep(10)
# processo de entrar pelo facebook com minhas credenciais



def open_chrome():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.get(url_insta)

def notifications_search():
    driver.find_element_by_xpath('//html//body//div[4]//div//div//div//div[3]//button[2]').click()


    #pesquisar perfil que eu quiser
    driver.find_element_by_xpath('//html//body//div[1]//section//nav//div[2]//div//div//div[2]//input').send_keys(perfil)

    time.sleep(3)

    #clicar no primeiro perfil achado
    driver.find_element_by_xpath('//html//body//div[1]//section//nav//div[2]//div//div//div[2]//div[3]//div//div[2]//div//div//a//div').click()

    #extrair numero de seguidores
    time.sleep(10)
    seguidores = driver.find_element_by_xpath('//html//body//div[1]//section//main//div//header//section//ul//li[2]//a//span').text
    print(f'O número de seguidores de {perfil} é {seguidores}.')

    time.sleep(10)
    driver.quit()

def enter_by_facebook():
    open_chrome()
    time.sleep(6)
    driver.find_element_by_xpath('//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[1]//div[5]//button').click()
                                
    time.sleep(3)

    driver.find_element_by_xpath('//html//body//div[1]//div[3]//div[1]//div//div//div[2]//div[1]//form//div//div[1]//input').send_keys(usuario + Keys.TAB)

    time.sleep(2)

    driver.find_element_by_xpath('//html//body//div[1]//div[3]//div[1]//div//div//div[2]//div[1]//form//div//div[2]//input').send_keys(senha + Keys.ENTER)

    time.sleep(10)
    notifications_search()
    #desativar notificoes ao entrar no instagram




def enter_by_instagram():
    open_chrome()
    time.sleep(8)
    driver.find_element_by_xpath('//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div//div[1]//div//label//input').click().send_keys(usuario + Keys.TAB)
    driver.find_element_by_xpath('//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div//div[2]//div//label//input').send_keys(senha + Keys.ENTER)
    time.sleep(5)
    notifications_search()

def pedir_credenciais():
    global usuario, senha, perfil
    usuario = str(input(f"usuário/email do {metodo}: "))
    senha = str(input(f"senha do {metodo}: "))
    perfil = str(input("perfil : "))
    

def menu():
    print('+---------------------------+')
    print("1.Entrar pelo facebook")
    print("2.Entrar pelo instagram.")
    print("+---------------------------+")
    selection = int(input("Escolha uma opção: "))
    if selection == 1:
        global metodo
        metodo = 'facebook'
        pedir_credenciais()
        enter_by_facebook()
    elif selection == 2:
        metodo = 'instagram'
        pedir_credenciais()
        enter_by_instagram()
    else:
        menu()

menu()
