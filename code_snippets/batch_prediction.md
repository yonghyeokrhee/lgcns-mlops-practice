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