from db_config import get_connection

def add_citizen():
    conn = get_connection()
    if not conn:
        print("❌ Error: Could not connect to the database.")
        return

    cursor = conn.cursor()
    print("\n🔑 Please enter the details of the citizen to add.")

    name = input("👤 Name: ")
    cnic = input("💳 CNIC: ")
    dob = input("🎂 Date of Birth (YYYY-MM-DD): ")
    gender = input("🚻 Gender (M/F): ")
    address = input("🏠 Address: ")
    phone = input("📞 Phone: ")

    query = """
        INSERT INTO citizens (cnic, name, dob, gender, address, phone)
        VALUES (:cnic, :name, TO_DATE(:dob, 'YYYY-MM-DD'), :gender, :address, :phone)
    """
    try:
        cursor.execute(query, {"cnic": cnic, "name": name, "dob": dob, "gender": gender, "address": address, "phone": phone})
        conn.commit()
        print("\n✅ Citizen added successfully! 🎉")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def view_citizen():
    conn = get_connection()
    if not conn:
        print("❌ Error: Could not connect to the database.")
        return

    cursor = conn.cursor()
    print("\n🔍 Enter the CNIC of the citizen to search.")
    cnic = input("💳 CNIC: ")

    query = "SELECT * FROM citizens WHERE cnic = :cnic"
    cursor.execute(query, {"cnic": cnic})
    result = cursor.fetchone()
    print(result)

    if result:
        print("\n👤 Citizen Details:")
        print(f"📄 Name: {result[2]}")
        print(f"💳 CNIC: {result[1]}")
        print(f"🎂 Date of Birth: {result[3]}")
        print(f"🚻 Gender: {result[4]}")
        print(f"🏠 Address: {result[5]}")
        print(f"📞 Phone: {result[6]}")
    else:
        print("\n❌ Citizen not found.")
    cursor.close()
    conn.close()

def view_all_citizens():
    conn = get_connection()
    if not conn:
        print("❌ Error: Could not connect to the database.")
        return

    cursor = conn.cursor()
    query = "SELECT * FROM citizens"
    cursor.execute(query)
    citizens = cursor.fetchall()
    print(citizens)

    if citizens:
        print("\n👥 All Citizens:")
        for citizen in citizens:
            print(f"\n📄 Name: {citizen[2]}")
            print(f"💳 CNIC: {citizen[1]}")
            print(f"🎂 Date of Birth: {citizen[3]}")
            print(f"🚻 Gender: {citizen[4]}")
            print(f"🏠 Address: {citizen[5]}")
            print(f"📞 Phone: {citizen[6]}")
            print("-" * 40)  # Separator between citizens
    else:
        print("\n❌ No citizens found.")

    cursor.close()
    conn.close()

