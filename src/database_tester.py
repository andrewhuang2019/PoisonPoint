from database_helper import DatabaseHelper

def test_basic_db_commands():
    db = DatabaseHelper()
    db.delete_dbs()
    db.initialize_dbs()
    db.add_to_restaurants("cfa_hq_id", "evil_cfa_hq_room", "round_burger,chicken_sandwich,waffle_fries")
    db.add_to_restaurants("wendys_id", "good_wendys_restr", "square_burger,non_waffle_fries")
    db.add_to_reports("cfa_hq_id", 1234098493, "chicken_sandwich")
    db.add_to_reports("cfa_hq_id", 1235982063, "waffle_fries")
    db.print_reports()
    db.print_restaurants()

def main():
    pass
    # test_basic_db_commands()

if __name__ == "__main__":
    main()