import sqlite3


def adicionar_livro(titulo, autor):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor) VALUES (?, ?)", (titulo, autor))
    conn.commit()
    conn.close()


def buscar_livro(titulo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    resultados = cursor.fetchall()
    conn.close()
    return resultados


# Exemplo de uso:
adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
adicionar_livro("Dom Quixote", "Miguel de Cervantes")

livros = listar_livros()
for livro in livros:
    print(livro)

resultado = buscar_livro("Quixote")
print(resultado)
