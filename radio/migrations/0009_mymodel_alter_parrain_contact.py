# Generated by Django 5.0.6 on 2024-07-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0008_contact_parrain'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.AlterField(
            model_name='parrain',
            name='contact',
            field=models.URLField(blank=True, null=True),
        ),
    ]