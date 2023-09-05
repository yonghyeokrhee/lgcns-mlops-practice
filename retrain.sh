BASH_ENV=~/.bashrc
ROOT_PATH=/workspaces/lgcns-mlops-practice
PIPENV_PIPFILE=$ROOT_PATH/Pipfile

export PATH=$PATH:/usr/local/py-utils/bin
export PIPENV_PIPFILE=$PIPENV_PIPFILE

CONCEPT_DRIFT_TEST=$(cat ${ROOT_PATH}/prediction_drift.json | jq '.Status')

if [ $CONCEPT_DRIFT_TEST = '"FAIL"' ]; then
    pipenv run python $ROOT_PATH/retrain.py >> $ROOT_PATH/retrain.log 2>&1
fi
