import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

usuario = str(input("MEU USUARIO: "))
senha = str(input("MINHA SENHA: "))
perfil = str(input("PERFIL: "))


#abrir a pagina do instagram no chrome
url_insta = "https://www.instagram.com"


option = Options()
option.add_argument('--window-size=1920,1080') 
option.add_argument('--start-maximized') 
#option.add_argument('--headless')
    
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)


# ver ou nao o chrome abrindo

pagina = driver.get(url_insta) #abre a pagina

# esperar o conteudo da pagina carregar
time.sleep(10)
# processo de entrar pelo facebook com minhas credenciais
click_enter_by_facebook = driver.find_element_by_xpath('//html//body//div[1]//section//main//article//div[2]//div[1]//div//form//div[1]//div[5]//button').click()



time.sleep(3)

fill_username = driver.find_element_by_xpath('//html//body//div[1]//div[3]//div[1]//div//div//div[2]//div[1]//form//div//div[1]//input').send_keys(usuario + Keys.TAB)

time.sleep(2)

fill_password = driver.find_element_by_xpath('//html//body//div[1]//div[3]//div[1]//div//div//div[2]//div[1]//form//div//div[2]//input').send_keys(senha + Keys.ENTER)

time.sleep(10)

#desativar notificoes ao entrar no instagram
no_notifications = driver.find_element_by_xpath('//html//body//div[4]//div//div//div//div[3]//button[2]').click()


#pesquisar perfil que eu quiser
search_user = driver.find_element_by_xpath('//html//body//div[1]//section//nav//div[2]//div//div//div[2]//input').send_keys(perfil)

time.sleep(3)

#clicar no primeiro perfil achado
search_user = driver.find_element_by_xpath('//html//body//div[1]//section//nav//div[2]//div//div//div[2]//div[4]//div//a[1]').click()

#extrair numero de seguidores
time.sleep(10)
numero_seguidores = driver.find_element_by_xpath('//html//body//div[1]//section//main//div//header//section//ul//li[2]//a//span').text
print(numero_seguidores)


time.sleep(5)


