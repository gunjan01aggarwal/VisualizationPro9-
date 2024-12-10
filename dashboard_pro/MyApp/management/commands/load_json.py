import json
from django.core.management.base import BaseCommand
from MyApp.models import Data
from datetime import datetime


def replace_null(data):
    for record in data:
        for key, value in record.items():
            # Check type and apply transformations
            if isinstance(value, str):
                if value.strip() == "":
                    record[key] = None
            elif isinstance(value, int):
                if value is None:
                    record[key] = 0
            elif value == "":  # Catch empty strings for unexpected types
                record[key] = None

    return data


fields=['added','published']

def update_dt_format(data, fields, current_format="%B, %d %Y %H:%M:%S", target_format="%Y-%m-%d %H:%M:%S"):
    """
    Update the datetime format for multiple fields in a list of dictionaries.
    If the field value is not a valid date string, set it to 0.

    Args:
        data (list): List of dictionaries containing datetime strings.
        fields (list): List of field names to update.
        current_format (str): The current format of the datetime strings.
        target_format (str): The target format to convert to.

    Returns:
        list: Updated list of dictionaries with formatted datetime strings or 0.
    """
    for record in data:
        for field in fields:
            value = record.get(field)

            # Ensure value is a string
            if isinstance(value, str):
                value = value.strip()  # Remove leading/trailing spaces
                if value:  # Check if it's not an empty string
                    try:
                        # Parse and reformat the datetime string
                        parsed_date = datetime.strptime(value, current_format)
                        record[field] = parsed_date.strftime(target_format)
                    except ValueError:
                        # If parsing fails, set to 0
                        record[field] = 0
            else:
                # If value is not a string or is None, set to 0
                record[field] = None
    return data



class Command(BaseCommand):
    help = 'Load data from JSON file into the database'

    def handle(self, *args, **kwargs):
        # Path to the JSON file
        json_file_path = 'MyApp/Data_Folder/jsondata.json'

        # Load JSON data
        with open(json_file_path, 'r',encoding='utf-8') as file:
            table_data = json.load(file)

        table_data=replace_null(table_data)
        table_data=update_dt_format(table_data,fields)
                   
        # Insert into database
        for item in table_data:

            Data.objects.create(
                end_year=item['end_year'],
                intensity=item['intensity'],
               sector=item['sector'],
               topic=item['topic'],
               insight=item['insight'],
               url=item['url'],
               region=item['region'],
               start_year=item['start_year'],
               impact=item['impact'],
               added=item['added'],
               published=item['published'],
               country=item['country'],
               relevance=item['relevance'],
               pestle=item['pestle'],
               source=item['source'],
               title=item['title'],
               likelihood=item['likelihood']
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))

