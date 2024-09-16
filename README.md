# recycle-method
플라스틱 분리수거 활용 시 이미지 인식/분류를 하여 플라스틱 종류를 외우지 않아도 미리 학습된 데이터로 플라스틱을 분류하는 작업을 대신 해줍니다.

## 주요 기능
1. json to text 변환 : text로 변환시킬 원본 데이터 코드
2. text to yaml 변환 : 모델 학습 시키기 전 text로 변환한 파일 yaml로 변환

## 설치 방법
1. `pip install ultralytics`
2. 아래 코드로 torch와 cuda 버전 맞춰 GPU로 학습 시킬 준비 필요
`pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121`

## 사용 방법
1. Jupyter Notebook을 실행하고 `Recyle_Web.ipynb` 파일을 열어 맨 하단에 있는 grdaio 웹 배포 된 셀을 실행
2. `V8Classifi.pt` `V4Classifi.pt` `Label.pt` 세 개 파일을 실행시킨다.
3. Gradio가 실행되면 drop and down 방식으로 되어 있는 라벨 이름을 클릭 
