from tinydb import TinyDB, Query

# Inițializarea bazei de date
db = TinyDB('db.json')

# Tabele pentru utilizatori și programări
users_table = db.table('users')
appointments_table = db.table('appointments')

# Verificare unicitate utilizator (după nume)
def is_user_name_unique(name):
    User = Query()
    return not users_table.search(User.name == name)

# Adăugare utilizator
def add_user(user_id, name, timezone):
    if not is_user_name_unique(name):
        return f"User with name '{name}' already exists!"
    users_table.insert({'user_id': user_id, 'name': name, 'timezone': timezone})
    return "User added successfully!"

# Ștergere utilizator
def delete_user(name):
    User = Query()
    if not is_user_name_unique(name):  # Asigurăm că utilizatorul există
        users_table.remove(User.name == name)
        return "User deleted successfully!"
    return f"User with name '{name}' does not exist."

# Listare utilizatori
def list_users():
    return users_table.all()

# Adăugare programare
def add_appointment(user, consultant, customer_time, mentor_time):
    appointments_table.insert({
        'user': user,
        'consultant': consultant,
        'customer_time': customer_time,
        'mentor_time': mentor_time
    })
    return "Appointment added successfully!"

# Listare programări
def list_appointments():
    return appointments_table.all()
