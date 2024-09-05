from django.db import models


# Create your models here.

class Skill(models.Model):
    """
       Model representing a user's skill.

       Fields:
           name (str): The name of the skill (e.g., 'Python').
           level (int): Proficiency level of the skill (e.g., 1 for beginner).

       Meta:
           verbose_name (str): 'Skill'.
           verbose_name_plural (str): 'Skills'.
       """
    name = models.CharField(max_length=1024)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Profile(models.Model):
    """
       Model representing a user's profile.

       Fields:
           title (str): A title for the profile (e.g., 'Software Engineer').
           user (OneToOneField): One-to-one relationship with the User model.
           bio (str): A short biography or description of the user.
           location (str): The user's location.
           birth_date (date): The user's birth date.
           phone (str): The user's phone number.
           website (URLField): The user's website URL.
           image (ImageField): Profile picture.
           skills (ManyToManyField): Relationship with the Skill model.
           created_at (datetime): When the profile was created.
           updated_at (datetime): When the profile was last updated.

       Meta:
           verbose_name (str): 'Profile'.
           verbose_name_plural (str): 'Profiles'.
       """
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
    """
        Model representing a user's social media link.

        Fields:
            profile (ForeignKey): Foreign key to the Profile model.
            name (str): Name of the social platform (e.g., 'LinkedIn').
            url (URLField): URL of the social profile.

        Meta:
            verbose_name (str): 'Social'.
            verbose_name_plural (str): 'Socials'.
        """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'


class Education(models.Model):
    """
        Model representing a user's education.

        Fields:
            profile (ForeignKey): Foreign key to the Profile model.
            degree (str): The degree obtained (e.g., 'BSc Computer Science').
            school (str): Name of the educational institution.
            field_of_study (str): The user's field of study (e.g., 'Computer Science').
            start_date (date): Start date of the education.
            end_date (date, nullable): End date of the education.
            description (TextField, optional): Description about the education.
            media (FileField, optional): Optional file (e.g., certificate).

        Meta:
            verbose_name (str): 'Education'.
            verbose_name_plural (str): 'Educations'.
        """
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
    """
       Model representing a user's professional experience.

       Fields:
           profile (ForeignKey): Foreign key to the Profile model.
           position (str): The position held (e.g., 'Software Developer').
           company (str): Name of the company.
           location (str): Location of the company.
           start_date (date): Start date of the job.
           end_date (date, nullable): End date of the job.
           description (TextField): Description of the role and responsibilities.
           skills (ManyToManyField): Relationship with the Skill model.

       Meta:
           verbose_name (str): 'Experience'.
           verbose_name_plural (str): 'Experiences'.
       """
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
    """
        Model representing media related to a user's experience.

        Fields:
            experience (ForeignKey): Foreign key to the Experience model.
            media (FileField): A file associated with the experience.

        Meta:
            verbose_name (str): 'Experience Media'.
            verbose_name_plural (str): 'Experience Media'.
        """
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    media = models.FileField(upload_to='experience_media/')

    def __str__(self):
        return self.experience.title

    class Meta:
        verbose_name = 'Experience Media'
        verbose_name_plural = 'Experience Media'


class Project(models.Model):
    """
        Model representing a user's project.

        Fields:
            profile (ForeignKey): Foreign key to the Profile model.
            title (str): The title of the project.
            description (TextField): A brief description of the project.
            link (URLField, optional): Optional URL linking to the project.
            start_date (date): Start date of the project.
            end_date (date, nullable): End date of the project.
            media (FileField, optional): Media file related to the project.
            skills (ManyToManyField): Relationship with the Skill model.

        Meta:
            verbose_name (str): 'Project'.
            verbose_name_plural (str): 'Projects'.
        """
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
    """
        Model representing media files related to a user's project.

        Fields:
            project (ForeignKey): Foreign key to the Project model.
            media (FileField): A file associated with the project.

        Meta:
            verbose_name (str): 'Project Media'.
            verbose_name_plural (str): 'Project Media'.
        """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media = models.FileField(upload_to='project_media/')

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = 'Project Media'
        verbose_name_plural = 'Project Media'


class Certificate(models.Model):
    """
        Model representing a user's certification.

        Fields:
            profile (ForeignKey): Foreign key to the Profile model.
            title (str): The name of the certificate.
            organization (str): Organization issuing the certificate.
            description (TextField, optional): Optional description of the certificate.
            link (URLField, optional): Optional link to the certificate.
            issue_date (date): Date the certificate was issued.
            expiration_date (date, nullable): Expiry date of the certificate.
            media (FileField, optional): Certificate file.
            skills (ManyToManyField): Relationship with the Skill model.

        Meta:
            verbose_name (str): 'Certificate'.
            verbose_name_plural (str): 'Certifications'.
        """

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
    """
        Model representing a job posting.

        Fields:
            title (str): The title of the job (e.g., 'Software Engineer').
            company (str): Name of the company offering the job.
            location (str): Location of the job.
            type (str): Job type (e.g., internship, part-time, full-time).
            salary (DecimalField, optional): Optional salary for the job.
            start_date (date): Start date of the job.
            end_date (date, nullable): End date of the job.
            description (TextField): Description of the job role.
            working_hours (str, optional): Working hours for the job.
            requirements (TextField): Requirements for the job.
            responsibilities (TextField): Responsibilities for the job.
            skills (ManyToManyField): Relationship with the Skill model.

        Meta:
            verbose_name (str): 'Job'.
            verbose_name_plural (str): 'Jobs'.
        """
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
    """
        Model representing a specific skill required for a job.

        Fields:
            job (ForeignKey): Foreign key to the Job model.
            name (str): Name of the skill.
            level (int): Required proficiency level for the skill.

        Meta:
            verbose_name (str): 'Job Skill'.
            verbose_name_plural (str): 'Job Skills'.
        """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Skill'
        verbose_name_plural = 'Job Skills'


class JobMedia(models.Model):
    """
        Model representing media related to a job posting.

        Fields:
            job (ForeignKey): Foreign key to the Job model.
            media (FileField): Media file related to the job.

        Meta:
            verbose_name (str): 'Job Media'.
            verbose_name_plural (str): 'Job Media'.
        """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    media = models.FileField(upload_to='job_media/')

    def __str__(self):
        return self.job.title

    class Meta:
        verbose_name = 'Job Media'
        verbose_name_plural = 'Job Media'


class JobListing(models.Model):
    """
        Model representing a job listing.

        Fields:
            job (ForeignKey): Foreign key to the Job model.
            employer (ForeignKey): Profile of the employer.
            recruiter (ForeignKey, optional): Profile of the recruiter.
            status (str): Status of the job (e.g., upcoming, active, closed).
            start_date (date): Start date of the job listing.
            deadline (date): Application deadline for the job.

        Meta:
            verbose_name (str): 'Job Listing'.
            verbose_name_plural (str): 'Job Listings'.
        """
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
    """
        Model representing a user's job application.

        Fields:
            job (ForeignKey): Foreign key to the Job model.
            applicant (ForeignKey): Profile of the applicant.
            cover_letter (TextField, optional): Optional cover letter for the application.
            status (str): Status of the application (e.g., pending, accepted, rejected).
            custom_status (str, optional): Custom status for the application.

        Meta:
            verbose_name (str): 'Job Application'.
            verbose_name_plural (str): 'Job Applications'.
        """
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
    """
       Model representing a course taken by a user.

       Fields:
           profile (ForeignKey): Foreign key to the Profile model.
           title (str): Title of the course.
           organization (str): Organization offering the course.
           description (TextField): Description of the course.
           link (URLField, optional): Optional URL to the course.
           start_date (date): Start date of the course.
           end_date (date, nullable): End date of the course.
           certificate (FileField, optional): File of the certificate obtained from the course.
           verification_status (str): Status of the course (e.g., pending, verified, rejected).
           skills (ManyToManyField): Relationship with the Skill model.

       Meta:
           verbose_name (str): 'Course'.
           verbose_name_plural (str): 'Courses'.
       """
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
    """
        Model to store the status of a mentor request.

        Attributes:
            mentor (ForeignKey): A reference to the Profile of the mentor.
            status (CharField): The current status of the request (Pending, Accepted, Rejected). Defaults to 'pending'.
            message (TextField): Optional message from the mentee when requesting mentorship.
            response (TextField): Optional response from the mentor regarding the request.
            created_at (DateTimeField): Timestamp when the request was created. Automatically set at creation.
            updated_at (DateTimeField): Timestamp when the request was last updated. Automatically set at each update.

        Meta:
            verbose_name (str): Human-readable singular name for the model.
            verbose_name_plural (str): Human-readable plural name for the model.

        Methods:
            __str__(): Returns the mentor's username as a string representation of the object.
        """
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
    """
        Model to store requests for mentorship between a mentor and a mentee.

        Attributes:
            mentor (ForeignKey): A reference to the mentor's Profile.
            mentee (ForeignKey): A reference to the mentee's Profile.
            status (CharField): The current status of the mentorship request (Pending, Accepted, Rejected). Defaults to 'pending'.
            message (TextField): Optional message from the mentee.
            response (TextField): Optional response from the mentor.
            created_at (DateTimeField): Timestamp when the request was created.
            updated_at (DateTimeField): Timestamp when the request was last updated.

        Meta:
            verbose_name (str): Human-readable singular name for the model.
            verbose_name_plural (str): Human-readable plural name for the model.

        Methods:
            __str__(): Returns the mentor's username as a string representation of the object.
    """
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
    """
        Model to store endorsements given by users to each other for specific skills.

        Attributes:
            endorser (ForeignKey): The user providing the endorsement.
            endorsee (ForeignKey): The user receiving the endorsement.
            skill (ManyToManyField): The skill(s) for which the endorsement is made.
            message (TextField): Optional message for the endorsement.
            created_at (DateTimeField): Timestamp when the endorsement was created.
            updated_at (DateTimeField): Timestamp when the endorsement was last updated.

        Meta:
            verbose_name (str): Human-readable singular name for the model.
            verbose_name_plural (str): Human-readable plural name for the model.

        Methods:
            __str__(): Returns the endorser's username as a string representation of the object.
        """

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
    """
        Model to store the work done between a mentor and a mentee.

        Attributes:
            mentor (ForeignKey): A reference to the mentor's Profile.
            mentee (ForeignKey): A reference to the mentee's Profile.
            title (CharField): Title of the mentorship work.
            description (TextField): A brief description of the work.
            start_date (DateField): Date when the work started.
            end_date (DateField): Date when the work ended (optional).
            media (FileField): Optional media file associated with the work.

        Meta:
            verbose_name (str): Human-readable singular name for the model.
            verbose_name_plural (str): Human-readable plural name for the model.

        Methods:
            __str__(): Returns the title of the mentorship work as a string representation of the object.
        """
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
    """
        Model to store featured courses on the platform.

        Attributes:
            course (ForeignKey): A reference to the Course model.
            description (TextField): Brief description of the course.
            price (DecimalField): Price of the course.
            duration (CharField): Duration of the course.
            level (CharField): The course level (Beginner, Intermediate, Advanced).
            link (URLField): Optional URL link to the course.
            media (FileField): Optional media associated with the course.
            created_at (DateTimeField): Timestamp when the course was featured.
            updated_at (DateTimeField): Timestamp when the course information was last updated.

        Meta:
            verbose_name (str): Human-readable singular name for the model.
            verbose_name_plural (str): Human-readable plural name for the model.

        Methods:
            __str__(): Returns the course title as a string representation of the object.
        """
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
