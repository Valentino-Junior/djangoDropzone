# Generated by Django 2.0 on 2023-01-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221218_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='ImageType',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
