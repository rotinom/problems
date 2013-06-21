// Standard includes here
#include <queue>

/**
    \brief Definition of a Node in a Binary Tree
    \todo Make this a class template for reusability
    \todo We really need to make use of std auto_ptr or boost::smart_ptr
*/
class IntTreeNode
{
public:
    /// \brief Default constructor
    IntTreeNode(const int val)
    {
        _lChild = NULL;
        _rChild = NULL;
        _Value = val;
    }

    /**
        \brief method used to get the left child of a node
        \returns pointer to the left child
        \note Check the pointer for null prior to using it
    */
    IntTreeNode* const getLeftChild()
    {
        return _lChild;
    }

    /**
        \brief Method used to set the left child of a node
        \param node Pointer to a node to assign as the left child
    */
    void setLeftChild(IntTreeNode* node)
    {
        _lChild = node;
    }

    /**
        \brief method used to get the right child of a node
        \returns pointer to the right child
        \note Check the pointer for null prior to using it
    */
    IntTreeNode* const getRightChild()
    {
        return _rChild;
    }

    /**
        \brief Method used to set the right child of a node
        \param node Pointer to a node to assign as the right child
    */
    void setRightChild(IntTreeNode* node)
    {
        _rChild = node;
    }

    /**
        \brief Method used to retrieve the node's value
        \returns The integer value of the node
    */
    int getValue()
    {
        return _Value;
    }

private:

    /// \brief The reft child of this node
    IntTreeNode* _lChild;

    /// \brief The right child of this node
    IntTreeNode* _rChild;

    /// \brief The value of this node
    int _Value;
};


/**
    \brief Stubbed definition of a Binary tree
    \todo Make this a class template for reusability
    \todo We really need to make use of std auto_ptr or boost::smart_ptr
*/
class IntBinaryTree
{
private:
    /// \brief Typedef of a Queue of integers
    typedef std::queue<int> IntQueue;

public:
    /// \brief Default constructor
    IntBinaryTree()
    {
        _root = NULL;
        _nodeCount = 0;
    }

    /**
        \brief Stub used to add values into the tree
        \todo Implement this and make sure to do the binary
              tree rules.  Also make sure to rotate if necessary
    */
    void addValue(const int value)
    {
    }

    /**
     \brief Equality operator
     \returns true if the two trees are identical, false otherwise
     \note The basic idea of this operator, is that because we do not
           care about the underlying structure of the trees, we must 
           therefore traverse them, only comparing their values, not
           the parent/child relationships.
           \par
           So, strategically, we should generate a list of the nodes' 
           values in each tree, and then compare each list of values
           to determine if they are identical.  Now, the list generation
           is the really interesting part.
           \par
           An interesting property of the Binary Search Tree, is that you
           can retrieve the data in an ordered fashion if you traverse 
           it by looking at the left child, then the current node, then
           the right child.  As part of processing, we can then place 
           the values on a queue in this ordered fashion while processing 
           one tree, and dequeue and compare the values while processing 
           the other tree.
           \par
           If the values differ at any point, then we do not have trees
           which contain identical data, and we can therefore return 
           false.  Otherwise, the data will be the same, and the trees
           are identical.
    */
    bool operator== (const IntBinaryTree& rValue)
    {
        // If the two trees do not have the same number
        // of nodes, then return false
        if(_nodeCount != rValue._nodeCount)
        {
            return false;
        }

        // If either of the root nodes are null, then return
        // a pointer comparison between the two
        else if(_root == NULL || rValue._root == NULL)
        {
            return (_root == rValue._root);
        }
        // NOTE: At this point, we know that both _root's are not NULL

        // The queue used to hold the data 
        IntQueue queue;

        // Traverse the nodes, starting at the root node
        listNodes(_root, queue);

        // Traverse the nodes, starting at the rValue's root node
        return compareNodes(rValue._root, queue);
    }

    /**
        \brief Helper method used to traverse the first tree, and 
               place the nodes into the queue
        \param node Pointer to an IntTreeNode which is the current
               node we are processing
        \param queue Reference to the queue which contains the values
               that we have read out of the tree already
        \note This method is called recursively
    */      
    void listNodes(IntTreeNode* node, IntQueue& queue)
    {
        // If we're at a leaf node, just exit
        if(NULL == node)
        {
            return;
        }        
        else
        {
            // Process the left child, then ourselves, then the right child            
            listNodes(node->getLeftChild(), queue);
            queue.push(node->getValue());
            listNodes(node->getRightChild(), queue);
        }
    }

    /**
        \brief Helper method used to traverse the second tree, and 
               compare against the values pulled out of the first tree
        \param node Pointer to an IntTreeNode which is the current
               node we are processing
        \param queue Reference to the queue which contains the values
               that we have read out of the tree already
        \returns true if the traversal of node (and all of its children)
                 matches the order of nodes encountered from the first
                 tree.  false otherwise
        \note This method is called recursively
    */  
    bool compareNodes(IntTreeNode* node, IntQueue& queue)
    {
        // At the leaf node condition, we indicate that all went well
        if(NULL == node)
        {
            return true;
        }
        else
        {
            // Process the left children
            // If the children are not equal, then just propagate
            // it upwards
            if(!compareNodes(node->getLeftChild(), queue))
            {
                return false;
            }

            // Dequeue the item from the front of the list.
            int val = queue.front();
            queue.pop();

            // The dequeued item should equal node's value
            if(val != node->getValue())
            {
                return false;
            }

            // Process the right children
            // If the children are not equal, then just propagate
            // it upwards
            if(!compareNodes(node->getRightChild(), queue))
            {
                return false;
            }
        }
        return true;
    }

private: 

    /// \brief The root of the tree
    IntTreeNode* _root;

    /// \brief The number of nodes in the tree  
    unsigned int _nodeCount;
};
