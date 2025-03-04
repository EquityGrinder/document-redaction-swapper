import os
import shutil
import pytest
from document_redaction_swapper.document_redaction_swapper import DocumentRedactionSwapper

def test_main():
    # Initialize the DocumentRedactionSwapper
    drs = DocumentRedactionSwapper()
    
    # Perform the swap
    drs.swap()
    
    # Check if the swapped_docs directory is created
    swapped_docs_path = os.path.join("data/swapped_docs")
    assert os.path.exists(swapped_docs_path)


def test_project():
    drs = DocumentRedactionSwapper(path="Z:\\Nachbereitung\\Sonderprozess\\Public Bilder Türkei" , 
                                   placeholder="Z:\\Nachbereitung\\Sonderprozess\\Public Bilder Türkei\\placeholder\\placeholder.pdf")
    drs.swap()
