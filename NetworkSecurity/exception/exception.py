import sys
from typing import Any
from NetworkSecurity.my_logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_details: Any):
        super().__init__(error_message)
        self.error_message = error_message
        
        exc_type, exc_value, exc_tb = sys.exc_info()

        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            # fallback in case traceback not available
            self.lineno = "Unavailable"
            self.file_name = "Unknown File"

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"at line [{self.lineno}] "
            f"with message: {self.error_message}"
        )


if __name__ == "__main__":
    try:
        logger.logging.info("Testing NetworkSecurityException class...")
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(e, sys)
