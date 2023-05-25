#!/usr/bin/env python
"""Django's утиліта командного рядка для виконання адміністративних завдань."""
import os
import sys


def main():
    """Виконує адміністративні завдання."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab5django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # обробка помилок відсутності необхідних пакетів
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# точка запуску програми
if __name__ == '__main__':
    main()
