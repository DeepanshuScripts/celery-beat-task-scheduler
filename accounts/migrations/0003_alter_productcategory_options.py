# Generated by Django 4.0 on 2024-05-23 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_brand_productcategory_alter_userprofile_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Category'},
        ),
    ]