# Protobuf 설치 방법

1. https://github.com/protocolbuffers/protobuf/releases 에서 
    - protobuf-python-3.10.1.zip 다운로드
    - protoc-3.10.1-win64.zip 다운로드

2. protobuf-3.10.1\src 안에 protoc.exe 파일 추가

3. powershell로 다음 명령어 실행
    
        cd protobuf-3.10.1\python
        python setup.py build

4. build\lib 안에 있는 google을 프로젝트로 복사