"""
Simple launcher for the Django + Channels server
"""
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Import and run daphne
from daphne.cli import CommandLineInterface

cli = CommandLineInterface()
cli.run(['-b', '0.0.0.0', '-p', '8000', 'asgi:application', '-v', '2'])
