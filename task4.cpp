#include <gtest/gtest.h>

// ------------------------------------------------------------
// Тесты для очереди
// ------------------------------------------------------------
TEST(QueueTest, NewQueueIsEmpty) {
    Queue<int> q;
    EXPECT_TRUE(q.empty());
    EXPECT_EQ(q.size(), 0);
}

TEST(QueueTest, PushIncreasesSize) {
    Queue<int> q;
    q.push(10);
    EXPECT_FALSE(q.empty());
    EXPECT_EQ(q.size(), 1);
    q.push(20);
    EXPECT_EQ(q.size(), 2);
}

TEST(QueueTest, PopReturnsElementsInFIFOOrder) {
    Queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    EXPECT_EQ(q.pop(), 1);
    EXPECT_EQ(q.pop(), 2);
    EXPECT_EQ(q.pop(), 3);
    EXPECT_TRUE(q.empty());
}

TEST(QueueTest, PopOnEmptyThrowsException) {
    Queue<int> q;
    EXPECT_THROW(q.pop(), std::out_of_range);
}

TEST(QueueTest, MixedPushPop) {
    Queue<int> q;
    q.push(5);
    q.push(6);
    EXPECT_EQ(q.pop(), 5);
    q.push(7);
    EXPECT_EQ(q.pop(), 6);
    EXPECT_EQ(q.pop(), 7);
    EXPECT_TRUE(q.empty());
}

// ------------------------------------------------------------
// Тесты для кучи (максимальная куча)
// ------------------------------------------------------------
TEST(HeapTest, NewHeapIsEmpty) {
    Heap<int> h;
    EXPECT_TRUE(h.empty());
    EXPECT_EQ(h.size(), 0);
}

TEST(HeapTest, PushIncreasesSize) {
    Heap<int> h;
    h.push(42);
    EXPECT_FALSE(h.empty());
    EXPECT_EQ(h.size(), 1);
}

TEST(HeapTest, PopReturnsMaxElement) {
    Heap<int> h;
    h.push(10);
    h.push(30);
    h.push(20);
    EXPECT_EQ(h.pop(), 30);
    EXPECT_EQ(h.pop(), 20);
    EXPECT_EQ(h.pop(), 10);
    EXPECT_TRUE(h.empty());
}

TEST(HeapTest, PopOnEmptyThrowsException) {
    Heap<int> h;
    EXPECT_THROW(h.pop(), std::out_of_range);
}

TEST(HeapTest, DuplicateElements) {
    Heap<int> h;
    h.push(5);
    h.push(5);
    h.push(3);
    EXPECT_EQ(h.pop(), 5);
    EXPECT_EQ(h.pop(), 5);
    EXPECT_EQ(h.pop(), 3);
    EXPECT_TRUE(h.empty());
}

// ------------------------------------------------------------
// Тесты для бинарного дерева
// ------------------------------------------------------------
TEST(BinaryTreeTest, NewTreeIsEmpty) {
    BinaryTree<int> tree;
    EXPECT_TRUE(tree.empty());
    EXPECT_EQ(tree.size(), 0);
}

TEST(BinaryTreeTest, PushAndSearch) {
    BinaryTree<int> tree;
    tree.push(5);
    tree.push(3);
    tree.push(7);
    EXPECT_TRUE(tree.search(5));
    EXPECT_TRUE(tree.search(3));
    EXPECT_TRUE(tree.search(7));
    EXPECT_FALSE(tree.search(4));
    EXPECT_FALSE(tree.search(10));
}

TEST(BinaryTreeTest, PopRemovesRootAndReturnsIt) {
    BinaryTree<int> tree;
    tree.push(10);
    tree.push(5);
    tree.push(15);
    int root = tree.pop();
    EXPECT_EQ(root, 10);
    EXPECT_FALSE(tree.search(10));
    EXPECT_TRUE(tree.search(5));
    EXPECT_TRUE(tree.search(15));
    EXPECT_FALSE(tree.empty());
}

TEST(BinaryTreeTest, PopUntilEmpty) {
    BinaryTree<int> tree;
    tree.push(1);
    tree.push(2);
    tree.push(3);
    while (!tree.empty()) {
        tree.pop();
    }
    EXPECT_TRUE(tree.empty());
    EXPECT_EQ(tree.size(), 0);
}

TEST(BinaryTreeTest, PopOnEmptyThrowsException) {
    BinaryTree<int> tree;
    EXPECT_THROW(tree.pop(), std::out_of_range);
}

TEST(BinaryTreeTest, SearchAfterRemoval) {
    BinaryTree<int> tree;
    tree.push(8);
    tree.push(3);
    tree.push(10);
    tree.pop();
    EXPECT_FALSE(tree.search(8));
    EXPECT_TRUE(tree.search(3));
    EXPECT_TRUE(tree.search(10));
}
