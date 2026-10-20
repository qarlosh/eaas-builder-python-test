import platform
import sys
from importlib.metadata import version

from connect.eaas.core.decorators import schedulable
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import ScheduledExecutionResponse


PACKAGE = 'eaas-builder-python-test'


def python_check_message():
    return (
        f'PYTHON-CHECK version={version(PACKAGE)} '
        f'python={platform.python_version()} '
        f'executable={sys.executable} '
        f'sys.version={sys.version!r}'
    )


class EaasBuilderPythonTestEventsApplication(EventsApplicationBase):
    @schedulable(
        'Python check',
        'Logs (level ERROR) the extension version and the Python version it runs on.',
    )
    def python_check(self, schedule):
        # ERROR so it shows up whatever the environment's log level is.
        self.logger.error(python_check_message())
        return ScheduledExecutionResponse.done()

