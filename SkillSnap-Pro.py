import json

from datetime import date
def add_skill_entry():
    today = date.today().isoformat()   
    skills = input("What skill(s) did you practice today? ") 
    note = input("Add a short note (optional): ")
    entry = { "date": today,
             "skills": skills,
              "note": note
             }
    filename = "skills.json"

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open (filename, "w") as file:
        json.dump(data, file, indent=4)
    print("✅ Entry saved to skills.json!")
    
    


def view_all_entries():
    filename = "skills.json"

    try:
        with open(filename, "r")as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No skill entries Found")
        return
    if not data:
        print("Your skill log is empty!")
        return
    print("\n Your Skill Entries:\n")
    for entry in data:
        print(f"📅 {entry['date']}")
        print(f"🧠 Skill: {entry['skills']}")
        print(f"📝 Note: {entry['note']}\n")
 

def Delete_entry():
    filename = "skills.json"

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No entry to Delete")
        return

    if not data:
        print("No Skill entry to Delete!")
        return

    print("\n🗑️ To Delete Skill Entries:\n")
    for idx, entry in enumerate(data, start=1):
        print(f"{idx}. 📅 {entry['date']}")
        print(f"   🧠 Skill: {entry['skills']}")
        print(f"   📝 Note: {entry['note']}\n")
    
    try:
        choice = int(input("Enter the number of the entry you want to delete: "))
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"✅ Deleted skill: {removed['skills']}")
        else:
            print("❌ Invalid number selected.")
    except ValueError:
        print("❌ Please enter a valid number.")

    view = input("👀 Do you want to view all remaining entries? (y/n): ")
    if view.lower() == "y":
        view_all_entries()



def main():
    while True:
        print("\n💼 Welcome to SkillSnap-Pro!")
        print("1️⃣ Add New Skill Entry")
        print("2️⃣ View All Entries")
        print("3️⃣ Delete an Entry")
        print("4️⃣ Exit")
        choice = input("Choose an option (1, 2, 3, or 4): ")

        if choice == "1":
            add_skill_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            Delete_entry() 
        elif choice == "4":
            print("👋 Exiting SkillSnap-Pro. Keep growing, Dithi!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
main()



    