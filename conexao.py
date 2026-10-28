import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'  
DB_HOST = 'localhost'
DB_NAME = 'teste_db'  
DB_PORT = 5432        
def criar_conexao_postgres():
    conexao = None
    try:
        conexao = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão bem-sucedida!")
        return conexao

    except OperationalError as e:
        print(f"Erro ao tentar conectar ao postgres: '{e}'")
        print("Verifique se o servidor PostgreSQL está ativo e se as credenciais estão corretas")
        return None

if __name__ == '__main__':
    print("Tentando estabelecer a conexão...")
    conexao_ativa = criar_conexao_postgres()
    
    if conexao_ativa:
        print(f"Status da conexão: {conexao_ativa.status}")
        print("Conexão ok. Bem-sucedida!")

        conexao_ativa.close()
        print("Conexão fechada.")
    else:
        print("Falha na conexão.")