"""Classes for melon orders."""
from random import randint


class AbstractMelonOrder(object):
    """ An abstract base class that other Melon Orders inherit from. """

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):

        self.base_price = randint(5, 9)
        return self.base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "christmas melons":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, order_type, tax):
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, order_type, tax, country_code):
        """ A melon order outside the USA. """

        super(InternationalMelonOrder, self).__init__(species, qty, 'international', 0.17)

        country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order purchased by the US Government."""

    def __init__(self, species, qty, order_type, tax):
        super(GovernmentMelonOrder, self).__init__(species, qty, 'government', 0)

        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        return self.passed_inspection
