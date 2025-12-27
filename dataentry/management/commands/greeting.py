from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help='print greeting message to the console'
    
    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Name of the person to greet')
        
    def handle(self,*args,**kwargs):
        name=kwargs['name']
        greeting=f'hello {name} , welcome to Django!'
        self.stdout.write(greeting)
        
        