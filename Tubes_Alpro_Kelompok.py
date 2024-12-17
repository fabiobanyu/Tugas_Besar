import tkinter as tk
from tkinter import messagebox
import random

# Implementasi Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Menambahkan node baru ke linked list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete(self, index):
        """Menghapus node dari linked list berdasarkan indeks."""
        try:
            if not self.head:
                raise IndexError("Linked list kosong, tidak bisa menghapus.")

            if index == 0:
                self.head = self.head.next
                return True

            current = self.head
            prev = None
            count = 0

            while current and count != index:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError("Indeks di luar batas linked list.")

            prev.next = current.next
            return True
        except IndexError as e:
            messagebox.showerror("Error", str(e))
            return False

    def get(self, index):
        """Mengambil data node berdasarkan indeks."""
        return self._get_recursive(self.head, index, 0)

    def _get_recursive(self, node, index, count):
        """Fungsi rekursif untuk mengambil data berdasarkan indeks."""
        if not node:
            return None
        if count == index:
            return node.data
        return self._get_recursive(node.next, index, count + 1)

    def update(self, index, new_data):
        """Memperbarui data node berdasarkan indeks."""
        try:
            current = self.head
            count = 0

            while current:
                if count == index:
                    current.data = new_data
                    return True
                current = current.next
                count += 1

            raise IndexError("Indeks di luar batas linked list.")
        except IndexError as e:
            messagebox.showerror("Error", str(e))
            return False

    def to_list(self):
        """Mengubah linked list menjadi list Python."""
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

accounts = {"admin": "admin"}  # Penyimpanan username-password sederhana
questions = LinkedList()

# Prepopulasi soal dengan 10 contoh soal
sample_questions = [
    {"question": "Apa hasil dari 2 + 2?", "options": ["1", "2", "3", "4"], "answer": "4"},
    {"question": "Apa ibu kota Prancis?", "options": ["Paris", "Berlin", "Roma", "Madrid"], "answer": "Paris"},
    {"question": "Siapa penulis 'Hamlet'?", "options": ["Shakespeare", "Tolstoy", "Hemingway", "Dickens"], "answer": "Shakespeare"},
    {"question": "Berapa titik didih air?", "options": ["90C", "100C", "110C", "80C"], "answer": "100C"},
    {"question": "Planet apa yang dikenal sebagai Planet Merah?", "options": ["Bumi", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "Apa lautan terbesar di dunia?", "options": ["Atlantik", "Pasifik", "Hindia", "Arktik"], "answer": "Pasifik"},
    {"question": "Berapa akar kuadrat dari 64?", "options": ["6", "8", "7", "9"], "answer": "8"},
    {"question": "Siapa yang melukis Mona Lisa?", "options": ["Van Gogh", "Picasso", "Leonardo Da Vinci", "Raphael"], "answer": "Leonardo Da Vinci"},
    {"question": "Apa ibu kota Jepang?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"},
    {"question": "Apa simbol kimia untuk Emas?", "options": ["G", "Au", "Ag", "Pb"], "answer": "Au"}
]

for q in sample_questions:
    questions.append(q)