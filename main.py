import sqlite3

# Conectando ao banco de dados (cria se não existir)
conn = sqlite3.connect('biblioteca.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando a tabela 'livros'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT
    )
''')

# Confirmando as alterações
conn.commit()
conn.close()