# Generated by Django 3.2.13 on 2022-06-22 15:00

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("features", "0042_default_type_to_STANDARD"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("features", "feature"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="feature",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]