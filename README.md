# 📖 졸업 작품 SED
Keras-Yolov3를 사용하여 건설현장에서 발생하는 사고를 예방하기 위해 안전 장비 착용 여부를 탐지하는 프로젝트를 개발.

Keras-Yolov3를 사용하여 건설현장에서 발생하는 사고를 예방하기 위해 안전
장비 착용 여부를 탐지하는 프로젝트를 개발.

**Technology** : Python, Keras, TensorFlow, PyQt, Jupyter

![image](https://github.com/lusate/SED/assets/95400441/46a1849b-bae9-49c0-824c-76e8458cdc90)


🔔 **<프로젝트 담당 업무>**

- Jupyter notebook을 기반으로 개발하여 구글 크롤링을 통해 이미지를 수집
- 수집한 이미지들을 모두 라벨링.
- yolo의 [train.py](http://train.py) 를 사용해서 학습시킨 .h 파일을 가지고 테스트를 진행.
- 이미지 정확도를 높이기 위해 클래스 수 수정, 이미지 증대, 추가 수집을 진행
