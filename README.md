# AI Stock Helper for Dev

인공지능을 이용한 주식 자동 매매 프로젝트 (2021-06-08 ~ )



### 실행 환경 구축

주식 조회 서버, 주식 매매 서버가 따로 구성

#### Window 환경

- Windows 10 Home
- Docker

#### Docker 환경

- PostgreSQL DB, Local 저장소

#### Anaconda 가상 환경

- python 3.9
- fastapi, uvicorn, sqlalchemy, psycopg2

#### IDE 환경

- Visual studio code - python, pylance, autopep8



### 실행 코드

- 최상위 프로젝트 폴더에서 다음 코드 실행

  `uvicorn app.main:app --host=localhost --port=7000 --workers=4 --reload`



### 소스 코드

- Postgres

```bash
$ docker volume create pgdata # 볼륨 생성

$ docker run -p 5432:5432 --name Postgres -e POSTGRES_PASSWORD=rlaguscjf -d -v pgdata:/var/lib/postgresql/data postgres # docker run 에 pgdata 마운트

$ docker ps -a

$ docker exec -it Postgres /bin/bash
-> $ winpty docker exec -it Postgres bash

# 볼륨 확인
$ docker volume inspect pgdata
```
```bash
psql -U postgres

# postgresql 유저 확인
SELECT * FROM PG_USER;

------------------- 설정 추가 -------------------------------

$ su - postgres
$ psql --username=postgres --dbname=postgres

CREATE ROLE [username] LOGIN SUPERUSER CREATEDB REPLICATION PASSWORD "password"


```



### GitHub Repository 수정 사항

- `git flow init` 을 통해 참고 문헌에 따라 Git Flow 를 관리

- Issue Template, Label, Milestone 등록, (2021-06-09)



### 참고

- 프로젝트 참고 자료

  [[인공지능 주식매매] 용도별 증권사 API 추천](https://ai-trader.tistory.com/49)

- 환경설정 관련 자료

  [Git-flow, 우아한형제들 기술 블로그](https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)

  [Windows 10 home docker WSL2 installation 에러 해결 방법](https://blog.nachal.com/1691)
  
- PostgreSQL Container 설치

  [Docker Postgresql 설치 및 셋팅하기](https://judo0179.tistory.com/96?category=281955)
  
- 파이썬, 에러 처리 및 참고 자료

  [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

  [[Python] 패키지 생성과 import](https://velog.io/@sji7532/Python-%ED%8C%A8%ED%82%A4%EC%A7%80-%EC%83%9D%EC%84%B1%EA%B3%BC-import)

  [Lazy Loading & Caching in ORM](https://velog.io/@minho/Lazy-Loading-Caching-in-ORM)

  [FastAPI import error](https://stackoverflow.com/questions/60819376/fastapi-throws-an-error-error-loading-asgi-app-could-not-import-module-api)

  [Python import error](https://naon.me/posts/til26)

