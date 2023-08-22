#include<stdio.h>
int main(){
  int n , no,mul;
  int a[1000][1000];
  printf("Enter the size of the square matrix:\n");
  scanf("%d",&n);
  printf("Enter the elements of 1st matrix:\n");
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      scanf("%d",&a[i][j]);
    }
  }
  int d[n][n];
  printf("Enter the elements of 2nd matrix :\n");
  for(int q=0;q<n;q++){
    for(int r =0;r<n;r++){
      scanf("%d",&d[q][r]);
      
    }
  }
  printf("|MENU|\n");
  printf("1. Adding the matrix \n");
  printf("2. Subtractiing matrix 2 from 1 \n");
  printf("3. Multiplying matrix of your choice with an intger \n");
  printf("4. Exit the calculator \n");
  printf("Enter your choice : \n");
  int ch;
  scanf("%d",&ch);
  switch (ch){
    case 1:
      printf("The 1st matrix is :\n");
      for(int s= 0 ; s<n;s++){
        for(int t = 0;t<n;t++){
          printf("%d ",a[s][t]);
        }
        printf("\n");
      }
      printf("The 2nd matrix is :\n");
      for (int a =0;a<n;a++){
        for(int b =0;b<n;b++){
          printf("%d ",d[a][b]);
        }
        printf("\n");
      }
      printf("The sum of both matrices is :\n");
      for(int e =0;e<n;e++){
        for(int b =0;b<n;b++){
          printf("%d ",a[e][b]+d[e][b]);
          
        }
        printf("\n");
      }
      
      break;
    case 2:
      printf("The 1st matrix is :\n");
      for(int s= 0 ; s<n;s++){
        for(int t = 0;t<n;t++){
          printf("%d ",a[s][t]);
        }
        printf("\n");
      }
      printf("The 2nd matrix is :\n");
      for (int a =0;a<n;a++){
        for(int b =0;b<n;b++){
          printf("%d ",d[a][b]);
        }
        printf("\n");
      }
      printf("The differnece of both matrices is :\n");
      for(int e =0;e<n;e++){
        for(int b =0;b<n;b++){
          printf("%d ",a[e][b]-d[e][b]);
        }
        printf("\n");
      }
    break;
    case 3: 
      printf("Enter the number of matrix you want to multiply the integer with at:\n");
    scanf("%d",&no);
      printf(" Enter the integer you want to multiply with : \n");
      scanf("%d",&mul);
      
    switch (no){
      case 1:
      for(int f=0;f<n;f++){
        for(int g =0;g<n;g++){
          printf("%d ",a[f][g]*mul);
        }
        printf("\n");
      }
      break;
      
      
    
      case 2:
      for(int f= 0;f<n;f++){
        for(int g = 0;g<n;g++){
          printf("%d ",d[f][g]*mul);
          
        }
        printf("\n");
      }}
    break;
    
    break;
    case 4:
      printf("Exiting the calculator");
    break;
    
    
      
  }
      
  
}