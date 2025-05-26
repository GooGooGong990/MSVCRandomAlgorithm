<h1 align="center">MSVCRandAlgorithm</h1>

* MSVC의 rand 의사 난수 생성기의 파이썬 구현체

## 알고리즘
* MSVC의 `rand()` 함수는 선형 합동 생성기를 기반으로 의사 난수를 생성합니다.

- 선형 합동 생성기(Linear congruential generator, LCG)는 널리 알려진 유사난수 생성기입니다. 
선형 합동 생성기는 다음 재귀 관계로 정의된 순열 `Xᵢ`을 반환합니다.
* ![LGC](https://github.com/GooGooGong990/MSVCRandAlgorithm/blob/main/image0.png?raw=true)
- 따라서 선형 합동 생성기는 다음과 같은 인자들로 유일하게 결정됩니다.
  - `m` (나눔수): 0 < m
  - `a` (곱함수): 0 < a < m
  - `c` (더함수): 0 ≤ c < m
  - `X₀` (초기값): 0 ≤ X₀ < m

- **MSVC에서 사용하는 상수값은 다음과 같습니다.**
  - `m` (나눔수): 2³²
  - `a` (곱함수): 214013
  - `c` (더함수): 2531011
* ![MSVC](https://github.com/GooGooGong990/MSVCRandAlgorithm/blob/main/image1.png?raw=true)

## C
* [**main.c**](https://github.com/GooGooGong990/MSVCRandAlgorithm/blob/main/main.c)
```c
#include <stdio.h>
#include <stdlib.h>

void main() {
    srand(7355608);

    for (int i = 0; i < 10; i++) {
        int random = rand();

        printf("%d\n", random);
    }
}
```

## 파이썬
* [**main.py**](https://github.com/GooGooGong990/MSVCRandAlgorithm/blob/main/main.py)
```py
class srand:
    def __init__(self, seed):
        self.state = seed

    def rand(self):
        self.state = (214013 * self.state + 2531011) & 0xFFFFFFFF
        return (self.state >> 16) & 0x7FFF

random = srand(7355608)
for i in range(10):
    print(random.rand())
```

## 참고한 문헌
* [위키백과](https://ko.wikipedia.org/wiki/선형_합동_생성기)
* [Microsoft Learn](https://learn.microsoft.com/ko-kr/cpp/c-runtime-library/reference/rand?view=msvc-170)
