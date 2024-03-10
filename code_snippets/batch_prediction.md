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