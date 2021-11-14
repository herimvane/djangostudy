from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.

#在admin站点让Choice对象在Question对象编辑页面编辑
# admin.StackedInline纵向显示
# admin.TabularInlin横向显示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 在admin站点注册Question
class QuestionAdmin(admin.ModelAdmin):
    # admin站点显示的字段（按顺序）
    # fields = ['pub_date', 'question_text']
    #将字段分组
    fieldsets = [
        ('Question Title', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 显示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

    # 结果过滤器
    list_filter = ['pub_date']
    # 搜索器
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# 设置admin页面标题
# admin.AdminSite.site_header = '后台管理页面'