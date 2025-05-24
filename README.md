<h1 align="center">MSVCRandAlgorithm</h1>

* 파이썬 MSVC 컴파일러 rand 함수 구현

## 알고리즘
![Algorithm](https://github.com/GooGooGong990/MSVCRandAlgorithm/blob/main/image.png)

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
    def __init__(self, seed = 523):
        self.state = seed

    def rand(self):
        self.state = (214013 * self.state + 2531011) & 0xFFFFFFFF
        return (self.state >> 16) & 0x7FFF

random = srand(7355608)
for i in range(10):
    print(random.rand())
```
