import pytest
from datetime import datetime
from pathlib import Path

def pytest_configure(config):
    """
    Dynamically sets the JUnit XML report path to include a timestamp.

    This hook is called by pytest after command-line options are parsed.
    It checks if a path for the XML report has been set. If not, it creates
    a timestamped filename and ensures the 'reports' directory exists.
    """
    if not config.option.xmlpath:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        reports_dir = Path("reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = reports_dir / f"report-{timestamp}.xml"
        config.option.xmlpath = str(report_path)