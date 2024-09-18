#include <stdio.h>
#include <stdlib.h>

int countNegatives(int grid[4][4], int gridSize, int* gridColSize) {
    int nums=0 ;
    int i;
    int j=gridColSize[0]-1 ;
    int temp[100];

    for (i=0; i<gridSize; i++){
        int tpp=1;
        temp[0]=0;
        while(j>0){
            temp[tpp]=j;
            j=(j+temp[tpp-1])/2;
            tpp++;
            
            if(j==temp[tpp-1]){
                if (grid[i][j]<0){
                    nums=nums+gridColSize[0]-j;
                }
                else{
                    nums=nums+gridColSize[0]-j-1;
                }
                break;
            }
        }
    }
    return nums;
}

int main(){
    int grid[4][4] ={{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}};
    int res;
    res =countNegatives(grid[4][4] ,4,4);
    printf("%d",res);
    return 0;
}