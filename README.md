# nnsvs-korean-support

> ⚠️ 해당 문서는 개발자의 경험을 토대로 작성되고 있습니다.  
> ⚠️ 잘못된 정보는 [이슈](https://github.com/Kor-SVS/nnsvs-korean-support/issues)를 열어 알려주세요.

:pushpin: [NNSVS](https://github.com/r9y9/nnsvs)/[ENUNU](https://github.com/oatsu-gh/ENUNU.git) 한국어 지원 프로젝트

이 저장소에서는 한국어 데이터 세트를 만드는 데 도움이 되는 table 및 hed 파일, 문서, 도구 등이 제공됩니다.

> [프로젝트 페이지 (진행 상황 확인 가능)](https://github.com/orgs/Kor-SVS/projects/1/views/1)

### 유의사항

```
모델이 잘 동작하지 않을 경우, 제게 정보를 공유하여 개선을 하는 것은 좋습니다.
하지만, 저 또한 독자적으로 공부를 하며, 취미로 해당 프로젝트를 진행하고 있기 때문에
반드시 이상적으로 동작할 것이라는 책임을 지지는 못합니다.

From @Cardroid6
```

### 데모 영상

[![Video Label](http://img.youtube.com/vi/FavesV-Huv4/0.jpg)](https://youtu.be/FavesV-Huv4?t=0s)

## 💾 파일

1. [hed 파일](./hed)

    > ❔ 음소들 간의 관계를 나타내고 연산에 특화된 형태로 변환할 때 사용된다고 합니다만, 완벽하게 이해하고 있진 않습니다.

2. [table 파일](./dic)

    > 자소 -> 음소 변환에 사용되는 사전 파일입니다.

    > 한국어 그대로 가사로 사용하려면, g2pk4utau 변환기가 필요합니다. (공개 준비중)

    1. hangul.table [기본 table 파일] (비음성 음소 + 한국어 음소)
    2. hangul_ext.table [확장 table 파일] (비음성 음소 + 한국어 음소 + 일본어(음소는 한국어))

3. [음소 정보](./PHONEMES.md)

4. [기타 문서들](./doc)

## 🛠️ 도구

> **[enunu-kor-tool](https://github.com/Kor-SVS/enunu-kor-tool)** 에서 관리되고 있습니다.

## 🍳 [레시피](./recipes)

> 전처리가 완료되거나 진행중인 **공개** 데이터 세트의 파일들

## 🙏 출처 및 도움을 받은 곳

> 도움을 주신 많은 분들에게 감사드립니다!

**📍 기여자**

-   [@MALCHA-UTAU](https://github.com/MALCHA-UTAU): 음소 사전 베이스 작성, 데이터 셋 구축

**🔍 참고 문서**

-   [NNSVS](https://github.com/nnsvs/nnsvs)
-   [ENUNU](https://github.com/oatsu-gh/ENUNU)
-   [enunu_training_kit](https://github.com/oatsu-gh/enunu_training_kit)
-   [nnsvs-custom-stripts](https://github.com/oatsu-gh/nnsvs-custom-stripts)
-   [nnsvs-english-support](https://github.com/intunist/nnsvs-english-support)
-   [nnsvs-japnese-plus](https://github.com/intunist/nnsvs-japnese-plus)
-   [utaupy](https://github.com/oatsu-gh/utaupy)
-   [g2pk](https://github.com/Kyubyong/g2pK)
