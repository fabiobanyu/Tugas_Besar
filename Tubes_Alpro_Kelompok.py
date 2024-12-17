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

# Objek GUI
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis Kelompok 6")
        self.current_user = None
        self.show_login()

    def show_login(self):
        """Menampilkan layar login."""
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.show_register).pack()

    def show_register(self):
        """Menampilkan layar registrasi."""
        self.clear_screen()
        tk.Label(self.root, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.reg_username_entry = tk.Entry(self.root)
        self.reg_username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.reg_password_entry = tk.Entry(self.root, show="*")
        self.reg_password_entry.pack()

        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.show_login).pack()

    def login(self):
        """Proses login pengguna."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in accounts and accounts[username] == password:
            self.current_user = username
            self.show_main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    def register(self):
        """Proses registrasi pengguna baru."""
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        if username in accounts:
            messagebox.showerror("Registrasi Gagal", "Username sudah ada.")
        elif username and password:
            accounts[username] = password
            messagebox.showinfo("Registrasi Berhasil", "Anda sekarang dapat login.")
            self.show_login()
        else:
            messagebox.showerror("Registrasi Gagal", "Masukkan username dan password.")

    def show_main_menu(self):
        """Menampilkan menu utama setelah login."""
        self.clear_screen()
        tk.Label(self.root, text=f"Selamat datang, {self.current_user}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Manajemen Kuis", command=self.manage_quiz).pack(pady=5)
        tk.Button(self.root, text="Mainkan Kuis", command=self.play_quiz).pack(pady=5)
        tk.Button(self.root, text="Tentang Kami", command=self.about_us).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.show_login).pack(pady=5)

    def manage_quiz(self):
        """Menampilkan layar manajemen kuis."""
        self.clear_screen()
        tk.Label(self.root, text="Manajemen Kuis", font=("Arial", 16)).pack(pady=10)

        # Daftar soal
        self.question_listbox = tk.Listbox(self.root, width=50)
        self.question_listbox.pack(pady=5)
        self.load_questions()

        tk.Button(self.root, text="Tambah Soal", command=self.add_question).pack(pady=5)
        tk.Button(self.root, text="Edit Soal", command=self.edit_question).pack(pady=5)
        tk.Button(self.root, text="Hapus Soal", command=self.delete_question).pack(pady=5)
        tk.Button(self.root, text="Kembali", command=self.show_main_menu).pack(pady=5)

    def load_questions(self):
        """Memuat daftar soal ke dalam listbox."""
        self.question_listbox.delete(0, tk.END)
        for i, q in enumerate(questions.to_list()):
            self.question_listbox.insert(tk.END, f"{i+1}. {q['question']}")

    def add_question(self):
        """Menambahkan soal baru ke database."""
        def save_question():
            try:
                question = question_entry.get()
                options = [opt1_entry.get(), opt2_entry.get(), opt3_entry.get(), opt4_entry.get()]
                answer = answer_entry.get()

                if not question or not all(options) or not answer:
                    raise ValueError("Semua field harus diisi.")

                new_question = {"question": question, "options": options, "answer": answer}
                questions.append(new_question)
                self.load_questions()
                add_window.destroy()
                messagebox.showinfo("Sukses", "Soal berhasil ditambahkan.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        add_window = tk.Toplevel(self.root)
        add_window.title("Tambah Soal")

        tk.Label(add_window, text="Pertanyaan").pack()
        question_entry = tk.Entry(add_window, width=50)
        question_entry.pack()

        tk.Label(add_window, text="Pilihan 1").pack()
        opt1_entry = tk.Entry(add_window, width=50)
        opt1_entry.pack()

        tk.Label(add_window, text="Pilihan 2").pack()
        opt2_entry = tk.Entry(add_window, width=50)
        opt2_entry.pack()

        tk.Label(add_window, text="Pilihan 3").pack()
        opt3_entry = tk.Entry(add_window, width=50)
        opt3_entry.pack()

        tk.Label(add_window, text="Pilihan 4").pack()
        opt4_entry = tk.Entry(add_window, width=50)
        opt4_entry.pack()

        tk.Label(add_window, text="Jawaban Benar").pack()
        answer_entry = tk.Entry(add_window, width=50)
        answer_entry.pack()

        tk.Button(add_window, text="Simpan", command=save_question).pack(pady=5)

    def edit_question(self):
        """Mengedit soal yang dipilih."""
        selected = self.question_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Pilih soal untuk diedit")

        def save_edited_question():
            try:
                question = question_entry.get()
                options = [opt1_entry.get(), opt2_entry.get(), opt3_entry.get(), opt4_entry.get()]
                answer = answer_entry.get()

                if not question or not all(options) or not answer:
                    raise ValueError("Semua field harus diisi.")

                updated_question = {"question": question, "options": options, "answer": answer}
                questions.update(selected_index, updated_question)
                self.load_questions()
                edit_window.destroy()
                messagebox.showinfo("Sukses", "Soal berhasil diperbarui.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        selected_index = selected[0]
        question_data = questions.get(selected_index)

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Soal")

        tk.Label(edit_window, text="Pertanyaan").pack()
        question_entry = tk.Entry(edit_window, width=50)
        question_entry.insert(0, question_data['question'])
        question_entry.pack()

        tk.Label(edit_window, text="Pilihan 1").pack()
        opt1_entry = tk.Entry(edit_window, width=50)
        opt1_entry.insert(0, question_data['options'][0])
        opt1_entry.pack()

        tk.Label(edit_window, text="Pilihan 2").pack()
        opt2_entry = tk.Entry(edit_window, width=50)
        opt2_entry.insert(0, question_data['options'][1])
        opt2_entry.pack()

        tk.Label(edit_window, text="Pilihan 3").pack()
        opt3_entry = tk.Entry(edit_window, width=50)
        opt3_entry.insert(0, question_data['options'][2])
        opt3_entry.pack()

        tk.Label(edit_window, text="Pilihan 4").pack()
        opt4_entry = tk.Entry(edit_window, width=50)
        opt4_entry.insert(0, question_data['options'][3])
        opt4_entry.pack()

        tk.Label(edit_window, text="Jawaban Benar").pack()
        answer_entry = tk.Entry(edit_window, width=50)
        answer_entry.insert(0, question_data['answer'])
        answer_entry.pack()

        tk.Button(edit_window, text="Simpan", command=save_edited_question).pack(pady=5)

    def delete_question(self):
        """Menghapus soal yang dipilih."""
        selected = self.question_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Pilih soal untuk dihapus.")
            return

        selected_index = selected[0]
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus soal ini?"):
            questions.delete(selected_index)
            self.load_questions()
            messagebox.showinfo("Sukses", "Soal berhasil dihapus.")