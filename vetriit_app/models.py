from django.db import models
from django.utils.text import slugify

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=255, default="Vetri IT")
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)

    def __str__(self):
        return self.site_title

class logo(models.Model):
    image = models.ImageField(upload_to='logos/', null=True, blank=True)
    alt_text = models.CharField(max_length=100, default='Vetri IT Systems Logo')

    def __str__(self):
        return self.alt_text
    
class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    service = models.CharField(max_length=100)  # "Web Development", "Software Development", "Digital Marketing"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.service}"
    
class Footer(models.Model):
    logo = models.ImageField(upload_to='footer/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='footer_videos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    section_four_heading = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Footer Section"
    
class FooterIcon(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="icons")
    icon_class = models.CharField(max_length=100, help_text="Example: fa-brands fa-whatsapp")
    link = models.URLField(max_length=500, help_text="Add the URL (e.g. https://wa.me/8438558627)")

    def __str__(self):
        return self.icon_class
    
    @property
    def resolved_link(self):
        if 'whatsapp' in self.icon_class.lower():
            # Remove spaces and special chars, build wa.me link
            num = ''.join(filter(str.isdigit, self.link))
            return f"https://wa.me/{num}"
        return self.link
    
class AboutContent(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading


class AboutFeature(models.Model):
    icon = models.ImageField(upload_to='about/icons/', null=True, blank=True)
    heading = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading
    
class DesignServiceSectionOne(models.Model):
    heading = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='design_services/', null=True, blank=True)
    def __str__(self):
        return self.heading
    
class DesignServiceSectionTwo(models.Model):
    icon_class = models.CharField(max_length=100, help_text='Ex: fa-solid fa-lightbulb')
    heading = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.heading

class DesignServiceSectionThree(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.heading)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.heading


class DesignServiceSectionThreeBox(models.Model):
    section = models.ForeignKey(DesignServiceSectionThree, on_delete=models.CASCADE, related_name='boxes')
    image = models.ImageField(upload_to='design_section3/images/', blank=True, null=True)
    icon_class = models.CharField(max_length=100,help_text='Ex: fa-solid fa-gear or fa-brands fa-figma',blank=True,null=True)
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading

class WebsiteDevelopmentSectionOne(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='website_development/', blank=True, null=True)

    def __str__(self):
        return self.heading

class WebsiteDevelopmentSectionTwo(models.Model):
    icon_class = models.CharField(max_length=100, help_text="Ex: fa-solid fa-laptop-code")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class WebsiteDevelopmentSectionThree(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading


class WebsiteDevelopmentSectionThreeBox(models.Model):
    section = models.ForeignKey(WebsiteDevelopmentSectionThree, on_delete=models.CASCADE, related_name='boxes')
    video = models.FileField(upload_to='webdev/videos/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    points = models.TextField(help_text="Add one point per line", blank=True)

    def get_points_list(self):
        return self.points.splitlines()

    def __str__(self):
        return self.title

class WebsiteDevelopmentSectionFour(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading


class WebsiteDevelopmentSectionFourBox(models.Model):
    section = models.ForeignKey(WebsiteDevelopmentSectionFour, on_delete=models.CASCADE, related_name="boxes")
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=50)

    gradient_start = models.CharField(max_length=20, help_text="Example: #0A933C")
    gradient_end = models.CharField(max_length=20, help_text="Example: #88FF88")

    features = models.TextField(help_text="Write points line by line")

    def features_list(self):
        return self.features.split("\n")

    def __str__(self):
        return self.title

class SoftwareDevelopmentSectionOne(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="software_dev/")

    def __str__(self):
        return self.heading

class SoftwareDevelopmentSectionTwo(models.Model):
    icon_class = models.CharField(max_length=100, help_text="Ex: fa-solid fa-code")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class SoftwareDevelopmentSectionThree(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading


class SoftwareDevelopmentSectionThreeBox(models.Model):
    section = models.ForeignKey(SoftwareDevelopmentSectionThree, on_delete=models.CASCADE, related_name="boxes")
    icon_class = models.CharField(max_length=100, help_text="Ex: fa-solid fa-code")
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="software_section_three/", blank=True, null=True)

    def __str__(self):
        return f"{self.title_one} {self.title_two}"

class HomeSectionOne(models.Model):
    heading = models.CharField(max_length=255)
    desc1 = models.CharField(max_length=255, blank=True, null=True)
    desc2 = models.CharField(max_length=255, blank=True, null=True)
    desc3 = models.CharField(max_length=255, blank=True, null=True)
    button_text = models.CharField(max_length=50, default="Enquiry Now")
    image = models.ImageField(upload_to="home/section_one/", blank=True, null=True)

    def __str__(self):
        return self.heading

class HomeSectionTwo(models.Model):
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title_one} {self.title_two}"


class HomeSectionTwoBox(models.Model):
    section = models.ForeignKey(HomeSectionTwo, on_delete=models.CASCADE, related_name="boxes")
    image = models.ImageField(upload_to="homesectiontwo/")

    def __str__(self):
        return f"Box for {self.section.title_one}"

class HomeSectionThree(models.Model):
    black_title = models.CharField(max_length=255)
    green_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.black_title} {self.green_title}"


class HomeSectionThreeBox(models.Model):
    section = models.ForeignKey(HomeSectionThree, on_delete=models.CASCADE, related_name='boxes')
    icon_class = models.CharField(max_length=100, help_text="Ex: fa-solid fa-lightbulb")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class HomeSectionFour(models.Model):
    black_title = models.CharField(max_length=255)
    green_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.black_title} {self.green_title}"


class HomeSectionFourServiceBox(models.Model):
    section = models.ForeignKey(HomeSectionFour, on_delete=models.CASCADE, related_name='service_boxes')
    image = models.ImageField(upload_to='section4_images/')
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    points = models.TextField(help_text="Enter each point on a new line")

    def point_list(self):
        return [point.strip() for point in self.points.split('\n') if point.strip()]

    def __str__(self):
        return self.heading

class HomeSectionFive(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading


class HomeSectionFiveReviewCard(models.Model):
    icon = models.ImageField(upload_to='review_icons/', help_text="Client/Reviewer profile picture or logo")
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, default='Unknown Company')
    description = models.TextField()
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    
    class Meta:
        verbose_name = "Review Box"
        verbose_name_plural = "Review Boxes (Section Five)"
        ordering = ['id']
        
    def __str__(self):
        return f"Review by {self.name} ({self.rating} stars)"

class HomeSectionSix(models.Model):
    heading = models.CharField(max_length=255)

    def __str__(self):
        return self.heading


class HomeSectionSixTab(models.Model):
    section = models.ForeignKey(HomeSectionSix, on_delete=models.CASCADE, related_name='tabs')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class HomeSectionSixImage(models.Model):
    tab = models.ForeignKey(HomeSectionSixTab, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='home/section6/')

    def __str__(self):
        return f"{self.tab.title} - Image"

class HomeSectionSeven(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading


class HomeSectionSevenBox(models.Model):
    section = models.ForeignKey(HomeSectionSeven, on_delete=models.CASCADE, related_name="boxes")
    question = models.CharField(max_length=255)
    answer = models.TextField()
    icon_open_class = models.CharField(max_length=100, help_text='Ex: fa-solid fa-plus')
    icon_close_class = models.CharField(max_length=100, help_text='Ex: fa-solid fa-minus')

    def __str__(self):
        return self.question
