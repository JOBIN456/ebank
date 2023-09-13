# Generated by Django 4.2.5 on 2023-09-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('branch', models.CharField(max_length=50)),
                ('sub_branch', models.CharField(max_length=50)),
                ('account_type', models.CharField(choices=[('S', 'Savings Account'), ('C', 'Current Account'), ('F', 'Fixed Deposit Account')], max_length=1)),
                ('debit_card', models.BooleanField(default=False)),
                ('credit_card', models.BooleanField(default=False)),
                ('cheque_book', models.BooleanField(default=False)),
            ],
        ),
    ]
