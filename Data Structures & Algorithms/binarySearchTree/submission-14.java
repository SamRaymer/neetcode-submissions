class TreeMap {
    class Node {
        Node(int k) {
            key = k;
        }
        int key;
        int value;
        Node left;
        Node right;
    }

    Node root;

    public TreeMap() {}

    public void insert(int key, int val) {
        System.out.println("Insert %d, %d".formatted(key, val));
        if (root == null) {
            root = new Node(key);
            root.value = val;
            return;
        }

        Node cur = root;
        while (cur.key != key) {
            if (key < cur.key) {
                if (cur.left == null) {
                    cur.left = new Node(key);
                }
                cur = cur.left;
            } else { // key > cur.key by elimination
                if (cur.right == null) {
                    cur.right = new Node(key);
                }
                cur = cur.right;
            }
        }

        cur.value = val;
    }

    public int get(int key) {
        System.out.println("Get %d".formatted(key));
        if (root == null) {
            System.out.println("Empty tree: %d".formatted(key));
            return -1;
        }

        Node cur = root;
        while (cur.key != key) {
            if (key < cur.key) {
                if (cur.left == null) {
                    System.out.println("Not present: %d".formatted(key));
                    return -1;
                }

                cur = cur.left;
            } else { // key > cur.key by elimination
                if (cur.right == null) {
                    System.out.println("Not present: %d".formatted(key));
                    return -1;
                }

                cur = cur.right;
            }
        }
        System.out.println("Got %d".formatted(cur.key));
        return cur.value;
    }

    public int getMin() {
        if (root == null)
            return -1;

        return getMinNode(root).value;
    }

    public Node getMinNode(Node start) {
        Node cur = start;
        while (cur.left != null) {
            cur = cur.left;
        }

        return cur;
    }

    public int getMax() {
        if (root == null)
            return -1;

        return getMaxNode(root).value;
    }

    public Node getMaxNode(Node start) {
        Node cur = start;
        while (cur.right != null) {
            cur = cur.right;
        }

        return cur;
    }

    public void remove(int key) {
        if (root == null)
            return;

        Node parent = null;
        Node toRemove = root;
        boolean leftOfParent = false;
        while (toRemove.key != key) {
            parent = toRemove;
            if (key < toRemove.key) {
                if (toRemove.left == null)
                    return;

                toRemove = toRemove.left;
                leftOfParent = true;
            } else { // key > toRemove.key by elimination
                if (toRemove.right == null)
                    return;

                toRemove = toRemove.right;
                leftOfParent = false;
            }
        }

        boolean quickReplaceWithLeft = toRemove.right == null;
        boolean quickReplaceWithRight = toRemove.left == null;

        Node replacementNode;
        if (quickReplaceWithLeft || quickReplaceWithRight) {
            replacementNode = quickReplaceWithLeft ? toRemove.left : toRemove.right;
        } else {
            replacementNode = getMinNode(toRemove.right);
            remove(replacementNode.key);
            replacementNode.left = toRemove.left;
            replacementNode.right = toRemove.right;
        }

        if (parent == null) {
            root = replacementNode;
        } else {
            if (leftOfParent) {
                parent.left = replacementNode;
            } else {
                parent.right = replacementNode;
            }
        }
    }

    public List<Integer> getInorderKeys() {
        ArrayList<Integer> toReturn = new ArrayList<Integer>();
        ArrayList<Integer> keys = new ArrayList<Integer>();
        addToList(null, root, keys, toReturn);

        return keys;
    }

    private void addToList(Node prev, Node current, List<Integer> keyList, List<Integer> valList) {
        if (prev == current && current == null) {
                return;
        }
        if (current.left != null)
            addToList(current, current.left, keyList, valList);
        keyList.add(current.key);
        valList.add(current.value);
        if (current.right != null)
            addToList(current, current.right, keyList, valList);
    }
}
