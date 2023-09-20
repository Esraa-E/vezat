# Generated by Django 4.2.3 on 2023-08-31 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fofo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('جراحه اورام', 'جراحه اورام'), ('امراض دم', 'امراض دم'), ('جراحه سمنه و مناظير', 'جراحه سمنه و مناظير'), ('انف و اذن', 'انف و اذن'), ('تخسيس و تغذيه', 'تخسيس و تغذيه'), ('اطفال حديثي الولاده', 'اطفال حديثي الولاده'), ('نساء و توليد', 'نساء و توليد'), ('عظام', 'عظام'), ('باطنه', 'باطنه'), ('نفسي', 'نفسي'), ('اورام', 'اورام'), ('جراحه اطفال', 'جراحه اطفال'), ('جراحه تجميل', 'جراحه تجميل'), ('اسنان', 'اسنان'), ('مخ و اعصاب', 'مخ و اعصاب'), ('جراحه اوعيه دمويه', 'جراحه اوعيه دمويه'), ('قلب و اعيه دمويه', 'فلب و اعيه دمويه'), ('جلديه', 'جلديه')], max_length=50, null=True, verbose_name='الدكتور ؟'),
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='الاسم:')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='وقت الكشف')),
                ('crated', models.CharField(max_length=50, verbose_name='الدفع')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docc', to='fofo.profile')),
            ],
        ),
    ]