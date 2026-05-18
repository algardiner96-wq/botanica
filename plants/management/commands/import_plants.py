import csv
from django.core.management.base import BaseCommand, CommandError
from plants.models import Plant


class Command(BaseCommand):
    help = 'Import plants from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        # Mapping dictionaries for choice fields
        watering_map = {
            'Dry': 'dry',
            'Light': 'light',
            'Moderate': 'moderate',
            'Moist': 'moist',
        }
        
        sunlight_map = {
            'Full sun': 'full_sun',
            'Partial shade': 'partial_sun',
            'Shade': 'shade',
        }
        
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                created_count = 0
                skipped_count = 0
                
                for row in reader:
                    try:
                        # Check if plant already exists
                        if Plant.objects.filter(name=row['Name']).exists():
                            self.stdout.write(
                                self.style.WARNING(f"Skipping '{row['Name']}' - already exists")
                            )
                            skipped_count += 1
                            continue
                        
                        # Map the CSV values to model choices
                        plant_type = row['Plant type'].lower() if row['Plant type'] else ''
                        lifespan = row['Lifespan'] if row['Lifespan'] else ''
                        watering = watering_map.get(row['Watering'], '')
                        sunlight = sunlight_map.get(row['Sunlight'], '')
                        
                        # Create the plant
                        plant = Plant.objects.create(
                            name=row['Name'],
                            scientific_name=row['Scientific name'],
                            plant_type=plant_type,
                            lifespan=lifespan,
                            watering=watering,
                            sunlight=sunlight,
                        )
                        
                        self.stdout.write(
                            self.style.SUCCESS(f"Created '{plant.name}'")
                        )
                        created_count += 1
                        
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f"Error creating plant from row {row}: {str(e)}")
                        )
                        skipped_count += 1
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f"\n✓ Import complete! Created: {created_count}, Skipped: {skipped_count}"
                    )
                )
        
        except FileNotFoundError:
            raise CommandError(f"CSV file not found at: {csv_file_path}")
        except Exception as e:
            raise CommandError(f"Error reading CSV file: {str(e)}")
