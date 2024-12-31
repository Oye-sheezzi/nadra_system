from auth import login
from citizen import add_citizen, view_citizen, view_all_citizens
from reports import generate_report

def main_menu():
    role = login()
    if not role:
        return

    while True:
        print("\n--- 🏛️ NADRA System Menu ---")
        print("1. 👤 Add Citizen")
        print("2. 🔍 Search Citizen")
        print("3. 🌍 View All Citizens")
        print("4. 📊 Generate Report")
        print("5. 🚪 Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_citizen()
        elif choice == "2":
            view_citizen()
        elif choice == "3":
            view_all_citizens()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("\n🚶‍♂️ Exiting... Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please try again. 🔄")

if __name__ == "__main__":
    main_menu()
