from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.course_name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    start_date = models.DateField()
    timing = models.CharField(max_length=50)

    def __str__(self):
        return self.batch_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    admission_date = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.student.first_name

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return self.student.first_name

class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='study_material/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')
    submission_date = models.DateField(auto_now_add=True)
    marks = models.IntegerField()

    def __str__(self):
        return self.student.first_name

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.exam_name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.student.first_name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    feedback_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name


class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    query_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name