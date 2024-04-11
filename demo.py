# from Diamond_price_predictions.pipline.training_pipeline import TrainPipeline


# pipline  = TrainPipeline()
# pipline.run_pipeline()

import sys
import os
from Diamond_price_predictions.logger import logging
from Diamond_price_predictions.exception import Diamond_PredictionException


#logging.info("Welcome to the customelogging")

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise Diamond_PredictionException(e, sys) from e 