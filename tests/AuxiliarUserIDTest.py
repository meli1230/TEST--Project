import unittest
from data.storage import users
from models.user import User

class TestUserIDGeneration(unittest.TestCase):
    """
    Testează generarea incrementală a ID-urilor utilizatorilor în funcție de numărul
    de elemente din lista globală `users`. Fiecare utilizator nou ar trebui să aibă un
    ID unic și să crească în ordine secvențială.
    """

    def setUp(self):
        """
        Configurare inițială pentru test:
        - Curăță lista globală `users` înainte de fiecare test pentru a asigura
          un mediu curat și izolat.
        """
        users.clear()

    def test_user_id_increment(self):
        """
        Testează dacă ID-urile utilizatorilor sunt generate corect și cresc în ordine:
        - Creează doi utilizatori și îi adaugă în lista `users`.
        - Verifică dacă ID-ul primului utilizator este 1.
        - Verifică dacă ID-ul celui de-al doilea utilizator este 2.
        """
        # Creează primul utilizator și îl adaugă în lista `users`
        user1 = User(len(users) + 1, "John Doe", "UTC")
        users.append(user1)

        # Creează al doilea utilizator și îl adaugă în lista `users`
        user2 = User(len(users) + 1, "Jane Smith", "UTC")
        users.append(user2)

        # Verifică ID-urile utilizatorilor
        self.assertEqual(user1.user_id, 1, "ID-ul primului utilizator ar trebui să fie 1.")
        self.assertEqual(user2.user_id, 2, "ID-ul celui de-al doilea utilizator ar trebui să fie 2.")
