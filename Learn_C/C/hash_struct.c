#include <stdlib.h>
#include <stdio.h>
#include "uthash.h"

typedef struct Key {
    char a;
    int b;
    UT_hash_handle hh;
} Key;

typedef struct Node {
    Key key;
    int value;
    UT_hash_handle hh;
} Node;
Node *g_head = NULL;

void AddNode(Key key, int value)
{
    Node *node = NULL;
    HASH_FIND(hh, g_head, &key, sizeof(Key), node);
    if (node == NULL) {
      node = (Node *)malloc(sizeof(Node));
      node->key = key;
      node->value = value;
      HASH_ADD(hh, g_head, key, sizeof(Key), node);
    }
    return;
}

void DeleteNode(Key key)
{
    Node *node = NULL;
    HASH_FIND(hh, g_head, &key, sizeof(Key), node);
    if (node != NULL) {
      HASH_DEL(g_head, node);
      free(node);
    }
    return;
}

void DeleteAllNode()
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
    if (a->key.a != b->key.a) {
        return a->key.a - b->key.a;
    }
    return a->key.b, b->key.b;
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