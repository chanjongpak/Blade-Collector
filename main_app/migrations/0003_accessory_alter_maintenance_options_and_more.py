# Generated by Django 4.1.3 on 2022-11-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='maintenance date'),
        ),
        migrations.AddField(
            model_name='blade',
            name='accessories',
            field=models.ManyToManyField(to='main_app.accessory'),
        ),
    ]
