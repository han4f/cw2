from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import migrate_users_from_file, register_user, login_user
from app.data.incidents import load_csv_to_table

def main():
    conn = connect_database()


    create_all_tables(conn)

    
    migrate_users_from_file(conn)

    
    load_csv_to_table("DATA/cyber_incidents.csv", "cyber_incidents", conn)
    load_csv_to_table("DATA/datasets_metadata.csv", "datasets_metadata", conn)
    load_csv_to_table("DATA/it_tickets.csv", "it_tickets", conn)


    print(register_user("alice", "SecurePass123", conn))
    print(login_user("alice", "SecurePass123", conn))

    conn.close()

if __name__ == "__main__":
    main()


