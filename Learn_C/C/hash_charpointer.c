#include <stdlib.h>
#include <stdio.h>
#include "uthash.h"

typedef struct Node {
    char *name;
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
      node->name = name;
      node->id = user_id;
      HASH_ADD_KEYPTR(hh, g_head, node->name, strlen(node->name), node);
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
