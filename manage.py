#!/usr/bin/env python
 import sys

 def main():
     """Run administrative tasks."""
     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'aws')
     try:
         from django.core.management import execute_from_command_line
     except ImportError as exc:
         raise ImportError(
             "Couldn't import Django. Are you sure it's installed and "
             "available on your PYTHONPATH environment variable? Did you "
             "forget to activate a virtual environment?"
         ) from exc
     try:
          execute_from_command_line(sys.argv) # just put this in try block
     except:
          pass

 if __name__ == '__main__':
     main()
