import os
import shutil
from pydantic import BaseModel

class DocumentRedactionSwapper(BaseModel):
    """
    This class takes a path as a input and than redacts the document by swapping them with 
    a placeholder. This is useful when you want to share a document with someone but want to
    keep compliant.
    """

    path: str = "data/"
    placeholder: str = "data/placeholder/placeholder.pdf"
    __names: list[str] = []

    def swap(self):
        """
        This function swaps the document with the placeholder.
        """
        # create a new dir in self.path 
        self.__create_new_dir()
        self.__retrieve_document_names()
        self.__write_new_docs()

    def __create_new_dir(self):
        """
        This function creates a new directory in the path named 'swapped_docs'.
        """
        new_dir = os.path.join(self.path, 'swapped_docs')
        os.makedirs(new_dir, exist_ok=True)

    def __retrieve_document_names(self):
        """
        This function retrieves the document names in the path and list them in self.__names.
        """
        self.__names = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def __write_new_docs(self):
        """
        copies the self.placeholder file and renames it for every element in self.__names.
        """
        new_dir = os.path.join(self.path, 'swapped_docs')
        for name in self.__names:
            new_file_path = os.path.join(new_dir, name)
            shutil.copy(self.placeholder, new_file_path)
