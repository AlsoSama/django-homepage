# 个人网站

一个基于Django的个人网站，以黑白为主色调，包含丰富的动画效果和交互体验。

## 功能特性

### 🎨 设计特色
- **黑白主色调**：简洁优雅的配色方案
- **复杂动画效果**：丰富的CSS动画和JavaScript交互
- **响应式设计**：完美适配各种设备尺寸

### 📱 页面功能
- **首页**：个人介绍、精选作品、项目展示
- **作品展示**：作品分类筛选、网格布局展示
- **项目展示**：技术项目详细介绍
- **学术论文**：论文列表、PDF下载
- **关于我**：个人简介、技能展示、教育背景
- **联系方式**：多种联系方式、在线表单

### 🛠 技术栈
- **后端**：Django 5.2.6
- **前端**：HTML5、CSS3、JavaScript
- **数据库**：SQLite（开发环境）
- **图片处理**：Pillow
- **字体**：Inter字体（Google Fonts）

## 快速开始

### 环境要求
- Python 3.8+
- Django 5.2.6
- Pillow 10.4.0

### 安装步骤

1. **克隆项目**
```bash
git clone <your-repo-url>
cd personal_website
```

2. **创建虚拟环境**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **数据库迁移**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **创建超级用户**
```bash
python manage.py createsuperuser
```

6. **启动开发服务器**
```bash
python manage.py runserver
```

7. **访问网站**
- 网站首页：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/

## 数据模型

### 个人信息 (PersonalInfo)
- 姓名、职位、个人简介
- 头像、背景图片

### 作品信息 (Work)
- 作品标题、描述、分类
- 作品图片、创作日期
- 精选标记、显示顺序

### 论文信息 (Paper)
- 论文标题、作者、期刊
- 摘要、DOI链接、PDF文件
- 发表日期、发表状态

### 项目信息 (Project)
- 项目名称、描述、技术栈
- GitHub链接、演示链接
- 开始/结束日期、进行状态

### 联系方式 (Contact)
- 联系方式类型（邮箱、电话、GitHub等）
- 联系方式值、图标
- 主要联系方式标记

### 技能信息 (Skill)
- 技能名称、熟练程度
- 技能分类、显示顺序

### 教育经历 (Education)
- 学位、学校、专业
- 开始/结束年份、描述

## 管理后台

访问 `/admin/` 可以管理所有数据：

1. **个人信息管理**：更新个人简介、头像等
2. **作品管理**：添加、编辑、删除作品
3. **论文管理**：管理学术论文信息
4. **项目管理**：管理技术项目
5. **联系方式管理**：更新各种联系方式
6. **技能管理**：管理技能信息
7. **教育经历管理**：更新教育背景

## 自定义配置

### 添加新页面
1. 在 `portfolio/views.py` 中添加视图函数
2. 在 `portfolio/urls.py` 中添加URL路由
3. 在 `portfolio/templates/portfolio/` 中创建模板文件

### 修改样式
- 主要样式文件：`static/css/style.css`
- 使用CSS变量进行主题定制
- 支持响应式设计

### 添加动画
- 动画效果在 `static/css/style.css` 中定义
- JavaScript交互在 `static/js/main.js` 中实现
- 支持AOS（Animate On Scroll）效果

## 部署建议

### 生产环境配置
1. 修改 `settings.py` 中的 `DEBUG = False`
2. 设置 `ALLOWED_HOSTS`
3. 配置静态文件服务
4. 使用PostgreSQL或MySQL数据库
5. 配置媒体文件存储

### 推荐部署平台
- **Heroku**：简单易用的云平台
- **DigitalOcean**：VPS部署
- **AWS**：企业级部署
- **阿里云**：国内访问优化

## 浏览器支持

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：

- 邮箱：your-email@example.com
- GitHub：https://github.com/your-username
- 网站：https://your-website.com

---

**享受创建您的个人网站！** 🚀
