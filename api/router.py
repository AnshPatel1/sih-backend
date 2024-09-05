from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import SkillViewSet, ProfileViewSet, SocialViewSet, EducationViewSet, ExperienceViewSet, ExperienceMediaViewSet, ProjectViewSet, ProjectMediaViewSet, \
    CertificateViewSet, JobViewSet, JobSkillViewSet, JobMediaViewSet, JobListingViewSet, JobApplicationViewSet, CourseViewSet, MentorStatusRequestViewSet, MentorshipRequestViewSet, \
    EndorsementViewSet, MentorshipWorkViewSet, FeaturedCourseViewSet


def get_router():
    router = DefaultRouter()
    router.register(r'skills', SkillViewSet, basename='skill')
    router.register(r'profiles', ProfileViewSet, basename='profile')
    router.register(r'socials', SocialViewSet, basename='social')
    router.register(r'educations', EducationViewSet, basename='education')
    router.register(r'experiences', ExperienceViewSet, basename='experience')
    router.register(r'experience-media', ExperienceMediaViewSet, basename='experience-media')
    router.register(r'projects', ProjectViewSet, basename='project')
    router.register(r'project-media', ProjectMediaViewSet, basename='project-media')
    router.register(r'certificates', CertificateViewSet, basename='certificate')
    router.register(r'jobs', JobViewSet, basename='job')
    router.register(r'job-skills', JobSkillViewSet, basename='job-skill')
    router.register(r'job-media', JobMediaViewSet, basename='job-media')
    router.register(r'job-listings', JobListingViewSet, basename='job-listing')
    router.register(r'job-applications', JobApplicationViewSet, basename='job-application')
    router.register(r'courses', CourseViewSet, basename='course')
    router.register(r'mentor-status-requests', MentorStatusRequestViewSet, basename='mentor-status-request')
    router.register(r'mentorship-requests', MentorshipRequestViewSet, basename='mentorship-request')
    router.register(r'endorsements', EndorsementViewSet, basename='endorsement')
    router.register(r'mentorship-works', MentorshipWorkViewSet, basename='mentorship-work')
    router.register(r'featured-courses', FeaturedCourseViewSet, basename='featured-course')

    return router
