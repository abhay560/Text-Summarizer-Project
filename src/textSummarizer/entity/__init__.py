from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_files: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list



@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenzier_name: Path