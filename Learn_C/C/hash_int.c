#include "uthash.h"

typedef struct Node {
    int id;
    char name[10];
    UT_hash_handle hh;
} Node;
Node *g_head = NULL;

void AddNode(int user_id, char *name)
{
    Node *node = NULL;
    HASH_FIND_INT(g_head, &user_id, node);
    if (node == NULL) {
      node = (Node *)malloc(sizeof(Node));
      node->id = user_id;
      HASH_ADD_INT(g_head, id, node);
    }
    strcpy(node->name, name);
}

void DeleteNode(int user_id)
{
    Node *node = NULL;
    HASH_FIND_INT(g_head, &user_id, node);
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

int CompareByValue(Node *a, Node *b)
{
    return strcmp(a->name, b->name);
}

int CompareByKey(Node *a, Node *b)
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