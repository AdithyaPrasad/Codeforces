#include <stdio.h>

int main(){
    int input;
    scanf("%d",&input);
    if (input >= 4 && input%2 == 0){
        printf("YES");
    } else {
        printf("NO");
    }
    return 0;
}