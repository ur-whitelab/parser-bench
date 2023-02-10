from enum import Enum
from pathlib import Path
from typing import List, Optional

import requests
from loguru import logger
from pydantic import BaseModel, ValidationError, parse_file_as, validator


def check_link(link):
    response = requests.get(link)
    if response.status_code == 200:
        return True
    return False


class LanguageEnum(str, Enum):
    python = "python"
    javascript = "javascript"


class SubjectEnum(str, Enum):
    compchem = "compchem"
    exptchem = "exptchem"
    pore_analysis = "pore_analysis"
    regex = "regex"


class ParserFileMeta(BaseModel):
    """Metadataschema for parser input files

    Attempts to be lightweight but still ensure some basic
    interoperability with https://github.com/marda-alliance/metadata_extractors_schema/blob/main/schemas/base.yaml
    """

    id: str
    """Unique identifier of filetype"""

    name: str
    """Name of filetype"""

    subject: List[str]
    """Tags describing the use of this filetype"""

    description: str
    """Free-text description of how the file is produced and uses"""

    extension: str
    """File extension, must start with dot"""

    associated_software: List[str]
    """List of softwares that produce or read this filetype"""

    # For experimental data
    associated_vendors: Optional[List[str]]
    """For files created by analytical instruments: Name of the manufacturer"""

    associated_instruments: Optional[List[str]]
    """For files created by analytical instruments: Names/Serial numbers of the instruments"""

    references: Optional[List[str]]

    @validator("extension")
    def extension_must_start_with_dot(cls, v):
        assert v.startswith(".")


class ParserCodeMeta(BaseModel):
    # For the parser code
    language: LanguageEnum
    """Language the parser code is written in."""

    source_repository: str
    """Link to the source code repository that contains the code."""

    license: str
    """License identifier."""

    version: Optional[str]
    """Version identifier."""

    @validator("source_repository")
    def url_must_work(cls, v):
        if v is not None:
            if not check_link(v):
                raise ValidationError("Link to source repository must work")


def validate_directory(directory):
    # make sure we have "input" and "output" directories
    # make sure we have the same file stems in both directories
    base_directory = Path(directory)
    metafile = base_directory / "meta.json"
    if not metafile.exists():
        raise ValueError("Each directory must contain a meta.json file")

    parse_file_as(path=metafile, type_=ParserFileMeta)

    input_dir = base_directory / "inputs"
    output_dir = base_directory / "outputs"
    input_files = sorted(input_dir.glob('*'))
    output_files = sorted(output_dir.glob('*'))

    if len(input_files) != len(output_files):
        raise ValueError("Number of input files must equal the number of output files")

    for input_file, output_file in zip(input_files, output_files):
        if Path(input_file).stem != Path(output_file).stem:
            raise ValueError("Input and output files must share filestems.")
        if Path(output_file).suffix != ".json":
            raise ValueError("Output files must be in json format")

    # validate implementations if this exists
    implementations_dir = base_directory / "implementations"
    if implementations_dir.exists():
        parser_dirs = implementations_dir.glob("*")
        for parser_dir in parser_dirs:
            parser_code_meta_file = Path(parser_dir) / "meta.json"
            if not parser_code_meta_file.exists():
                parse_file_as(path=parser_code_meta_file, type_=ParserCodeMeta)

    return True


def validate_directories(basedir):
    basedir = Path(basedir)
    subdirs = basedir.glob('*')

    for subdir in subdirs:
        if not subdir.is_dir():
            logger.warning(f'File found at unexpected place {subdir}')
            continue
        logger.info(f'Validating {subdir}')
        validate_directory(subdir)
    
    return True