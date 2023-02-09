from pydantic import BaseModel
from typing import List 

class ParserFileMeta(BaseModel): 
    # attempt some basic interoperability with https://github.com/marda-alliance/metadata_extractors_schema/blob/main/schemas/base.yaml
    id: str
    name: str
    subject: List[str]
    description: str
    extension: str

    # For experimental data
    associated_vendors: List[str]
    associated_instruments: List[str]
    associated_software: List[str]

    source_repository: str

class ParserCodeMeta(BaseModel):
    # For the parser code
    language: str 
    source_repository: str 
    license: str 
    version: str