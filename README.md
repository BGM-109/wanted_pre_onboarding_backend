# wanted_pre_onboarding

과제 링크 
https://docs.google.com/document/d/1Wu429EZ9tR72ITb5u_5wCfw8s5_U_07a01rWEFZiKyQ/edit


# 🔆 과제설명
-   아래 서비스 개요 및 요구사항을 만족하는 Backend 시스템을 구현합니다. 
 - [x] 예 
 - [ ] 아니오
- Django 또는 Flask 를 사용하여 구현합니다.
 - [x] Django
 - [ ] Flask
# ⛈️ 서비스 개요
-   본 서비스는 크라우드 펀딩 기능을 제공합니다. 게시자는 크라우드 펀딩을 받기위한 상품(=게시물)을 등록합니다.
- 유저는 해당 게시물의 펀딩하기 버튼을 클릭하여 해당 상품 ‘1회펀딩금액’ 만큼 펀딩합니다.

# 🌈 요구사항
- **상품을 등록합니다.**
	- 제목, 게시자명, 상품설명, 목표금액, 펀딩종료일, 1회펀딩금액로 구성. 
-   **상품을 수정합니다.**
	-   단, 모든 내용이 수정 가능하나 '목표금액'은 수정이 불가능합니다.
-   **상품을 삭제합니다.**
	-   DB에서 삭제됩니다.
-   **상품 목록을 가져옵니다.**
	-   제목, 게시자명, 총펀딩금액, 달성률 및 D-day(펀딩 종료일까지) 가 포함되어야 합니다.
-   **상품 검색 기능 구현**
	-   (상품 리스트 API 에 ?search=취미 조회 시 ,제목에 ‘내 취미 만들..’ ‘취미를 위한 ..’ 등 검색한 문자 포함된 상품 리스트만 조회)
-   **상품 정렬 기능 구현**
	-   생성일기준, 총펀딩금액 두 가지 정렬이 가능해야합니다.
	-   ?order_by=생성일 / ?order_by=총펀딩금액
	-   (달성률: 1,000,000원 목표금액 일때, 총 펀딩금액이 5,000,000원 이면 500%, 소수점 무시)
-   **상품 상세 페이지를 가져옵니다.**
	-   제목, 게시자명, 총펀딩금액, 달성률, D-day(펀딩 종료일까지), 상품설명, 목표금액 및 참여자 수 가 포함되어야 합니다.
# 🌪️ 필수 기술요건
-   Django ORM or SQLAlchemy 등 ORM을 사용하여 구현.
-   REST API 로 구현.
-   RDBMS 사용 (SQLite, PostgreSQL 등).
-   Backend 이외의 요소 개발 하지 않음(html, css, js 등).
# ⚡ 평가 요소
-   코드 효율성
-   모델링
-   요구사항 구현정도
-   REST API 설계 적합성
-   코드 가독성 및 코드 컨벤션

# 💭 가산점 요소
-   Unit Test 구현
-   README 에 요구사항 분석 및 구현 과정을 작성
-   Git commit 메시지 컨벤션
