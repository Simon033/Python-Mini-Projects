from decimal import Decimal, getcontext, localcontext

class GaussLegendre:
    """
    A class to calculate the value of pi using the Gauss-Legendre algorithm.
    """

    def __init__(self, iterations=100):
        """
        Initialize the GaussLegendre object.

        Args:
            iterations (int, optional): The number of iterations to perform. Defaults to 100.
        """
        self.iterations = iterations

    def calculate_pi(self):
        """
        Calculate the value of pi using the Gauss-Legendre algorithm.

        Returns:
            Decimal: An approximation of pi.
        """
        # Set the precision to a higher value
        getcontext().prec = self.iterations + 2  # Add extra digits for precision

        # Initial values for a, b, t, p
        a = Decimal('1.0')
        b = Decimal('1.0') / (Decimal('2')).sqrt()  # Use Decimal.sqrt() method
        t = Decimal('0.25')
        p = Decimal('1.0')

        for _ in range(self.iterations):
            a_next = (a + b) / Decimal('2')
            b = (a * b).sqrt()  # Use Decimal.sqrt() method
            t -= p * (a - a_next) ** 2
            a = a_next
            p *= Decimal('2')

        pi_approx = (a + b) ** 2 / (Decimal('4') * t)
        return pi_approx

class PiCalculator:
    """
    A class to calculate an approximation of pi using the Gauss-Legendre algorithm.
    """

    def __init__(self, iterations=100, precision=1000000):
        """
        Initialize the PiCalculator object.

        Args:
            iterations (int, optional): The number of iterations to perform in the Gauss-Legendre algorithm. Defaults to 100.
            precision (int, optional): The number of digits to use for the precision of the pi approximation. Defaults to 1000000 (1 million digits).
        """
        self.iterations = iterations
        self.precision = precision

    def calculate_pi(self):
        """
        Calculate an approximation of pi using the Gauss-Legendre algorithm.

        Returns:
            Decimal: An approximation of pi with the specified precision.
        """
        gauss_legendre = GaussLegendre(self.iterations)
        with localcontext() as ctx:
            ctx.prec = self.precision
            pi_approx = gauss_legendre.calculate_pi()
        return pi_approx

if __name__ == "__main__":
    pi_calculator = PiCalculator(iterations=100, precision=1000000)
    approximated_pi = pi_calculator.calculate_pi()
    print("Approximated pi:\n", approximated_pi)