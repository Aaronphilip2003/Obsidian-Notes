
- `pip install poetry`
- Navigate to /backend/app and run `poetry install`
- run `deactivate` to get out of the venv
- `docker-compose up -d`
- `docker-compose exec backend bash`

## **Backend Tests**

- `pip install coverage`
- `pip install pytest-cov`
- `sh ./scripts/test.sh`
- `pip install redis`
- delete the `test_celery.py` located in `/app/tests/api/api_v1`

now run ` docker-compose exec backend bash /app/tests-start.sh --cov-report=html`

and if the backend is running properly then it will generate an html report 

![[Pasted image 20240113013547.png]]
![[Pasted image 20240113013557.png]]
![[Pasted image 20240113013606.png]]
