import sqlite3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

#configuração do banco de dados - 
db_path = os.path.abspath("info.db")
cursor = conn.cursor()

# Criar tabela de vagas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vagas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    localizacao TEXT,
    requisitos TEXT,
    link TEXT UNIQUE,
    data_postagem DATE DEFAULT CURRENT_DATE
)
""")

# Criar tabela de informações da empresa
cursor.execute("""
CREATE TABLE IF NOT EXISTS informacoes_empresa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sobre TEXT NOT NULL,
    localizacao TEXT,
    site TEXT,
    contato TEXT,
    cultura_trabalho TEXT
)
""")

# Criar tabela de perguntas frequentes
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL
)
""")

# Inserir informações iniciais
cursor.execute("""
INSERT OR IGNORE INTO informacoes_empresa 
(id, sobre, localizacao, site, contato, cultura_trabalho) 
VALUES (1, 'Empresa líder no setor de TI', 'São Paulo', 'www.empresa.com.br', 'contato@empresa.com', 'Ambiente colaborativo, foco em inovação')
""")

faq_data = [
    ("Qual a cultura da empresa?", "Nossa cultura é baseada na inovação, colaboração e crescimento."),
    ("Quantas vagas estão abertas?", "Atualmente, temos X vagas disponíveis. Acesse [link] para ver todas."),
    ("A empresa oferece benefícios?", "Sim, oferecemos VR, VA e plano de saúde para funcionários CLT."),
    ("Aceita trabalho remoto?", "Algumas vagas são 100% remotas. Verifique as descrições das vagas."),
    ("Onde fica a sede da empresa?", "Nossa sede está localizada em São Paulo.")
]

cursor.executemany("INSERT OR IGNORE INTO faq (pergunta, resposta) VALUES (?, ?)", faq_data)

# Salvar e fechar conexão
conn.commit()
conn.close()