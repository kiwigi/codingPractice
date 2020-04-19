#include <stdio.h>

int main(){
    printf("Howdy cowboy, enter your login info below:\n");
    printf("username:");
    char username[20];
    scanf("%s", username);
 

    if (strcmp(username,"cowboy")==0)
    {
        welcome();
    }
    else{
        printf("incorrect.\n");
        main();
    }
    return 0;
}

int welcome(){
    printf("WOOHOOOOO! congrats on your first buffer overflow!");
    return 0;
}
