# sourcery skip: raise-specific-error
import os
import sys
import warnings
from shutil import copyfile

import bentoml
import joblib
import numpy as np
import pandas as pd

from src.common.constants import ARTIFACT_PATH, DATA_PATH, LOG_FILEPATH
from src.common.logger import (
    handle_exception,
    set_logger,
)
from src.common.metrics import rmse_cv_score
from src.common.utils import get_param_set
from src.preprocess import preprocess_pipeline

logger = set_logger(os.path.join(LOG_FILEPATH, "logs.log"))
sys.excepthook = handle_exception
warnings.filterwarnings(action="ignore")


if __name__ == "__main__":
    train_df = pd.read_csv(os.path.join(DATA_PATH, "house_rent_test.csv")).drop(
        ["id"], axis=1
    )
    logger.debug("Load data")

    X = train_df.drop(["rent"], axis=1)
    y = np.log1p(train_df["rent"])

    # Data storage - 피처 데이터 저장
    if not os.path.exists(os.path.join(DATA_PATH, "storage")):
        os.makedirs(os.path.join(DATA_PATH, "storage"))
    X.assign(rent=y).to_csv(
        os.path.join(DATA_PATH, "storage", "house_rent_train_features.csv"),
        index=False,
    )

    # 기존 모델 백업
    logger.info("Backup the previous model...")
    copyfile(
        os.path.join(ARTIFACT_PATH, "model.pkl"),
        os.path.join(ARTIFACT_PATH, "model.pkl.bak"),
    )
    model = joblib.load(os.path.join(ARTIFACT_PATH, "model.pkl"))
    logger.info("Fit the model...")
    model.fit(X, y)

    logger.info("Save the model...")
    joblib.dump(model, os.path.join(ARTIFACT_PATH, "model.pkl"))
    
    bentoml.sklearn.save_model(
        name="house_rent",
        model=model,
        signatures={"predict": {"batchable": True, "batch_dim": 0}},
    )
