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

    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Subject: {self.subject}")

    def upload_content(self, content_title):
        print(f"{self.name} uploaded content: {content_title}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject, course_name):
        super().__init__(name, email, subject)
        self.course_name = course_name
        self.modules = []

    def display_info(self):
        print(f"Course Creator: {self.name}, Email: {self.email}, Subject: {self.subject}, Course: {self.course_name}")

    def create_module(self, module_title):
        self.modules.append(module_title)
        print(f"Module '{module_title}' added to course '{self.course_name}'")

# Test the code
if __name__ == "__main__":
    creator = CourseCreator("Meena", "meena@example.com", "Math", "Algebra Basics")
    creator.display_info()
    creator.upload_content("Introduction to Algebra")
    creator.create_module("Variables and Expressions")
    creator.create_module("Equations and Inequalities")
