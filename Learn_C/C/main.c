#include <stdlib.h>
#include <stdio.h>
#include "uthash.h"

typedef struct Node
{
    void *key;
    int value;
    UT_hash_handle hh;
} Node;
Node *g_head = NULL;

void AddNode(void *key, int value)
{
    Node *node = NULL;
    HASH_FIND_PTR(g_head, key, node);
    if (node == NULL)
    {
        node = (Node *)malloc(sizeof(Node));
        node->key = key;
        node->value = value;
        HASH_ADD_PTR(g_head, key, node);
    }
    return;
}

void DeleteNode(void *key)
{
    Node *node = NULL;
    HASH_FIND_PTR(g_head, key, node);
    if (node != NULL)
    {
        HASH_DEL(g_head, node);
        free(node);
    }
    return;
}

void DeleteAllNode()
{
    Node *cur = NULL;
    Node *next = NULL;
    HASH_ITER(hh, g_head, cur, next)
    {
        HASH_DEL(g_head, cur);
        free(cur);
    }
    return;
}

int CompareByKey(Node *a, Node *b)
{
    char *stra = (char *)(a->key);
    char *strb = (char *)(b->key);
    return strcmp(stra, strb);
}

int CompareByValue(Node *a, Node *b)
{
    return (a->value - b->value);
}

void SortByValue()
{
    HASH_SORT(g_head, CompareByValue);
}

void SortByKey()
{
    HASH_SORT(g_head, CompareByKey);
}

int GetCount()
{
    return HASH_COUNT(g_head);
}

#define MACHINE_MAX_NUM 1000
#define DATA_MAX_NUM 1000
#define CONTRIBUTION 10

typedef struct
{
    int genData[DATA_MAX_NUM];
    int hasData[DATA_MAX_NUM];
    int tranData[DATA_MAX_NUM];
    int contribution;
} DataMachineSystem;

DataMachineSystem *DataMachineSystemCreate(int num)
{
    if (num <= 0)
    {
        return NULL;
    }
    DataMachineSystem *obj = (DataMachineSystem *)malloc((num + 1) * sizeof(DataMachineSystem));
    memset(obj, 0, sizeof((num + 1) * sizeof(DataMachineSystem)));
    return obj;
}

int DataMachineSystemTransferData(DataMachineSystem *obj, int machineA, int machineB, int dataId)
{
    if (obj == NULL)
    {
        return 0;
    }
    if (obj[machineB].hasData[dataId] == 1)
    {
        return 0;
    }
    if (obj[machineA].hasData[dataId] == 0)
    {
        obj[machineA].genData[dataId] = 1;
        obj[machineA].hasData[dataId] = 1;
        obj[machineA].contribution += CONTRIBUTION;
    }
    obj[machineB].hasData[dataId] = 1;
    obj[machineB].tranData[dataId] = machineA;
    int machine = machineA;
    while (obj[machine].genData[dataId] == 0)
    {
        obj[machine].contribution += CONTRIBUTION;
        machine = obj[machine].tranData[dataId];
    }
    return 1;
}

int DataMachineSystemTransferDataToAll(DataMachineSystem *obj, int machine, int dataId)
{
}

int DataMachineSyetemQueryContribution(DataMachineSystem *obj, int machine)
{
}

void DataMachineSystemFree(DataMachineSystem *obj)
{
    if (obj == NULL)
    {
        return;
    }
    free(obj);
    return;
}

int main(int argc, char *argv[])
{
    printf("Hello World!");
    getchar();
    return 0;
}
