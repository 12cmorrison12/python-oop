"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Makes a new serial generator, starting at the start input."""
        self.start = self.next = start

    def __repr__(self):
        """Shows the representation logically."""
        return f"SerialGenerator(start={self.start} next={self.next})"

    def generate_num(self):
        """Returns the next serial number."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the generator to the original start number."""
        self.next = self.start