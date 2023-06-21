from dataclasses import dataclass
from pathlib import Path

#Here is to create the entity - entity is providing the output-return type of the funtions
@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data Ingestion Configuration
    """
    root_dit: Path
    source_URL: str
    local_data_file : Path
    unzip_dir : Path