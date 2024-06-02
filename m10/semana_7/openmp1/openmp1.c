// Programação em OpenMP 1 - Moises Cazé

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

void initialize_array(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100; // números aleatórios de 0 a 99
    }
}

int sum_serial(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int sum_parallel(int *arr, int size, int num_threads) {
    int sum = 0;
    #pragma omp parallel for num_threads(num_threads) reduction(+:sum)
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int N = 1000000; // tamanho do vetor
    int *arr = (int *)malloc(N * sizeof(int));

    srand(time(NULL));
    initialize_array(arr, N);

    // versão serial
    double start_serial = omp_get_wtime();
    int sum_serial_val = sum_serial(arr, N);
    double end_serial = omp_get_wtime();
    printf("soma serial: %d\n", sum_serial_val);
    printf("tempo serial: %f segundos\n\n", end_serial - start_serial);

    // versão paralela com diferentes números de threads
    for (int num_threads = 1; num_threads <= 8; num_threads *= 2) {
        double start_parallel = omp_get_wtime();
        int sum_parallel_result = sum_parallel(arr, N, num_threads);
        double end_parallel = omp_get_wtime();
        printf("soma paralela com %d threads: %d\n", num_threads, sum_parallel_result);
        printf("tempo paralelo com %d threads: %f segundos\n", num_threads, end_parallel - start_parallel);
    }

    free(arr);
    return 0;
}
