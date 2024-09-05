from django.db import models


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=1024)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Profile(models.Model):
    title = models.CharField(max_length=1024)
    user = models.OneToOneField('Account.User', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Social(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=1024)
    school = models.CharField(max_length=1024)
    field_of_study = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    media = models.FileField(upload_to='education_media/', blank=True)

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=1024)
    company = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class ExperienceMedia(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    media = models.FileField(upload_to='experience_media/')

    def __str__(self):
        return self.experience.title

    class Meta:
        verbose_name = 'Experience Media'
        verbose_name_plural = 'Experience Media'


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    description = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    media = models.FileField(upload_to='project_media/', blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media = models.FileField(upload_to='project_media/')

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = 'Project Media'
        verbose_name_plural = 'Project Media'


class Certificate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    organization = models.CharField(max_length=1024)
    description = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    media = models.FileField(upload_to='certificate_media/', blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certifications'


class Job(models.Model):
    title = models.CharField(max_length=1024, verbose_name="Job Title/Position")
    company = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024)
    type = models.CharField(max_length=1024, choices=((
        ("internship", "Internship"),
        ("part_time", "Part Time"),
        ("full_time", "Full Time"),
        ("contract", "Contract"),
        ("temporary", "Temporary"),
        ("volunteer", "Volunteer"),
        ("remote", "Remote"),
    )))
    salary = models.CharField(max_length=1024, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    working_hours = models.CharField(max_length=1024, blank=True, null=True)
    requirements = models.TextField(max_length=500, blank=True)
    responsibilities = models.TextField(max_length=500, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Skill'
        verbose_name_plural = 'Job Skills'


class JobMedia(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    media = models.FileField(upload_to='job_media/')

    def __str__(self):
        return self.job.title

    class Meta:
        verbose_name = 'Job Media'
        verbose_name_plural = 'Job Media'


class JobListing(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='employer')
    recruiter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recruiter', blank=True, null=True)
    status = models.CharField(max_length=1024, choices=(
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
        ('closed', 'Closed')
    ), default='upcoming')
    start_date = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return self.job.title

    class Meta:
        verbose_name = 'Job Listing'
        verbose_name_plural = 'Job Listings'


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cover_letter = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1024, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ), default='pending')
    custom_status = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.job.title

    class Meta:
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'


class Course(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    organization = models.CharField(max_length=1024)
    description = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    certificate = models.FileField(upload_to='course_media/', blank=True)
    verification_status = models.CharField(max_length=1024, choices=(
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected')
    ), default='pending')
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class MentorStatusRequest(models.Model):
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentor')
    status = models.CharField(max_length=1024, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ), default='pending')
    message = models.TextField(max_length=500, blank=True, null=True)
    response = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mentor.user.username

    class Meta:
        verbose_name = 'Mentor Status Request'
        verbose_name_plural = 'Mentor Status Requests'


class MentorshipRequest(models.Model):
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentor_request')
    mentee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentee_request')
    status = models.CharField(max_length=1024, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ), default='pending')
    message = models.TextField(max_length=500, blank=True, null=True)
    response = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mentor.user.username

    class Meta:
        verbose_name = 'Mentorship Request'
        verbose_name_plural = 'Mentorship Requests'


class Endorsement(models.Model):
    endorser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='endorser')
    endorsee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='endorsee')
    skill = models.ManyToManyField(Skill, blank=True)
    message = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.endorser.user.username

    class Meta:
        verbose_name = 'Endorsement'
        verbose_name_plural = 'Endorsements'


class MentorshipWork(models.Model):
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentor_work')
    mentee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentee_work')
    title = models.CharField(max_length=1024)
    description = models.TextField(max_length=500, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    media = models.FileField(upload_to='mentorship_work_media/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mentorship Work'
        verbose_name_plural = 'Mentorship Works'


class FeaturedCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=1024)
    level = models.CharField(max_length=1024, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ))
    link = models.URLField(blank=True)
    media = models.FileField(upload_to='featured_course_media/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = 'Featured Course'
        verbose_name_plural = 'Featured Courses'


