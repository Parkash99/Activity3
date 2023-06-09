# Generated by Django 4.2 on 2023-05-17 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baham', '0002_userprofile_remove_companion_user_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='date_voided',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_updater', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='void_reason',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='voided',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='voided_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_voider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_voided',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_updater', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='void_reason',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voided',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voided_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_voider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date_voided',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_updater', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='void_reason',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='voided',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='voided_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_voider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiclemodel_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='date_voided',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehiclemodel_updater', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='void_reason',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='voided',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='voided_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiclemodel_voider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
