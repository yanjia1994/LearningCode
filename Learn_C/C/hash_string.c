#include <stdlib.h>
#include <stdio.h>
#include "uthash.h"

typedef struct Node {
    char name[10];
    int id;
    UT_hash_handle hh;
} Node;
Node *g_head = NULL;

void AddNode(char *name, int user_id)
{
    Node *node = NULL;
    HASH_FIND_STR(g_head, name, node);
    if (node == NULL) {
      node = (Node *)malloc(sizeof(Node));
      strcpy(node->name, name);
      node->id = user_id;
      HASH_ADD_STR(g_head, name, node);
    }
    return;
}

void DeleteNode(char *name)
{
    Node *node = NULL;
    HASH_FIND_STR(g_head, name, node);
    if (node != NULL) {
      HASH_DEL(g_head, node);
      free(node);
    }
    return;
}

void DeleteAllNode(int user_id)
{
    Node *cur = NULL;
    Node *next = NULL;
    HASH_ITER(hh, g_head, cur, next) {
        HASH_DEL(g_head, cur);
        free(cur);
    }
    return;
}

int CompareByKey(Node *a, Node *b)
{
    return strcmp(a->name, b->name);
}

int CompareByValue(Node *a, Node *b)
{
    return (a->id - b->id);
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