import sqlite3


conn = sqlite3.connect('torchbotdb.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_row_create(user_id: int, count: int):
    cursor.execute(
        'INSERT INTO users (user_id, count) VALUES (?,?)',
        (user_id, count)
    )
    conn.commit()


def db_table_read_user_choice(user_id):
    sql_select_query = """SELECT user_choice FROM users WHERE user_id = ?"""
    cursor.execute(sql_select_query, (user_id,))
    records = cursor.fetchone()
    return records


def db_table_wright_user_choice(user_choice, user_id):
    cursor.execute("UPDATE users SET user_choice = ? WHERE user_id = ?", (user_choice, user_id))
    conn.commit()


def db_table_wright_user_type(user_type, user_id):
    cursor.execute("UPDATE users SET user_type = ? WHERE user_id = ?", (user_type, user_id))
    conn.commit()


def db_table_read_user_type(user_id):
    sql_select_query = """SELECT user_type FROM users WHERE user_id = ?"""
    cursor.execute(sql_select_query, (user_id,))
    records = cursor.fetchone()
    return records


def db_table_read_user_contact(user_id):
    sql_select_query = """SELECT user_contact FROM users WHERE user_id = ?"""
    cursor.execute(sql_select_query, (user_id,))
    records = cursor.fetchone()
    return records


def db_table_wright_user_contact(user_contact, user_id):
    cursor.execute("UPDATE users SET user_contact = ? WHERE user_id = ?", (user_contact, user_id))
    conn.commit()


def db_table_read_count(user_id):
    sql_select_query = """SELECT count FROM users WHERE user_id = ?"""
    cursor.execute(sql_select_query, (user_id,))
    records = cursor.fetchone()
    return records


def db_table_wright_count(count, user_id):
    cursor.execute("UPDATE users SET count = ? WHERE user_id = ?", (count, user_id))
    conn.commit()


def delet_row(user_id):
    cursor.execute("DELETE FROM users  WHERE  user_id = ?", (user_id,))
    conn.commit()
