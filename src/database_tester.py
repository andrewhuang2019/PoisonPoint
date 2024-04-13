from database_helper import DatabaseHelper

def test_basic_db_commands():
    db = DatabaseHelper()
    db.reset_dbs()
    db.initialize_dbs()
    db.add_to_reports("cfa_hq_id", 1234098493, "[True,False,True,False,False,False]", "Chick Fil A")
    db.add_to_reports("wendys_hq_id", 1235982063, "[False,False,False,False,True,False]", "Wendys")
    db.print_reports()
    db.reset_dbs()

def main():
    pass
    test_basic_db_commands()

if __name__ == "__main__":
    main()