import sqlite3, sys, os, printer # type: ignore


def connect_to_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        Printer.printc(f"Connected to database '{db_name}' successfully.", "Green")
        return conn
    except sqlite3.Error as e:
        Printer.printc(f"Error connecting to database: {e}", "Red")
        return None

def execute_sql_command(conn, command: str):
    try:
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()

        # If it's a SELECT query, fetch and display results
        if command.strip().lower().startswith("select"):
            results = cursor.fetchall()
            for row in results:
                Printer.printc(row)
        else:
            Printer.printc("Command executed successfully.", "Cyan")
    except sqlite3.Error as e:
        Printer.printc(f"An error occurred: {e}", "Red")

def show_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if tables:
            Printer.printc("Tables in the database:", "Yellow")
            for table in tables:
                Printer.printc(table[0])
        else:
            Printer.printc("No tables found in the database.", "Red")
    except sqlite3.Error as e:
        Printer.printc(f"An error occurred: {e}", "Red")

def show_table_info(conn, table_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        if columns:
            Printer.printc(f"Table structure for '{table_name}':", "Yellow")
            Printer.printc("cid | name | type | notnull | dflt_value | pk", "Blue")
            for column in columns:
                Printer.printc(column)
        else:
            Printer.printc(f"No information found for table '{table_name}'.", "Red")
    except sqlite3.Error as e:
        Printer.printc(f"An error occurred: {e}", "Red")

def help():
    Printer.printc("Hello, happy to see you using this bs code", "White")
    Printer.printc("If you need help feel free to see homepage of this project: https://github.com/news-s/db_console", "White")
    Printer.printc("Or dm me on Discord: news.exe")
    Printer.printc("    exit                  - just what it says, exits program. Easier than in vim.", "White")
    Printer.printc("    show tables           - shows all tables in the database.", "White")
    Printer.printc("    describe <table_name> - prints everything about all cilumns in the table.", "White")
    Printer.printc("Everything else is like in normal sqlite3.", "White")

def find_file(name: str) -> bool:
    for f in os.listdir():
        if f == name: return True
    return False

def run_commands(command: str, conn, table_name: str):
    try:
        comm = command.lower().split()[0]
    except IndexError:
        Printer.printc("Please provide a command", "Red")
        return 1
    

    match comm:
        case 'exit':        return 0
        case 'help':        help()
        case 'prev':        run_commands(globals()['prev'], conn, table_name)
        case 'show':        show_tables(conn)
        case 'describe':    show_table_info(conn, table_name)
        case _:             execute_sql_command(conn, command)
    globals()['prev'] = command
            

def main(db_name: str) -> None:
    conn = connect_to_database(db_name)
    globals()['prev'] = ""
    if conn:
        while True:
            command = Printer.inputc(">>", "Green")
            if len(command.split()) == 0:
                name = command.split()[1]
            else: name = None
            if run_commands(command, conn, name) == 0:
                break

        conn.close()
        Printer.printc("Connection closed.", "Red")

def start() -> None:
    db_name = Printer.inputc("Enter the name of the sqlite3 database file: ")
    db_name = db_name + ".sqlite3"
    if find_file(db_name):
        Printer.printc("Connecting to database")
        main(db_name)
    else:
        response = Printer.inputc(f"No file with name '{db_name}'. Do you want to create new? y/n: ", "Cyan")
        if response.lower() == 'y':
            main(db_name)
        elif response.lower() == 'n':
            Printer.printc("oki")
            return 0
        else:
            Printer.printc("huh? lets try again")
            start()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "colors":
            Printer = printer.Printer(True)
        else:
            Printer = printer.Printer(False)
    else:
        Printer = printer.Printer(False)
    Printer.printc("Welcome", "Red")
    start()