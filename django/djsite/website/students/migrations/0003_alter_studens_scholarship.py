# Generated by Django 4.2.6 on 2023-12-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_money_studens_scholarship_studens_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studens',
            name='scholarship',
            field=models.BooleanField(),
        ),
    ]