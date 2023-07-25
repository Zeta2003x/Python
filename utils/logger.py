import logging

logname = 'logger.txt'

logging.basicConfig(filename=logname,
                    filemode='a',
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Test message.")