from django.db import models
import pycountry


class Address(models.Model):
    """A postal address.

    I opted for adding a title to the address to make it easier to identify
    (common practice in, for example, food delivery apps).

    Since our application has to manage addresses from a variety of countries,
    I took a very conservative approach and added a multitude of fields such as
    state/province and two address lines.

    Also, I embedded the country-state-zip-city four-tuple in this model,
    although, one could argue that it should be represented separately. Since
    our application is a simple one, I wanted to go with a simpler approach.
    """

    COUNTRIES = [(country.alpha_2, country.name) for country in pycountry.countries]

    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100)

    country = models.CharField(choices=COUNTRIES, max_length=2)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100)
