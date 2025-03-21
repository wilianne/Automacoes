import pdfplumber
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Função para extrair texto do PDF
def extrair_texto_pdf(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ''
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto

# Função para comparar valores
def comparar_valores(texto_pdf, df):
    # Supondo que o nome esteja na primeira linha do texto extraído
    linhas = texto_pdf.split('\n')
    nome = linhas[0].strip()
    valor_pdf = float(linhas[1].strip())
    
    # Localizar o nome na planilha
    linha = df[df['Nome'] == nome]
    
    if not linha.empty:
        # Comparar valores
        valor_excel = float(linha['Valor'].values[0])
        
        if valor_pdf == valor_excel:
            return True, nome, valor_pdf, valor_excel
        else:
            return False, nome, valor_pdf, valor_excel
    else:
        return False, nome, valor_pdf, None

# Função para preencher os dados no navegador
def preencher_no_navegador(nome, valor):
    # Configurar o WebDriver (no exemplo, usamos o Chrome)
    driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver está no PATH
    driver.get(r'C:\Users\willi\OneDrive\Desktop\projeto\teste.html')  # Substitua pelo URL do seu formulário

    # Aguardar o carregamento da página
    time.sleep(2)

    # Preencher os campos (ajuste os seletores conforme o seu formulário)
    campo_nome = driver.find_element(By.NAME, 'nome')  # Substitua 'nome' pelo nome do campo
    campo_valor = driver.find_element(By.NAME, 'email')  # Substitua 'valor' pelo nome do campo

    campo_nome.send_keys(nome)
    campo_valor.send_keys(str(valor))

    # Submeter o formulário (se necessário)
    campo_valor.send_keys(Keys.RETURN)

    # Fechar o navegador após alguns segundos (opcional)
    time.sleep(5)
    driver.quit()

# Carregar a planilha do Excel
df = pd.read_excel('dados.xlsx')

# Lista de PDFs para conferir
pdfs = ['documento1.pdf', 'documento2.pdf', 'documento3.pdf']

# Conferir cada PDF
for pdf in pdfs:
    texto_pdf = extrair_texto_pdf(pdf)
    resultado, nome, valor_pdf, valor_excel = comparar_valores(texto_pdf, df)
    
    if resultado:
        print(f"PDF: {pdf} - Valores batem! PDF: {valor_pdf}, Excel: {valor_excel}")
        # Preencher os dados no navegador
        preencher_no_navegador(nome, valor_pdf)
    else:
        if valor_excel is not None:
            print(f"PDF: {pdf} - Valores não batem. PDF: {valor_pdf}, Excel: {valor_excel}")
        else:
            print(f"PDF: {pdf} - Nome não encontrado na planilha.")