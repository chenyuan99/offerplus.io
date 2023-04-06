# Generated by Django 3.1.7 on 2023-03-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_auto_20220816_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationrecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='applicationrecord',
            name='outcome',
            field=models.TextField(choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REFER', 'REFER'), ('REJECT(Resume)', 'REJECT(Resume)'), ('REJECT(VO)', 'REJECT(VO)'), ('REJECT(OA)', 'REJECT(OA)'), ('VO', 'VO'), ('OA', 'OA')]),
        ),
    ]