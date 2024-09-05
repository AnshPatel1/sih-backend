from rest_framework import serializers
from api.models import Skill, Profile, Social, Education, Experience, ExperienceMedia, Project, ProjectMedia, \
    Certificate, Job, JobSkill, JobMedia, JobListing, JobApplication, Course, MentorStatusRequest, MentorshipRequest, \
    Endorsement, MentorshipWork, FeaturedCourse

"""
This file contains the serializers for the models in the api app.
"""


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ExperienceMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceMedia
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = '__all__'


class JobMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobMedia
        fields = '__all__'


class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MentorStatusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorStatusRequest
        fields = '__all__'


class MentorshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipRequest
        fields = '__all__'


class EndorsementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endorsement
        fields = '__all__'


class MentorshipWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipWork
        fields = '__all__'


class FeaturedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedCourse
        fields = '__all__'
