# Generated by Django 2.1 on 2018-08-17 04:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=60, verbose_name='公司名')),
                ('certificate', models.CharField(max_length=18, unique=True, verbose_name='税号')),
                ('total_user', models.SmallIntegerField(default=0, verbose_name='使用总人数')),
                ('com_tel', models.CharField(max_length=13, verbose_name='电话')),
                ('fax', models.CharField(max_length=13, verbose_name='传真')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
            ],
            options={
                'verbose_name': '公司',
                'verbose_name_plural': '公司表',
            },
        ),
        migrations.CreateModel(
            name='Damage_state_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage_id', models.SmallIntegerField(verbose_name='损伤编号')),
                ('damage_state', models.CharField(max_length=45, verbose_name='损伤状态')),
                ('damage_description', models.CharField(max_length=300, verbose_name='损伤状态描述')),
                ('median', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='中位值')),
                ('variance', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='方差')),
                ('lost_parameter', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='损失参数')),
                ('rehabilitation_coeffcient', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='修复系数')),
                ('min_rehab_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='最小工程量折减数量(修复费用)')),
                ('min_lost_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='工程量折减系数(修复费用)')),
                ('max_rehab_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='最大工程量折减数量(修复费用)')),
                ('max_lost_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='工程量折减系数(修复费用)')),
                ('cov_cost', models.DecimalField(decimal_places=4, default=0, max_digits=8, verbose_name='费用COV')),
                ('repair_people_day', models.IntegerField(default=0, verbose_name='修复时间(人*天)')),
                ('min_rehab_time', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='最小工程量折减数量(修复时间)')),
                ('min_lost_time', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='工程量折减系数(修复时间)')),
                ('max_rehab_time', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='最大工程量折减数量(修复时间)')),
                ('max_lost_time', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='工程量折减系数(修复时间)')),
                ('cov_time', models.DecimalField(decimal_places=4, default=0, max_digits=8, verbose_name='时间COV')),
            ],
            options={
                'verbose_name': '易损件损伤',
                'verbose_name_plural': '易损件损伤详情',
            },
        ),
        migrations.CreateModel(
            name='DB_part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_id', models.CharField(max_length=10, verbose_name='易损件id')),
                ('part_name', models.CharField(max_length=10, verbose_name='易损件名称')),
                ('description', models.CharField(max_length=300, verbose_name='易损件描述')),
                ('basic_unit', models.CharField(default='1个', max_length=10, verbose_name='基本单位')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='易损件单价')),
                ('EDP_type', models.CharField(choices=[('S', 'Story Drift Ratio'), ('A', 'Acceleration')], default='S', max_length=1, verbose_name='EDP类型')),
                ('data_resource', models.CharField(default='《建筑抗震韧性评价标准》编委会', max_length=45, verbose_name='数据来源')),
                ('is_formal', models.BooleanField(default=True, verbose_name='官方认证')),
                ('part_type', models.CharField(choices=[('h', 'hospital'), ('o', 'office'), ('s', 'school'), ('c', 'common')], default='c', max_length=1, verbose_name='场地类别')),
                ('damage_state_number', models.SmallIntegerField(default=0, verbose_name='损伤数量')),
            ],
            options={
                'verbose_name': '易损件',
                'verbose_name_plural': '易损件数据库',
            },
        ),
        migrations.CreateModel(
            name='Earthquake_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defense_intensity', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='设防烈度')),
                ('site_type', models.CharField(choices=[('0', 'zero'), ('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')], default='0', max_length=1, verbose_name='场地类别')),
                ('number', models.SmallIntegerField(verbose_name='地震波数')),
                ('group', models.SmallIntegerField(choices=[('0', 'zero'), ('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')], default=1, verbose_name='地震分组')),
                ('earthquake_level', models.CharField(choices=[('L', '多遇'), ('M', '设防'), ('S', '罕遇')], default='S', max_length=1, verbose_name='地震水准')),
            ],
        ),
        migrations.CreateModel(
            name='Earthquake_wave_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earthquake_wave_no', models.SmallIntegerField(verbose_name='地震波编号')),
                ('earthquake_wave_name', models.CharField(max_length=15, verbose_name='地震波名称')),
                ('peak', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='地震波峰值')),
                ('earthquake_wave_file', models.FileField(upload_to='<django.db.models.fields.related.ForeignKey>/%Y/%m/%d/', verbose_name='地震波文件')),
            ],
            options={
                'verbose_name': '地震波详情',
                'verbose_name_plural': '地震波详情',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_type', models.CharField(choices=[('s', 'StructuraElement/结构构件'), ('n', 'NonSturctualElement/非结构构件')], default='s', max_length=1, verbose_name='构建类型')),
                ('start_floor', models.SmallIntegerField(default=1, verbose_name='起始楼层')),
                ('stop_floor', models.SmallIntegerField(default=1, verbose_name='终止楼层')),
                ('X', models.SmallIntegerField(default=0, verbose_name='X方向偏移')),
                ('Y', models.SmallIntegerField(default=0, verbose_name='Y方向偏移')),
                ('Non', models.SmallIntegerField(default=0, verbose_name='无方向偏移')),
                ('element', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.DB_part', verbose_name='易损件编号')),
            ],
            options={
                'verbose_name': '构建信息',
                'verbose_name_plural': '构建信息表',
            },
        ),
        migrations.CreateModel(
            name='Floor_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_no', models.IntegerField(verbose_name='楼层')),
                ('floor_height', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='楼层高度')),
                ('floor_area', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='楼层面积')),
                ('influence_coefficient', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='楼层影响系数')),
                ('population_density', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='人口密度')),
            ],
            options={
                'verbose_name': '楼层信息',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=45, verbose_name='项目名称')),
                ('client_name', models.CharField(max_length=45, verbose_name='客户名称')),
                ('project_description', models.CharField(max_length=300, verbose_name='项目描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')),
                ('project_leader', models.CharField(default='unknown', max_length=20, verbose_name='项目负责人')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('is_finished', models.BooleanField(default=False, verbose_name='完成')),
                ('rate', models.CharField(max_length=1, verbose_name='定级')),
                ('material', models.CharField(max_length=30, verbose_name='材料')),
                ('structure_type', models.CharField(max_length=20, verbose_name='结构类型')),
                ('floor', models.IntegerField(verbose_name='楼层数')),
                ('figure_time', models.DateField(verbose_name='图审时间')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='楼层总高')),
                ('area', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='总面积')),
                ('cost_per_squaremeter', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='每平米造价')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Structure_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('X', 'X'), ('Y', 'Y')], default='X', max_length=1)),
                ('EDP_type', models.CharField(choices=[('S', 'Story Drift Ratio'), ('A', 'Acceleration')], default='S', max_length=1)),
                ('floor_no', models.SmallIntegerField(verbose_name='楼层编号')),
                ('earthquake_no', models.SmallIntegerField(verbose_name='地震波编号')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Project')),
            ],
            options={
                'verbose_name': '结构响应',
                'verbose_name_plural': '结构响应',
            },
        ),
        migrations.CreateModel(
            name='User_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('title', models.CharField(max_length=45, verbose_name='标题')),
                ('context', models.CharField(max_length=450, verbose_name='正文')),
                ('response', models.CharField(max_length=450, verbose_name='管理员回复')),
                ('is_response', models.BooleanField(default=False, verbose_name='是否已回复')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('response_time', models.DateTimeField(verbose_name='回复时间')),
            ],
            options={
                'verbose_name': '用户评价',
                'verbose_name_plural': '用户评价',
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('truename', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('telephone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('architect_id', models.CharField(blank=True, max_length=12, unique=True, verbose_name='建筑师证号')),
                ('job', models.CharField(blank=True, max_length=20, verbose_name='公司职务')),
                ('login_amount', models.IntegerField(default=1, verbose_name='登陆次数')),
                ('project_amount', models.SmallIntegerField(default=0, verbose_name='项目数')),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Company_Info', verbose_name='公司')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user_comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='floor_info',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='element',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='earthquake_wave_detail',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='earthquake_info',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='db_part',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='damage_state_detail',
            name='DB_part',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BTESDB.DB_part', verbose_name='易损件'),
        ),
        migrations.AlterUniqueTogether(
            name='user_comment',
            unique_together={('user', 'comment_id')},
        ),
        migrations.AlterUniqueTogether(
            name='db_part',
            unique_together={('part_id', 'part_type')},
        ),
        migrations.AlterUniqueTogether(
            name='damage_state_detail',
            unique_together={('DB_part', 'damage_id')},
        ),
    ]
