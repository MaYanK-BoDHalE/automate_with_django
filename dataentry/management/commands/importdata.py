from django.core.management.base import BaseCommand,CommandError
from dataentry.models import Student
from django.apps import apps
import csv  

#proposed command = python manage.py importdata file_path


class Command(BaseCommand):
    help='import data from csav file'
    
    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help='path to the csv file to be imported')
        parser.add_argument('model_name',type=str,help='name of the model')
    
    def handle(self, *args, **kwargs):
        file_path=kwargs['file_path']
        model_name=kwargs['model_name'].capitalize()
        print(f'Importing data into model: {model_name}')
        print(f'Importing data from {file_path}...')
        model= None
        for app_config in apps.get_app_configs():
            #try to serach for model
            try:
                model=apps.get_model(app_config.label,model_name)
                break # stop searching for model
            except LookupError:
                continue # continue searching in other apps 
        if not model:  
            raise CommandError(f'Model "{model_name}" not found in any app')  
        with open(file_path,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                model.objects.create(**row) 
                 
        self.stdout.write(self.style.SUCCESS('Initial data imported successfully.'))