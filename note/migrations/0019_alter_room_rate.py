# Generated by Django 4.1.4 on 2023-09-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0018_alter_customer_email_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rate',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
