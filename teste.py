from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Seminovos:
    def __init__(self):
        self.SITE_LINK = "https://www.bariguiseminovos.com.br"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def abrir_seminovos(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(5)  # Espera 5 segundos para garantir que a página esteja totalmente carregada

    def digitar_carro(self, texto):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="t-buscar"]')
        input_field.clear()
        input_field.send_keys(texto)
        input_field.send_keys(Keys.ENTER)

    def selecionar_loja(self):
        loja_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/form/ul/li[7]')))
        loja_button.click()
        time.sleep(2)
        loja_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/form/ul/li[7]/ul/li[2]/span[8]/label/a/div')))
        loja_option.click()

    def selecionar_primeiro_carro(self):
        primeiro_carro = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/section/div[2]/div[1]/a[1]/div[2]/div[1]')))
        primeiro_carro.click()
        self.rolar_para_baixo()

    def rolar_para_baixo(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def gerar_campoUm(self, nome):
        self.driver.execute_script("window.scrollBy(0, 500);")
        type_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form_nome_proposta"]')))
        type_name.send_keys(nome)

    def gerar_campoDois(self, fone):
        type_telefone = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form_telefone_proposta"]')))
        type_telefone.send_keys(fone)

    def gerar_campoTres(self, mail):
        type_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form_email_proposta"]')))
        type_email.send_keys(mail)

    def selecionar_enviarlead(self):
        enviar_lead = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-send-form-fale-consultor"]')))
        enviar_lead.click()

site = Seminovos()
site.abrir_seminovos()
site.digitar_carro("HB20")
site.selecionar_loja()
site.selecionar_primeiro_carro()
site.gerar_campoUm("Bot teste")
site.gerar_campoDois("99999999999")
site.gerar_campoTres("bot.teste@teste.com.br")
site.selecionar_enviarlead()