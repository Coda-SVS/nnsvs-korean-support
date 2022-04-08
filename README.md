# nnsvs-korean-support

> ⚠️ **해당 저장소는 아직 완벽하지 않습니다!** ⚠️  
> 🚨 내용이 언제든지 변경될 수 있습니다. 🚨

:pushpin: [NNSVS](https://github.com/r9y9/nnsvs) 한국어 지원 프로젝트

이 저장소에서는 한국어 데이터 세트를 만드는 데 도움이 되는 스크립트와 hed 및 table 파일, 지침서, 도구 등이 제공됩니다.

## 💾 파일

1. hed => hed 파일  
    >❔ 이전 발음과 이후 발음과의 관계를 나타내고 연산에 특화된 형태로 변환할 때 사용된다고 합니다만, 확실하게 이해하고 있진 않습니다.  
    
    > ⚠️ 현재 존재하는 hed 파일은 실험을 통한 성능 검증이 되지 않았습니다.

2. table => 테이블 파일  
    >한글의 각 글자마다 초성, 중성, 종성으로 분해하여 각각에 맞는 음소로 변환 되어있습니다.
    1. 서로 붙어있는 음소와 띄어쓰기로 구분된 음소 테이블  
        (한글을 지원하지 않는 시스템을 위한 기본 테이블)
    2. 한글 + 띄어쓰기로 구분된 음소 테이블  
        ([한글 -> 음소] 변환할 때 주로 사용하는 테이블)
    3. 한글과 서로 붙어있는 음소 + 띄어쓰기로 구분된 음소 테이블

## 🛠️ 도구

**:package: 필요한 패키지**  
```python -m pip install -r requirements.txt```

* tool => 유용한 도구 및 스크립트 파일  
    > 다른 곳에서 가져와서 수정한 파일도 있습니다. (출처 부분을 확인해 주세요)
    > 대부분 Python으로 작성하고 있습니다.
    - hed 파일 생성기
    - table 파일 생성기
    - 한글 발음법과 문맥에 맞게 최대한 변환해 주는 Utau 용 g2p 모듈  
        (g2pk와 mecab을 사용하여 영어 및 숫자도 변환 가능합니다)
    - 한글 자모에 대응되는 알파벳 음소 사전 및 생성기  
        (해당 사전은 국어 표준 표기법과 다를 수 있습니다)
    - 사전을 이용해 텍스트를 변환
    - textgrid 형식을 wavesurfer의 lab 형식으로 변환  
        (마지막 음소는 변환 과정에 오차가 있습니다)

* Montreal-Forced-Aligner => 음소 강제 정렬을 도와주는 외부 도구  
    > **📄 사용방법 작성 필요**  
    
    > 음소를 실제 발음이 들리는 곳에 위치시키는 작업인 음소 강제 정렬 작업을 쉽게 할 수 있도록 해당 도구를 사용할 수 있습니다.  
    > 일반적인 상황에서는 상당한 정확도를 보이지만, 가창 데이터를 정렬할 때는 정확도가 조금 떨어집니다.  
    하지만 MFA를 한 번 거치고 나면 간단한 수정 작업만 하면 되기에 조금 더 작업시간을 단축시키는 것이 가능합니다!  

## 🍳 레시피

> 전처리가 완료되거나 진행중인 데이터 세트의 파일들

> 🚨 데이터 세트의 라이선스 및 저작권을 확인하지 않고 원본 파일을 그대로 올리면 안 됩니다!

**💿 데이터 세트 목록**

- [CSD](https://zenodo.org/record/4785016#.YlBhL8jP24Q)
    * MFA로 자동 정렬은 수행되었지만, 검사 및 수정이 필요합니다.
    * 그 중 오류률이 심한 20개의 정렬파일은 제거되었습니다. 수동으로 처음부터 정렬해야 합니다.

## 🚩로드맵

<img src="./resources/nnsvs-korean-support.kor.svg" />


## 🙏 출처 및 도움을 받은 곳

**🔍 참고 문서**
- [NNSVS](https://github.com/r9y9/nnsvs)
- [ENUNU](https://github.com/oatsu-gh/ENUNU)
- [nnsvs-custom-stripts](https://github.com/oatsu-gh/nnsvs-custom-stripts)
- [nnsvs-english-support](https://github.com/DynamiVox/nnsvs-english-support)
- [NNSVS Voicebank Making Tutorial Thing](https://docs.google.com/document/d/1uMsepxbdUW65PfIWL1pt2OM6ZKa5ybTTJOpZ733Ht6s/edit)
- [g2pk](https://github.com/Kyubyong/g2pK)
- [Kaldi](https://github.com/kaldi-asr/kaldi)
- [MFA (Montreal-Forced-Aligner)](https://montreal-forced-aligner.readthedocs.io)
- [MFA 메뉴얼](https://chldkato.tistory.com/195)

도움을 주신 많은 분들에게 감사드립니다!