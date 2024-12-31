from db_config import get_connection

def login():
    conn = get_connection()
    if not conn:
        print("❌ Error: Could not connect to the database. Please try again later.")
        return None

    cursor = conn.cursor()
    print("\n🔐 Please log in to access the system.")

    username = input("👤 Username: ")
    password = input("🔑 Password: ")

    # Query to check the credentials
    query = "SELECT role FROM users WHERE username = :username AND password = :password"
    cursor.execute(query, {"username": username, "password": password})
    result = cursor.fetchone()

    if result:
        role = result[0]
        print(f"\n✅ Login Successful!\nWelcome, {username}! 👏\nYour role is: {role.capitalize()} 🎉\n")
        return role  # Return the role (admin/officer)
    else:
        print("\n❌ Invalid credentials. Please try again. 🔄\n")
        return None
