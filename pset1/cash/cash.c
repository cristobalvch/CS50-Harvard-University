#include <stdio.h>
#include <cs50.h>
#include <math.h>


int main(void){
    
    float dollars;
    int changes;
    int coins = 0;
    
    do{
        dollars = get_float("Change Owned: ");
    }
    
    while (dollars < 0);
    changes = round(dollars * 100);
    
    while (changes >= 25){
        changes = changes - 25;
        coins++;
    }
    while (changes >= 10){
        changes = changes -10;
        coins++;
    }
    while (changes >= 5){
        changes = changes - 5 ;
        coins++;
    }
    while (changes >= 1){
        changes = changes -1 ;
        coins++;
    }
    {
        printf("Coins needed %d\n", coins);
    }

}