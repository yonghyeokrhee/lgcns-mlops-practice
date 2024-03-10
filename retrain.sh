BASH_ENV=~/.bashrc
ROOT_PATH=/workspaces/lgcns-mlops-practice


CONCEPT_DRIFT_TEST=$(cat ${ROOT_PATH}/prediction_drift.json | jq '.Status')
echo $CONCEPT_DRIFT_TEST

if [ $CONCEPT_DRIFT_TEST = '"FAIL"' ]; then
    $ROOT_PATH/.venv/bin/python $ROOT_PATH/retrain.py >> $ROOT_PATH/retrain.log 2>&1
fi
