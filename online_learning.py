# online_learning.py

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self, topic):
        print(f"Uploaded content on: {topic}")

    def display_info(self):
        super().display_info()
        print(f"Role: Instructor, Subject: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = []

    def create_course(self, course_name, modules):
        self.courses.append((course_name, modules))
        print(f"Course '{course_name}' with {modules} modules created.")

    def display_info(self):
        super().display_info()
        print("Role: Course Creator")

# Demo
creator = CourseCreator("Anita", "anita@example.com", "Python")
creator.upload_content("OOP Concepts")
creator.create_course("Advanced Python", 5)
creator.display_info()
