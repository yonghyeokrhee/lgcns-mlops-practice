## 배치 추론 코드 쉘 스크립트

```bash
# batch_prediction.sh
BASH_ENV=~/.bashrc
ROOT_PATH=/workspaces/lgcns-mlops-practice
PIPENV_PIPFILE=$ROOT_PATH/Pipfile

export PATH=$PATH:/usr/local/py-utils/bin
export PIPENV_PIPFILE=$PIPENV_PIPFILE
pipenv run python $ROOT_PATH/batch_prediction.py >> $ROOT_PATH/cron.log 2>&1
```

## BentoML 서비스 설정 YAML

```yaml
# bentofile.yaml
service: "service.py:svc"
include:
  - "service.py"
python:
  requirements_txt: “./requirements.txt"

# requirements.txt
bentoml>=1.0.0
scikit-learn
```

## BentoML 서빙 실습 시 입력값

```python
{
  "bhk": 2,
  "size": 1000,
  "floor": "Ground out of 2",
  "area_type": "Super Area",
  "city": "Chennai",
  "furnishing_status": "Unfurnished",
  "tenant_preferred": "Bachelors/Family",
  "bathroom": 2,
  "point_of_contact": "Contact Owner"
}
```