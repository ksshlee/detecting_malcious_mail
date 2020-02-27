# cyber_sec_project

## 악성 메일 탐지 프로젝트

### 구현 언어

**Python 3**

### 사용한 기술 Stack

- python whois
- gmail 파싱
- 정규표현식
- virus total api
- json 파싱
- bs4 활용 웹 크롤링

### 데이터 수집
[https://www.alexa.com/](https://www.alexa.com/)

- top 50 웹사이트 정보 수집


### 프로젝트 Flow

![flow](/readmeFile/flow.png)

  
#### URL 검사 Flow

![flow](/readmeFile/flow2.png)

- 본문 URL 검사
  - 이메일 파싱 구현
  - 정규표현식 사용하여 URL 추출
  - 추출후 구현한 로직에 URL 전달

- 사용한 기술
  - python whois
  - 정규표현식
  - txt 파일 -> dic 으로 데이터화

##### URL 검사 기준

![flow](/readmeFile/flow3.png)

- 출처 : 인도 Anna 대학교 논문


#### 첨부파일 검사 Flow

![flow](/readmeFile/flow4.png)


- 사용한 기술
  - virustotal api
  - json 파싱

>결과 Example

![flow](/readmeFile/flow5.png)





### 실행전 주의사항
1. virusttotal api 사용기간 만료로 인한 추가 api 발급후 사용
2. 해당 계정 IMAP, POP 사용 허가

### 실행 방법
1. 해당 프로젝트 clone
2. terminal 혹은 콘솔창으로 해당 디렉토리 이동
3. python3 main.py로 실행
