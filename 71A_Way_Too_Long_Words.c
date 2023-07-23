/*
#include <stdio.h>
#include <string.h>
int main(){
    int i;
    int n;
    scanf("%d",&n);
    for (i=1;i<=n;++i){
        char word[100];
        scanf("%s",&word);
        int length = strlen(word);
        if (length <= 10){
            printf("%s",word);
            printf("\n");
        } else {
            char result[4];
            result[0] = word[0];
            printf("%s",word[0]);
        }
    }
    return 0;
}
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int length;
    scanf("%d", &length);

    char word[100]; // assuming words have a maximum length of 100
    for (int i = 0; i < length; i++) {
        scanf("%s", word);
        int word_length = strlen(word);
        if (word_length <= 10) {
            printf("%s\n", word);
        } else {
            printf("%c%d%c\n", word[0], word_length - 2, word[word_length - 1]);
        }
    }

    return 0;
}