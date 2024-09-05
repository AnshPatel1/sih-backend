from django.contrib import admin

# Register your models here.


from api.models import *

admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(ExperienceMedia)
admin.site.register(Project)
admin.site.register(ProjectMedia)
admin.site.register(Certificate)
admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(JobMedia)
admin.site.register(JobListing)
admin.site.register(JobApplication)
admin.site.register(Course)
admin.site.register(MentorStatusRequest)
admin.site.register(MentorshipRequest)
admin.site.register(Endorsement)
admin.site.register(MentorshipWork)
admin.site.register(FeaturedCourse)
