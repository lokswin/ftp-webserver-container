import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a custom authorizer
authorizer = DummyAuthorizer()
authorizer.add_anonymous("website", perm="elradfmwMT")  # Corrected folder path


# Configure the FTP server
handler = FTPHandler
handler.authorizer = authorizer
handler.passive_ports = range(30000, 30009)

server = FTPServer(("0.0.0.0", 21), handler)

# Start the FTP server
try:
    logger.info("FTP server started")
    server.serve_forever()
except Exception as e:
    logger.error("Error: %s" % str(e))
