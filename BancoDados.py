import sqlite3

conn = sqlite3.connect('DadosUsuarios.bd')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS  Usuarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cidade TEXT NOT NULL
);
''')

print('Conectado ao banco de dados')