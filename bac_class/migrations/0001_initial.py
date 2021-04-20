# Generated by Django 3.2 on 2021-04-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bac_image_store',
            fields=[
                ('S_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Bacteria Image Database',
            },
        ),
    ]
