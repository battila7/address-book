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
    even though it somewhat violates DB normalization rules. Since
    our application is a simple one, I wanted to go with the simplest approach
    possible, which was definitely denormalization and plain text fields.

    Considering the duplicates requirement: I added a unique constraint on the
    title and a separate one the remaining address-locating fields.

    The 100 max_length is completely arbitrary, in this case, it really does not
    matter that much. The key is the use of a CharField, as it is handled differently
    (and more efficiently) thank a TextField.
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

    owner = models.ForeignKey(
        "auth.User", related_name="addresses", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [
            [
                "owner",
                "title",
            ],
            # We don't need to consider the title attribute, as it
            # has its own unique constraint.
            [
                "owner",
                "country",
                "state",
                "zip_code",
                "city",
                "address_line_one",
                "address_line_two",
            ],
        ]
