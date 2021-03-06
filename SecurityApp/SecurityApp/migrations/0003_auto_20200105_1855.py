# Generated by Django 2.2.7 on 2020-01-05 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityApp', '0002_auto_20191220_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='call',
            options={'verbose_name': 'Call', 'verbose_name_plural': 'Calls'},
        ),
        migrations.AlterModelOptions(
            name='call_status',
            options={'verbose_name': 'Call_Status', 'verbose_name_plural': 'Call_Statuses'},
        ),
        migrations.AlterModelOptions(
            name='call_type',
            options={'verbose_name': 'Call_Type', 'verbose_name_plural': 'Call_Types'},
        ),
        migrations.AlterModelOptions(
            name='close_chp',
            options={'verbose_name': 'Close_ChP', 'verbose_name_plural': 'Close_ChPes'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='mode',
            options={'verbose_name': 'Mode', 'verbose_name_plural': 'Modes'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Object', 'verbose_name_plural': 'Objects'},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'Period', 'verbose_name_plural': 'Periods'},
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'Plan', 'verbose_name_plural': 'Plans'},
        ),
        migrations.AlterModelOptions(
            name='plan_raw',
            options={'verbose_name': 'Plan_raw', 'verbose_name_plural': 'Plan_raws'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AlterModelOptions(
            name='status_chp',
            options={'verbose_name': 'Status_ChP', 'verbose_name_plural': 'Status_ChPes'},
        ),
        migrations.AlterModelOptions(
            name='tick_chp',
            options={'verbose_name': 'Tick_ChP', 'verbose_name_plural': 'Tick_ChPes'},
        ),
        migrations.AlterModelOptions(
            name='type_chp',
            options={'verbose_name': 'Type_ChP', 'verbose_name_plural': 'Type_ChPes'},
        ),
    ]
