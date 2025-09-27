from django.db import models
from django.utils import timezone


class PersonalInfo(models.Model):
    """个人信息模型"""
    name = models.CharField(max_length=100, verbose_name="姓名")
    title = models.CharField(max_length=200, verbose_name="职位/头衔")
    bio = models.TextField(verbose_name="个人简介")
    avatar = models.ImageField(upload_to='avatars/', verbose_name="头像")
    background_image = models.ImageField(upload_to='backgrounds/', verbose_name="背景图片")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = "个人信息"

    def __str__(self):
        return self.name


class Work(models.Model):
    """作品信息模型"""
    title = models.CharField(max_length=200, verbose_name="作品标题")
    description = models.TextField(verbose_name="作品描述")
    image = models.ImageField(upload_to='works/', verbose_name="作品图片")
    category = models.CharField(max_length=50, verbose_name="作品分类")
    created_date = models.DateField(verbose_name="创作日期")
    is_featured = models.BooleanField(default=False, verbose_name="是否精选")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "作品"
        verbose_name_plural = "作品"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Paper(models.Model):
    """论文信息模型"""
    title = models.CharField(max_length=300, verbose_name="论文标题")
    authors = models.CharField(max_length=500, verbose_name="作者")
    journal = models.CharField(max_length=200, verbose_name="期刊/会议")
    publication_date = models.DateField(verbose_name="发表日期")
    abstract = models.TextField(verbose_name="摘要")
    doi = models.URLField(blank=True, null=True, verbose_name="DOI链接")
    pdf_file = models.FileField(upload_to='papers/', blank=True, null=True, verbose_name="PDF文件")
    is_published = models.BooleanField(default=True, verbose_name="是否已发表")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "论文"
        verbose_name_plural = "论文"
        ordering = ['order', '-publication_date']

    def __str__(self):
        return self.title


class Project(models.Model):
    """项目信息模型"""
    name = models.CharField(max_length=200, verbose_name="项目名称")
    description = models.TextField(verbose_name="项目描述")
    image = models.ImageField(upload_to='projects/', verbose_name="项目图片")
    technologies = models.CharField(max_length=300, verbose_name="使用技术")
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub链接")
    demo_url = models.URLField(blank=True, null=True, verbose_name="演示链接")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(blank=True, null=True, verbose_name="结束日期")
    is_ongoing = models.BooleanField(default=False, verbose_name="是否进行中")
    is_featured = models.BooleanField(default=False, verbose_name="是否精选")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"
        ordering = ['order', '-start_date']

    def __str__(self):
        return self.name


class Contact(models.Model):
    """联系方式模型"""
    CONTACT_TYPES = [
        ('email', '邮箱'),
        ('phone', '电话'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('wechat', '微信'),
        ('other', '其他'),
    ]
    
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPES, verbose_name="联系方式类型")
    value = models.CharField(max_length=200, verbose_name="联系方式值")
    icon = models.CharField(max_length=50, blank=True, verbose_name="图标类名")
    is_primary = models.BooleanField(default=False, verbose_name="是否主要联系方式")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "联系方式"
        verbose_name_plural = "联系方式"
        ordering = ['order', 'contact_type']

    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.value}"


class Skill(models.Model):
    """技能模型"""
    name = models.CharField(max_length=100, verbose_name="技能名称")
    level = models.IntegerField(choices=[(i, f"{i}%") for i in range(0, 101, 10)], verbose_name="熟练程度")
    category = models.CharField(max_length=50, verbose_name="技能分类")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "技能"
        verbose_name_plural = "技能"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Education(models.Model):
    """教育经历模型"""
    degree = models.CharField(max_length=100, verbose_name="学位")
    school = models.CharField(max_length=200, verbose_name="学校")
    major = models.CharField(max_length=100, verbose_name="专业")
    start_year = models.IntegerField(verbose_name="开始年份")
    end_year = models.IntegerField(blank=True, null=True, verbose_name="结束年份")
    description = models.TextField(blank=True, verbose_name="描述")
    is_current = models.BooleanField(default=False, verbose_name="是否在读")
    order = models.IntegerField(default=0, verbose_name="显示顺序")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "教育经历"
        verbose_name_plural = "教育经历"
        ordering = ['order', '-start_year']

    def __str__(self):
        return f"{self.degree} - {self.school}"