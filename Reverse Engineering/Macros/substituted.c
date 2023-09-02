#include <stdio.h>

#define cheers (
#define bruv )
#define footie {
#define fam }
#define jokes [
#define shook ]
#define tele int
#define lemmeknow main 
#define ye_enough ;
#define bare rows 
#define wagwan scanf 
#define lots array 
#define fromthetop for 
#define bloke i 
#define yeet printf 
#define mandem j 
#define innit if 
#define dunno else
#define k return

int main ( )
{
    int rows ;
    scanf ( "%d" , &rows ) ;
    int array [ rows ] [ rows ] ;
    for ( int i = 0 ; i < rows ; i++ )
    {
        printf ( "\n" ) ;
        for ( int j = 0 ; j <= i; j++ )
        {
            if ( i == j || j == 0 )
                array [ i ] [ j ] = 1 ;
            else
                array [ i ] [ j ] = array [ i - 1 ] [ j - 1 ] + array [ i - 1 ] [ j ] ;
            printf( "%d ", array [ i ] [ j ] ) ;
        }   
    }
    printf ( "\n\n" ) ;
    return 0 ;
}