from abc import ABC,abstractmethod
class Document:
    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass

# Concrete implementation of Printable
class PDFPrinter(Printable):
    def print(self, document):
        print("Printing PDF:", document.get_content())

class InkjetPrinter(Printable):
    def print(self, document):
        print("Printing via Inkjet:", document.get_content())