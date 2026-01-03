from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help='Insert initial data into the database'
    def handle(self, *args, **kwargs):
        dataset=[
            {'roll_no':'104', 'name':'Mayank', 'age':25},
            {'roll_no':'105', 'name':'Anjali', 'age':22},
            {'roll_no':'106', 'name':'Rohit', 'age':24},
            {'roll_no':'107', 'name':'Sneha', 'age':23},
            {'roll_no':'108', 'name':'Amit', 'age':26},
            ]
        for data in dataset:
            roll_no=data['roll_no']
            existing_student=Student.objects.filter(roll_no=roll_no).exists()
            if not existing_student:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exists. Skipping insertion.'))    
                    
        
        
        self.stdout.write(self.style.SUCCESS('Initial data inserted successfully.'))