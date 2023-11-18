#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#define CANTIDAD_LETRAS 26

/**
 * Genera 
*/
void desordenar(int i, char table[], char letras_ordenadas[], char letras_desordenadas[])
{
    if (i < 0)
    {
        return;
    }

    table[letras_ordenadas[i] - 'A'] = letras_desordenadas[i];
    desordenar(i - 1, table, letras_ordenadas, letras_desordenadas);
}

void generador_tabla(char table[])
{
    char letras_ordenadas[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char letras_desordenadas[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i;
    int j;
    char temp;

    srand(time(NULL));
    
    for (i = 25; i > 0; i--)
    {
        j = rand() % (i + 1);

        temp = letras_desordenadas[i];
        letras_desordenadas[i] = letras_desordenadas[j];
        letras_desordenadas[j] = temp;
    }

    creador_nodos_recursivos(25, table, letras_ordenadas, letras_desordenadas);
}

int main() 
{
    srand(time(NULL));
    char tabla[CANTIDAD_LETRAS];

    generador_tabla(tabla);

    FILE *archivo = fopen("tabla.txt", "w");
    if (archivo == NULL) {
        printf("No se pudo abrir el archivo.\n");
        return 1;
    }

    for (int i = 0; i < 26; i++) {
        fprintf(archivo, "%c %c\n", 'A' + i, tabla[i]);
    }

    fclose(archivo);

    printf("Tabla generada y guardada en tabla.txt\n");

    return 0;
}