import sqlite3
import bcrypt
from contextlib import closing


def criar_hash_senha(senha: str) -> str:
    """Retorna o hash bcrypt de uma senha (usado ao cadastrar usuário)."""
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verificar_senha(senha_plain: str, hash_stored: str) -> bool:
    """Compara uma senha em texto puro com um hash bcrypt armazenado."""
    return bcrypt.checkpw(senha_plain.encode('utf-8'), hash_stored.encode('utf-8'))


def migrar_senhas_para_hash() -> int:
    """Atualiza senhas em texto puro para hash bcrypt na base de dados.

    Retorna a quantidade de registros atualizados.
    """
    atualizados = 0
    with closing(sqlite3.connect('banco_de_dados.db')) as conexao:
        cursor = conexao.cursor()
        # Só considera já hash se começar com o prefixo $2 (bcrypt).
        cursor.execute("SELECT id, username, password FROM usuarios")
        for _id, usuario, senha in cursor.fetchall():
            if senha and senha.startswith('$2'):
                continue  # já está hasheado
            try:
                hash_novo = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                cursor.execute("UPDATE usuarios SET password = ? WHERE id = ?", (hash_novo, _id))
                atualizados += 1
            except Exception:
                # Senha em branco ou inválida: ignora, evita parar o processo.
                continue
        conexao.commit()
    return atualizados


def fazer_login(usuario: str, senha: str) -> str:
    """Autentica um usuário com consulta parametrizada e hash bcrypt."""
    # Migra senhas em texto puro para hash bcrypt antes de autenticar,
    # garantindo que a base de dados esteja sempre em estado seguro.
    migrar_senhas_para_hash()

    with closing(sqlite3.connect('banco_de_dados.db')) as conexao:
        cursor = conexao.cursor()
        # Busca apenas o hash pelo nome de usuário (nunca a senha na query).
        query = "SELECT password FROM usuarios WHERE username = ?"
        cursor.execute(query, (usuario,))
        linha = cursor.fetchone()

        if linha and verificar_senha(senha, linha[0]):
            return "Login bem-sucedido!"
        return "Acesso negado."
    