#include <stdio.h>
#include <stdlib.h>

void main() {
	srand(7355608);

	for (int i = 0; i < 10; i++) {
		int random = rand();

		printf("%d\n", random);
	}
}
