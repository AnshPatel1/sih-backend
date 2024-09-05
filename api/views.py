from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import *


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsAuthenticated]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]


class ExperienceMediaViewSet(viewsets.ModelViewSet):
    queryset = ExperienceMedia.objects.all()
    serializer_class = ExperienceMediaSerializer
    permission_classes = [IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectMediaViewSet(viewsets.ModelViewSet):
    queryset = ProjectMedia.objects.all()
    serializer_class = ProjectMediaSerializer
    permission_classes = [IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


class JobSkillViewSet(viewsets.ModelViewSet):
    queryset = JobSkill.objects.all()
    serializer_class = JobSkillSerializer
    permission_classes = [IsAuthenticated]


class JobMediaViewSet(viewsets.ModelViewSet):
    queryset = JobMedia.objects.all()
    serializer_class = JobMediaSerializer
    permission_classes = [IsAuthenticated]


class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_classes = [IsAuthenticated]


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class MentorStatusRequestViewSet(viewsets.ModelViewSet):
    queryset = MentorStatusRequest.objects.all()
    serializer_class = MentorStatusRequestSerializer
    permission_classes = [IsAuthenticated]


class MentorshipRequestViewSet(viewsets.ModelViewSet):
    queryset = MentorshipRequest.objects.all()
    serializer_class = MentorshipRequestSerializer
    permission_classes = [IsAuthenticated]


class EndorsementViewSet(viewsets.ModelViewSet):
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer
    permission_classes = [IsAuthenticated]


class MentorshipWorkViewSet(viewsets.ModelViewSet):
    queryset = MentorshipWork.objects.all()
    serializer_class = MentorshipWorkSerializer
    permission_classes = [IsAuthenticated]


class FeaturedCourseViewSet(viewsets.ModelViewSet):
    queryset = FeaturedCourse.objects.all()
    serializer_class = FeaturedCourseSerializer
    permission_classes = [IsAuthenticated]
