class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def display_info(self):
        print(f"Name: {self.name}, Membership ID: {self.membership_id}")


class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.books_borrowed = 0

    def add_book(self):
        self.books_borrowed += 1
        print(f"Book added. Total books borrowed: {self.books_borrowed}")

    def return_book(self):
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            print(f"Book returned. Total books now: {self.books_borrowed}")
        else:
            print("No books to return.")

    def display_status(self):
        self.display_info()
        print(f"Books currently borrowed: {self.books_borrowed}")


# 👇 This is your test code
if __name__ == "__main__":
    student = StudentMember("Ravi", "S123")
    student.add_book()
    student.add_book()
    student.return_book()
    student.display_status()
