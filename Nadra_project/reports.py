from db_config import get_connection

def generate_report():
    conn = get_connection()
    if not conn:
        print("❌ Error: Could not connect to the database.")
        return

    cursor = conn.cursor()
    print("\n📊 Generating report... Please wait.")

    query = "SELECT COUNT(*) FROM citizens WHERE status = 'active'"
    cursor.execute(query)
    active_population = cursor.fetchone()[0]

    print(f"\n✅ Report Generated Successfully!\n")
    print(f"🌍 Active Population: {active_population} citizens")

    cursor.close()
    conn.close()
